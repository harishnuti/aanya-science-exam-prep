# 📁 COMPLETE DIRECTORY STRUCTURE - Phase 2 v4.0

**Date**: May 16, 2026  
**Version**: 4.0 - Master App  
**Status**: Frozen for Production  
**Total Files**: 50+  
**Code Size**: ~5 MB (excluding PDFs & database)

---

## 📊 STRUCTURE OVERVIEW

```
aanya-science-exam-prep/                    (GitHub repository root)
│
├── 📱 ROOT LEVEL APPS                      (Streamlit entry points)
├── 📁 apps/                                (Organized applications)
├── 📁 src/                                 (Shared source code)
├── 📁 docs/                                (Comprehensive documentation)
├── 📁 data/                                (Database - git-ignored)
├── 📁 resources/                           (Learning materials - git-ignored)
├── 📁 versions/                            (Rollback versions)
├── 📄 Configuration files
└── 📄 Root documentation
```

---

## 📋 DETAILED FILE LISTING

### 📱 ROOT LEVEL - STREAMLIT ENTRY POINTS

**Location**: Repository root (`/`)

```
streamlit_app.py                           (PRIMARY ENTRY POINT)
├── Size: ~150 KB
├── Purpose: Main app for Streamlit Cloud deployment
├── Content: Imports and runs Master App from apps/exam_prep_master.py
├── Status: ✅ Active
└── When to modify: Only if changing main entry point logic
```

```
app_exam_prep_pro.py                       (BACKUP ENTRY POINT)
├── Size: ~2.3 MB
├── Purpose: Backward compatibility wrapper
├── Content: Complete Master App v4.0 code (duplicate of apps/exam_prep_master.py)
├── Status: ✅ Active (fallback)
└── When to modify: Never modify directly; edit apps/exam_prep_master.py instead
```

```
streamlit.app                              (CONFIGURATION FILE)
├── Size: <1 KB
├── Content: apps/exam_prep_master.py
├── Purpose: Optional config specifying main file path for Streamlit Cloud
├── Status: ✅ Active
└── Format: Plain text, single line pointing to entry point
```

---

### 📁 apps/ - ORGANIZED APPLICATIONS

**Location**: `/apps/`

```
apps/
│
├── exam_prep_master.py                    (v4.0 MASTER APP - MAIN FILE)
│   ├── Size: ~2.3 MB
│   ├── Lines: 2300+
│   ├── Status: ✅ Production Ready
│   ├── Purpose: Complete unified Master App with all features
│   │
│   ├── Sections (major functions):
│   │   ├── show_login()                   ← Authentication & user setup
│   │   ├── show_home()                    ← Dashboard with stats
│   │   ├── show_chapters()                ← 6 chapters selection
│   │   ├── show_topic_select()            ← Chapter content selection
│   │   ├── show_practice_mode()           ← Learning section
│   │   ├── show_mock_exam()               ← 45-min mock exam
│   │   ├── show_challenge_mode()          ← Brain drainer challenges
│   │   ├── show_analytics()               ← Progress & stats
│   │   └── show_admin_dashboard()         ← Admin controls
│   │
│   ├── Key Features:
│   │   ✅ Personalized username (dynamic, not hardcoded "Aanya")
│   │   ✅ Beautiful gradient UI (home page, cards)
│   │   ✅ Multi-user support via database
│   │   ✅ Gamification system (XP, badges, streaks)
│   │   ✅ 6 complete chapters with content
│   │   ✅ 45-minute PSLE mock exam
│   │   ✅ Brain drainer challenge mode (228+ questions)
│   │   ✅ Admin dashboard
│   │   ✅ Analytics & progress tracking
│   │
│   ├── Dependencies:
│   │   import streamlit as st
│   │   import pandas as pd
│   │   import plotly.express as px
│   │   sys.path.insert(0, 'apps')
│   │   sys.path.insert(0, 'src')
│   │   from modules import ch1_reproduction, ch2_water, ... ch6_circuits
│   │   from components import animations, gamification, brain_drainers
│   │   from utils import database, state_manager
│   │
│   └── When to modify: For feature additions, bug fixes, UI improvements
│
├── exam_prep_pro.py                       (v3.0 - ARCHIVE)
│   ├── Size: ~1.8 MB
│   ├── Status: 📦 Archived (not active)
│   ├── Purpose: Previous version, kept for reference
│   └── Note: Do NOT use - Master App (exam_prep_master.py) is current
│
├── README_APPS.md                         (APPS DOCUMENTATION)
│   ├── Size: ~5 KB
│   ├── Purpose: Explains purpose and structure of each app
│   ├── Content: Overview of all 3 app versions
│   └── When to update: When adding new app versions
│
└── legacy/                                (LEGACY APPS - ARCHIVE)
    ├── old_app_v2.0.py
    ├── old_app_v2.1.py
    └── (other previous versions)
```

---

### 📁 src/ - SHARED SOURCE CODE

**Location**: `/src/`

```
src/
│
├── 📁 modules/                            (CHAPTER CONTENT MODULES)
│   │
│   ├── ch1_reproduction.py
│   │   ├── Purpose: Chapter 1 - Reproduction in Animals & Plants
│   │   ├── Size: ~200 KB
│   │   ├── Content:
│   │   │   ├── Flashcards (10+)
│   │   │   ├── Matching pairs (10)
│   │   │   ├── Quiz questions (15+)
│   │   │   ├── Brain drainers (50+)
│   │   │   ├── Interactive elements
│   │   │   └── Learning activities
│   │   ├── Key Function: render_chapter_1(user_name)
│   │   └── XP Values: Quiz=10, Brain drainer=15+, Mini-game=20
│   │
│   ├── ch2_water.py
│   │   ├── Purpose: Chapter 2 - Water Cycles
│   │   ├── Size: ~180 KB
│   │   ├── Content: Water cycle content, states of matter, water processes
│   │   ├── Special Features: Water cycle simulator (Canvas animation)
│   │   └── Key Function: render_chapter_2(user_name)
│   │
│   ├── ch3_plant.py
│   │   ├── Purpose: Chapter 3 - Plant Transport
│   │   ├── Size: ~170 KB
│   │   ├── Content: Plant transport, xylem, phloem, photosynthesis
│   │   ├── Special Features: Plant diagram, transport visualization
│   │   └── Key Function: render_chapter_3(user_name)
│   │
│   ├── ch4_human.py
│   │   ├── Purpose: Chapter 4 - Human Systems
│   │   ├── Size: ~190 KB
│   │   ├── Content: Digestive, respiratory, circulatory, nervous systems
│   │   ├── Special Features: Body system diagrams
│   │   └── Key Function: render_chapter_4(user_name)
│   │
│   ├── ch5_electrical.py
│   │   ├── Purpose: Chapter 5 - Electrical Systems
│   │   ├── Size: ~160 KB
│   │   ├── Content: Conductors, insulators, electrical phenomena
│   │   ├── Special Features: Electrical circuit basics
│   │   └── Key Function: render_chapter_5(user_name)
│   │
│   ├── ch6_circuits.py
│   │   ├── Purpose: Chapter 6 - Electric Circuits
│   │   ├── Size: ~200 KB
│   │   ├── Content: Series circuits, parallel circuits, circuit components
│   │   ├── Special Features: Dynamic circuit builder, simulator
│   │   ├── Key Function: render_chapter_6(user_name)
│   │   └── Note: Most interactive chapter
│   │
│   └── ch*_new.py                        (EXTENDED VERSIONS)
│       ├── ch1_reproduction_new.py        (Extended questions & activities)
│       ├── ch2_water_new.py
│       ├── ch3_plant_new.py
│       ├── ch4_human_new.py
│       ├── ch5_electrical_new.py
│       └── ch6_circuits_new.py
│
├── 📁 components/                         (SHARED COMPONENTS)
│   │
│   ├── animations.py
│   │   ├── Purpose: Visual effects and animations
│   │   ├── Size: ~50 KB
│   │   ├── Key Classes/Functions:
│   │   │   ├── MalteseDogFeedback        (Animated mascot)
│   │   │   ├── show_celebration()        (Confetti, particles)
│   │   │   ├── show_achievement()        (Badge unlock animation)
│   │   │   └── Lottie animation loading
│   │   └── Technologies: Lottie, CSS animations, HTML5 Canvas
│   │
│   ├── brain_drainers.py
│   │   ├── Purpose: PSLE-style tricky questions for all chapters
│   │   ├── Size: ~150 KB
│   │   ├── Content Structure:
│   │   │   ├── Ch1_Reproduction: 50+ questions
│   │   │   ├── Ch2_Water: 30+ questions
│   │   │   ├── Ch3_Plant: 30+ questions
│   │   │   ├── Ch4_Human: 30+ questions
│   │   │   ├── Ch5_Electrical: 30+ questions
│   │   │   └── Ch6_Circuits: 30+ questions
│   │   ├── Question Format:
│   │   │   ├── Question text
│   │   │   ├── 4 answer options
│   │   │   ├── Correct answer
│   │   │   ├── Trap explanation (why other answers trick you)
│   │   │   ├── Difficulty level (🟡🟠🔴)
│   │   │   └── Concept tag (e.g., "Photosynthesis")
│   │   └── Total Questions: 228+
│   │
│   ├── gamification.py
│   │   ├── Purpose: XP system, badges, streaks, achievements
│   │   ├── Size: ~80 KB
│   │   ├── Key Functions:
│   │   │   ├── calculate_xp()             (How much XP earned)
│   │   │   ├── award_xp()                 (Add XP to user)
│   │   │   ├── check_level_up()           (Level progression)
│   │   │   ├── check_achievements()       (Badge unlocks)
│   │   │   ├── update_streak()            (Daily streak tracking)
│   │   │   └── get_gamification_stats()   (User's stats)
│   │   ├── Features:
│   │   │   ✅ 50 levels (increasing XP requirements)
│   │   │   ✅ 20+ achievement badges
│   │   │   ✅ Daily streak counter
│   │   │   ✅ Week leaderboard
│   │   │   ✅ Level progression animation
│   │   └── XP Formula: level_n needs 100*(n+1) XP
│   │
│   ├── minigames.py
│   │   ├── Purpose: Interactive mini-games per chapter
│   │   ├── Size: ~120 KB
│   │   ├── Games Included:
│   │   │   ├── Ch1: Plant the Seed (drag-drop sequencing)
│   │   │   ├── Ch2: State Sorter (classification)
│   │   │   ├── Ch3: Transport Race (timed flow simulation)
│   │   │   ├── Ch4: Body Part Match (anatomy puzzle)
│   │   │   ├── Ch5: [Electrical game]
│   │   │   └── Ch6: Light It Up (circuit builder)
│   │   └── XP Awards: 20+ XP per game, 2x for no hints
│   │
│   ├── circuit_generator.py
│   │   ├── Purpose: Dynamic circuit generation for Ch6
│   │   ├── Size: ~50 KB
│   │   ├── Functions:
│   │   │   ├── generate_random_circuit()  (Create valid circuits)
│   │   │   ├── render_circuit()           (Draw on Canvas)
│   │   │   ├── calculate_brightness()     (Predict output)
│   │   │   └── generate_circuit_quiz()    (Auto-create questions)
│   │   └── Purpose: Infinite variety for practice
│   │
│   └── exam_questions_extended.py
│       ├── Purpose: Extended question bank for mock exam
│       ├── Size: ~100 KB
│       ├── Questions: 50+ PSLE-style questions
│       └── Format: [Question, Options, Answer, Explanation]
│
├── 📁 utils/                              (UTILITY MODULES)
│   │
│   ├── database.py
│   │   ├── Purpose: SQLite database management + gamification
│   │   ├── Size: ~60 KB
│   │   ├── Key Classes:
│   │   │   └── Database                   (Main class)
│   │   │
│   │   ├── Core Tables (Original):
│   │   │   ├── users                      (user_id, name)
│   │   │   ├── quiz_sessions             (quiz attempts)
│   │   │   └── answers                   (user answers to questions)
│   │   │
│   │   ├── Gamification Tables (NEW):
│   │   │   ├── user_gamification         (XP, level, streak)
│   │   │   ├── user_achievements         (unlocked badges)
│   │   │   ├── chapter_progress          (mastery per chapter)
│   │   │   └── minigame_scores           (high scores)
│   │   │
│   │   ├── Key Functions (30+):
│   │   │   ├── init_db()                 (Create/initialize)
│   │   │   ├── get_or_create_user()      (User setup)
│   │   │   ├── save_quiz_answer()        (Store answer)
│   │   │   ├── add_xp()                  (Award XP)
│   │   │   ├── get_user_stats()          (Level, streak, XP)
│   │   │   ├── unlock_achievement()      (Award badge)
│   │   │   ├── update_chapter_progress() (Track mastery)
│   │   │   ├── get_admin_stats()         (All users)
│   │   │   └── (20+ more functions)
│   │   │
│   │   └── Database File: data/app.db (SQLite, git-ignored)
│   │
│   └── state_manager.py
│       ├── Purpose: Session state management for Streamlit
│       ├── Size: ~25 KB
│       ├── Key Functions:
│       │   ├── initialize_session_state() (Setup on login)
│       │   ├── save_session_state()       (Persist between pages)
│       │   ├── restore_session_state()    (Load after refresh)
│       │   ├── clear_session()            (On logout)
│       │   └── (Other state helpers)
│       │
│       └── Session Variables Tracked:
│           ├── user_id, user_name
│           ├── current_chapter
│           ├── current_quiz_answers
│           ├── xp, level, streak
│           ├── unlocked_achievements
│           └── (Streamlit session_state dict)
│
├── config.py
│   ├── Purpose: Configuration constants
│   ├── Size: ~5 KB
│   ├── Content:
│   │   ├── ADMIN_PASSWORD = "admin123"
│   │   ├── CHAPTER_NAMES = ["Reproduction", "Water Cycles", ...]
│   │   ├── XP_MULTIPLIERS = {"Easy": 1.0, "Hard": 2.0}
│   │   ├── Database paths
│   │   └── UI configuration
│   └── When to modify: For configuration changes, not logic
│
└── README.md
    ├── Purpose: Overview of src/ folder structure
    ├── Content: What each module does, how they connect
    └── Useful for: Understanding code organization
```

---

### 📁 docs/ - COMPREHENSIVE DOCUMENTATION (22+ files)

**Location**: `/docs/`

```
docs/
│
├── 📁 deployment/                         (DEPLOYMENT GUIDES)
│   ├── CLOUD_DEPLOYMENT_GUIDE.md          (Streamlit Cloud setup)
│   ├── DEPLOY_NOW_CHECKLIST.md            (Pre-deploy checklist)
│   └── DEPLOYMENT_CHECKLIST_v3.0.md       (v3.0 specific)
│
├── 📁 user_guides/                        (HOW-TO GUIDES)
│   ├── HOW_TO_RUN_APPS.md                 (Run locally vs cloud)
│   ├── EXAM_PREP_GUIDE.md                 (Using exam features)
│   ├── NAVIGATION_QUICK_REFERENCE.md      (UI navigation)
│   ├── QUICKSTART.md                      (5-min intro)
│   └── RESUME_HERE.md                     (Resume context window)
│
├── 📁 technical/                          (TECHNICAL DOCUMENTATION)
│   ├── CONTEXT_TRANSFER_GUIDE.md          (Resume in new context)
│   ├── PHASE_2_COMPLETE_DOCUMENTATION.md (All technical specs)
│   ├── IMPLEMENTATION_SUMMARY.md          (What was built)
│   └── BUG_FIX_REPORT_May16.md            (Fixes applied)
│
├── 📁 version_history/                    (VERSION TRACKING)
│   ├── VERSION_HISTORY.md                 (All versions listed)
│   ├── VERSION_FREEZE_v2.2.md             (Older freeze)
│   ├── PHASE_2_OFFICIALLY_FROZEN.txt      (Freeze notice)
│   └── EXAM_APP_FROZEN.txt                (Earlier freeze)
│
├── 📁 roadmap/                            (FUTURE PLANNING)
│   ├── PHASE_3_ROADMAP.md                 (Quick roadmap)
│   └── PHASE_2C_STRATEGY.md               (Phase 2C planning)
│
├── 📁 features/                           (FEATURE DOCUMENTATION)
│   ├── CHALLENGE_MODE_ANNOUNCEMENT.md     (Brain drainer intro)
│   ├── CHALLENGE_QUESTIONS_REFERENCE.md   (Question samples)
│   ├── BUG_WINDOW_UPDATES.md              (Bug fixes)
│   ├── CHALLENGE_MODE_DEPLOYMENT.txt      (Deployment notes)
│   └── BUG_FIX_SUMMARY.txt                (Fix summary)
│
└── README.md                              (DOCS NAVIGATION)
    ├── Purpose: Index to all documentation
    ├── Content: What each folder contains
    └── Useful for: Finding what you need
```

---

### 📁 data/ - DATABASE (GIT-IGNORED)

**Location**: `/data/`

```
data/
│
└── app.db                                 (SQLITE DATABASE)
    ├── Size: ~500 KB - 5 MB (depends on usage)
    ├── Status: 🔒 Git-ignored (in .gitignore)
    ├── Format: SQLite 3
    ├── Created: Automatically when app starts (init_db())
    ├── Tables (7 total):
    │   ├── users                          (User profiles)
    │   ├── quiz_sessions                  (Quiz attempts)
    │   ├── answers                        (Individual answers)
    │   ├── user_gamification              (XP, level, streak)
    │   ├── user_achievements              (Unlocked badges)
    │   ├── chapter_progress               (Mastery tracking)
    │   └── minigame_scores                (Game high scores)
    │
    ├── Backup: Not automatically backed up
    │   └── Manual backup: Copy app.db to safe location
    │
    └── If Corrupted:
        └── Delete app.db and restart app (will recreate from scratch)
```

---

### 📁 resources/ - LEARNING MATERIALS (GIT-IGNORED)

**Location**: `/resources/`

```
resources/
│
├── textbooks/                             (PDF FILES - NOT IN GIT)
│   ├── P5_Science_Textbook.pdf            (MOE curriculum)
│   ├── PSLE_Science_Guide.pdf
│   ├── Workbook_1_Reproduction.pdf
│   └── (Other reference materials)
│   
│   Size: ~100+ MB (reason for .gitignore exclusion)
│   Purpose: Reference material for creating questions
│   Access: Stored locally only, not in GitHub
│
└── curriculum/                            (CURRICULUM FILES)
    ├── MOE_P5_Syllabus.pdf
    ├── Learning_Objectives.txt
    └── Topic_Coverage.xlsx
```

---

### 📁 versions/ - ROLLBACK VERSIONS

**Location**: `/versions/`

```
versions/
│
└── app_exam_prep_pro_v2.2_no_database.py
    ├── Purpose: Rollback version (working without database)
    ├── Size: ~1.5 MB
    ├── Use Case: If database becomes corrupted and need to continue
    ├── Status: Archive only
    └── Note: No gamification, local session only
```

---

### 📄 ROOT LEVEL - CONFIGURATION & DOCUMENTATION

**Location**: Repository root (`/`)

```
ROOT CONFIGURATION FILES:
│
├── .gitignore
│   ├── Size: <1 KB
│   ├── Purpose: Exclude files from git
│   ├── Exclusions:
│   │   ├── __pycache__/               (Python cache)
│   │   ├── *.pdf                      (PDFs - save space)
│   │   ├── data/app.db                (Database)
│   │   ├── .streamlit/secrets.toml    (Secrets)
│   │   ├── .env                       (Environment variables)
│   │   ├── .venv/ / venv/             (Virtual environments)
│   │   └── (10+ other patterns)
│   │
│   └── Impact: Reduces repo size from 120 MB → 5 MB
│
├── requirements.txt
│   ├── Size: <1 KB
│   ├── Purpose: Python dependencies
│   ├── Pinned Versions:
│   │   ├── streamlit >= 1.28.0
│   │   ├── pandas >= 2.0.0
│   │   ├── plotly >= 5.17.0
│   │   └── (sqlite3 is built-in)
│   │
│   └── Use: pip install -r requirements.txt
│
└── .streamlit/ (OPTIONAL)
    └── config.toml                    (Streamlit config)
        ├── Theme settings
        ├── Layout preferences
        └── Port configuration
```

```
ROOT DOCUMENTATION FILES (15+ files):
│
├── README.md
│   ├── Size: ~10 KB
│   ├── Purpose: Main project overview
│   ├── Content:
│   │   ├── What is this project?
│   │   ├── Features overview
│   │   ├── How to run locally
│   │   ├── How to deploy
│   │   └── Contributing guidelines
│   └── Audience: Everyone (first read)
│
├── FINAL_FREEZE_v4.0.md                 (NEW)
│   ├── Size: ~15 KB
│   ├── Purpose: Complete freeze status
│   ├── Content: All files, features, statistics
│   └── Updated: May 16, 2026
│
├── VERSION_FREEZE_v4.0.md
│   ├── Size: ~20 KB
│   ├── Purpose: Detailed freeze notice
│   ├── Content: Known issues, quick reference
│   └── Updated: May 16, 2026
│
├── RESUME_HERE.md                       (CRITICAL FOR CONTEXT WINDOWS)
│   ├── Size: ~8 KB
│   ├── Purpose: Quick resume guide for new context windows
│   ├── Content: What is v4.0, file structure, quick start
│   ├── Read Time: 2 minutes
│   └── Must Read: YES (before anything else)
│
├── MASTER_APP_V4.0_GUIDE.md              (FEATURE TESTING GUIDE)
│   ├── Size: ~25 KB
│   ├── Purpose: Feature explanations & testing
│   ├── Content: How to test every feature
│   ├── Read Time: 15-20 minutes
│   └── For: Testers, QA, understanding features
│
├── TESTING_CHECKLIST.md                  (30+ TEST CASES)
│   ├── Size: ~30 KB
│   ├── Purpose: Comprehensive testing guide
│   ├── Content: 10 test suites with pass/fail tracking
│   ├── Test Cases: 30+
│   └── For: Aanya, testers, validation
│
├── BUG_REPORT_TEMPLATE.md                (BUG REPORTING)
│   ├── Size: ~10 KB
│   ├── Purpose: Standardized bug report format
│   ├── Content: Template for 3+ bugs, example bug
│   └── For: Reporting issues found during testing
│
├── STREAMLIT_DEPLOYMENT_GUIDE.md         (NEW)
│   ├── Size: ~40 KB
│   ├── Purpose: Step-by-step deployment guide
│   ├── Content: 10 sections covering all deployment aspects
│   ├── Read Time: 20-30 minutes
│   └── For: Deployment, maintenance, troubleshooting
│
├── GITHUB_REPO_SETTINGS.md               (NEW)
│   ├── Size: ~35 KB
│   ├── Purpose: GitHub repository configuration
│   ├── Content: Settings, secrets, branches, workflows
│   ├── Read Time: 20-30 minutes
│   └── For: GitHub management, DevOps
│
├── CONTEXT_CONTINUITY_GUIDE.md           (NEW)
│   ├── Size: ~30 KB
│   ├── Purpose: Resume development in new context window
│   ├── Content: Reading order, file map, troubleshooting
│   ├── Read Time: 15 minutes
│   └── For: Context window resumption
│
├── PHASE_3_ROADMAP_DETAILED.md           (NEW)
│   ├── Size: ~50 KB
│   ├── Purpose: Complete Phase 3 plan
│   ├── Content: 6-week development roadmap
│   ├── Read Time: 30-45 minutes
│   └── For: Phase 3 planning & development
│
├── DIRECTORY_STRUCTURE.md                (NEW - THIS FILE)
│   ├── Size: ~30 KB
│   ├── Purpose: Complete file inventory
│   ├── Content: Every file with description
│   └── For: Understanding project structure
│
└── (Other documentation files)
    ├── PUSH_CHECKLIST_FINAL.md
    ├── VERSION_HISTORY.md
    └── (More archived docs)
```

---

## 📊 FILE STATISTICS

| Category | Count | Size | Purpose |
|----------|-------|------|---------|
| **Python Files** | 30+ | ~3 MB | Application code |
| **Documentation** | 22+ | ~500 KB | Guides, specs, plans |
| **Configuration** | 3 | <5 KB | Dependencies, config |
| **Database** | 1 | ~5 MB | SQLite (git-ignored) |
| **Resources** | 10+ | ~100 MB | PDFs (git-ignored) |
| **TOTAL** | 50+ | ~5 MB (git) | Full project |

---

## 🔍 FILE ORGANIZATION PRINCIPLES

### By Purpose

**Application Logic**:
- All in `apps/` (entry point) or `src/` (shared code)
- One main file: `apps/exam_prep_master.py`

**Content & Data**:
- Chapter content: `src/modules/ch*.py`
- Quiz questions: `src/components/brain_drainers.py`
- Database: `data/app.db` (auto-created)

**Support & Utilities**:
- Database functions: `src/utils/database.py`
- Shared functions: `src/utils/` and `src/components/`
- Configuration: `src/config.py`

**Documentation**:
- User guides: `docs/user_guides/`
- Technical docs: `docs/technical/`
- Deployment: `docs/deployment/`
- Roadmap: `docs/roadmap/`
- Root level: Quick references (`RESUME_HERE.md`, etc.)

### By Audience

**For New Users**:
- Start: `README.md`
- Then: `RESUME_HERE.md`
- Then: `MASTER_APP_V4.0_GUIDE.md`

**For Developers**:
- Start: `CONTEXT_CONTINUITY_GUIDE.md`
- Then: `PHASE_2_COMPLETE_DOCUMENTATION.md`
- Then: Actual Python files

**For Testers**:
- Start: `TESTING_CHECKLIST.md`
- Report: `BUG_REPORT_TEMPLATE.md`
- Reference: `MASTER_APP_V4.0_GUIDE.md`

**For DevOps/Deployment**:
- Start: `STREAMLIT_DEPLOYMENT_GUIDE.md`
- Then: `GITHUB_REPO_SETTINGS.md`
- Troubleshoot: Both guides have sections

**For Phase 3 Planning**:
- Start: `PHASE_3_ROADMAP_DETAILED.md`
- Understand current: `PHASE_2_COMPLETE_DOCUMENTATION.md`
- Architecture: `docs/technical/`

---

## 🔄 COMMON OPERATIONS

### "I need to find X"

| Looking for | Location | File |
|-------------|----------|------|
| Main app code | Root, apps/, src/ | `apps/exam_prep_master.py` |
| Chapter 3 content | src/modules/ | `ch3_plant.py` |
| Database functions | src/utils/ | `database.py` |
| XP/gamification logic | src/components/ | `gamification.py` |
| Quiz questions | src/components/ | `brain_drainers.py` |
| How to deploy | Root docs | `STREAMLIT_DEPLOYMENT_GUIDE.md` |
| What was frozen | Root docs | `FINAL_FREEZE_v4.0.md` |
| How to resume context | Root docs | `CONTEXT_CONTINUITY_GUIDE.md` |
| Phase 3 plan | Root docs | `PHASE_3_ROADMAP_DETAILED.md` |
| How to test | Root docs | `TESTING_CHECKLIST.md` |

---

## ✅ FILE INTEGRITY CHECKLIST

**When resuming or deploying, verify**:

```
Repository Root:
□ streamlit_app.py exists                 ✅
□ app_exam_prep_pro.py exists             ✅
□ requirements.txt exists                 ✅
□ .gitignore exists                       ✅
□ README.md exists                        ✅

Apps Folder:
□ apps/exam_prep_master.py exists         ✅
□ apps/README_APPS.md exists              ✅

Src Folder:
□ src/modules/ch1-ch6.py files exist      ✅
□ src/components/*.py files exist         ✅
□ src/utils/database.py exists            ✅
□ src/utils/state_manager.py exists       ✅
□ src/config.py exists                    ✅

Docs Folder:
□ docs/README.md exists                   ✅
□ docs/deployment/ files exist            ✅
□ docs/user_guides/ files exist           ✅
□ docs/technical/ files exist             ✅

Root Documentation:
□ RESUME_HERE.md exists                   ✅
□ FINAL_FREEZE_v4.0.md exists             ✅
□ STREAMLIT_DEPLOYMENT_GUIDE.md exists    ✅
□ GITHUB_REPO_SETTINGS.md exists          ✅
□ CONTEXT_CONTINUITY_GUIDE.md exists      ✅
□ PHASE_3_ROADMAP_DETAILED.md exists      ✅
```

---

## 🚀 TOTAL PROJECT SIZE

```
Component                    Size        Git? 
─────────────────────────────────────────────
Application code            ~3 MB       ✅ YES
Documentation              ~0.5 MB      ✅ YES
Configuration              ~0.1 MB      ✅ YES
Database (app.db)          ~5 MB        ❌ NO (git-ignored)
PDFs & Resources          ~100+ MB      ❌ NO (git-ignored)
─────────────────────────────────────────────
TOTAL IN GITHUB            ~3.6 MB      ✅
TOTAL WITH RESOURCES      ~110 MB       ❌ Local only
```

---

**Last Updated**: May 16, 2026  
**Version**: 4.0 Master App  
**Status**: ✅ Complete & Frozen

