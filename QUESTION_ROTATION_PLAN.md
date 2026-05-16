# 🔄 SMART QUESTION ROTATION SYSTEM - Implementation Plan

**Issue**: Questions repeat quickly (limited dataset feeling)  
**Solution**: Smart rotation system with wrong-answer review & variations  
**Status**: Planning phase  
**Timeline**: Can be implemented in phases  

---

## 📊 CURRENT STATE

### Question Dataset Size
```
Total Questions Available: 228+
├── Water Cycles: 30+ brain drainers
├── Reproduction: 50+ brain drainers  
├── Electrical Systems: 30+ brain drainers
├── All Chapters: 25+ MCQs each
└── Variations possible: Unlimited
```

### Problem
- Questions are finite (228 questions)
- Users see repeats after ~15-20 practice sessions
- No tracking of question history per user
- No mechanism to retry wrong answers at higher difficulty
- Feels like "limited dataset"

---

## 🎯 SOLUTION OVERVIEW

### Three-Tier Implementation

#### TIER 1: Immediate (Week 1) ⚡
**Smart Question Selection + History Tracking**
- Track which questions user has seen
- Skip already-answered questions
- Queue wrong answers for later
- Increase difficulty on retry

#### TIER 2: Medium-term (Weeks 2-4) 🚀  
**Question Variation System**
- Parameterized questions (values change)
- Same concept, different scenarios
- Example: "Evaporation of 20%" vs "Evaporation of 30%"
- Infinite variety from finite templates

#### TIER 3: Long-term (Phase 3) 🤖
**AI-Generated Variations**
- Claude API generates question variations
- Maintains pedagogical integrity
- Unlimited, unique questions per session
- Same concept, different examples

---

## 🛠️ TIER 1: SMART QUESTION SELECTION (IMMEDIATE)

### Database Schema Changes

**New Table: question_history**
```sql
CREATE TABLE IF NOT EXISTS question_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id TEXT NOT NULL,
    chapter TEXT,
    quiz_mode TEXT,  -- 'practice', 'mock_exam', 'challenge'
    first_seen_date TEXT,
    last_seen_date TEXT,
    times_seen INTEGER DEFAULT 1,
    times_correct INTEGER DEFAULT 0,
    times_incorrect INTEGER DEFAULT 0,
    max_difficulty_attempted TEXT,  -- 'easy', 'medium', 'hard'
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE(user_id, question_id, quiz_mode)
)
```

**New Table: question_queue**
```sql
CREATE TABLE IF NOT EXISTS question_queue (
    queue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id TEXT NOT NULL,
    chapter TEXT,
    queue_type TEXT,  -- 'new', 'wrong_answer', 'review'
    difficulty_level TEXT,  -- Difficulty to present at
    added_date TEXT,
    priority INTEGER,  -- Higher = show first
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
```

### Implementation Logic

**Function: get_next_question(user_id, chapter, quiz_mode)**
```python
def get_next_question(user_id, chapter, quiz_mode):
    """
    Smart question selection algorithm:
    1. Check user's question queue (new questions first)
    2. Look for wrong answers that need review
    3. If pool exhausted, generate variations
    """
    
    # Priority order:
    # 1. Wrong answers to review (with increased difficulty)
    # 2. New questions they haven't seen
    # 3. Questions they got partially right (60-79%)
    # 4. Generated variations of known questions
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Get next question from queue
    cursor.execute("""
        SELECT question_id, queue_type, difficulty_level 
        FROM question_queue
        WHERE user_id = ? AND chapter = ?
        ORDER BY 
            CASE queue_type
                WHEN 'wrong_answer' THEN 1  -- Highest priority
                WHEN 'review' THEN 2
                WHEN 'new' THEN 3
            END,
            priority DESC,
            added_date ASC
        LIMIT 1
    """, (user_id, chapter))
    
    next_q = cursor.fetchone()
    conn.close()
    
    if next_q:
        question_id, queue_type, difficulty = next_q
        question = get_question_by_id(question_id)
        if difficulty == 'hard':
            question = make_question_harder(question)
        return question
    
    # If queue empty, return None (time to generate variations)
    return None
```

**Function: track_question_answer(user_id, question_id, is_correct, difficulty)**
```python
def track_question_answer(user_id, question_id, is_correct, difficulty):
    """
    Track question history and update queue
    """
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Update history
    cursor.execute("""
        INSERT OR REPLACE INTO question_history 
        (user_id, question_id, last_seen_date, times_seen, times_correct, times_incorrect, max_difficulty_attempted)
        VALUES (?, ?, ?, 
                COALESCE((SELECT times_seen FROM question_history WHERE user_id=? AND question_id=?), 0) + 1,
                COALESCE((SELECT times_correct FROM question_history WHERE user_id=? AND question_id=?), 0) + ?, 
                COALESCE((SELECT times_incorrect FROM question_history WHERE user_id=? AND question_id=?), 0) + ?,
                ?)
    """, (
        user_id, question_id, datetime.now().isoformat(),
        user_id, question_id,  # For times_seen
        user_id, question_id, 1 if is_correct else 0,  # For times_correct
        user_id, question_id, 0 if is_correct else 1,  # For times_incorrect
        difficulty  # max_difficulty
    ))
    
    # If wrong answer, add to queue with higher difficulty
    if not is_correct:
        new_difficulty = get_harder_difficulty(difficulty)
        cursor.execute("""
            INSERT INTO question_queue 
            (user_id, question_id, queue_type, difficulty_level, added_date, priority)
            VALUES (?, ?, 'wrong_answer', ?, ?, ?)
        """, (user_id, question_id, new_difficulty, datetime.now().isoformat(), 10))
    
    conn.commit()
    conn.close()
```

### Benefits of Tier 1
✅ Eliminates immediate repetition  
✅ Focuses on learning (review wrong answers)  
✅ Increases difficulty naturally (spaced repetition)  
✅ Can implement this week  
✅ No new question creation needed  
✅ Works with existing question pool  

---

## 🎲 TIER 2: QUESTION VARIATIONS (MEDIUM-TERM)

### Approach: Parameterized Questions

**Current Question**:
```python
{
    'q': 'Evaporation of water at 30°C produces how much vapor?',
    'options': ['10L', '20L', '30L', '40L'],
    'answer': '30L',
    'difficulty': 'hard'
}
```

**Parameterized Template**:
```python
{
    'template_id': 'evaporation_amount',
    'template': 'Evaporation of water at {temp}°C produces how much vapor?',
    'parameters': {
        'temp': [20, 25, 30, 35, 40],  # Random selection
        'volume_loss_percent': [10, 15, 20, 25],
        'scenario': ['in sun', 'in shade', 'with wind', 'in closed container']
    },
    'answer_formula': lambda params: f"{params['volume_loss_percent']}%",
    'difficulty': 'hard'
}
```

### Variation Generation
```python
def generate_question_variation(template):
    """
    Generate a variation of a question from its template
    Same concept, different values = new question
    """
    import random
    
    # Sample random parameters
    params = {}
    for param_name, param_values in template['parameters'].items():
        params[param_name] = random.choice(param_values)
    
    # Create question with sampled values
    question = template.copy()
    question['q'] = template['template'].format(**params)
    question['answer'] = template['answer_formula'](params)
    question['_params'] = params  # Track what was used
    
    return question
```

### Example Variations

**Template: Water Cycle Evaporation**
```
Original: "At 25°C, how much water evaporates in 1 hour?"
Variation 1: "At 35°C, how much water evaporates in 2 hours?"
Variation 2: "At 20°C, how much water evaporates in 30 minutes?"
Variation 3: "At 40°C, how much water evaporates in 90 minutes?"
```

All test same concept (evaporation + temperature + time) but with different numbers

**Template: Electrical Resistance**
```
Original: "A wire with 10Ω resistance carries 2A current. Voltage?"
Variation 1: "A wire with 15Ω resistance carries 3A current. Voltage?"
Variation 2: "A wire with 8Ω resistance carries 1.5A current. Voltage?"
Variation 3: "A wire with 20Ω resistance carries 4A current. Voltage?"
```

Uses V = I × R formula with different values

### Benefits of Tier 2
✅ Infinite question variety (from finite templates)  
✅ Maintains pedagogical integrity (same concept)  
✅ Prevents memorization of answers  
✅ Personalizable difficulty scaling  
✅ Can create 100+ variations per template  
✅ Moderate implementation effort  

---

## 🤖 TIER 3: AI-GENERATED VARIATIONS (PHASE 3)

### Using Claude API for Generation

```python
def generate_ai_variation(user_id, question, difficulty):
    """
    Use Claude API to generate a variation of a question
    """
    from anthropic import Anthropic
    
    client = Anthropic()
    
    prompt = f"""
    Generate a variation of this science question at {difficulty} difficulty:
    
    Original Question: {question['q']}
    Answer: {question['answer']}
    Concept: {question['concept']}
    
    Requirements:
    - Same concept as original
    - Different numbers/scenario
    - Still answerable
    - Appropriate for age 10 (P5)
    - Format as: Q: [question] | A: [answer] | Options: [A, B, C, D]
    
    Generate 1 unique variation:
    """
    
    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Parse and return generated question
    return parse_generated_question(response.content[0].text)
```

### Benefits of Tier 3
✅ Unlimited unique questions  
✅ Maintains learning integrity  
✅ Adapts to user level  
✅ Personalized content  
✅ Scales infinitely  
✅ Best long-term solution  

---

## 📈 IMPLEMENTATION TIMELINE

### Week 1: Tier 1 (Smart Selection)
```
Day 1-2: Database schema changes
Day 3-4: Implement tracking functions
Day 5: Integrate into quiz flow
Day 6-7: Testing & refinement
```

### Weeks 2-4: Tier 2 (Variations)
```
Week 2: Create 20 parameterized templates
Week 3: Integrate variation generation
Week 4: Testing with Aanya
```

### Phase 3 (Weeks 5-6): Tier 3 (AI Generation)
```
Week 5: Claude API integration
Week 6: Testing & deployment
```

---

## 🧪 TESTING PLAN

### Tier 1 Testing
1. **Question History Tracking**
   - Answer Q1 → See Q2
   - Return to Q1 → Should NOT appear in main rotation
   - Answer Q1 wrong → Should appear in review queue later at harder difficulty

2. **Question Queue Management**
   - Wrong answers appear first on next session
   - New questions appear after wrong answers handled
   - Correct answers don't re-appear

3. **Difficulty Progression**
   - Wrong answer at Easy → Appears at Medium next time
   - Wrong answer at Medium → Appears at Hard next time
   - Correct answers → Stay at same level

### Tier 2 Testing
1. **Parameter Variation**
   - Generate 5 variations of same question
   - Verify all are unique
   - Verify all are valid (answerable)
   - Verify concept consistency

2. **User Experience**
   - Aanya answers 50+ questions without repetition
   - Never sees exact same question twice
   - Each variation feels natural (not awkward)

---

## 💻 CODE STRUCTURE

### New Files to Create
```
src/utils/
├── question_rotation.py        ← Smart selection logic
├── question_variations.py      ← Parameterization system
└── question_tracking.py        ← History management

src/components/
└── question_generator.py       ← AI generation (Phase 3)
```

### Files to Modify
```
src/utils/database.py           ← Add new tables & functions
apps/exam_prep_master.py        ← Integrate selection logic
src/modules/ch*.py              ← Use smart selection
```

---

## 📊 EXPECTED IMPACT

### Before Smart Rotation
- Questions repeat after ~20 attempts
- No tracking of learning progress per question
- Wrong answers not highlighted for review
- Same difficulty regardless of performance
- User feels "limited dataset"

### After Tier 1 (Week 1)
- Questions rotate through unique pool first
- Wrong answers re-appear at higher difficulty
- No repetition until all questions used
- Better learning outcomes
- Feels like "infinite questions"

### After Tier 2 (Weeks 2-4)
- Infinite variety from parameterized questions
- Never see exact same question twice (unless by chance)
- Concept consistency maintained
- Users can practice 1000+ questions from base of 228

### After Tier 3 (Phase 3)
- Truly unlimited unique questions
- AI-generated variations
- Perfectly personalized difficulty
- Ultimate learning experience

---

## 🎓 PEDAGOGICAL BENEFITS

This system implements proven learning science:

1. **Spaced Repetition**: Wrong answers reviewed at optimal intervals
2. **Difficulty Progression**: Challenges increase with mastery
3. **Variety**: Prevents memorization, forces understanding
4. **Tracking**: User sees progress per concept
5. **Personalization**: Each user gets custom learning path

---

## 🚀 NEXT STEPS

1. **Approve Approach**: Review this plan with Aanya
2. **Start Tier 1**: Begin implementation this week
3. **Test with Aanya**: Get feedback after Tier 1 done
4. **Plan Tier 2**: Schedule parameterization work
5. **Prepare Phase 3**: Design AI generation system

---

## 💬 QUESTIONS FOR AANYA

1. **Preference**: Do you want all new questions first, then wrong answers? Or mix them?
2. **Difficulty**: Should wrong answers always go up in difficulty, or same difficulty as first attempt?
3. **Variety**: How many unique questions total would you like before seeing any repeats?
4. **Variations**: Are you comfortable with slightly different numbers in same concept?

---

**Status**: Ready for implementation  
**Priority**: High (improves learning outcomes significantly)  
**Complexity**: Medium (Tier 1), High (Tier 2-3)  
**Timeline**: Tier 1 this week, Tier 2 next month, Tier 3 Phase 3

