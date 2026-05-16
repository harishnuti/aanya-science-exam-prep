import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

class XPSystem:
    """Manages XP, leveling, and rewards"""

    LEVEL_BASE_XP = 100
    LEVEL_MULTIPLIER = 1.1

    @staticmethod
    def calculate_xp_for_level(level):
        """Calculate XP needed for a specific level"""
        return int(XPSystem.LEVEL_BASE_XP * (XPSystem.LEVEL_MULTIPLIER ** (level - 1)))

    @staticmethod
    def display_xp_bar():
        """Display current XP progress bar"""
        user = st.session_state.user_state
        progress = user['xp'] / user['xp_for_next_level']

        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(min(progress, 1.0), text=f"XP: {user['xp']}/{user['xp_for_next_level']}")
        with col2:
            st.metric("Level", user['level'])

    @staticmethod
    def display_level_badge():
        """Display interactive level badge"""
        user = st.session_state.user_state
        xp_percentage = (user['total_xp'] % 1000) / 10  # Show progress within current 1000 block

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⚡ Level", user['level'], f"{user['total_xp']} total XP")
        with col2:
            st.metric("🔥 Streak", f"{user['streak']} days")
        with col3:
            st.metric("🏆 Badges", len(user['achievements']))

    @staticmethod
    def award_xp(amount, reason=""):
        """Award XP with reason"""
        from utils.state_manager import StateManager
        StateManager.add_xp(amount, source=reason)
        st.toast(f"⚡ +{amount} XP {reason}")

class AchievementBadge:
    """Manages achievement badges display and unlock"""

    BADGE_EMOJIS = {
        'chapter_mastery': '📚',
        'brain_drainer': '🧠',
        'speedrunner': '⚡',
        'streak': '🔥',
        'perfect': '💯',
        'all_rounder': '🌟',
    }

    @staticmethod
    def display_achievements():
        """Display achievement gallery"""
        user = st.session_state.user_state
        achievements = user['achievements']

        st.subheader("🏆 Achievements")

        if not achievements:
            st.info("Complete challenges to unlock achievements!")
            return

        # Display unlocked achievements
        cols = st.columns(4)
        for idx, (ach_id, ach_data) in enumerate(achievements.items()):
            with cols[idx % 4]:
                st.metric(
                    ach_data.get('icon', '🏆'),
                    ach_data['name'],
                    ach_data.get('unlocked_date', 'Unknown')
                )

    @staticmethod
    def check_achievement_unlock(achievement_type, context=None):
        """Check and unlock achievements based on context"""
        from utils.state_manager import AchievementManager
        user = st.session_state.user_state

        if achievement_type == 'quiz_complete':
            AchievementManager.check_and_unlock(user, 'first_quiz')

        elif achievement_type == 'chapter_mastery':
            if context and context['mastery'] >= 90:
                ach_id = f"chapter_{context['chapter']}"
                if ach_id not in user['achievements']:
                    user['achievements'][ach_id] = {
                        'name': f"{context['chapter']} Master",
                        'unlocked_date': datetime.now().strftime('%Y-%m-%d'),
                        'icon': '📚'
                    }

        elif achievement_type == 'streak':
            if user['streak'] >= 7:
                if '7day_streak' not in user['achievements']:
                    user['achievements']['7day_streak'] = {
                        'name': 'Week Warrior',
                        'unlocked_date': datetime.now().strftime('%Y-%m-%d'),
                        'icon': '🔥'
                    }

        elif achievement_type == 'perfect_score':
            if '100_score' not in user['achievements']:
                user['achievements']['100_score'] = {
                    'name': 'Perfect Score',
                    'unlocked_date': datetime.now().strftime('%Y-%m-%d'),
                    'icon': '💯'
                }

class DailyChallenge:
    """Manages daily challenges and bonuses"""

    @staticmethod
    def display_daily_challenge():
        """Display today's challenge"""
        from utils.state_manager import StateManager
        user = st.session_state.user_state
        today = datetime.now().strftime('%Y-%m-%d')

        st.subheader("🎯 Daily Challenge")

        if user.get('daily_challenge_completed'):
            st.success("✅ Daily Challenge Completed! Come back tomorrow for a new one.")
        else:
            challenge_text = "Answer 3 brain drainer questions correctly to earn 20 XP bonus!"
            st.info(f"📌 {challenge_text}")

            if st.button("Start Daily Challenge", key="daily_challenge_btn"):
                st.session_state.daily_challenge_active = True

    @staticmethod
    def complete_daily_challenge():
        """Mark daily challenge as completed"""
        user = st.session_state.user_state
        user['daily_challenge_completed'] = True
        from utils.state_manager import StateManager
        StateManager.add_xp(20, "daily challenge bonus")

class RewardSystem:
    """Manages unlockable rewards and cosmetics"""

    UNLOCKABLE_REWARDS = {
        'skin_hamster': {'name': 'Sparky the Hamster', 'unlock_xp': 500, 'emoji': '🐹'},
        'skin_cat': {'name': 'Luna the Cat', 'unlock_xp': 1000, 'emoji': '🐱'},
        'skin_robot': {'name': 'AAIA Bot', 'unlock_xp': 1500, 'emoji': '🤖'},
        'theme_ocean': {'name': 'Ocean Theme', 'unlock_xp': 750, 'emoji': '🌊'},
        'theme_space': {'name': 'Space Theme', 'unlock_xp': 1000, 'emoji': '🌌'},
        'theme_forest': {'name': 'Forest Theme', 'unlock_xp': 750, 'emoji': '🌲'},
    }

    @staticmethod
    def display_reward_shop():
        """Display unlockable rewards"""
        user = st.session_state.user_state

        st.subheader("🎁 Reward Shop")
        st.write(f"You have **{user['total_xp']}** total XP")

        cols = st.columns(3)
        for idx, (reward_id, reward_info) in enumerate(RewardSystem.UNLOCKABLE_REWARDS.items()):
            with cols[idx % 3]:
                is_unlocked = user['total_xp'] >= reward_info['unlock_xp']
                status = "🔓 Unlocked" if is_unlocked else f"🔒 {reward_info['unlock_xp']} XP"

                st.metric(
                    reward_info['emoji'],
                    reward_info['name'],
                    status
                )

class ProgressRadar:
    """Displays mastery across all chapters"""

    @staticmethod
    def display_mastery_radar():
        """Render radar chart for chapter mastery"""
        user = st.session_state.user_state
        chapters = list(user['chapter_progress'].keys())
        mastery_scores = [user['chapter_progress'][ch]['mastery_percentage'] for ch in chapters]

        fig = go.Figure(data=go.Scatterpolar(
            r=mastery_scores,
            theta=chapters,
            fill='toself',
            name='Mastery',
            line_color='#FF6B6B'
        ))

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            height=400,
            title="📊 Chapter Mastery Levels"
        )

        st.plotly_chart(fig, use_container_width=True)

class LeaderboardSystem:
    """Manages personal leaderboard and stats"""

    @staticmethod
    def display_stats():
        """Display personal statistics"""
        from utils.state_manager import StateManager
        stats = StateManager.get_user_stats()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📈 Level", stats['level'])
        with col2:
            st.metric("🔥 Streak", f"{stats['streak']} days")
        with col3:
            st.metric("🏆 Achievements", stats['achievements_unlocked'])
        with col4:
            st.metric("📚 Chapters", stats['chapters_started'])
