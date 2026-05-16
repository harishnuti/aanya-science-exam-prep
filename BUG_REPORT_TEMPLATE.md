# 🐛 BUG REPORT - Phase 2 v4.0 Master App

Use this template to report bugs found during testing. Copy the format below for each bug.

---

## BUG #1: [Brief Title]

### Severity
- [ ] 🔴 **Critical** - App crashes, core feature broken
- [ ] 🟠 **High** - Feature doesn't work, major impact
- [ ] 🟡 **Medium** - Feature partially works, workaround possible
- [ ] 🟢 **Low** - Cosmetic issue, doesn't affect functionality

### Environment
- **OS**: Windows / Mac / Linux
- **Browser**: Chrome / Safari / Firefox / Edge
- **Deployment**: Local / Streamlit Cloud
- **Date Found**: ___________
- **Tester**: ___________

### Description
Clear description of the bug:

___________________________________________________________

### Steps to Reproduce
1. ___________________________________________________________
2. ___________________________________________________________
3. ___________________________________________________________
4. ___________________________________________________________

### Expected Behavior
What should happen:

___________________________________________________________

### Actual Behavior
What actually happens:

___________________________________________________________

### Screenshots/Logs
Paste error messages or console logs:

```
[Error message/log here]
```

### Additional Notes
Any extra context:

___________________________________________________________

### Affected Component
- [ ] Login/Auth
- [ ] Home Page
- [ ] Chapter Navigation
- [ ] Mock Exam
- [ ] Challenge Mode
- [ ] Analytics
- [ ] Admin Dashboard
- [ ] Database
- [ ] UI/Styling
- [ ] Performance
- [ ] Other: ___________

---

## BUG #2: [Brief Title]

### Severity
- [ ] 🔴 **Critical**
- [ ] 🟠 **High**
- [ ] 🟡 **Medium**
- [ ] 🟢 **Low**

### Environment
- **OS**: ___________
- **Browser**: ___________
- **Deployment**: ___________
- **Date Found**: ___________
- **Tester**: ___________

### Description
___________________________________________________________

### Steps to Reproduce
1. ___________________________________________________________
2. ___________________________________________________________

### Expected Behavior
___________________________________________________________

### Actual Behavior
___________________________________________________________

### Screenshots/Logs
```
[Error message/log here]
```

### Additional Notes
___________________________________________________________

### Affected Component
- [ ] Login/Auth
- [ ] Home Page
- [ ] Chapter Navigation
- [ ] Mock Exam
- [ ] Challenge Mode
- [ ] Analytics
- [ ] Admin Dashboard
- [ ] Database
- [ ] UI/Styling
- [ ] Performance
- [ ] Other: ___________

---

## BUG #3: [Brief Title]

### Severity
- [ ] 🔴 **Critical**
- [ ] 🟠 **High**
- [ ] 🟡 **Medium**
- [ ] 🟢 **Low**

### Environment
- **OS**: ___________
- **Browser**: ___________
- **Deployment**: ___________
- **Date Found**: ___________
- **Tester**: ___________

### Description
___________________________________________________________

### Steps to Reproduce
1. ___________________________________________________________
2. ___________________________________________________________

### Expected Behavior
___________________________________________________________

### Actual Behavior
___________________________________________________________

### Screenshots/Logs
```
[Error message/log here]
```

### Additional Notes
___________________________________________________________

### Affected Component
- [ ] Login/Auth
- [ ] Home Page
- [ ] Chapter Navigation
- [ ] Mock Exam
- [ ] Challenge Mode
- [ ] Analytics
- [ ] Admin Dashboard
- [ ] Database
- [ ] UI/Styling
- [ ] Performance
- [ ] Other: ___________

---

## SUMMARY OF ALL BUGS

### Critical Bugs (🔴)
- _______________________________________________________
- _______________________________________________________

### High Priority Bugs (🟠)
- _______________________________________________________
- _______________________________________________________

### Medium Priority Bugs (🟡)
- _______________________________________________________
- _______________________________________________________

### Low Priority Bugs (🟢)
- _______________________________________________________
- _______________________________________________________

---

## HOW TO REPORT BUGS

### Option 1: In This File
- Copy the template above
- Fill in your bug details
- Add to this file
- Commit to git: `git add BUG_REPORT_TEMPLATE.md && git commit -m "Report: [bug title]"`
- Push: `git push`

### Option 2: Create New File
- Create `BUG_REPORT_[DATE].md`
- Use template format
- Commit and push

### Option 3: GitHub Issues
- Go to: https://github.com/harishnuti/aanya-science-exam-prep
- Click "Issues"
- Click "New Issue"
- Use this template format

---

## EXAMPLE BUG REPORT

### Severity
- [x] 🟠 **High**

### Environment
- **OS**: Windows 10
- **Browser**: Chrome
- **Deployment**: Streamlit Cloud
- **Date Found**: May 16, 2026
- **Tester**: Harry

### Description
When answering questions in mock exam, clicking "Next" skips 2 questions instead of 1.

### Steps to Reproduce
1. Login with any username
2. Click "🎯 45-Min Mock Exam"
3. Answer Question 1
4. Click "Next >" button
5. Observe - now on Question 3 (skipped Question 2)
6. Click "Previous <" button
7. Verify - back on Question 1 (skipped Question 2)

### Expected Behavior
Clicking "Next" should advance exactly 1 question. Current on Q1, click Next = go to Q2.

### Actual Behavior
Clicking "Next" advances 2 questions. Current on Q1, click Next = go to Q3.

### Screenshots/Logs
```
Question counter jumps from 1 to 3
Expected: 1 → 2 → 3 → 4...
Actual: 1 → 3 → 5 → 7...
```

### Additional Notes
This affects the entire mock exam experience. User can't answer all questions properly.

### Affected Component
- [x] Mock Exam

---

## TRACKING FIX STATUS

When you fix a bug, update it like this:

```
### Fix Status
- [ ] Not Started
- [ ] In Progress
- [ ] Fixed
- [ ] Tested
- [ ] Deployed

Fix Applied: _______________________________
Fixed By: _______________________________
Date Fixed: _______________________________
Commit: _______________________________
```

---

## Questions?

Refer to:
1. `TESTING_CHECKLIST.md` - What to test
2. `MASTER_APP_V4.0_GUIDE.md` - How features work
3. `RESUME_HERE.md` - Quick reference
4. Code: `apps/exam_prep_master.py`

