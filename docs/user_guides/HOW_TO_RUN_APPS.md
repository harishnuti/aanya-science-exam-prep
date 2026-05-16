# 🚀 HOW TO RUN THE APPS
## Quick Guide for Tomorrow (or Any Day)

**Last Updated**: 2026-05-16

---

## QUICK START (2 Steps)

### Step 1: Open Terminal/Command Prompt
```
Press: Windows Key + R
Type: cmd
Press: Enter
```

### Step 2: Run the App You Want

**Option A: Main Learning App** (RECOMMENDED)
```bash
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
streamlit run app_phase2.py
```
Opens at: **http://localhost:8503**

**Option B: Exam Prep Pro** (For Aanya's exam this week)
```bash
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
streamlit run app_exam_prep_pro.py
```
Opens at: **http://localhost:8503**

---

## DETAILED INSTRUCTIONS

### What You Need First
✅ Python 3.9+ installed (should be there)  
✅ Streamlit installed (already installed)  
✅ Internet browser (Chrome, Firefox, Safari, Edge)  

### Command Line Steps

#### 1. Navigate to Project Folder
```bash
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
```

#### 2. Choose Your App

**FOR AANYA'S GENERAL LEARNING** (Recommended):
```bash
streamlit run app_phase2.py
```
- 228 textbook-aligned questions
- 6 chapters to choose from
- Gamification (XP, badges, streaks)
- Brain drainers for PSLE practice
- Good for: Daily learning, practice

**FOR INTENSIVE EXAM PREP** (This week):
```bash
streamlit run app_exam_prep_pro.py
```
- 3 learning modes
- 45-minute mock exam
- Detailed analytics
- Confidence tracking
- Good for: Exam preparation (May 16-18)

**FOR BASIC EXAM PREP** (Legacy - use Pro instead):
```bash
streamlit run app_exam_prep.py
```
- Simpler interface
- Still functional
- Superseded by Pro version
- Don't use - use Pro instead

#### 3. App Opens Automatically
Browser opens at: **http://localhost:8503**

If it doesn't:
- Manually type: http://localhost:8503 in browser
- Or follow the link shown in terminal

#### 4. Use the App
- Navigate sidebar menus
- Click chapters to learn
- Answer questions
- Earn XP
- Track progress

#### 5. When Done
Press in terminal: **Ctrl + C**
App stops running

---

## WHICH FILE TO RUN? (Decision Guide)

### For Different Purposes:

**"I want Aanya to learn science topics"**
→ Run: `app_phase2.py`
→ Has: Flashcards, matching, quizzes, brain drainers
→ Good for: Anytime, any topic

**"I want Aanya to practice for her exam (May 16-18)"**
→ Run: `app_exam_prep_pro.py`
→ Has: Topic practice + 45-min mock exam + analytics
→ Good for: Intensive 3-day exam prep

**"I don't know which one"**
→ Use: `app_phase2.py` (most complete)
→ Why: Best for all-around learning

---

## FILE REFERENCE: What Each Does

### Main Files to Run

| File | Purpose | When to Use |
|------|---------|------------|
| **app_phase2.py** | Main learning app | Daily learning, practice |
| **app_exam_prep_pro.py** | Exam prep (advanced) | Exam preparation |
| **app_exam_prep.py** | Exam prep (basic) | Legacy - use Pro instead |

### Support Files (Don't Run These)

| File | Purpose |
|------|---------|
| modules/ch*_new.py | Chapter content (auto-loaded) |
| components/*.py | Features (auto-loaded) |
| utils/*.py | Utilities (auto-loaded) |
| config.py | Settings (auto-loaded) |

---

## TROUBLESHOOTING

### Problem: "Command not found" / "Python not installed"
**Solution**: 
1. Check Python is installed: `python --version`
2. If not installed, install from python.org
3. Restart terminal after installation

### Problem: "Port 8503 already in use"
**Solution**: 
1. Streamlit auto-assigns next port (8504, 8505, etc.)
2. Check terminal for new URL: "Local URL: http://localhost:850X"
3. Browser should open automatically

### Problem: Browser doesn't open automatically
**Solution**:
1. Find URL in terminal output: "Local URL: http://localhost:8503"
2. Copy and paste in browser manually
3. Should open the app

### Problem: "Module not found" error
**Solution**:
1. Make sure you're in correct directory: `C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2`
2. Check directory with: `dir`
3. You should see: `app_phase2.py` in the list

### Problem: "requirements not installed"
**Solution**:
1. Install dependencies: `pip install -r requirements.txt`
2. Or manually: `pip install streamlit plotly pandas numpy`
3. Then run app again

### Problem: App is very slow
**Solution**:
1. Wait 10-15 seconds (first load is slower)
2. Close other apps to free memory
3. Restart terminal and app

---

## COMPLETE COMMAND SEQUENCE (Copy & Paste)

### For Windows Command Prompt:
```cmd
cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2
streamlit run app_phase2.py
```

### For PowerShell:
```powershell
cd "C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2"
streamlit run app_phase2.py
```

### For Mac/Linux Terminal:
```bash
cd ~/OneDrive/AAIA/Aanya/streamlit/phase2
streamlit run app_phase2.py
```

---

## WHAT HAPPENS WHEN YOU RUN

### Terminal Output Example:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8503
  Network URL: http://192.168.1.24:8503

  Press CTRL+C to quit
```

### Browser Opens Showing:
- Sidebar with navigation menu
- Welcome message
- Chapter selection
- Statistics dashboard
- XP/level display

### Then:
- Click "📖 Chapters" to select a chapter
- Or "🧠 Brain Drainers" for PSLE practice
- Or "📊 Progress" to see stats
- Answer questions and earn XP!

---

## STOPPING THE APP

### When You're Done:

**In Terminal**:
```bash
Press: Ctrl + C
```

App stops, terminal prompt returns.

**Browser**:
- Close the tab
- Or leave it (app continues running until Ctrl+C)

---

## QUICK REFERENCE

| Action | Command |
|--------|---------|
| **Go to folder** | `cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2` |
| **Start main app** | `streamlit run app_phase2.py` |
| **Start exam prep** | `streamlit run app_exam_prep_pro.py` |
| **Open in browser** | http://localhost:8503 |
| **Stop app** | Ctrl + C (in terminal) |
| **Check Python** | `python --version` |
| **Install packages** | `pip install -r requirements.txt` |

---

## SUMMARY: 3 SIMPLE STEPS

### Tomorrow When You Want to Run:

1. **Open Command Prompt**
   - Windows Key + R → type `cmd` → Enter

2. **Run This Command**
   ```bash
   cd C:\Users\harry\OneDrive\AAIA\Aanya\streamlit\phase2 && streamlit run app_phase2.py
   ```

3. **Wait 5 Seconds**
   - Browser opens automatically
   - App is ready to use!

---

## THAT'S IT! 🎉

You now have everything you need to run the apps tomorrow.

**Questions?** Check:
- FINAL_SUMMARY.md (overview)
- CONTEXT_TRANSFER_GUIDE.md (detailed reference)
- PHASE_2_COMPLETE_DOCUMENTATION.md (technical specs)

---

**Version**: 1.0  
**Last Updated**: 2026-05-16  
**Status**: Ready to use tomorrow!
