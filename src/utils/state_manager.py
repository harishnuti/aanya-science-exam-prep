import json
import streamlit as st
from datetime import datetime, timedelta

class StateManager:
    """Manages session state and localStorage persistence for Phase 2"""

    @staticmethod
    def init_user_state():
        """Initialize default user state if not exists"""
        if 'user_state' not in st.session_state:
            st.session_state.user_state = {
                'user_id': 'aanya_default',
                'level': 1,
                'xp': 0,
                'xp_for_next_level': 100,
                'total_xp': 0,
                'streak': 0,
                'last_login_date': datetime.now().strftime('%Y-%m-%d'),
                'achievements': {},
                'chapter_progress': {},
                'daily_challenge_completed': False,
                'theme': 'colorful',
                'animation_intensity': 'full',
                'difficulty_mode': 'beginner',
                'high_scores': {},
            }
            StateManager.init_chapters()
        return st.session_state.user_state

    @staticmethod
    def init_chapters():
        """Initialize chapter progress tracking"""
        chapters = [
            'Ch1_Reproduction', 'Ch2_Water', 'Ch3_Plant',
            'Ch4_Human', 'Ch5_Electrical', 'Ch6_Circuits'
        ]
        for ch in chapters:
            st.session_state.user_state['chapter_progress'][ch] = {
                'flashcards_learned': 0,
                'quizzes_completed': 0,
                'quiz_scores': [],
                'brain_drainer_completed': 0,
                'brain_drainer_scores': [],
                'mini_games_played': 0,
                'mini_game_high_score': 0,
                'mastery_percentage': 0,
            }

    @staticmethod
    def add_xp(amount, source='quiz'):
        """Add XP and handle leveling"""
        user = st.session_state.user_state
        user['xp'] += amount
        user['total_xp'] += amount

        # Check for level up
        while user['xp'] >= user['xp_for_next_level']:
            user['xp'] -= user['xp_for_next_level']
            user['level'] += 1
            user['xp_for_next_level'] = int(100 * (1.1 ** (user['level'] - 1)))
            st.success(f"🎉 Level {user['level']} Unlocked!")

    @staticmethod
    def update_streak():
        """Update daily streak"""
        user = st.session_state.user_state
        today = datetime.now().strftime('%Y-%m-%d')
        last_login = user.get('last_login_date', today)

        if last_login == today:
            return  # Already logged in today

        last_login_date = datetime.strptime(last_login, '%Y-%m-%d')
        today_date = datetime.now()
        days_since = (today_date - last_login_date).days

        if days_since == 1:
            user['streak'] += 1
        elif days_since > 1:
            user['streak'] = 1  # Reset streak if more than 1 day

        user['last_login_date'] = today

    @staticmethod
    def update_chapter_progress(chapter, metric, value):
        """Update progress for a specific chapter"""
        user = st.session_state.user_state
        if chapter in user['chapter_progress']:
            if metric == 'quiz_scores':
                user['chapter_progress'][chapter]['quiz_scores'].append(value)
                scores = user['chapter_progress'][chapter]['quiz_scores']
                avg_score = sum(scores) / len(scores) if scores else 0
                user['chapter_progress'][chapter]['mastery_percentage'] = avg_score
            elif metric == 'brain_drainer_scores':
                user['chapter_progress'][chapter]['brain_drainer_scores'].append(value)
            elif metric == 'mini_game_high_score':
                if value > user['chapter_progress'][chapter]['mini_game_high_score']:
                    user['chapter_progress'][chapter]['mini_game_high_score'] = value
            else:
                user['chapter_progress'][chapter][metric] = value

    @staticmethod
    def unlock_achievement(achievement_id, achievement_name):
        """Unlock an achievement"""
        user = st.session_state.user_state
        if achievement_id not in user['achievements']:
            user['achievements'][achievement_id] = {
                'name': achievement_name,
                'unlocked_date': datetime.now().strftime('%Y-%m-%d'),
                'icon': '🏆'
            }
            st.balloons()
            st.success(f"🏆 Achievement Unlocked: {achievement_name}!")

    @staticmethod
    def get_user_stats():
        """Get comprehensive user statistics"""
        user = st.session_state.user_state
        stats = {
            'level': user['level'],
            'xp': user['xp'],
            'xp_for_next_level': user['xp_for_next_level'],
            'total_xp': user['total_xp'],
            'streak': user['streak'],
            'achievements_unlocked': len(user['achievements']),
            'chapters_started': sum(1 for ch in user['chapter_progress'].values() if ch['quizzes_completed'] > 0),
        }
        return stats

    @staticmethod
    def export_progress_json():
        """Export progress as JSON string"""
        return json.dumps(st.session_state.user_state, indent=2)

    @staticmethod
    def import_progress_json(json_str):
        """Import progress from JSON string"""
        try:
            st.session_state.user_state = json.loads(json_str)
            st.success("Progress imported successfully!")
            return True
        except json.JSONDecodeError:
            st.error("Invalid JSON format")
            return False

class AchievementManager:
    """Manages achievement unlocking logic"""

    ACHIEVEMENTS = {
        'first_quiz': {'name': 'First Steps', 'icon': '👶'},
        'chapter_mastery_1': {'name': 'Ch1 Master', 'icon': '🌱'},
        'chapter_mastery_all': {'name': 'All-Rounder', 'icon': '🌟'},
        'brain_drainer_10': {'name': 'Brain Drainer 10', 'icon': '🧠'},
        'brain_drainer_50': {'name': 'Brain Drainer Master', 'icon': '🧠💪'},
        '7day_streak': {'name': 'Week Warrior', 'icon': '🔥'},
        'speedrunner': {'name': 'Speedrunner', 'icon': '⚡'},
        'perfect_quiz': {'name': 'Perfect Score', 'icon': '💯'},
    }

    @staticmethod
    def check_and_unlock(user_state, context):
        """Check conditions and unlock achievements"""
        # First Steps
        if context == 'first_quiz' and 'first_quiz' not in user_state['achievements']:
            StateManager.unlock_achievement('first_quiz', AchievementManager.ACHIEVEMENTS['first_quiz']['name'])

        # Chapter Mastery
        for chapter, progress in user_state['chapter_progress'].items():
            if progress['mastery_percentage'] >= 90:
                achievement_id = f'chapter_mastery_{chapter}'
                if achievement_id not in user_state['achievements']:
                    StateManager.unlock_achievement(achievement_id, f"{chapter} Master!")

        # Streak achievements
        if user_state['streak'] >= 7:
            if '7day_streak' not in user_state['achievements']:
                StateManager.unlock_achievement('7day_streak', AchievementManager.ACHIEVEMENTS['7day_streak']['name'])

        # Perfect score
        if context.get('score') == 100 and 'perfect_quiz' not in user_state['achievements']:
            StateManager.unlock_achievement('perfect_quiz', AchievementManager.ACHIEVEMENTS['perfect_quiz']['name'])
