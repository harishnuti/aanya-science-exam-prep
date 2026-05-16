# 🚀 STREAMLIT CLOUD DEPLOYMENT GUIDE - Phase 2 v4.0

**Date**: May 16, 2026  
**Version**: 4.0 - Master App  
**Status**: Production Ready  
**URL**: https://aanya-science-exam-prep.streamlit.app/

---

## 📋 TABLE OF CONTENTS

1. [Prerequisites](#prerequisites)
2. [Initial Deployment Setup](#initial-deployment-setup)
3. [GitHub Repository Configuration](#github-repository-configuration)
4. [Streamlit Cloud Connection](#streamlit-cloud-connection)
5. [Main File Configuration](#main-file-configuration)
6. [Secrets & Environment Variables](#secrets--environment-variables)
7. [Auto-Deployment Configuration](#auto-deployment-configuration)
8. [Monitoring & Troubleshooting](#monitoring--troubleshooting)
9. [Redeployment & Updates](#redeployment--updates)
10. [Common Issues & Solutions](#common-issues--solutions)

---

## 📌 PREREQUISITES

### Account & Tools Required
- ✅ GitHub account (with push access to repository)
- ✅ Streamlit Cloud account (free tier or paid)
- ✅ Git installed locally
- ✅ Python 3.10+ installed
- ✅ Repository cloned to local machine
- ✅ All dependencies in `requirements.txt`

### Repository Status
- ✅ GitHub repo: https://github.com/harishnuti/aanya-science-exam-prep
- ✅ Branch: `main` (production)
- ✅ All code committed and pushed
- ✅ .gitignore properly configured (excludes PDFs, database, caches)
- ✅ requirements.txt complete and tested

### Local Testing
```bash
# Before deploying, verify app runs locally:
cd /path/to/phase2/
streamlit run streamlit_app.py
# App should load at localhost:8501 without errors
```

---

## 🏗️ INITIAL DEPLOYMENT SETUP

### Step 1: Prepare Repository Structure

**Verify the following file structure at repository root**:

```
aanya-science-exam-prep/
├── streamlit_app.py              ✅ Main entry point (REQUIRED)
├── app_exam_prep_pro.py          ✅ Backward compatibility wrapper
├── streamlit.app                 ✅ Config file
├── requirements.txt              ✅ Dependencies
├── .gitignore                    ✅ Exclusions configured
├── README.md                     ✅ Project overview
├── apps/
│   ├── exam_prep_master.py       ✅ Master App v4.0 (main code)
│   └── README_APPS.md            ✅ Apps documentation
├── src/
│   ├── modules/                  ✅ (6 chapter modules)
│   ├── components/               ✅ (animations, gamification, etc.)
│   └── utils/                    ✅ (database, state_manager)
├── docs/                         ✅ (All documentation)
└── data/
    └── app.db                    ❌ Git-ignored (created at runtime)
```

**Files MUST exist at root level for Streamlit Cloud**:
- ✅ `streamlit_app.py` - Standard Streamlit Cloud entry point
- ✅ `app_exam_prep_pro.py` - Backward compatibility (if Streamlit looks here)
- ✅ `streamlit.app` - Optional config file

### Step 2: Verify requirements.txt

```bash
# Check all dependencies are listed:
cat requirements.txt

# Should contain:
# streamlit >= 1.28.0
# pandas >= 2.0.0
# plotly >= 5.17.0
# (sqlite3 is built-in, don't list it)
```

### Step 3: Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run streamlit_app.py

# Verify:
# - App loads without errors
# - Login page appears
# - Can login with any username
# - Home page displays with personalized welcome
# - All navigation buttons work
# - Database initializes (data/app.db created)
```

---

## 🔗 GITHUB REPOSITORY CONFIGURATION

### Step 1: Verify GitHub Repository

```bash
# Check remote is configured correctly
git remote -v
# Should show:
# origin  https://github.com/harishnuti/aanya-science-exam-prep (fetch)
# origin  https://github.com/harishnuti/aanya-science-exam-prep (push)

# Verify you're on main branch
git branch
# Should show: * main

# Verify all changes are committed
git status
# Should show: On branch main, nothing to commit, working tree clean

# Verify all changes are pushed
git log --oneline -5
# Compare with GitHub web interface - commits should match
```

### Step 2: GitHub Settings

**Go to https://github.com/harishnuti/aanya-science-exam-prep/settings**

**Branch Protection (Optional but Recommended)**:
1. Click "Branches" in sidebar
2. Add protection rule for `main`:
   - ✅ Require status checks to pass before merging
   - ✅ Dismiss stale pull request approvals
   - ✅ Require branches to be up to date before merging

**Collaborators (if applicable)**:
1. Click "Collaborators" in sidebar
2. Add team members if needed with appropriate permissions

### Step 3: Webhook Configuration (Optional)

Streamlit Cloud automatically deploys when you push to GitHub, but you can verify:

1. Go to https://github.com/harishnuti/aanya-science-exam-prep/settings/hooks
2. Should see a webhook for Streamlit Cloud
3. If not present, Streamlit Cloud will create it when connected

---

## 🌐 STREAMLIT CLOUD CONNECTION

### Step 1: Create Streamlit Cloud Account

1. Visit https://streamlit.io/cloud
2. Click "Sign up"
3. Use GitHub to sign up (easiest)
4. Authorize Streamlit to access your GitHub account

### Step 2: Deploy Your App

1. Go to https://share.streamlit.io/ (Streamlit Cloud dashboard)
2. Click "New app"
3. Fill in deployment details:
   - **Repository**: `harishnuti/aanya-science-exam-prep`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`

### Step 3: Verify Deployment

1. Click "Deploy"
2. Wait for app to build (2-5 minutes)
3. App should be available at: `https://aanya-science-exam-prep.streamlit.app/`
4. Test the app:
   - Login with any username
   - Navigate to all sections
   - Verify database works
   - Check console for errors (Manage app → Logs)

---

## 🔑 MAIN FILE CONFIGURATION

### Option 1: streamlit_app.py (Recommended)

Streamlit Cloud looks for `streamlit_app.py` by default. This should be a copy or import of your main app:

**File**: `streamlit_app.py` (at repository root)

```python
"""
Phase 2 v4.0 Master App - Streamlit Cloud Entry Point

This file serves as the main entry point for Streamlit Cloud deployment.
It imports and runs the Master App from apps/exam_prep_master.py
"""

import sys
import os

# Add src folder to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

# Import and run the main app
from exam_prep_master import main

if __name__ == "__main__":
    main()
```

### Option 2: Custom Main File via streamlit.app (If Needed)

Create a `streamlit.app` config file to specify a different entry point:

**File**: `streamlit.app`

```
apps/exam_prep_master.py
```

**Note**: This is only needed if using non-standard naming. The file should contain just the relative path to your main Python file.

### Option 3: app_exam_prep_pro.py (Backward Compatibility)

If Streamlit Cloud was previously configured to look for `app_exam_prep_pro.py`:

**File**: `app_exam_prep_pro.py` (at repository root)

This should be a complete copy of `apps/exam_prep_master.py` or an import wrapper.

---

## 🔐 SECRETS & ENVIRONMENT VARIABLES

### Step 1: Identify Secrets Needed

Check your app for hardcoded secrets that should be protected:

```bash
# Search for potential secrets in code:
grep -r "admin" apps/exam_prep_master.py | head -20
grep -r "password" apps/exam_prep_master.py | head -20
```

**Current Secrets** (from exam_prep_master.py):
- Admin password: `admin123` (should be protected if changing)

### Step 2: Configure Secrets in Streamlit Cloud

1. Go to Streamlit Cloud dashboard: https://share.streamlit.io/
2. Find your app: `aanya-science-exam-prep`
3. Click the three dots (...) → Settings
4. Click "Secrets" tab
5. Add secrets as TOML format:

```toml
# Secrets format for Streamlit Cloud
admin_password = "admin123"

# If using external database (future):
# database_url = "your_external_db_url"
# api_key = "your_api_key"
```

### Step 3: Access Secrets in Code

```python
import streamlit as st

# Access secrets in your app:
admin_pwd = st.secrets.get("admin_password", "admin123")

# Or with default:
admin_pwd = st.secrets["admin_password"]
```

### Step 4: Local Testing with Secrets

Create `.streamlit/secrets.toml` locally (NEVER commit this):

```bash
# Create directory
mkdir -p .streamlit

# Create secrets.toml
cat > .streamlit/secrets.toml << EOF
admin_password = "admin123"
EOF

# Test locally
streamlit run streamlit_app.py
```

**IMPORTANT**: Add `.streamlit/secrets.toml` to `.gitignore`:
```bash
echo ".streamlit/secrets.toml" >> .gitignore
```

---

## 🔄 AUTO-DEPLOYMENT CONFIGURATION

### How Auto-Deployment Works

1. **You push to GitHub** → `git push origin main`
2. **GitHub webhook triggers** → Notifies Streamlit Cloud
3. **Streamlit Cloud detects change** → Starts rebuild
4. **App redeploys** → New version live at URL
5. **Takes 1-3 minutes** → You can check logs meanwhile

### Step 1: Verify Auto-Deploy is Enabled

1. Go to Streamlit Cloud app dashboard
2. Click your app: `aanya-science-exam-prep`
3. Click the three dots (...) → Settings
4. Under "General":
   - ✅ "Rerun script on update" should be checked
   - ✅ Git branch should be set to `main`

### Step 2: Check Deployment Status

**While deploying**:
1. Click "View logs" during deployment
2. Watch build progress
3. If fails, logs show error (usually import or dependency issue)

**After deployment**:
1. Visit app URL: https://aanya-science-exam-prep.streamlit.app/
2. Do a hard refresh: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
3. Test login and basic functionality

### Step 3: Disable Auto-Deploy (If Needed)

To prevent automatic deploys:
1. Settings → General
2. Uncheck "Rerun script on update"
3. Deploy manually only when ready

---

## 📊 MONITORING & TROUBLESHOOTING

### Check App Status

**Streamlit Cloud Dashboard**:
- URL: https://share.streamlit.io/
- Shows: Last deploy time, status (healthy/error), memory/CPU usage

**App Logs**:
1. Click app in dashboard
2. Click the three dots (...) → View logs
3. Scroll to see:
   - Build logs (dependencies, setup)
   - Runtime logs (errors, prints)
   - Recent timestamps

### Common Errors to Watch For

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError` | Missing import or wrong path | Check sys.path, verify files in apps/ folder |
| `streamlit.errors.StreamlitAPIException` | Streamlit API misuse | Check version compatibility in requirements.txt |
| `sqlite3.DatabaseError` | Database schema issue | Check data/app.db permissions (might be git-ignored) |
| `ImportError: No module named 'src'` | src/ not in Python path | Verify sys.path.insert in main file |

### Real-Time Monitoring

**Check app is running**:
```bash
# From terminal
curl -s https://aanya-science-exam-prep.streamlit.app/ | head -20
# Should return HTML content, not error
```

**Check logs from terminal** (if Streamlit CLI installed):
```bash
streamlit logs
# Shows real-time app logs
```

---

## 🔃 REDEPLOYMENT & UPDATES

### Standard Redeployment Workflow

**1. Make code changes locally**:
```bash
cd /path/to/repo
# Edit your Python files
nano apps/exam_prep_master.py
```

**2. Test locally**:
```bash
streamlit run streamlit_app.py
# Verify changes work
```

**3. Commit to git**:
```bash
git add .
git commit -m "Feature: [description of change]"
```

**4. Push to GitHub**:
```bash
git push origin main
```

**5. Wait for auto-deploy** (1-3 minutes)

**6. Verify in cloud**:
```
Visit: https://aanya-science-exam-prep.streamlit.app/
Hard refresh: Ctrl+Shift+R
Test the changes
```

### Emergency Rollback

If deployment breaks the app:

**Option 1: Revert to Previous Commit**
```bash
# Check recent commits
git log --oneline -5

# Revert to previous working version
git revert HEAD
git push origin main
# Streamlit Cloud auto-redeploys
```

**Option 2: Manual Rollback in Streamlit Cloud** (if available)
1. Dashboard → App → Settings
2. Look for "Revert to previous version" option
3. Select last known good version
4. Click "Revert"

### Database Migration Between Versions

**If you update the database schema** (add tables, columns):

1. **Local migration**:
   ```bash
   # Delete old database to start fresh
   rm data/app.db
   
   # Run app locally to initialize new schema
   streamlit run streamlit_app.py
   ```

2. **Streamlit Cloud migration**:
   ```bash
   # Option 1: Database auto-initializes on first run with new schema
   # (if using init_db() function that creates tables)
   
   # Option 2: If manual migration needed:
   # Connect to app, trigger manual migration command
   # (would need to add migration endpoint in app)
   ```

---

## 🔧 COMMON ISSUES & SOLUTIONS

### Issue 1: "Main module does not exist"

**Error message**:
```
The main module file does not exist: /mount/src/aanya-science-exam-prep/app_exam_prep_pro.py
```

**Causes**:
- Streamlit Cloud looking for wrong file name
- File moved to subfolder without updating config

**Solutions**:
1. Ensure `streamlit_app.py` exists at root level
2. Ensure `app_exam_prep_pro.py` exists at root level (if configured to use it)
3. In Streamlit Cloud Settings → update "Main file path" to point to correct file
4. Commit and push again

**Verification**:
```bash
# Verify files exist at root
ls -la streamlit_app.py
ls -la app_exam_prep_pro.py
```

---

### Issue 2: "ModuleNotFoundError: No module named 'apps'"

**Error message**:
```
ModuleNotFoundError: No module named 'apps'
```

**Cause**: sys.path doesn't include the apps/ folder

**Solution**:
Make sure main file has:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))
```

**Verification**:
```bash
# Check sys.path in main file
grep -n "sys.path" streamlit_app.py
# Should see the insert line
```

---

### Issue 3: "sqlite3.DatabaseError: database disk image is malformed"

**Error message**:
```
sqlite3.DatabaseError: database disk image is malformed
```

**Causes**:
- Database file corrupted (rare)
- Concurrent access issues
- Database not properly closed

**Solutions**:
1. **Delete and reinitialize**:
   ```bash
   # Locally, delete old database
   rm data/app.db
   # Run app to recreate
   streamlit run streamlit_app.py
   # Commit changes
   git add data/.gitkeep  # if you want to keep folder
   git commit -m "Reset database"
   git push origin main
   ```

2. **Check database initialization**:
   - Verify `init_db()` function creates tables properly
   - Check for syntax errors in SQL

---

### Issue 4: "App is loading very slowly"

**Possible causes**:
- Large dataframes being processed
- Inefficient database queries
- Too many animations rendering
- Streamlit caching not working

**Solutions**:
```python
# Add Streamlit caching decorators
@st.cache_data
def load_quiz_questions():
    # Load expensive data once
    return questions

@st.cache_resource
def get_database_connection():
    # Reuse database connection
    return sqlite3.connect('data/app.db')
```

**Check logs**:
1. Click app in Streamlit Cloud
2. View logs → Look for long operation times
3. Profile code locally with timing statements

---

### Issue 5: "Out of memory error"

**Error message**:
```
MemoryError or Process exited with code 137
```

**Causes**:
- Loading huge datasets
- Memory leak in code
- Too many sessions running

**Solutions**:
1. **Use pagination** for large datasets
2. **Clear session state** when not needed
3. **Use st.cache** to avoid recomputation
4. **Upgrade Streamlit Cloud tier** if consistently running out

---

## 📝 DEPLOYMENT CHECKLIST

Before each deployment:

- ✅ Code tested locally: `streamlit run streamlit_app.py`
- ✅ No console errors: Check browser console (F12 → Console tab)
- ✅ All imports working: No red error messages
- ✅ Database initializes: data/app.db created
- ✅ Login works: Can login with any username
- ✅ All pages load: Navigation works across all sections
- ✅ Gamification works: XP, badges, streaks display
- ✅ Multi-user works: Login as different users, verify isolation
- ✅ Changes committed: `git status` shows nothing to commit
- ✅ Changes pushed: `git log` matches GitHub web interface
- ✅ requirements.txt updated: All new dependencies listed

---

## 🚀 QUICK DEPLOY REFERENCE

**5-minute deployment**:
```bash
# 1. Make changes locally and test
nano apps/exam_prep_master.py
streamlit run streamlit_app.py  # Test locally

# 2. Commit and push
git add .
git commit -m "Update: [description]"
git push origin main

# 3. Wait and verify (1-3 minutes)
# Visit: https://aanya-science-exam-prep.streamlit.app/
# Hard refresh: Ctrl+Shift+R
# Test the app
```

**Check status**:
```bash
# See deployment progress
git log --oneline -1  # Show current commit
# Compare commit hash with GitHub web interface to verify it was deployed
```

---

## 📞 SUPPORT & RESOURCES

- **Streamlit Docs**: https://docs.streamlit.io/
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-cloud/
- **GitHub Help**: https://docs.github.com/
- **App URL**: https://aanya-science-exam-prep.streamlit.app/
- **Repository**: https://github.com/harishnuti/aanya-science-exam-prep

---

**Status**: ✅ Ready for Production Deployment  
**Last Updated**: May 16, 2026  
**Version**: 4.0 Master App

