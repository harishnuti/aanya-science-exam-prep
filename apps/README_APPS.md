# 📱 Applications

This folder contains all Streamlit applications for the exam prep system.

## Current Applications

### 🎯 **exam_prep_pro.py** (v3.0 - PRODUCTION)
**Status**: ✅ ACTIVE - Current production version
**Launch**: `streamlit run exam_prep_pro.py`

**Features**:
- ✅ User login system with name-based identification
- ✅ Multi-user support with persistent SQLite database
- ✅ Topic Mastery mode (practice per topic)
- ✅ Mock Exam mode (45-minute full exam)
- ✅ Challenge Mode (PSLE brain drainers)
- ✅ Progress Tracker with detailed statistics
- ✅ Settings with 2-step reset confirmation
- ✅ Admin Dashboard for monitoring all users (password: admin123)
- ✅ Real-time answer saving to database
- ✅ Performance analytics by difficulty and concept
- ✅ CSV export capability

**Deployment**: Streamlit Cloud
**URL**: https://aanya-science-exam-prep.streamlit.app/

---

## Legacy Applications

### `legacy/app_exam_prep.py`
**Status**: ❌ DEPRECATED - Old version
**Reason**: Replaced by exam_prep_pro.py v3.0

**Features**: Basic quiz functionality (no database)

---

### `legacy/app_phase2.py`
**Status**: ❌ DEPRECATED - Older alternative version
**Reason**: Replaced by exam_prep_pro.py v3.0

**Features**: Learning module structure (no database)

---

## How to Run Locally

### Start Production App
```bash
cd apps
streamlit run exam_prep_pro.py
```
Opens at: http://localhost:8501

### Run Tests
```bash
# Test database initialization
python -c "from src.utils.database import init_database; init_database(); print('✅ DB OK')"
```

---

## Application Architecture

```
exam_prep_pro.py (MAIN APP)
    ↓
Imports from src/:
    ├── components/
    │   ├── animations.py (Maltese feedback)
    │   ├── brain_drainers.py (PSLE questions)
    │   ├── gamification.py (XP, badges)
    │   └── ...
    ├── modules/
    │   ├── ch1_reproduction.py
    │   ├── ch2_water.py
    │   └── ... (ch3-6)
    └── utils/
        ├── database.py (SQLite)
        └── state_manager.py
```

---

## Deployment

### Local Streamlit
```bash
streamlit run exam_prep_pro.py
```

### Streamlit Cloud (Automatic)
- Push to GitHub
- Streamlit Cloud detects changes
- Auto-deploys in 1-2 minutes
- No manual deployment needed

### Docker (Future)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "apps/exam_prep_pro.py"]
```

---

## Admin Dashboard Access

1. Open app at login screen
2. Expand "🔑 Admin Access"
3. Enter password: `admin123`
4. View all users and their progress

**Change password**: Edit line in `exam_prep_pro.py` function `show_login()`

---

## Troubleshooting

### App won't start
```bash
# Check Python version (need 3.7+)
python --version

# Check dependencies
pip list | grep streamlit

# Reinstall from requirements.txt
pip install -r ../requirements.txt
```

### Port already in use
```bash
streamlit run exam_prep_pro.py --server.port 8502
```

### Clear Streamlit cache
```bash
streamlit cache clear
```

---

## Future Applications (Phase 3+)

Planned apps to be added:
- [ ] Mobile app version (React Native)
- [ ] Teacher dashboard (separate app)
- [ ] Analytics report generator
- [ ] Content management app (admin only)

---

**Last Updated**: May 16, 2026
**Maintained By**: Development Team
