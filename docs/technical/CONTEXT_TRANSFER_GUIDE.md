# Context Transfer Guide - Phase 2C Science App
## Complete Knowledge Base for Resuming Development in New Context Windows

**Last Updated**: 2026-05-16  
**Current Phase**: Week 3 (Module Integration) ✅ COMPLETE  
**Next Phase**: Week 4 (Interactive Labs) ⏭️  
**App Status**: 🟢 Running at http://localhost:8503

---

## EXECUTIVE SUMMARY (Read This First)

### What Is This Project?
A comprehensive Streamlit science learning app for **Aanya**, a 10-year-old Primary 5 student at **Waterway Primary School, Singapore**. The app focuses on MOE Primary 5 curriculum with gamification, PSLE exam preparation, and textbook alignment.

### Current State (as of 2026-05-16)
- ✅ **Exam Prep App**: `app_exam_prep_pro.py` - FROZEN for Aanya's 3-day exam prep
- ✅ **Phase 2 Main App**: `app_phase2.py` - Running with 228 textbook-aligned questions
- ✅ **6 Chapters**: Ch1-6 complete with 90 flashcards + 90 matching + 48 MCQ
- ✅ **Integration**: Week 3 complete - all modules loaded and displaying correctly

### Critical Files
```
phase2/
├── app_exam_prep_pro.py          🔒 FROZEN (exam prep)
├── app_phase2.py                 ✅ Main app (228 questions live)
├── modules/
│   ├── ch1_reproduction_new.py   ✅ Reproduction (15+15+8 questions)
│   ├── ch2_water_new.py          ✅ Water Cycles (15+15+8 questions)
│   ├── ch3_plant_new.py          ✅ Plant Transport (15+15+8 questions)
│   ├── ch4_human_new.py          ✅ Human Systems (15+15+8 questions)
│   ├── ch5_electrical_new.py     ✅ Electrical (15+15+8 questions)
│   └── ch6_circuits_new.py       ✅ Circuits (15+15+8 questions)
├── components/
│   ├── brain_drainers.py         (PSLE tricky questions)
│   ├── animations.py             (Maltese dog feedback)
│   ├── gamification.py           (XP, badges, streaks)
│   └── minigames.py              (Interactive games)
├── utils/
│   ├── state_manager.py          (Session state persistence)
│   └── data_utils.py             (Utility functions)
└── config.py                     (Student name, school, settings)
```

---

## PHASE TIMELINE & COMPLETION STATUS

### ✅ COMPLETED PHASES

#### Phase 2C Week 1 (May 16-22): Content Extraction
**Objective**: Extract MOE textbook content and create flashcards/matching pairs  
**Deliverable**: 6 chapter modules with 228 textbook-aligned questions
**Status**: ✅ COMPLETE

**What Was Done**:
- Read Inspiring Science P5 textbook (all 120 pages)
- Extracted key definitions for each chapter
- Created flashcard sets (15 per chapter = 90 total)
- Created matching pairs (15 per chapter = 90 total)
- Created MCQ questions (8 per chapter = 48 total)
- Tagged every question with exact textbook page reference

**Files Created**:
- `ch1_reproduction_new.py` - Pages 2-25
- `ch2_water_new.py` - Pages 26-49
- `ch3_plant_new.py` - Pages 52-63
- `ch4_human_new.py` - Pages 64-87
- `ch5_electrical_new.py` - Pages 88-104
- `ch6_circuits_new.py` - Pages 105-120

**Why "_new" Suffix**: To preserve old files and allow parallel testing before full migration

---

#### Phase 2C Week 2 (May 23-29): Brain Drainers
**Objective**: Create 50+ PSLE-style tricky questions per chapter  
**Deliverable**: 84+ brain drainer questions with trap answer explanations
**Status**: ✅ COMPLETE

**What Was Done**:
- Analyzed common PSLE misconceptions (from exam scope document)
- Created questions with trap answers
- Added explanations for why wrong answers are tricky
- Organized by difficulty: Easy (🟡), Medium (🟠), Hard (🔴)
- Included textbook page references for each

**Files Created/Updated**:
- `brain_drainers_phase2c.py` - 84+ questions with explanations
- `exam_questions_extended.py` - Additional advanced questions

**Brain Drainer Question Structure**:
```python
{
    'type': 'MCQ' or 'STRUCT',
    'topic': 'Chapter name',
    'q': 'Question text',
    'options': ['A', 'B', 'C', 'D'],
    'answer': 'Correct answer',
    'explanation': 'Why this answer',
    'ref': 'Page X',
    'difficulty': 'easy|medium|hard'
}
```

---

#### Phase 2C Week 3 (May 30-June 5): Module Integration
**Objective**: Integrate all 6 chapter modules into app_phase2.py  
**Deliverable**: All 228 questions live and running
**Status**: ✅ COMPLETE (TODAY - May 16)

**What Was Done**:
1. Updated `app_phase2.py` chapter loading logic:
   - Changed imports from old files to `_new` versions
   - Added function call to `show_chapter()` from each module
   - Added error handling for missing functions

2. Verified integration:
   - All 6 chapter modules load without errors
   - Flashcards display with page references
   - Matching pairs shuffle correctly
   - MCQ options render properly
   - Maltese dog feedback triggers on answers

3. Tested user flow:
   - Navigation: Home → Chapters → Select Chapter ✅
   - Each chapter shows 3 tabs: Flashcards, Matching, Quiz ✅
   - Progress tracking works ✅
   - No console errors ✅

**Code Change in app_phase2.py (Lines 45-61)**:
```python
# BEFORE
from modules import ch1_reproduction  # Old version
# ... just imports, no display

# AFTER  
from modules import ch1_reproduction_new as chapter_module  # New textbook version
if hasattr(chapter_module, 'show_chapter'):
    chapter_module.show_chapter()  # Now displays content
```

---

### ⏭️ UPCOMING PHASES

#### Phase 2C Week 4 (June 6-12): Interactive Labs
**Objective**: Create interactive simulators for hands-on learning  
**Priority**: HIGH - Critical for engagement

**What Will Be Built**:

**Chapter 2 (Water)**:
- State change simulator: Ice → Water → Steam visualization
- Temperature slider (0°C, 100°C phase changes)
- Water cycle animation: Evaporation → Condensation → Precipitation
- Real-time particle animations showing state changes

**Chapter 3 (Plant)**:
- Xylem vs. Phloem comparison visual
- Transport pathway animation
- Root hair absorption simulation
- Transpiration process diagram

**Chapter 4 (Human)**:
- Diaphragm breathing animation
- Lung expansion/compression mechanics
- Pulse measurement activity
- Healthy vs. smoker's lungs comparison

**Chapter 6 (Circuits)** - Most Important:
- Dynamic circuit builder (drag batteries, bulbs, wires)
- Series vs. Parallel comparison side-by-side
- Real-time Ohm's Law calculation (V=I×R)
- Voltage drop visualization
- Current flow animation

**Implementation Approach**:
- Use Streamlit Canvas or Plotly for animations
- Create reusable simulator template
- Each simulator should tie to specific textbook concepts
- Include "Learning Message" at completion

---

#### Phase 2C Week 5 (June 13-19): Validation with Aanya
**Objective**: Test with actual user and refine  
**Method**:
1. Have Aanya use the app
2. Ask: "Do you recognize this from your textbook?"
3. Collect feedback on:
   - Question difficulty appropriateness
   - Animation smoothness
   - Navigation clarity
   - Overall engagement
4. Make refinements based on feedback

---

## ARCHITECTURE OVERVIEW

### App Structure
```
User Opens http://localhost:8503
        ↓
    Sidebar Navigation (8 pages)
    ├─ 🏠 Home (Dashboard)
    ├─ 📖 Chapters (Learn from textbook)
    ├─ 🧠 Brain Drainers (PSLE practice)
    ├─ 🎮 Mini-Games (Interactive games)
    ├─ 🏆 Achievements (Badges & rewards)
    ├─ 📊 Progress (Stats & tracking)
    ├─ ⚙️ Settings (Preferences)
    └─ Daily Challenge (Daily quest)
        ↓
    Each Page Components
    ├─ GameManager (XP, streaks, levels)
    ├─ Animations (Maltese dog reactions)
    ├─ State Manager (Progress persistence)
    └─ Content Modules (Chapter data)
```

### Chapter Module Structure (Template)
Every `ch*_new.py` file has this structure:
```python
# 1. FLASHCARDS: List of concept-definition pairs
FLASHCARDS = [
    {'concept': 'Term', 'definition': 'From textbook', 'ref': 'Page X'},
    ...
]

# 2. MATCHING PAIRS: List of term-definition tuples
MATCHING_PAIRS = [
    ('Term', 'Definition'),
    ...
]

# 3. MCQ QUESTIONS: List of multiple choice questions
MCQ_QUESTIONS = [
    {
        'q': 'Question?',
        'options': ['A', 'B', 'C', 'D'],
        'answer': 'B',
        'explanation': 'Why B is correct',
        'difficulty': 'easy|medium|hard'
    },
    ...
]

# 4. DISPLAY FUNCTIONS
def show_flashcards(): ...
def show_matching(): ...
def show_quiz(): ...
def show_chapter():  # Main entry point
    tabs = [Flashcards, Matching, Quiz]
    # Display all three
```

### Key Components

**StateManager** (`utils/state_manager.py`):
- Manages session state (XP, level, streak, achievements)
- Tracks chapter progress
- Persists progress to localStorage
- Handles user profile initialization

**XPSystem** (`components/gamification.py`):
- Awards XP for quiz completion
- Calculates level progression
- Manages streak counting
- Handles achievement unlocking

**MalteseDogFeedback** (`components/animations.py`):
- Shows happy Maltese on correct answers
- Shows sad Maltese on wrong answers
- Personalizes messages with Aanya's name
- Provides celebration effects

**BrainDrainerQuestions** (`components/brain_drainers.py`):
- Manages PSLE-style tricky questions
- Filters by difficulty and chapter
- Tracks performance on tricky questions
- Shows explanations for trap answers

---

## CRITICAL KNOWLEDGE

### How to Add a New Question to a Chapter

**File**: `phase2/modules/ch1_reproduction_new.py` (example for Chapter 1)

**To Add a Flashcard**:
```python
FLASHCARDS = [
    # ... existing cards
    {'concept': 'New Term', 'definition': 'Definition from textbook', 'ref': 'Page XX'},
]
```

**To Add a Matching Pair**:
```python
MATCHING_PAIRS = [
    # ... existing pairs
    ('Term', 'Definition or description'),
]
```

**To Add an MCQ**:
```python
MCQ_QUESTIONS = [
    # ... existing questions
    {
        'q': 'What is X?',
        'options': ['Option A', 'Option B (correct)', 'Option C', 'Option D'],
        'answer': 'Option B (correct)',
        'explanation': 'Why this is the right answer from textbook',
        'difficulty': 'easy'  # or 'medium' or 'hard'
    },
]
```

**IMPORTANT**: 
- Always include page reference in explanation
- Never add content not in the textbook
- Maintain difficulty distribution (roughly 1/3 easy, 1/3 medium, 1/3 hard)

---

## HOW TO RUN THE APP

### Start Phase 2 App (Main App)
```bash
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
streamlit run app_phase2.py
# Opens at: http://localhost:8503
```

### Start Exam Prep App (Frozen)
```bash
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
streamlit run app_exam_prep_pro.py
# Opens at: http://localhost:8503 (or different port if 8503 in use)
```

### Kill Streamlit Process
```bash
# Windows PowerShell
Get-Process streamlit | Stop-Process -Force
```

---

## CONFIGURATION & PERSONALIZATION

**File**: `config.py`

```python
STUDENT_NAME = "Aanya"
SCHOOL_NAME = "Waterway Primary School"
SCHOOL_LOCATION = "Punggol, Singapore"
CURRICULUM = "MOE Primary 5"

CHAPTERS = {
    'Ch1_Reproduction': {
        'title': '👶 Reproduction in Animals & Plants',
        'description': 'Learn how living things reproduce',
        'emoji': '👶',
        'textbook_pages': '2-25'
    },
    # ... etc for Ch2-6
}

def get_student_message(key):
    messages = {
        'welcome': f"🌟 Welcome, {STUDENT_NAME}! Ready to master science? 🌟",
        'dashboard_location': f"📍 {SCHOOL_NAME}, {SCHOOL_LOCATION}",
        # ... etc
    }
    return messages.get(key, '')
```

### How to Personalize for a Different Student
1. Change `STUDENT_NAME` to student's actual name
2. Update `SCHOOL_NAME` and `SCHOOL_LOCATION`
3. All messages automatically update with personalization

---

## CONTENT STRUCTURE & TEXTBOOK MAPPING

### Textbook Details
- **Book**: Inspiring Science P5 (Foundation)
- **Authors**: Tan Aik Ling & Jennifer Yeo
- **Pages**: 2-120 (6 chapters covered)
- **Format**: MOE Primary 5 Curriculum

### Chapter Breakdown

| Chapter | Theme | Pages | Focus | Textbook |
|---------|-------|-------|-------|----------|
| 1. Reproduction | Cycles | 2-25 | Animal & plant reproduction | WOW germination, inherited traits |
| 2. Water Cycles | Cycles | 26-49 | States of water, phase changes | Melting (0°C), boiling (100°C) |
| 3. Plant Transport | Systems | 52-63 | Xylem/phloem, transpiration | Transport pathways, water movement |
| 4. Human Systems | Systems | 64-87 | Respiratory & circulatory | 21% O₂ inhaled, 16% exhaled |
| 5. Electrical Systems | Systems | 88-104 | Circuits, conductors, insulators | Circuit symbols, safety |
| 6. Series Circuits | Systems | 105-120 | Series effects, Ohm's Law | V=I×R, voltage division |

### Common Misconceptions (Brain Drainer Focus)
1. ❌ **Pollination = Fertilization** → NO! Fertilization must follow pollination
2. ❌ **Water vapor is visible** → NO! Steam is visible, vapor is invisible
3. ❌ **Series bulbs stay bright with more bulbs** → NO! All get dimmer
4. ❌ **Heat above 100°C makes water hotter** → NO! Latent heat used for evaporation

---

## KNOWN ISSUES & SOLUTIONS

### Issue 1: Streamlit Version Compatibility
**Problem**: `use_container_width` parameter not recognized  
**Solution**: Use try/except block:
```python
try:
    st.image(url, use_container_width=True)
except TypeError:
    st.image(url, use_column_width=True)
```

### Issue 2: Chapter Module Import Errors
**Problem**: Module not found when changing filenames  
**Solution**: Verify `_new` suffix in imports:
```python
# CORRECT
from modules import ch1_reproduction_new as chapter_module

# WRONG
from modules import ch1_reproduction  # Old version
```

### Issue 3: Page References Not Showing
**Problem**: Flashcards/MCQ don't display page numbers  
**Solution**: Ensure `'ref': 'Page XX'` in every question dict

---

## COMMON TASKS & HOW TO DO THEM

### Task 1: Add 5 New Flashcards to Chapter 2
1. Open `phase2/modules/ch2_water_new.py`
2. Find `FLASHCARDS = [...]`
3. Add 5 new dicts at the end
4. Format: `{'concept': 'X', 'definition': 'From textbook', 'ref': 'Page XX'}`
5. Save file
6. Restart app - flashcards auto-load

### Task 2: Fix a Wrong Answer in Chapter 3 MCQ
1. Open `phase2/modules/ch3_plant_new.py`
2. Find the incorrect MCQ in `MCQ_QUESTIONS`
3. Change 'answer' or 'options' or 'explanation'
4. Save file
5. Restart app - question auto-updates

### Task 3: Add a Brain Drainer Question
1. Open `components/brain_drainers.py`
2. Find the chapter's question list
3. Add new question dict with full structure
4. Include: type, q, options, answer, explanation, difficulty, ref
5. Save file
6. Brain drainer automatically includes new question

### Task 4: Create New Interactive Lab
1. Create new function in appropriate chapter module
2. Use Streamlit components (st.slider, st.button, st.pyplot, etc.)
3. Add as new tab in `show_chapter()`
4. Include learning message at completion
5. Award XP for completion

---

## MEMORY & CONTEXT REFERENCES

### Where to Find Info
- **Phase 1 Code**: `C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\app.py`
- **Textbook**: `C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2\974695525-InspiringScience-P5-Textbook-FDN-Opal-Unlocked.pdf`
- **Exam Scope**: `C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2\WAPS Assessment Scope_P5 2026_20260515_202726.pdf`
- **Memory Files**: `C:\Users\harry\.claude\projects\C--Users-harry-OneDrive-AAIA-Aanya-streamlit\memory\*.md`

### Important Memory Files
1. **phase2c_completion.md** - Week 1 & 2 work (228 questions created)
2. **phase2c_textbook_alignment_plan.md** - Full curriculum analysis
3. **phase2c_week3_integration.md** - Week 3 integration details

---

## NEXT STEPS FOR RESUMING DEVELOPMENT

### If Resuming in Week 4 (Interactive Labs)
1. **Start with Chapter 2** (Water) - highest engagement impact
2. Use Streamlit Canvas or Plotly for state change animations
3. Create reusable simulator template
4. Link each lab to specific textbook diagrams
5. Test with Aanya before moving to other chapters

### If Resuming in Week 5 (Validation)
1. Deploy app to Aanya
2. Have her verify: "Is this from your textbook?"
3. Collect feedback on difficulty and clarity
4. Identify any gaps vs. actual textbook
5. Make quick refinements

### If Starting Something New
1. Always cross-reference with TEXTBOOK first
2. Never add content outside MOE P5 syllabus
3. Tag every question/definition with page reference
4. Test on different devices (desktop, tablet)
5. Verify Maltese dog feedback triggers correctly

---

## QUICK REFERENCE

### File Locations (Windows)
```
C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2\
├── app_phase2.py                (Main app)
├── app_exam_prep_pro.py         (Frozen exam app)
├── modules\ch*_new.py           (6 chapter modules)
├── components\                  (gamification, animations, etc.)
├── utils\                       (state_manager, data_utils)
└── TEXTBOOK PDF                 (Reference for all content)
```

### Git/Version Control
- **Not currently in git** (local development only)
- **No GitHub remote** (desktop app)
- Backup strategy: Save context transfer docs regularly

### Python Version & Dependencies
- Python 3.9+
- Streamlit 1.X
- See `requirements.txt` for full list
- Install: `pip install -r requirements.txt`

---

## FINAL CHECKLIST FOR CONTEXT TRANSFER

When resuming in a new context window, verify:
- [ ] Read this file (context transfer guide)
- [ ] Check Phase 2C Memory files (phase2c_*.md)
- [ ] Review EXAM_PREP_GUIDE.md for Aanya's exam context
- [ ] Verify app runs at http://localhost:8503
- [ ] Confirm all 6 chapter modules load
- [ ] Check that chapter selection shows correct tabs
- [ ] Verify Maltese dog feedback works
- [ ] Review next week's phase plan

---

**Document Version**: 1.0  
**Last Updated**: 2026-05-16  
**Maintained By**: Claude (AI Assistant)  
**For**: Resuming Phase 2C development in new context windows

---

**Key Principle**: This document is the "single source of truth" for understanding the project without reading code. Keep it updated as you make changes!
