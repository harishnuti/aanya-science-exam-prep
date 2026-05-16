# 📖 CONTINUATION GUIDE
## Step-by-Step Guide to Resume Phase 2 Implementation
**For**: Next session startup  
**Purpose**: Ensure seamless continuation from frozen v4.0 to v4.2  
**Duration**: 3-5 days to completion  

---

## 🎯 BEFORE YOU START (Setup - 15 minutes)

### Step 1: Verify Code is Current
```bash
# Navigate to phase2 directory
cd /path/to/streamlit/phase2

# Check latest commit
git log --oneline -1
# Should show: 01c7c89 (or later)

# Verify working tree is clean
git status
# Should show: "nothing to commit, working tree clean"

# Pull latest from GitHub
git pull origin main
```

### Step 2: Verify App Still Works
```bash
# Run the app locally
streamlit run apps/exam_prep_master.py

# Should open at: http://localhost:8501
# Login with any username
# Navigate through chapters
# Run a quiz to verify everything works
```

### Step 3: Read Key Documents (40 minutes)
Read in this order:
1. **SESSION_FREEZE_CHECKLIST.md** (5 min) - What's frozen
2. **NEXT_SESSION_START.md** (10 min) - How to begin
3. **FAST_TRACK_IMPLEMENTATION_PLAN.md** (15 min) - Your roadmap
4. **QUESTION_ROTATION_PLAN.md** (15 min) - Technical details

**Total**: ~45 minutes of reading before coding

---

## 🚀 IMPLEMENTATION TIMELINE (Days 1-5)

### Day 1: Tier 1 Database Setup (4-5 hours)

#### Task 1.1: Create question_history Table
**File**: `apps/exam_prep_master.py` (around line 1000)

**Add this code**:
```python
def create_question_history_table():
    """Create question_history table to track user questions"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            chapter TEXT,
            quiz_mode TEXT,
            first_seen_date TEXT,
            last_seen_date TEXT,
            times_seen INTEGER DEFAULT 1,
            times_correct INTEGER DEFAULT 0,
            times_incorrect INTEGER DEFAULT 0,
            max_difficulty_attempted TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            UNIQUE(user_id, question_id, quiz_mode)
        )
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_user_quiz 
        ON question_history(user_id, quiz_mode)
    """)
    
    conn.commit()
    conn.close()

# Call this when app starts
create_question_history_table()
```

**Verification**:
- [ ] Function created
- [ ] No syntax errors
- [ ] App runs without errors
- [ ] Commit to git

#### Task 1.2: Create question_queue Table
**File**: `apps/exam_prep_master.py` (after Task 1.1)

**Add this code**:
```python
def create_question_queue_table():
    """Create question_queue table to manage next questions"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_queue (
            queue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            chapter TEXT,
            queue_type TEXT,
            difficulty_level TEXT,
            added_date TEXT,
            priority INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_queue_user 
        ON question_queue(user_id)
    """)
    
    conn.commit()
    conn.close()

# Call this when app starts
create_question_queue_table()
```

**Verification**:
- [ ] Function created
- [ ] No syntax errors
- [ ] App runs without errors
- [ ] Commit to git

#### Task 1.3: Implement Tracking Function
**File**: `apps/exam_prep_master.py` (after table creation)

**Add this code**:
```python
def track_question_answer(user_id, question_id, is_correct, difficulty):
    """Track user's answer and update question history"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Update or insert into question_history
    cursor.execute("""
        INSERT OR REPLACE INTO question_history 
        (user_id, question_id, last_seen_date, times_seen, 
         times_correct, times_incorrect, max_difficulty_attempted)
        SELECT 
            ?, ?, ?, 
            COALESCE((SELECT times_seen FROM question_history 
                     WHERE user_id=? AND question_id=?), 0) + 1,
            COALESCE((SELECT times_correct FROM question_history 
                     WHERE user_id=? AND question_id=?), 0) + ?, 
            COALESCE((SELECT times_incorrect FROM question_history 
                     WHERE user_id=? AND question_id=?), 0) + ?,
            ?
    """, (
        user_id, question_id, datetime.now().isoformat(),
        user_id, question_id,  # For times_seen
        user_id, question_id, (1 if is_correct else 0),  # For times_correct
        user_id, question_id, (0 if is_correct else 1),  # For times_incorrect
        difficulty  # max_difficulty
    ))
    
    # If wrong answer, add to queue with higher difficulty
    if not is_correct:
        new_difficulty = get_harder_difficulty(difficulty)
        cursor.execute("""
            INSERT INTO question_queue 
            (user_id, question_id, queue_type, difficulty_level, added_date, priority)
            VALUES (?, ?, 'wrong_answer', ?, ?, ?)
        """, (user_id, question_id, new_difficulty, 
              datetime.now().isoformat(), 10))
    
    conn.commit()
    conn.close()
```

**Helper function** (add before track_question_answer):
```python
def get_harder_difficulty(current_difficulty):
    """Get next difficulty level"""
    difficulty_levels = {
        'easy': 'medium',
        'medium': 'hard',
        'hard': 'hard'  # Stay at hard
    }
    return difficulty_levels.get(current_difficulty, 'hard')
```

**Verification**:
- [ ] Function created
- [ ] Helper function added
- [ ] No syntax errors
- [ ] Imports added (datetime if needed)
- [ ] Commit to git

#### Day 1 Verification
```bash
# Test locally
streamlit run apps/exam_prep_master.py

# Verify:
- [ ] App starts without errors
- [ ] Can login
- [ ] Can take a quiz
- [ ] No database errors in console

# Commit
git add apps/exam_prep_master.py
git commit -m "Feat: Add question_history & question_queue tables + tracking function"
git push origin main
```

---

### Day 2: Tier 1 Selection Logic (4-5 hours)

#### Task 2.1: Implement Selection Function
**File**: `apps/exam_prep_master.py` (after tracking function)

**Add this code**:
```python
def queue_next_question(user_id, chapter, quiz_mode):
    """Get next question based on user's history and queue"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Get next question from queue (priority order)
    cursor.execute("""
        SELECT question_id, queue_type, difficulty_level 
        FROM question_queue
        WHERE user_id = ? AND chapter = ?
        ORDER BY 
            CASE queue_type
                WHEN 'wrong_answer' THEN 1
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
        return next_q
    return None  # No more queued questions

def get_next_question(user_id, chapter, quiz_mode, all_questions):
    """Smart question selection with history tracking"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Check queue first
    queued = queue_next_question(user_id, chapter, quiz_mode)
    if queued:
        question_id, queue_type, difficulty = queued
        # Find the actual question
        for q in all_questions:
            if q['id'] == question_id:
                return q, difficulty
    
    # If no queued question, get new ones
    cursor.execute("""
        SELECT question_id FROM question_history
        WHERE user_id = ? AND quiz_mode = ?
    """, (user_id, quiz_mode))
    
    seen_questions = {row[0] for row in cursor.fetchall()}
    conn.close()
    
    # Filter out seen questions
    unseen = [q for q in all_questions 
              if q['id'] not in seen_questions]
    
    if unseen:
        return random.choice(unseen), 'easy'
    
    # All questions seen, restart
    return random.choice(all_questions), 'easy'
```

**Verification**:
- [ ] Functions created
- [ ] No syntax errors
- [ ] Logic is clear
- [ ] Imports included (random)
- [ ] Commit to git

#### Task 2.2: Integrate into Quiz Flow
**File**: `apps/exam_prep_master.py` (in quiz functions section)

For **Mock Exam**, find the section where questions are selected and modify:
```python
# OLD CODE (find this):
# question = get_random_question(chapter)

# NEW CODE (replace with):
difficulty = 'easy'  # Default
question, difficulty = get_next_question(
    user_id, chapter, 'mock_exam', all_questions
)
```

Do the same for **Challenge Mode** and **Practice Mode**.

After user answers:
```python
# After getting user answer:
is_correct = user_answer == question['answer']

# Track the answer
track_question_answer(user_id, question['id'], is_correct, difficulty)
```

**Verification**:
- [ ] Integration points found
- [ ] Calls added in quiz flow
- [ ] Variables passed correctly
- [ ] App runs without errors
- [ ] Quiz questions now tracked
- [ ] Commit to git

#### Day 2 Verification
```bash
# Test locally
streamlit run apps/exam_prep_master.py

# Verify:
- [ ] Take a quiz (answer 5+ questions)
- [ ] Check database for records in question_history
- [ ] Take another quiz - questions should not repeat
- [ ] Answer one wrong - should reappear later

# Check database directly:
sqlite3 session_data.db
sqlite> SELECT * FROM question_history LIMIT 5;
sqlite> SELECT * FROM question_queue LIMIT 5;

# Commit
git add apps/exam_prep_master.py
git commit -m "Feat: Implement question selection logic with history tracking"
git push origin main
```

---

### Day 3: Tier 2 Templates & Generation (5-6 hours)

#### Task 3.1: Design Parameterized Templates
**File**: Create `src/components/question_templates.py`

**Add this code**:
```python
# Question templates with parameters
QUESTION_TEMPLATES = {
    'evaporation_amount': {
        'template': 'Water at {temp}°C evaporates. How much becomes vapor?',
        'answer_formula': lambda p: f"{p['temp']}%",
        'parameters': {
            'temp': [15, 20, 25, 30, 35, 40, 45, 50],
            'time': [30, 60, 90, 120],
        },
        'difficulty': 'hard',
        'chapter': 'water'
    },
    # ... Add 19 more templates
}
```

**Verification**:
- [ ] At least 20 templates designed
- [ ] Each has all required fields
- [ ] Answer formulas are correct
- [ ] File saved

#### Task 3.2: Build Variation Generator
**File**: `apps/exam_prep_master.py` (add function)

**Add this code**:
```python
def generate_question_variation(template, num_variations=10):
    """Generate N variations from a template"""
    variations = []
    
    for _ in range(num_variations):
        # Sample random parameters
        params = {}
        for param_name, param_values in template['parameters'].items():
            params[param_name] = random.choice(param_values)
        
        # Create question with sampled values
        variation = {
            'template_id': template.get('template_id'),
            'text': template['template'].format(**params),
            'answer': template['answer_formula'](params),
            'difficulty': template['difficulty'],
            'chapter': template['chapter'],
            'params': params
        }
        variations.append(variation)
    
    return variations

def generate_all_variations():
    """Generate 2,280 variations (228 questions × 10 each)"""
    from src.components.question_templates import QUESTION_TEMPLATES
    
    all_variations = []
    for template_id, template in QUESTION_TEMPLATES.items():
        variations = generate_question_variation(template, 10)
        all_variations.extend(variations)
    
    return all_variations
```

**Verification**:
- [ ] Functions created
- [ ] Logic is correct
- [ ] Imports added
- [ ] Commit to git

#### Task 3.3: Integrate Variations
**File**: `apps/exam_prep_master.py` (modify get_next_question)

**Update the function**:
```python
def get_next_question(user_id, chapter, quiz_mode, all_questions):
    """Smart selection with variations"""
    # ... existing code ...
    
    # If many questions seen, use variations
    if len(seen_questions) > 100:
        # Generate variations of unseen templates
        variations = generate_all_variations()
        return random.choice(variations), 'easy'
    
    # ... rest of existing code ...
```

**Verification**:
- [ ] Integration complete
- [ ] Variations generated on demand
- [ ] No duplicates
- [ ] Performance acceptable
- [ ] Commit to git

#### Day 3 Verification
```bash
# Test locally
streamlit run apps/exam_prep_master.py

# Verify:
- [ ] Templates load without errors
- [ ] Variations generate correctly
- [ ] 2,280 total variations (228 × 10)
- [ ] Questions are different each time
- [ ] Parameters vary correctly

# Commit
git add apps/exam_prep_master.py src/components/question_templates.py
git commit -m "Feat: Add question variations generator (Tier 2)"
git push origin main
```

---

### Days 4-5: Testing, Deployment, & Lock

#### Day 4: Testing
Use **TESTING_CHECKLIST.md** (all 30+ test cases):
- [ ] All tests passed
- [ ] No critical bugs
- [ ] Performance acceptable
- [ ] Deploy to Streamlit Cloud

#### Day 5: Documentation & Lock
- [ ] Update README.md
- [ ] Create GitHub Release v4.2
- [ ] Final commit
- [ ] Mark Phase 2 complete

---

## 📋 DAILY CHECKLIST TEMPLATE

Use this for each day:

```markdown
### Day X (Date) - [Task Name]

**Morning**:
- [ ] Read relevant documentation
- [ ] Understand today's tasks
- [ ] Review code changes needed

**Work**:
- [ ] Task 1 complete
- [ ] Task 2 complete
- [ ] Task 3 complete

**Testing**:
- [ ] Local verification passed
- [ ] No console errors
- [ ] Functionality confirmed

**Evening**:
- [ ] Code committed
- [ ] Push to GitHub
- [ ] Ready for next day

**Blockers/Issues**:
[Note any problems encountered]

**Next Day Plan**:
[Summarize what's next]
```

---

## 🚨 IF YOU GET STUCK

### Problem: App won't run
```bash
# Check for syntax errors
python -m py_compile apps/exam_prep_master.py

# Check git status
git status

# Try reverting last change
git diff HEAD~1
git checkout HEAD -- apps/exam_prep_master.py
```

### Problem: Database errors
```bash
# Check database exists
sqlite3 session_data.db ".tables"

# Check tables created
sqlite3 session_data.db ".schema question_history"

# Clear database if corrupted
rm session_data.db
# (App will recreate it on next run)
```

### Problem: Questions not tracking
```bash
# Verify function is called
# Add debug print: print(f"Tracked: {question_id}, {is_correct}")

# Check database
sqlite3 session_data.db "SELECT * FROM question_history;"
```

---

## 📞 REFERENCE DOCUMENTS

Keep these open while working:

| Need | Document |
|------|----------|
| Overall plan | FAST_TRACK_IMPLEMENTATION_PLAN.md |
| Technical details | QUESTION_ROTATION_PLAN.md |
| Testing | TESTING_CHECKLIST.md |
| Current state | PHASE_2_CURRENT_STATE.md |
| File locations | DIRECTORY_STRUCTURE_REFERENCE.md |

---

## ✅ SUCCESS CHECKLIST (End of Session)

- [ ] Tier 1 fully implemented
- [ ] Tier 2 fully implemented
- [ ] All tests passed
- [ ] Deployed to cloud
- [ ] v4.2 released on GitHub
- [ ] Documentation updated
- [ ] Phase 2 marked LOCKED
- [ ] Session closed

**When all above are done → Phase 2 is complete!**

---

**Ready to Resume?** Start with NEXT_SESSION_START.md  
**Need Clarity?** Check FAST_TRACK_IMPLEMENTATION_PLAN.md  
**Code Help?** Check QUESTION_ROTATION_PLAN.md  

