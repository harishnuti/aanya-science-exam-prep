# 🧭 Navigation & Progress Features - Quick Reference

**Last Updated**: May 16, 2026  
**Apps Covered**: app_exam_prep_pro.py (Exam Prep Pro)  

---

## 🏠 Home Page Overview

```
┌─────────────────────────────────────────────────────────────┐
│                 AANYA'S SCIENCE EXAM PREP PRO                │
│                   MCQ-Focused PSLE Training                  │
├─────────────────────────────────────────────────────────────┤
│  📊 Quick Stats: Total Attempted | Accuracy | Exam Info     │
├─────────────────────────────────────────────────────────────┤
│                   🎯 CHOOSE YOUR LEARNING PATH               │
│  ┌──────────────────┬──────────────────┬──────────────────┐  │
│  │  📖 Topic        │  🎯 Mock Exam    │  📊 Performance  │  │
│  │  Mastery         │                  │  Review          │  │
│  │  [Start Button]  │  [Start Button]  │  [View Button]   │  │
│  └──────────────────┴──────────────────┴──────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                📊 MANAGE YOUR LEARNING                       │
│  ┌──────────────────────────┬──────────────────────────┐    │
│  │  📈 Progress Tracker     │  ⚙️ Settings             │    │
│  │  View Statistics         │  Manage Progress         │    │
│  │  [View Progress →]       │  [Open Settings →]       │    │
│  └──────────────────────────┴──────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📖 Topic Mastery Mode - 5-Button Navigation

```
┌─────────────────────────────────────────────────────────────┐
│  Q1/10: What is the melting point of ice?                   │
│  📌 Concept: Phase Changes | Ref: Page 31 | EASY            │
├─────────────────────────────────────────────────────────────┤
│  ⭕ 0°C                                                       │
│  ⭕ 10°C                                                      │
│  ⭕ -10°C                                                     │
│  ⭕ 100°C                                                     │
├─────────────────────────────────────────────────────────────┤
│  Confidence: [========]  3/5                                 │
├─────────────────────────────────────────────────────────────┤
│  ┌──────┬──────────┬──────────┬─────────┬──────────────────┐│
│  │ ⬅️   │ ✓ Check  │ Next ➡️  │ 🔄      │ 🏠 Exit to Home  ││
│  │ Prev │  Answer  │          │ Reset   │                  ││
│  └──────┴──────────┴──────────┴─────────┴──────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

**Button Guide:**
| Button | Disabled When | Action |
|--------|---------------|--------|
| ⬅️ Previous | On first question | Go to previous question |
| ✓ Check Answer | - | Submit answer & show result |
| Next ➡️ | On last question | Go to next question |
| 🔄 Reset | - | Clear all answers & start over |
| 🏠 Exit to Home | - | Return to home (saves progress) |

---

## 🎯 Mock Exam Mode - 5-Button Navigation

```
┌─────────────────────────────────────────────────────────────┐
│  FULL MOCK EXAM - 45 Minutes                                │
│  All 3 Topics - 25+ MCQ Questions         ⏱️ 42:15  5/25    │
├─────────────────────────────────────────────────────────────┤
│  Q5/25: Which process happens when wet clothes dry?         │
│  📌 Concept: Evaporation | Ref: Page 42 | EASY              │
├─────────────────────────────────────────────────────────────┤
│  ⭕ Melting                                                   │
│  ⭕ Freezing                                                  │
│  ⭕ Evaporation                                               │
│  ⭕ Condensation                                              │
├─────────────────────────────────────────────────────────────┤
│  Confidence: [========]  3/5                                 │
├─────────────────────────────────────────────────────────────┤
│  ┌──────┬──────────┬──────────┬─────────┬──────────────────┐│
│  │ ⬅️   │ ✓ Submit │ Next ➡️  │ 🔄      │ 🏠 Exit to Home  ││
│  │ Prev │  Answer  │          │ Reset   │                  ││
│  └──────┴──────────┴──────────┴─────────┴──────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

**Special Notes:**
- Timer counts down (⏱️ minutes:seconds)
- Auto-shows results when time expires
- Progress bar shows exam completion %
- Exit to Home pauses exam (can resume later)

---

## 📈 Progress Tracker - What You'll See

```
┌─────────────────────────────────────────────────────────────┐
│  📈 PROGRESS TRACKER - Your Learning Journey                │
├─────────────────────────────────────────────────────────────┤
│                    📊 OVERALL STATISTICS                    │
│  ┌──────────────┬──────────────┬──────────────┬─────────┐  │
│  │ Questions    │ ✅ Correct   │ Overall      │ Avg      │  │
│  │ Answered: 15 │ Answers: 12  │ Accuracy:    │ Confid:  │  │
│  │              │              │ 80.0%        │ 3.8/5    │  │
│  └──────────────┴──────────────┴──────────────┴─────────┘  │
├─────────────────────────────────────────────────────────────┤
│            🎯 PERFORMANCE BY DIFFICULTY LEVEL                │
│  ┌─────────────┬──────────┬──────────┬──────────────────┐  │
│  │ Difficulty  │ Correct  │ Accuracy │ Status           │  │
│  ├─────────────┼──────────┼──────────┼──────────────────┤  │
│  │ EASY        │ 5/5      │ 100%     │ 🟢 Strong        │  │
│  │ MEDIUM      │ 6/7      │ 86%      │ 🟢 Strong        │  │
│  │ HARD        │ 1/3      │ 33%      │ 🔴 Needs Work    │  │
│  └─────────────┴──────────┴──────────┴──────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│           📚 PERFORMANCE BY CONCEPT/TOPIC                    │
│  ┌──────────────────┬──────────┬──────────┬─────────────┐  │
│  │ Concept          │ Correct  │ Accuracy │ Status      │  │
│  ├──────────────────┼──────────┼──────────┼─────────────┤  │
│  │ Phase Changes    │ 4/4      │ 100%     │ 🟢          │  │
│  │ Evaporation      │ 3/4      │ 75%      │ 🟡          │  │
│  │ Water Cycle      │ 2/3      │ 67%      │ 🔴          │  │
│  │ Condensation     │ 3/4      │ 75%      │ 🟡          │  │
│  └──────────────────┴──────────┴──────────┴─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│              ⚠️ AREAS FOR IMPROVEMENT                        │
│  📌 Water Cycle: 67% accuracy (2/3 correct)                │
│  → Focus on: Water cycle stages and evaporation timing      │
├─────────────────────────────────────────────────────────────┤
│              📋 COMPLETE ANSWER HISTORY                      │
│  ┌──────┬──────┬──────┬────┬────┬────┬──────────────────┐  │
│  │Question│Your  │Corr. │Rslt│Conf│Diff│Concept        │  │
│  ├──────┼──────┼──────┼────┼────┼────┼──────────────────┤  │
│  │What is│0°C  │0°C  │✅  │4/5│EASY│Phase Changes   │  │
│  │melting│     │     │    │   │    │                │  │
│  │point? │     │     │    │   │    │                │  │
│  └──────┴──────┴──────┴────┴────┴────┴──────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  [📖 More Practice] [⚙️ Settings] [🏠 Back to Home]         │
└─────────────────────────────────────────────────────────────┘
```

**Key Information Shown:**
- ✅ Total questions answered
- ✅ Number correct
- ✅ Accuracy percentage
- ✅ Average confidence level
- ✅ Breakdown by difficulty (easy/medium/hard)
- ✅ Breakdown by concept/topic
- ✅ Weak areas identified (<70%)
- ✅ Complete table of all answers
- ✅ Visual status indicators (🟢🟡🔴)

---

## ⚙️ Settings Page - Progress Management

```
┌─────────────────────────────────────────────────────────────┐
│  ⚙️ SETTINGS & PROGRESS MANAGEMENT                          │
├─────────────────────────────────────────────────────────────┤
│  [Progress Management] [App Settings]                       │
├─────────────────────────────────────────────────────────────┤
│                  🗂️ PROGRESS MANAGEMENT                     │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────────┬──────────────────┬──────────────────┐ │
│  │ Questions        │ ✅ Correct       │ Overall Accuracy │ │
│  │ Answered: 0      │ Answers: 0       │ -                │ │
│  └──────────────────┴──────────────────┴──────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                  🔄 RESET PROGRESS                          │
│  ⚠️ WARNING: This action will permanently delete:            │
│  • All answers you've submitted                              │
│  • Your accuracy scores                                      │
│  • Your practice history                                     │
│  • Your confidence ratings                                   │
├─────────────────────────────────────────────────────────────┤
│  ☐ I understand that resetting will delete all progress     │
│                                                              │
│  [Reset button DISABLED until you check the box]            │
│                                                              │
│  ✓ Confirmation enabled.                                    │
│  [🔴 RESET ALL PROGRESS]  ← Becomes red & enabled          │
│                                                              │
│  ✅ All progress has been reset successfully!               │
│  You can now start fresh.                                   │
│  Redirecting to home in 2 seconds...                        │
├─────────────────────────────────────────────────────────────┤
│  [📈 View Progress] [🏠 Back to Home]                       │
└─────────────────────────────────────────────────────────────┘
```

**How It Works:**
1. Read the ⚠️ warning carefully
2. Check the "I understand..." checkbox
3. "Reset All Progress" button becomes enabled (red)
4. Click to reset
5. All data deleted immediately
6. Auto-redirect to home page

---

## 🔄 Complete Navigation Paths

### Path 1: Practice → Check Progress → Settings
```
Home
  ↓ [View Progress →]
  ↓ Progress Tracker
  ├─ [⚙️ Settings]
  │   └─ Reset Progress (optional)
  │       └─ [🏠 Back to Home]
  └─ [🏠 Back to Home]
      └─ Home
```

### Path 2: Quiz → Exit Mid-Quiz → Review Progress
```
Home
  ↓ [Start Topic Practice →]
  ↓ Topic Select
  ↓ Practice Mode (Q1)
  ├─ [🏠 Exit to Home] → Home
  │                    ↓ [View Progress →]
  │                    ↓ Progress Tracker (shows Q1 data)
  │                    └─ [🏠 Back to Home] → Home
  └─ Continue normally...
```

### Path 3: Complete Practice → See Summary → Check Overall Progress
```
Home
  ↓ [Start Topic Practice →]
  ↓ Topic Select
  ↓ Complete All Questions
  ↓ Topic Results (summary table)
  ├─ [🔄 Retry Topic] → Start over
  ├─ [🏠 Back to Topics] → Topic Select
  ├─ [🏠 Home] → Home
  │           ↓ [View Progress →]
  │           ↓ Progress Tracker
  │           ├─ All historical data shown
  │           └─ [🏠 Back to Home] → Home
  └─ Continue...
```

---

## 🧪 Quick Testing Checklist

### For Aanya During Bug Window (May 16-18)

**✅ Navigation Tests**
- [ ] During practice, click all 5 navigation buttons
- [ ] Exit to Home mid-quiz and come back
- [ ] Verify answers are still saved after exit
- [ ] Practice complete topic, see summary
- [ ] From summary, go back to topic select

**✅ Progress Tracker Tests**
- [ ] Open Progress Tracker after answering 3+ questions
- [ ] Verify statistics are accurate
- [ ] View answer history table
- [ ] Check that weak topics are highlighted
- [ ] Navigate back to home from Progress Tracker

**✅ Settings Tests**
- [ ] Open Settings from home page
- [ ] Read warning message
- [ ] Try to reset WITHOUT checking box
- [ ] Reset button should stay DISABLED
- [ ] Check the "I understand..." box
- [ ] Reset button becomes ENABLED (red)
- [ ] Click reset and verify all data cleared
- [ ] Verify Progress Tracker shows "No data" after reset

**✅ Data Persistence Tests**
- [ ] Answer quiz questions
- [ ] Exit to Home (don't finish)
- [ ] Close the browser
- [ ] Reopen app and start quiz again
- [ ] Verify previous answers still saved

---

## 📱 Features by App

| Feature | app_exam_prep_pro.py | app_phase2.py |
|---------|----------------------|---------------|
| Exit to Home (quiz) | ✅ NEW | ✅ Existing |
| Progress Tracker | ✅ NEW | ✅ Existing |
| Settings Page | ✅ NEW | ✅ Existing |
| Reset Progress | ✅ NEW (2-step) | ✅ Existing (checkbox) |
| Answer History | ✅ NEW (table) | ✅ Existing |
| Performance by Concept | ✅ NEW | ✅ Existing |
| Overall Statistics | ✅ Enhanced | ✅ Existing |

---

## 🆘 Troubleshooting

**Q: I clicked "Exit to Home" - did my answers get saved?**
- A: ✅ Yes! All submitted answers are saved. Unanswered questions are not saved.

**Q: I reset my progress. Can I undo it?**
- A: ❌ No, reset is permanent. You'll have to start fresh with new answers.

**Q: Why is the reset button disabled?**
- A: ✅ Safety feature. You must check "I understand..." first.

**Q: The Progress Tracker shows "No data". Why?**
- A: You haven't answered any questions yet OR your progress was reset.

**Q: Can I export my progress?**
- A: Not in this version. Available in app_phase2.py. Can be added if needed.

**Q: Are my answers saved in the cloud?**
- A: ❌ No, they're stored in your browser's localStorage. Clearing cache deletes them.

---

**Ready to test?** Start with topic practice and try each navigation button!  
**Found a bug?** Report it with: what happened, steps to reproduce, and expected behavior.

---

**Last Updated**: May 16, 2026  
**Status**: Ready for bug-window testing  
**Questions?** Check BUG_WINDOW_UPDATES.md for detailed documentation

