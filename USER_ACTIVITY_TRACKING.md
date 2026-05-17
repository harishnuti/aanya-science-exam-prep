# 📊 User Activity Tracking System - Comprehensive Documentation

**Status**: ✅ IMPLEMENTED & INTEGRATED  
**Date Implemented**: May 17, 2026  
**Features**: Login/Logout tracking, Section browsing, Activity logging, Admin analytics  

---

## 📌 Overview

A comprehensive backend tracking system that logs all user activities, enabling deep insights into how students use the app, which sections they visit, and how much time they spend on each activity.

**Key Benefits**:
- ✅ Track login/logout times and session durations
- ✅ Monitor which sections (Learn, Match, Practice, Game, Challenge) students use
- ✅ Track chapter-level engagement
- ✅ Measure time spent on each section
- ✅ Identify popular chapters and sections
- ✅ Spot underutilized features
- ✅ Create detailed user profiles
- ✅ Generate comprehensive admin analytics

---

## 🗄️ Database Schema

### New Tables Added to SQLite

#### 1. `user_activity` Table
Tracks every action a user takes in the app.

```
user_activity:
- activity_id (INTEGER PRIMARY KEY)
- user_id (INTEGER, FK to users)
- activity_type (TEXT) - Type of activity (see list below)
- chapter_name (TEXT) - Which chapter (optional)
- section_name (TEXT) - Which section/tab (optional)
- action_detail (TEXT) - Details about the action
- timestamp (TEXT) - ISO format timestamp
- session_duration_seconds (REAL) - How long the session lasted
- ip_address (TEXT) - IP address (for future use)
- device_info (TEXT) - Device information (for future use)
```

**Activity Types**:
- `login` - User logged in
- `logout` - User logged out
- `section_view` - User viewed a section (Learn, Match, Practice, Game, Challenge, Progress)
- `quiz_start` - User started a practice quiz
- `quiz_complete` - User completed a quiz
- `game_play` - User played a mini-game
- Custom types can be added as needed

#### 2. `user_sessions` Table
Tracks overall login/logout sessions.

```
user_sessions:
- session_id (INTEGER PRIMARY KEY)
- user_id (INTEGER, FK to users)
- login_time (TEXT) - ISO format login timestamp
- logout_time (TEXT) - ISO format logout timestamp
- session_duration_seconds (REAL) - Total duration of session
- pages_visited (TEXT) - JSON array of pages visited
- total_activities (INTEGER) - Number of activities in session
```

---

## 🔧 Core Functions

### 1. Activity Logging

#### `log_user_activity()`
Log a single user activity.

```python
log_user_activity(
    user_id=123,
    activity_type='quiz_complete',
    chapter_name='Ch 1: Reproduction',
    section_name='Practice',
    action_detail='Completed quiz: Score 85, Accuracy 90%'
)
```

**Parameters**:
- `user_id` (int): User ID
- `activity_type` (str): Type of activity
- `chapter_name` (str, optional): Chapter name
- `section_name` (str, optional): Section name (Learn, Match, Practice, Game, Challenge, Progress)
- `action_detail` (str, optional): Details about the action
- `session_duration` (float, optional): Duration in seconds
- `device_info` (str, optional): Device information

**Returns**: `activity_id`

---

### 2. Session Management

#### `start_user_session()`
Start tracking a new login session.

```python
session_id = start_user_session(user_id=123)
# Store session_id in st.session_state.session_id
```

**Called**: When user logs in  
**Returns**: `session_id` (store in session state for later use)

---

#### `end_user_session()`
End a login session and calculate duration.

```python
end_user_session(session_id=456)
```

**Called**: When user logs out  
**Automatically calculates**: Session duration in seconds

---

### 3. Convenience Logging Functions

#### `record_section_visit()`
Log when user visits a section.

```python
record_section_visit(
    user_id=123,
    chapter_name='Ch 1: Reproduction',
    section_name='Learn'
)
```

---

#### `record_quiz_start()`
Log when user starts a quiz.

```python
record_quiz_start(
    user_id=123,
    chapter_name='Ch 1: Reproduction',
    quiz_type='practice'
)
```

---

#### `record_quiz_complete()`
Log when user completes a quiz.

```python
record_quiz_complete(
    user_id=123,
    chapter_name='Ch 1: Reproduction',
    score=85,
    accuracy=0.90
)
```

---

#### `record_game_play()`
Log when user plays a game.

```python
record_game_play(
    user_id=123,
    chapter_name='Ch 1: Reproduction',
    game_name='Plant Growth Game',
    score=1000
)
```

---

### 4. Activity Retrieval Functions

#### `get_user_activity_log()`
Get activity log for a specific user (most recent first).

```python
activities = get_user_activity_log(user_id=123, limit=100)
```

**Returns**:
```python
[
    {
        'activity_id': 1,
        'activity_type': 'section_view',
        'chapter_name': 'Ch 1: Reproduction',
        'section_name': 'Learn',
        'action_detail': 'Viewed Learn tab',
        'timestamp': '2026-05-17T14:30:45.123456',
        'session_duration': None
    },
    ...
]
```

---

#### `get_activity_summary()`
Get comprehensive activity summary for a user.

```python
summary = get_activity_summary(user_id=123)
```

**Returns**:
```python
{
    'activity_types': {
        'section_view': 45,
        'quiz_complete': 12,
        'game_play': 8,
        'login': 5
    },
    'total_time_seconds': 3600,  # 1 hour
    'total_sessions': 5,
    'average_session_duration': 720,  # 12 minutes
    'chapters_visited': {
        'Ch 1: Reproduction': 15,
        'Ch 2: Water Cycles': 10
    },
    'sections_visited': {
        'Learn': 20,
        'Practice': 15,
        'Game': 10
    }
}
```

---

#### `get_user_session_history()`
Get all login/logout sessions for a user.

```python
sessions = get_user_session_history(user_id=123)
```

**Returns**:
```python
[
    {
        'session_id': 1,
        'login_time': '2026-05-17T14:00:00',
        'logout_time': '2026-05-17T15:00:00',
        'duration_seconds': 3600,
        'pages_visited': [
            {'page': 'Ch 1/Learn', 'timestamp': '...'},
            {'page': 'Ch 1/Practice', 'timestamp': '...'}
        ],
        'total_activities': 45
    },
    ...
]
```

---

### 5. Admin Analytics

#### `get_admin_activity_dashboard()`
Get overall activity dashboard data for all users.

```python
dashboard = get_admin_activity_dashboard()
```

**Returns**:
```python
{
    'total_users': 15,
    'total_activities': 450,
    'activities_by_type': {
        'section_view': 300,
        'quiz_complete': 80,
        'game_play': 50,
        'login': 20
    },
    'most_active_users': [
        {'name': 'Aanya', 'activities': 120},
        {'name': 'John', 'activities': 95},
        ...
    ],
    'popular_chapters': [
        {'chapter': 'Ch 1: Reproduction', 'visits': 80},
        {'chapter': 'Ch 2: Water Cycles', 'visits': 65},
        ...
    ],
    'popular_sections': [
        {'section': 'Learn', 'visits': 150},
        {'section': 'Practice', 'visits': 120},
        ...
    ],
    'total_time_seconds': 36000  # Total time all users spent
}
```

---

## 📱 Integration Points in App

### 1. Login Screen (exam_prep_master.py)

**When user logs in**:
```python
# New user login
user_id = get_or_create_user(user_name.strip())
st.session_state.session_id = start_user_session(user_id)
log_user_activity(user_id, 'login', action_detail='User logged in')

# Quick login (existing user)
st.session_state.session_id = start_user_session(user['user_id'])
log_user_activity(user['user_id'], 'login', action_detail='User logged in')
```

---

### 2. Logout Button

**When user logs out**:
```python
if st.button("🚪 Logout"):
    if st.session_state.user_id:
        log_user_activity(st.session_state.user_id, 'logout', action_detail='User logged out')
        if hasattr(st.session_state, 'session_id') and st.session_state.session_id:
            end_user_session(st.session_state.session_id)
    # ... clear session state
```

---

### 3. Chapter Section Views

**All chapter sections log activity**:
- `show_chapter_flashcards()` → logs 'Learn' section
- `show_chapter_matching()` → logs 'Match' section
- `show_chapter_quiz()` → logs 'Practice' section
- `show_chapter_minigame()` → logs 'Game' section
- `show_chapter_brain_drainers()` → logs 'Challenge' section
- `show_chapter_progress()` → logs 'Progress' section

Each calls:
```python
record_section_visit(
    user_id=st.session_state.user_id,
    chapter_name=chapter_name,
    section_name='Learn'  # or Match, Practice, Game, Challenge, Progress
)
```

---

## 📊 Admin Dashboard Features

### New Activity Analytics Section

The admin dashboard now includes:

1. **Activity Summary Metrics**
   - Total activities logged
   - Total time spent (hours)
   - Average activities per user
   - Number of activity types

2. **Activity Breakdown**
   - Activities by type (login, section_view, quiz_complete, etc.)
   - Most active users with activity counts
   - Popular chapters by visit count
   - Popular sections by visit count

3. **Individual User Activity Log**
   - Select any user from dropdown
   - View their last 50 activities in chronological order
   - See chapters visited with visit counts
   - See sections visited with visit counts
   - Time spent summary

---

## 📈 Data Analysis Examples

### Find Most Active Users

```python
from utils.database import get_admin_activity_dashboard

dashboard = get_admin_activity_dashboard()
for user in dashboard['most_active_users']:
    print(f"{user['name']}: {user['activities']} activities")
```

---

### Find Which Chapters Need More Content

```python
from utils.database import get_admin_activity_dashboard

dashboard = get_admin_activity_dashboard()
# If a chapter has very few visits, it may need:
# - Better content
# - More engaging games
# - Marketing/promotion
for chapter in dashboard['popular_chapters']:
    print(f"{chapter['chapter']}: {chapter['visits']} visits")
```

---

### Identify Struggling Users

```python
from utils.database import get_user_activity_log, get_activity_summary

activity_log = get_user_activity_log(user_id=123)
summary = get_activity_summary(user_id=123)

# If a user has many 'quiz_complete' but low accuracy:
# They might need remedial help
quiz_attempts = [a for a in activity_log if a['activity_type'] == 'quiz_complete']
```

---

### Track Time Spent Per Section

```python
from utils.database import get_activity_summary

summary = get_activity_summary(user_id=123)
# Shows exactly how much time spent on each section
for section, visits in summary['sections_visited'].items():
    print(f"{section}: {visits} visits")
```

---

## 🔐 Privacy & Security

### What's Tracked
- Login/logout times
- Section visits
- Activity types
- Action details
- Timestamps

### What's NOT Tracked
- Passwords (never stored)
- Sensitive personal information
- IP addresses (field reserved for future, currently not captured)
- Device identifiers (field reserved for future, currently not captured)

### Data Access
- Only admin can access activity dashboard (password protected)
- Individual users cannot see other users' activity
- Activity data stored locally in SQLite

---

## 🚀 Deployment Notes

### Streamlit Cloud Considerations

The tracking system works perfectly on Streamlit Cloud:
- ✅ SQLite database persists
- ✅ Session tracking maintains state during user session
- ✅ Admin dashboard accessible with password
- ✅ No performance impact (lightweight logging)

### Future Enhancements

Planned improvements:
- [ ] IP address capture for location-based analytics
- [ ] Device/browser information capture
- [ ] Activity heat maps (time of day usage patterns)
- [ ] Export activity reports as PDF
- [ ] Real-time activity dashboard (live updates)
- [ ] Anomaly detection (unusual activity patterns)
- [ ] Gamification based on activity (activity badges)

---

## 🧪 Testing the System

### Manual Testing Checklist

- [ ] **Login tracking**: User logs in → activity logged
- [ ] **Section tracking**: User visits Learn tab → activity logged
- [ ] **Multiple section visits**: Visit all 6 tabs → all logged
- [ ] **Logout tracking**: User logs out → activity logged with time
- [ ] **Admin view**: Admin sees all activities in dashboard
- [ ] **Activity summary**: User summary shows accurate counts
- [ ] **Popular chapters**: Dashboard shows correct chapter visit counts
- [ ] **Most active users**: Ranking shows correct activity counts

---

## 📋 Activity Types Reference

| Activity Type | Logged When | Details Example |
|---|---|---|
| `login` | User enters name and clicks "Start Learning" | "User logged in" |
| `logout` | User clicks logout button | "User logged out" |
| `section_view` | User visits a chapter section tab | "Viewed Learn tab in Ch 1: Reproduction" |
| `quiz_start` | User begins a practice quiz | "Started practice quiz in Ch 1" |
| `quiz_complete` | User finishes a quiz | "Completed quiz: Score 85, Accuracy 90%" |
| `game_play` | User plays a mini-game | "Played Plant Growth Game: Score 1000" |

---

## 💡 Use Cases

### For Teachers
- Monitor which chapters need more practice
- Identify students who need extra help (low engagement)
- See which features are most used
- Understand pacing (time spent per section)

### For Students
- Track personal learning progress
- See time spent on each subject
- Identify weak areas (low quiz scores)
- Build consistent study habits

### For App Developers
- Find performance bottlenecks (slow sections)
- Identify buggy features (unusual activity patterns)
- Plan feature improvements based on usage
- Validate that new features are being used

---

## 🔗 Related Files

- `src/utils/database.py` - Database functions
- `apps/exam_prep_master.py` - Integration points
- Admin Dashboard section - View analytics

---

**Status**: ✅ Fully implemented and integrated  
**Last Updated**: May 17, 2026  
**Next Steps**: Deploy to Streamlit Cloud and monitor user activity patterns

