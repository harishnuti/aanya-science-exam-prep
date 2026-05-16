# ✅ TESTING CHECKLIST - Phase 2 v4.0 Master App

**Date**: May 16, 2026  
**Version**: 4.0 - Frozen for Testing  
**Status**: Ready for comprehensive testing  

---

## 🎯 Testing Instructions

For each section below:
1. Follow the steps exactly
2. Document results (✅ pass, ❌ fail, 🟡 issue)
3. If fail/issue, use `BUG_REPORT_TEMPLATE.md` to report
4. Take screenshots for documentation

---

## 📋 TEST SUITE 1: LOGIN & AUTHENTICATION

### Test 1.1: Basic Login
**Steps:**
1. Go to app (local: `localhost:8501` or Streamlit Cloud URL)
2. Enter name: `Aanya`
3. Click `✅ Login`
4. Observe home page

**Expected:**
- ✅ Login page loads
- ✅ Input field is visible
- ✅ Login button is clickable
- ✅ Home page appears with personalized welcome: "🌟 Welcome, Aanya! 🌟"
- ✅ No errors in console

**Result:** _____ (Pass/Fail/Issue)

---

### Test 1.2: Multiple User Logins
**Steps:**
1. Login as user "Aanya" (complete test 1.1)
2. Click `🚪 Logout` button
3. Enter name: `Chan Chan`
4. Click `✅ Login`
5. Verify welcome shows "Chan Chan"
6. Logout and login as "test"
7. Verify welcome shows "test"

**Expected:**
- ✅ Each user sees their own name in welcome
- ✅ Welcome message: "🌟 Welcome, [name]! 🌟"
- ✅ Each login is independent
- ✅ No cross-user data visible

**Result:** _____ (Pass/Fail/Issue)

---

### Test 1.3: Gamification Stats Display
**Steps:**
1. Login as any user
2. Check home page stats section (4 cards at top)
3. Verify each stat shows:
   - ⚡ Level: 1
   - 🔥 Streak: 0 days
   - 🏆 Badges: 0
   - 🎯 Best Streak: 0 days

**Expected:**
- ✅ All 4 stat cards visible
- ✅ First login shows Level 1, XP 0, Streak 0
- ✅ Values update correctly (tested in next section)
- ✅ No "-" or "error" values

**Result:** _____ (Pass/Fail/Issue)

---

### Test 1.4: Admin Access
**Steps:**
1. At login screen, expand `🔑 Admin Access`
2. Enter password: `admin123`
3. Click `📊 View Admin Dashboard`
4. Observe dashboard

**Expected:**
- ✅ Admin access section expands
- ✅ Password field appears
- ✅ Correct password (admin123) opens dashboard
- ✅ Wrong password shows error
- ✅ Admin dashboard shows all users

**Result:** _____ (Pass/Fail/Issue)

---

## 📊 TEST SUITE 2: HOME PAGE UI

### Test 2.1: Welcome Banner
**Steps:**
1. Login with username "Aanya"
2. Look at the large purple gradient banner at top

**Expected:**
- ✅ Banner shows: "🌟 Welcome, Aanya! 🌟"
- ✅ Subtext: "🚀 Master all 6 chapters AND ace your PSLE exam!"
- ✅ Purple-pink gradient background
- ✅ Centered text, large font
- ✅ Professional styling

**Result:** _____ (Pass/Fail/Issue)

---

### Test 2.2: Learning Path Cards
**Steps:**
1. On home page, scroll down to "Choose Your Learning Path"
2. Look at 3 cards displayed

**Expected:**
- ✅ Card 1: "📖 Learn All Chapters" (green gradient)
- ✅ Card 2: "🎯  45-Min Mock Exam" (blue gradient)
- ✅ Card 3: "📊 View Progress" (light blue gradient)
- ✅ Each card has description text
- ✅ Each card has clickable button

**Result:** _____ (Pass/Fail/Issue)

---

### Test 2.3: Challenge Section
**Steps:**
1. On home page, scroll down to "Challenge Yourself!"
2. Look at the challenge banner

**Expected:**
- ✅ Banner shows: "🎯 Challenge to [username]!"
- ✅ Text mentions "PSLE-Style Brain Drainers"
- ✅ Mentions "tricky questions"
- ✅ Pink-yellow gradient
- ✅ "Start Brain Drain Challenge →" button

**Result:** _____ (Pass/Fail/Issue)

---

## 📚 TEST SUITE 3: CHAPTER NAVIGATION

### Test 3.1: Chapter Selection
**Steps:**
1. On home page, click `📚 Master All Chapters` button
2. Observe chapter selection page

**Expected:**
- ✅ Page title: "📚 Master All Chapters | [username]"
- ✅ All 6 chapters displayed in grid:
  - 🌱 Ch 1: Reproduction in Animals & Plants
  - 💧 Ch 2: Cycles in Water
  - 🌿 Ch 3: Plant Transport
  - ❤️ Ch 4: Human Systems
  - ⚡ Ch 5: Electrical Systems
  - 🔌 Ch 6: Electric Circuits
- ✅ Each chapter card shows topics list
- ✅ Each has clickable button

**Result:** _____ (Pass/Fail/Issue)

---

### Test 3.2: Chapter Button Navigation
**Steps:**
1. On chapter selection page
2. Click button for Chapter 1
3. Observe result

**Expected:**
- ✅ Navigates to practice mode (or placeholder page)
- ✅ Page shows chapter content
- ✅ Can navigate back to home
- ✅ No errors in console

**Result:** _____ (Pass/Fail/Issue)

---

### Test 3.3: Back Navigation
**Steps:**
1. From any page, click `← Back` button (or in header)
2. Verify return to previous page

**Expected:**
- ✅ Clicking back returns to home
- ✅ From chapter page, back goes to chapter select
- ✅ State is preserved correctly
- ✅ No data loss

**Result:** _____ (Pass/Fail/Issue)

---

## 🎯 TEST SUITE 4: MOCK EXAM

### Test 4.1: Mock Exam Start
**Steps:**
1. On home page, click `🎯 45-Min Mock Exam`
2. Observe exam start

**Expected:**
- ✅ Page title: "🎯 FULL MOCK EXAM - 45 Minutes | [username]"
- ✅ Timer displays (45:00 or similar)
- ✅ First question visible
- ✅ Question number shown
- ✅ 4 answer options displayed

**Result:** _____ (Pass/Fail/Issue)

---

### Test 4.2: Question Navigation
**Steps:**
1. In mock exam, select an answer
2. Click "Next" button
3. Verify next question appears
4. Click "Previous" button
5. Verify previous question appears

**Expected:**
- ✅ Next button advances exactly 1 question
- ✅ Previous button goes back exactly 1 question
- ✅ Question counter updates (e.g., "Question 2 of 25")
- ✅ Selected answer is remembered when navigating

**Result:** _____ (Pass/Fail/Issue)

---

### Test 4.3: Question Feedback
**Steps:**
1. Answer a question
2. Observe feedback

**Expected:**
- ✅ If correct: ✅ appears, maybe Maltese dog celebration
- ✅ If incorrect: ❌ appears, explanation shown
- ✅ Correct answer highlighted
- ✅ Feedback is clear and helpful

**Result:** _____ (Pass/Fail/Issue)

---

### Test 4.4: Exam Results
**Steps:**
1. Complete all questions in mock exam (or scroll to end)
2. Click "Submit Exam"
3. Observe results page

**Expected:**
- ✅ Results page appears
- ✅ Shows score: "X/25 (Y%)"
- ✅ Shows XP earned: "🎉 +Z XP!"
- ✅ Summary table of results
- ✅ Performance breakdown (by difficulty, concept)
- ✅ Back to home button

**Result:** _____ (Pass/Fail/Issue)

---

## 🧠 TEST SUITE 5: CHALLENGE MODE

### Test 5.1: Challenge Mode Start
**Steps:**
1. On home page, click `🧠 Challenge to [username]!` button
2. Observe challenge page

**Expected:**
- ✅ Challenge mode page loads
- ✅ Title shows username: "🧠 Brain Drainer Challenge | [username]"
- ✅ First brain drainer question appears
- ✅ Question number shown

**Result:** _____ (Pass/Fail/Issue)

---

### Test 5.2: Brain Drainer Question Format
**Steps:**
1. On challenge mode page
2. Examine the question

**Expected:**
- ✅ Question text is clear
- ✅ 4 answer options (usually similar-looking)
- ✅ Difficulty label: 🟡 Easy, 🟠 Medium, or 🔴 Hard
- ✅ "Explain the trap" option available
- ✅ Concept mentioned (e.g., "Photosynthesis")

**Result:** _____ (Pass/Fail/Issue)

---

### Test 5.3: Challenge Feedback
**Steps:**
1. Answer a brain drainer question
2. Observe feedback
3. Click "Explain the trap" if available

**Expected:**
- ✅ Feedback shown (correct/incorrect)
- ✅ Correct answer highlighted
- ✅ Trap answer explanation appears when clicked
- ✅ Explanation helps understand misconception
- ✅ XP awarded (if wired in)

**Result:** _____ (Pass/Fail/Issue)

---

## 📊 TEST SUITE 6: ANALYTICS & PROGRESS

### Test 6.1: Analytics Page
**Steps:**
1. On home page, click `📊 View Analytics`
2. Observe analytics page

**Expected:**
- ✅ Page title shows username
- ✅ Overall stats displayed:
  - Total Correct/Total Answered
  - Overall Accuracy (%)
  - Average Confidence
  - Total Sessions
- ✅ Performance by difficulty table
- ✅ Weak concepts section
- ✅ Navigation buttons (More Practice, Back to Home)

**Result:** _____ (Pass/Fail/Issue)

---

### Test 6.2: Progress Data Accuracy
**Steps:**
1. Complete a quiz or exam
2. Go to analytics
3. Verify stats match quiz results

**Expected:**
- ✅ Total correct matches quiz results
- ✅ Accuracy % calculated correctly
- ✅ Performance by difficulty accurate
- ✅ Weak concepts identified (if < 70%)
- ✅ Data persists across page refreshes

**Result:** _____ (Pass/Fail/Issue)

---

## 👥 TEST SUITE 7: MULTI-USER & DATABASE

### Test 7.1: User Isolation
**Steps:**
1. Login as "User1", complete a quiz
2. Check analytics
3. Logout
4. Login as "User2"
5. Check analytics (should be empty)

**Expected:**
- ✅ User1 has their quiz results
- ✅ User2 starts fresh
- ✅ No cross-user data
- ✅ Database isolates users correctly

**Result:** _____ (Pass/Fail/Issue)

---

### Test 7.2: Data Persistence
**Steps:**
1. Login as "User1"
2. Complete a quiz
3. Refresh page (F5)
4. Check if data still there

**Expected:**
- ✅ Data persists after refresh
- ✅ Results still visible
- ✅ Database working correctly
- ✅ No data loss

**Result:** _____ (Pass/Fail/Issue)

---

### Test 7.3: Admin Dashboard Data
**Steps:**
1. Login as 3+ different users, complete quizzes
2. Access admin dashboard
3. Verify user data shown

**Expected:**
- ✅ All users listed in table
- ✅ User names correct
- ✅ Level shown
- ✅ XP count shown
- ✅ Sessions count accurate
- ✅ Badges count shown

**Result:** _____ (Pass/Fail/Issue)

---

## ⚡ TEST SUITE 8: PERFORMANCE & STABILITY

### Test 8.1: App Load Time
**Steps:**
1. Navigate to app
2. Time how long home page loads
3. Reload multiple times

**Expected:**
- ✅ First load: < 5 seconds
- ✅ Subsequent loads: < 2 seconds
- ✅ Consistent performance
- ✅ No lag or freezing

**Result:** _____ (Pass/Fail/Issue) | Time: _____ seconds

---

### Test 8.2: Navigation Speed
**Steps:**
1. Click between different sections
2. Time page transitions
3. Try rapid clicking

**Expected:**
- ✅ Instant transitions (< 1 second)
- ✅ No lag when clicking buttons
- ✅ Graceful handling of rapid clicks
- ✅ No double-submissions

**Result:** _____ (Pass/Fail/Issue)

---

### Test 8.3: Stability Under Use
**Steps:**
1. Perform multiple complete workflows:
   - Login → Chapter → Home → Analytics → Logout
   - Login → Mock Exam → Home → Admin → Logout
   - Login → Challenge → Home → Logout
2. No crashes or errors

**Expected:**
- ✅ App never crashes
- ✅ No console errors
- ✅ All pages responsive
- ✅ Graceful error handling

**Result:** _____ (Pass/Fail/Issue)

---

## 🔄 TEST SUITE 9: GAMIFICATION (WHEN WIRED)

### Test 9.1: XP Awarding
**Steps:**
1. Login, check initial XP (should be 0)
2. Complete a quiz question correctly
3. Check if XP increases
4. Complete 10+ questions

**Expected:**
- ✅ XP increases for correct answers
- ✅ Different questions award different XP
- ✅ XP count updates in real-time
- ✅ Total accumulated correctly

**Result:** _____ (Pass/Fail/Issue)

---

### Test 9.2: Level Progression
**Steps:**
1. Complete enough activities to earn 200 XP
2. Verify Level increases from 1 to 2

**Expected:**
- ✅ Level increases at XP milestones
- ✅ Level progression correct
- ✅ Achievement badge shows level up
- ✅ XP resets for next level

**Result:** _____ (Pass/Fail/Issue)

---

### Test 9.3: Achievements
**Steps:**
1. Complete activities to unlock achievements
2. Check achievements list

**Expected:**
- ✅ Achievements unlock automatically
- ✅ Celebration when unlocked
- ✅ Achievement shown in dashboard
- ✅ Multiple users can have different achievements

**Result:** _____ (Pass/Fail/Issue)

---

## 🌐 TEST SUITE 10: RESPONSIVE & BROWSER COMPATIBILITY

### Test 10.1: Desktop View
**Steps:**
1. Open app on desktop
2. Resize window (1920x1080, 1366x768, 1280x720)
3. Check all elements visible and aligned

**Expected:**
- ✅ All elements visible at different sizes
- ✅ Cards stack properly
- ✅ Text readable
- ✅ Buttons clickable
- ✅ No horizontal scrolling needed

**Result:** _____ (Pass/Fail/Issue)

---

### Test 10.2: Tablet View
**Steps:**
1. Open app on tablet (or resize to 768 width)
2. Navigate all pages
3. Check touch interactions

**Expected:**
- ✅ Buttons large enough to tap
- ✅ Text readable
- ✅ Responsive layout works
- ✅ No zoom needed

**Result:** _____ (Pass/Fail/Issue)

---

### Test 10.3: Mobile View
**Steps:**
1. Open app on mobile (or resize to 375 width)
2. Navigate pages
3. Check usability

**Expected:**
- ✅ Content readable
- ✅ Buttons tappable
- ✅ Layout optimized
- ✅ Navigation clear

**Result:** _____ (Pass/Fail/Issue)

---

## 📝 TEST SUMMARY

### Results Overview
- **Total Tests**: 30+
- **Passed**: _____
- **Failed**: _____
- **Issues**: _____

### Critical Issues Found
(List any critical bugs that block functionality)

1. _________________
2. _________________
3. _________________

### Medium Issues Found
(List any medium bugs that reduce functionality)

1. _________________
2. _________________

### Minor Issues Found
(List any cosmetic/minor issues)

1. _________________
2. _________________

---

## 🎯 Next Steps

1. Report all failures/issues using `BUG_REPORT_TEMPLATE.md`
2. Categorize by severity (Critical/High/Medium/Low)
3. Track fixes and retest
4. Update this checklist after each fix

---

**Testing Date**: ___________  
**Tester Name**: ___________  
**Environment**: Windows / Mac / Linux | Browser: ___________

