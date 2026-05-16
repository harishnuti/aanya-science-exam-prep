# 📁 DIRECTORY STRUCTURE REFERENCE
## Complete File Organization & Naming Conventions
**Status**: Organized and ready for next session  
**Last Updated**: May 16, 2026  

---

## 🗂️ COMPLETE DIRECTORY MAP

```
phase2/
│
├── 📄 Root Documentation (Critical - Read These First)
│   ├── SESSION_FREEZE_CHECKLIST.md ✅ (What's frozen, what's ready)
│   ├── NEXT_SESSION_START.md ✅ (How to begin next session)
│   ├── PHASE_2_CURRENT_STATE.md ✅ (Current code status)
│   ├── DIRECTORY_STRUCTURE_REFERENCE.md ✅ (This file)
│   ├── CONTINUATION_GUIDE.md ⏳ (How to continue - pending)
│   ├── EMERGENCY_SESSION_NOTES.md ⏳ (For emergencies - pending)
│   │
│   ├── 📋 Implementation Plans
│   ├── FAST_TRACK_IMPLEMENTATION_PLAN.md ✅ (Main reference)
│   ├── QUESTION_ROTATION_PLAN.md ✅ (Technical design)
│   ├── AANYA_FEEDBACK_QUESTION_VARIETY.md ✅ (Context)
│   ├── START_HERE_IMPLEMENTATION.md ✅ (Quick start)
│   ├── IMPLEMENTATION_FOCUS_NOTE.md ✅ (Approach explanation)
│   │
│   ├── 🧪 Testing & Documentation
│   ├── TESTING_CHECKLIST.md ✅ (30+ test cases)
│   ├── BUG_REPORT_TEMPLATE.md ✅ (Standard format)
│   ├── TESTING_PHASE_START_MESSAGE.md ✅
│   ├── DAYS_1_2_TESTING_PHASE_START.md ✅
│   │
│   ├── 📚 Reference Docs
│   ├── PHASE_2_2WEEK_SPRINT_SUMMARY.md ✅
│   ├── PHASE_2_COMPLETION_2WEEK_PLAN.md ✅
│   ├── PHASE_2_MASTER_COMPLETION_CHECKLIST.md ✅
│   ├── PHASE_2_COMPLETION_DOCUMENTATION_INDEX.md ✅
│   ├── PHASE_2_SPRINT_STATUS_DASHBOARD.md ✅
│   ├── WEEK_1_KICKOFF_SUMMARY.md ✅
│   │
│   ├── README.md ✅ (Project overview)
│   ├── requirements.txt ✅ (Python dependencies)
│   └── streamlit.app (Streamlit Cloud config)
│
├── 📂 apps/ (Main Application Code)
│   ├── exam_prep_master.py ✅ (PRIMARY FILE - Main app, 2,300+ lines)
│   │   └── Where to make changes for Tier 1 & 2
│   ├── exam_prep_pro.py (Legacy - don't modify)
│   └── legacy/ (Archived older versions)
│       ├── exam_prep_v1.py
│       ├── exam_prep_v2.py
│       └── exam_prep_v3.py
│
├── 📂 modules/ (Chapter Content Modules)
│   ├── ch1_reproduction.py ✅ (Chapter 1: Reproduction)
│   ├── ch2_water.py ✅ (Chapter 2: Water Cycles)
│   ├── ch3_plant.py ✅ (Chapter 3: Plant Transport)
│   ├── ch4_human.py ✅ (Chapter 4: Human Systems)
│   ├── ch5_electrical.py ✅ (Chapter 5: Electrical Systems)
│   ├── ch6_circuits.py ✅ (Chapter 6: Electric Circuits)
│   │
│   ├── ch1_reproduction_new.py (Enhanced version)
│   ├── ch2_water_new.py (Enhanced version)
│   ├── ch3_plant_new.py (Enhanced version)
│   ├── ch4_human_new.py (Enhanced version)
│   ├── ch5_electrical_new.py (Enhanced version)
│   └── ch6_circuits_new.py (Enhanced version)
│
├── 📂 components/ (Reusable Components)
│   ├── gamification.py ✅ (XP, levels, badges)
│   ├── animations.py ✅ (Lottie, effects)
│   ├── minigames.py ✅ (Drag-drop, puzzles)
│   ├── brain_drainers.py ✅ (PSLE questions)
│   ├── state_manager.py ✅ (Session state)
│   └── __pycache__/ (Cache - auto-generated)
│
├── 📂 src/ (Source Utilities)
│   ├── components/ (Additional components)
│   │   ├── circuit_generator.py
│   │   └── __pycache__/
│   ├── data/ (Data utilities)
│   │   └── __pycache__/
│   └── __pycache__/
│
├── 📂 docs/ (Documentation Organization)
│   ├── deployment/ (Deployment guides)
│   ├── features/ (Feature specifications)
│   ├── technical/ (Technical documentation)
│   ├── roadmap/ (Phase roadmaps)
│   │   └── PHASE_3_ROADMAP_DETAILED.md
│   └── version_history/ (Version notes)
│
├── 📂 resources/ (Assets & Curriculum)
│   ├── curriculum/ (MOE curriculum references)
│   │   └── p5_science_syllabus/
│   └── images/ (Images, icons, sprites)
│
├── 📂 .git/ (Git Repository)
│   └── (Git internal files - don't modify)
│
└── 📂 __pycache__/ (Cache - auto-generated)
    └── (Python cache - ignore)
```

---

## 🎯 WHAT TO MODIFY (Next Session)

### PRIMARY FILE TO MODIFY
```
apps/exam_prep_master.py
├─ Around line 1000: Add database table creation
├─ New section: Add tracking functions
├─ Around line 1500: Modify quiz selection logic
├─ New section: Add variation generator
└─ Around line 2000: Integrate into quiz modes
```

### FILES TO READ (Don't modify)
```
modules/ch*.py
├─ Reference for question structure
└─ May need minor updates for Tier 2
```

### FILES TO LEAVE ALONE
```
- exam_prep_pro.py (legacy, don't touch)
- legacy/ folder (archived versions)
- .git/ (git internal)
- __pycache__/ (auto-generated)
```

---

## 📋 NAMING CONVENTIONS

### Python Files
```
✅ Correct:
- exam_prep_master.py (snake_case)
- ch1_reproduction.py (snake_case)
- question_rotation.py (snake_case)

❌ Avoid:
- ExamPrepMaster.py (PascalCase)
- exam-prep-master.py (kebab-case)
```

### Functions
```
✅ Correct:
- def track_question_answer(user_id, question_id):
- def queue_next_question(user_id):
- def generate_question_variation(template):

❌ Avoid:
- def TrackQuestionAnswer():
- def queue-next-question():
```

### Variables
```
✅ Correct:
- question_history_table
- user_id, question_id
- is_correct, max_difficulty

❌ Avoid:
- QuestionHistoryTable
- uid, qid (too abbreviated)
- is_correct_answer (redundant)
```

### Database Tables
```
✅ Correct:
- question_history (lowercase, underscore)
- question_queue (lowercase, underscore)
- quiz_results (lowercase, underscore)

❌ Avoid:
- QuestionHistory (PascalCase)
- question-history (kebab-case)
- QUESTION_HISTORY (ALL CAPS)
```

### Documentation Files
```
✅ Correct:
- SESSION_FREEZE_CHECKLIST.md (CAPS, underscores)
- NEXT_SESSION_START.md (CAPS, underscores)
- PHASE_2_CURRENT_STATE.md (CAPS, underscores)

❌ Avoid:
- session_freeze_checklist.md (lowercase)
- SessionFreezeChecklist.md (PascalCase)
- session-freeze-checklist.md (kebab-case)
```

---

## 🔧 FILE PURPOSE REFERENCE

### Documentation to READ (This Session Closing)
| File | Purpose | Priority |
|------|---------|----------|
| SESSION_FREEZE_CHECKLIST.md | What's frozen & ready | Critical |
| NEXT_SESSION_START.md | How to begin next session | Critical |
| PHASE_2_CURRENT_STATE.md | Current status | Important |
| FAST_TRACK_IMPLEMENTATION_PLAN.md | Implementation roadmap | Important |
| QUESTION_ROTATION_PLAN.md | Technical design | Important |

### Documentation to READ (Next Session)
| File | Purpose | When |
|------|---------|------|
| FAST_TRACK_IMPLEMENTATION_PLAN.md | Main reference | Days 1-5 |
| QUESTION_ROTATION_PLAN.md | Technical details | Days 1-2 (Tier 1) |
| TESTING_CHECKLIST.md | Test procedures | Days 4-5 |
| PHASE_2_CURRENT_STATE.md | Reference | Whenever needed |

### Code Files
| File | Purpose | Modify? |
|------|---------|---------|
| apps/exam_prep_master.py | Main app | ✅ Yes (Tier 1 & 2) |
| modules/ch*.py | Chapter content | ⚠️ Minor updates only |
| components/*.py | Components | ⚠️ Only if needed |
| apps/exam_prep_pro.py | Legacy | ❌ No |
| apps/legacy/*.py | Old versions | ❌ No |

---

## 📊 CURRENT FOLDER SIZES (Approximate)

```
apps/                 200 KB  (main code)
modules/              150 KB  (chapter content)
components/           100 KB  (reusable components)
docs/                 200 KB  (documentation)
resources/            100 KB  (assets)
src/                   50 KB  (utilities)
.git/              5000+ KB  (git repository)
Root .md files       1000 KB  (documentation)
```

**Total**: ~7 MB (excluding .git)

---

## 🔑 KEY LOCATIONS FOR NEXT SESSION

### Where to Add Tier 1 Code
```
File: apps/exam_prep_master.py
Location: Around line 1000
Action: Add database table creation for question_history, question_queue
```

### Where to Add Tracking Functions
```
File: apps/exam_prep_master.py
Location: After database tables (around line 1100)
Action: Add track_question_answer(), queue_next_question(), get_next_question()
```

### Where to Add Tier 2 Code
```
File: apps/exam_prep_master.py
Location: After Tier 1 functions (around line 1300)
Action: Add variation generator and integration logic
```

### Where to Modify Quiz Logic
```
File: apps/exam_prep_master.py
Location: Mock exam section (~line 1500)
Location: Challenge mode section (~line 1700)
Location: Practice mode section (~line 1900)
Action: Integrate smart question selection
```

---

## ✅ CONFIGURATION MANAGEMENT

### Git Configuration
```
Branch: main (primary development)
Remote: origin (GitHub)
Strategy: Commit frequently, descriptive messages
History: Keep clean and organized
```

### Streamlit Configuration
```
Port: 8501 (local development)
Cloud URL: [configured in Streamlit Cloud dashboard]
Config file: streamlit.app (points to main app)
```

### Database Configuration
```
Type: SQLite
Storage: Same directory as app (session_data.db)
Tables: 3 current (users, user_sessions, quiz_results)
Future: +2 tables (question_history, question_queue)
```

---

## 📝 FILE MODIFICATION GUIDELINES

### When Modifying Code
1. Always work in `apps/exam_prep_master.py` (main file)
2. Keep naming conventions consistent
3. Add comments for complex logic
4. Test locally before committing
5. Commit with descriptive messages

### When Creating New Files
1. Use snake_case for Python files
2. Add docstrings to modules
3. Include comments for functions
4. Follow existing code style
5. Document in this reference file

### When Committing
```bash
git add [specific files]
git commit -m "Clear message describing changes"
git push origin main
```

---

## 🚀 NEXT SESSION CHECKLIST

Before starting implementation, verify:

- [ ] Directory structure matches this document
- [ ] All files in correct locations
- [ ] Naming conventions understood
- [ ] apps/exam_prep_master.py is readable
- [ ] Git repository is clean
- [ ] No uncommitted changes
- [ ] Ready to add new code

---

## 🔗 CROSS-REFERENCE GUIDE

**For Documentation Index**:
→ PHASE_2_COMPLETION_DOCUMENTATION_INDEX.md

**For Continuation Instructions**:
→ CONTINUATION_GUIDE.md (create in next session)

**For Technical Details**:
→ QUESTION_ROTATION_PLAN.md

**For Implementation Steps**:
→ FAST_TRACK_IMPLEMENTATION_PLAN.md

**For Testing**:
→ TESTING_CHECKLIST.md

---

**Status**: ✅ Complete and Organized  
**Ready For**: Next session implementation  
**Naming**: Consistent (snake_case, descriptive)  
**Configuration**: Proper (git, Streamlit, database)  

