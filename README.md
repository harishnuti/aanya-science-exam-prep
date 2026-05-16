# 🧪 AANYA'S SCIENCE EXAM PREP PRO

An enhanced science learning application for Aanya (Primary 5, Waterway Primary School, Singapore) featuring:

- ⚡ **Enhanced Gamification**: XP system, levels, badges, daily challenges, and streaks
- 🎨 **Better Animations**: CSS animations, particle effects, celebratory feedback
- 🧠 **PSLE Brain Drainers**: Exam-style tricky questions for all 6 chapters
- 🎮 **Interactive Mini-Games**: Drag-and-drop, sequencing, matching, and timed challenges
- 📊 **Progress Tracking**: Detailed stats, mastery radar, and achievement gallery
- 🎯 **Difficulty Levels**: Beginner, Intermediate, and Advanced modes
- 💾 **Progress Persistence**: localStorage-based automatic saving

## 📚 Chapters Included

1. **Ch 1: Reproduction in Animals & Plants** 🌱
2. **Ch 2: Cycles in Water** 💧
3. **Ch 3: Plant Transport** 🌿
4. **Ch 4: Human Systems** ❤️
5. **Ch 5: Electrical Systems** ⚡
6. **Ch 6: Electric Circuits** 🔌

## 🚀 Getting Started

### Installation

```bash
# Navigate to phase2 directory
cd phase2

# Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
# Run the main application
streamlit run app_phase2.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
phase2/
├── app_phase2.py                    # Main entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── components/
│   ├── __init__.py
│   ├── gamification.py             # XP, badges, streaks, achievements
│   ├── animations.py               # CSS, Lottie, particle effects
│   ├── brain_drainers.py          # PSLE questions (all chapters)
│   └── minigames.py               # Drag-drop, timed challenges
│
├── modules/
│   ├── __init__.py
│   ├── ch1_reproduction.py         # Chapter 1 (fully implemented)
│   ├── ch2_water.py               # Chapter 2 (template)
│   ├── ch3_plant.py               # Chapter 3 (template)
│   ├── ch4_human.py               # Chapter 4 (template)
│   ├── ch5_electrical.py          # Chapter 5 (template)
│   └── ch6_circuits.py            # Chapter 6 (template)
│
└── utils/
    ├── __init__.py
    ├── state_manager.py           # Session state & persistence
    └── data_utils.py              # Quiz data utilities
```

## 🎮 Key Features Explained

### 1. XP & Leveling System
- Earn XP from quizzes, brain drainers, mini-games
- Level up with increasing XP thresholds
- Unlock cosmetic rewards at higher levels

### 2. Daily Challenges & Streaks
- Daily login bonus (5 XP + random bonus)
- Daily challenge (20 XP for completion)
- Streak tracking with visual fire display
- Streak freeze mechanic (skip 1 day with 10 XP)

### 3. Achievement Badges
- Topic Mastery (90%+ in chapter)
- Brain Drainer Expert (50 correct answers)
- Week Warrior (7-day streak)
- Speedrunner (complete quiz in 2 min)
- Perfect Score (100% on any quiz)
- All-Rounder (80%+ in all chapters)

### 4. PSLE Brain Drainers
- Exam-style questions with "trap answers"
- Explanations for why trap answers are tricky
- Difficulty labels (🟡Easy, 🟠Medium, 🔴Hard)
- Timed mode and untimed mode
- Score tracking per difficulty

### 5. Mini-Games by Chapter
| Chapter | Game | Mechanic |
|---------|------|----------|
| Ch 1 | Plant the Seed | Sequence germination stages |
| Ch 2 | State Sorter | Categorize water states |
| Ch 3 | Transport Race | Guide water/food through plant |
| Ch 4 | Body Match Pro | Match organs to systems |
| Ch 5 | Circuit Constructor | Build circuits |
| Ch 6 | Light It Up | Reach target brightness |

### 6. Difficulty Modes
- **🟡 Beginner**: Flashcards + matching + basic MCQ (5-10 min, 1.0x XP)
- **🟠 Intermediate**: + mini-game + 10 brain drainers (15-20 min, 1.5x XP)
- **🔴 Advanced**: + full brain drainers + timed (25-40 min, 2.0x XP)

## 📊 Dashboard Elements

### Home Page
- Level & XP bar with progress
- Daily challenge status
- Quick mastery radar
- Session recommendations

### Progress Page
- Overall statistics (level, streak, achievements, chapters)
- Chapter mastery breakdown
- Brain drainer performance by difficulty
- Mini-game high scores
- 7/30-day activity timeline
- Achievement gallery

### Settings
- Theme preference (colorful, dark, light)
- Animation intensity
- Sound effects toggle
- Progress export/import
- Clear progress option

## 🛠️ Technology Stack

- **Framework**: Streamlit 1.28+
- **Animations**: CSS3, Canvas, Lottie (future)
- **Visualization**: Plotly (radar charts)
- **State Management**: Streamlit session_state + browser localStorage
- **Data**: JSON (local)

## 📝 Customization

### Adding New Brain Drainer Questions
Edit `components/brain_drainers.py` and add to the BRAIN_DRAINERS dictionary:

```python
BRAIN_DRAINERS = {
    'Chapter_Name': [
        {
            'q': 'Question text?',
            'options': ['Option A', 'Option B', 'Option C', 'Option D'],
            'answer': 'Option B',
            'trap': 'Why option A is tempting...',
            'difficulty': 'medium'
        },
        ...
    ]
}
```

### Adding New Mini-Games
Create new game classes in `components/minigames.py` following the pattern of `DragDropGame`, `SequencingGame`, etc.

### Customizing Achievement Triggers
Edit `utils/state_manager.py` `AchievementManager` class to add new unlock conditions.

## 🧪 Testing Checklist

- [ ] All chapters accessible from home
- [ ] Flashcards flip and navigate correctly
- [ ] Quizzes award correct XP based on difficulty
- [ ] Brain drainer questions display with explanations
- [ ] XP bar fills and levels up
- [ ] Achievements unlock with balloons animation
- [ ] Streak updates on daily login
- [ ] Progress persists on refresh (localStorage)
- [ ] Dashboard stats update in real-time
- [ ] Mini-games launch without errors

## 🎯 Future Enhancements

**Phase 2B (Week 2-3)**
- Implement all 6 chapter modules
- Add mini-games for all chapters
- Expand brain drainer pools

**Phase 2C (Week 3-4)**
- Integrate Lottie animations
- Add sound effects
- Enhance visual polish
- Theme system implementation

**Phase 2D (Week 4)**
- User testing with Aanya
- Feedback collection
- Rapid iteration
- Performance optimization

## 📱 Browser Support

- ✅ Chrome/Edge (Windows, Mac)
- ✅ Safari (Mac, iPad)
- ✅ Firefox (Windows, Mac)
- ⚠️ Mobile browsers (responsive but optimized for tablets)

## 🔒 Data Privacy

- All progress stored locally in browser (localStorage)
- No external API calls or data transmission
- Optional JSON export for backups
- Parent-controlled clear progress option

## ❓ Troubleshooting

### App won't run
```bash
# Clear Streamlit cache
rm -rf ~/.streamlit/cache
streamlit run app_phase2.py
```

### Animations not showing
- Ensure CSS is being injected correctly
- Check browser DevTools console for errors
- Try a different browser

### Progress not saving
- Check browser localStorage is enabled
- Try a different browser
- Export/import JSON as backup

## 👩 For Parents/Teachers

This app is designed for:
- **Age**: 10 years old (Primary 5)
- **School**: Waterway Primary School, Tampines, Singapore
- **Curriculum**: MOE Primary 5 Science (6 chapters)
- **Time Commitment**: 5-40 minutes per session depending on difficulty
- **Learning Goals**: Concept mastery + PSLE exam preparation

### Monitoring Progress
- Check "Progress" tab to see mastery by chapter
- View brain drainer performance to identify weak areas
- Track streaks to encourage daily learning habits
- Monitor XP to celebrate small wins

## 📞 Support

For issues or feature requests, contact the developer or check the project documentation.

---

**Created with ❤️ for Aanya** 🌟

Version: 2.0 (Phase 2 - Enhanced Edition)
Last Updated: May 2026
