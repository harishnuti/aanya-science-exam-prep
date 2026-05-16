# Version History - Aanya's Science Exam Prep

## Current Production Version
**v3.0** - Multi-User with SQLite Database (CURRENT)
- Location: `app_exam_prep_pro.py`
- Features: User login, persistent data storage, admin dashboard
- Database: SQLite (`data/app.db`)
- Deployment: Streamlit Cloud (auto-deploy from GitHub)
- Date: May 16, 2026

---

## Version Archive

### v2.2 - Clean Single-User Version (ROLLBACK AVAILABLE)
**Filename**: `versions/app_exam_prep_pro_v2.2_no_database.py`

**Features:**
- ✅ Topic Mastery mode (practice per topic)
- ✅ Mock Exam mode (45-minute full exam)
- ✅ Challenge Mode (PSLE brain drainers - 15 tricky questions)
- ✅ Progress Tracker (comprehensive statistics)
- ✅ Settings with 2-step reset confirmation
- ✅ Enhanced Maltese dog feedback (happy/sad animations)
- ✅ Performance analytics by difficulty and concept
- ✅ All 25+ MCQ questions fully tested
- ❌ NO database (single browser session only)
- ❌ NO user login (single user per browser)
- ❌ NO multi-user support

**Status:** FROZEN (May 16, 2026) - Locked for production, all bugs fixed

**Known Limitations:**
- Progress only saved in browser session (localStorage)
- If browser cleared, all progress lost
- Cannot share progress between devices
- No admin view for multiple users

**Bugs Fixed in v2.2:**
1. ✅ KeyError: 'difficulty' crash on first question
2. ✅ Next button double-jumping (jumping 2 questions)
3. ✅ Score calculation bug (34/30, 113.3% accuracy)
4. ✅ Answer validation prevents skipping questions
5. ✅ Double-count guard prevents score inflation

---

### v1.0 - Original Buggy Version
**Filename**: `versions/app_exam_prep_pro_v1.0.py`

**Status:** DEPRECATED - Do not use

**Known Bugs:**
- ❌ KeyError: 'difficulty' crash
- ❌ Next button jumps 2 questions
- ❌ Score exceeds total (34/30)
- ❌ Accuracy exceeds 100% (113.3%)

---

## How to Rollback to v2.2

If you need to rollback to v2.2 (without database integration):

**Step 1: Copy the clean version**
```powershell
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
Copy-Item versions/app_exam_prep_pro_v2.2_no_database.py app_exam_prep_pro.py -Force
```

**Step 2: Commit and push**
```powershell
git add app_exam_prep_pro.py
git commit -m "Rollback to v2.2 (no database integration)"
git push
```

**Step 3: Wait 1-2 minutes**
- Streamlit Cloud will auto-redeploy
- Live version reverts to v2.2

---

## Future Versions

### v3.1+ Planned Features (Post-Deployment)
- [ ] Leaderboard (top scorers)
- [ ] Weekly challenges
- [ ] Email progress reports
- [ ] Mobile app version
- [ ] Spaced repetition algorithm
- [ ] AI-suggested weak topics

---

## Quick Reference

| Version | Features | Users | Data Persistence | Admin View |
|---------|----------|-------|-----------------|-----------|
| v1.0 | Basic quiz | 1 | ❌ Session only | ❌ |
| v2.2 | All features | 1 | ❌ localStorage | ❌ |
| v3.0 | All + database | ✅ Multi-user | ✅ SQLite | ✅ Admin Dashboard |

---

**Last Updated**: May 16, 2026
**Maintained By**: Development Team
**Backup Location**: `versions/` folder

