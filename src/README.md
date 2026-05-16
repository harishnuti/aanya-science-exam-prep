# 🔧 Source Code (`src/`)

Shared source code modules used by all applications.

## Folder Structure

```
src/
├── components/          # UI components & features
├── modules/             # Learning content (6 chapters)
├── utils/               # Utility functions & database
├── config.py            # Configuration settings
├── exam_questions_extended.py  # Extended question bank
└── __init__.py
```

---

## 📦 Components (`src/components/`)

Reusable UI components and features.

### `animations.py`
Maltese dog feedback animations and visual effects.
```python
from components.animations import MalteseDogFeedback
MalteseDogFeedback.show_happy_maltese("Aanya")
```

### `brain_drainers.py`
PSLE-style tricky questions with trap answers.
- 15 brain drainer questions (5 per topic)
- Similar-looking answer options
- Detailed explanations

### `gamification.py`
XP system, badges, streaks, and rewards.

### `minigames.py`
Interactive mini-games for each chapter.
- Drag-and-drop mechanics
- Timed challenges
- Sequencing games

### `circuit_generator.py`
Dynamic circuit builder for Electrical Systems chapter.

---

## 📚 Modules (`src/modules/`)

Chapter content for 6 topics:

### Ch1: Reproduction in Animals & Plants
**File**: `ch1_reproduction.py`
- Flashcards
- Matching pairs
- MCQ questions
- Brain drainers

### Ch2: Cycles in Water
**File**: `ch2_water.py`
- Flashcards
- Water state animations
- MCQ questions

### Ch3: Plant Transport
**File**: `ch3_plant.py`
- Interactive diagrams
- Transport mechanisms
- MCQ questions

### Ch4: Human Systems
**File**: `ch4_human.py`
- Organ system diagrams
- MCQ questions

### Ch5: Electrical Systems
**File**: `ch5_electrical.py`
- Circuit basics
- MCQ questions

### Ch6: Electric Circuits
**File**: `ch6_circuits.py`
- Series vs Parallel circuits
- Circuit simulator
- Interactive labs

---

## 🛠️ Utils (`src/utils/`)

Utility functions and database management.

### `database.py`
SQLite database functions:
- User management
- Quiz session tracking
- Answer persistence
- Analytics & reporting
- CSV export

**Key Functions**:
```python
from utils.database import (
    init_database,                    # Initialize SQLite
    get_or_create_user,              # Get/create user
    create_quiz_session,              # Start quiz
    save_answer,                      # Save answer
    get_user_stats,                   # Get user stats
    export_user_data_csv              # Export as CSV
)
```

### `state_manager.py`
Streamlit session state management.

---

## ⚙️ Configuration

### `config.py`
Global settings:
```python
STUDENT_NAME = "Aanya"
SCHOOL_NAME = "Waterway Primary School"
```

### `exam_questions_extended.py`
Extended question bank with all MCQ questions.

---

## Import Patterns

From apps, import like this:

```python
# Components
from components.animations import MalteseDogFeedback
from components.brain_drainers import CHALLENGE_QUESTIONS

# Modules
from modules.ch1_reproduction import get_flashcards

# Utils
from utils.database import init_database, save_answer
```

---

## Adding New Code

### 1. New Component
Create `src/components/new_feature.py`:
```python
def my_new_feature():
    """Description of feature"""
    pass
```

Import in app:
```python
from components.new_feature import my_new_feature
```

### 2. New Chapter Module
Create `src/modules/ch7_new_topic.py`:
```python
FLASHCARDS = [...]
QUESTIONS = [...]

def get_flashcards():
    return FLASHCARDS
```

### 3. New Utility
Add to `src/utils/new_util.py`:
```python
def helper_function():
    pass
```

---

## Testing Code

### Test Database
```bash
cd src
python -c "from utils.database import init_database; init_database(); print('✅ OK')"
```

### Test Imports
```bash
python -c "from components.animations import MalteseDogFeedback; print('✅ OK')"
```

---

## Code Style

- **Python Version**: 3.7+
- **Formatter**: Keep code readable
- **Docstrings**: Add for all functions
- **Type Hints**: Optional but encouraged

---

## Dependencies

Required packages in `requirements.txt`:
- streamlit >= 1.28.0
- pandas >= 2.0.0
- plotly >= 5.17.0
- sqlite3 (built-in)

---

**Last Updated**: May 16, 2026
**Maintained By**: Development Team
