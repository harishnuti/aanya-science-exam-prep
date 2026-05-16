"""
Phase 2 Science App - Enhanced Edition for Aanya
Primary 5 Science Curriculum with Gamification, Animations, and PSLE Brain Drainers
"""

import streamlit as st
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from utils.state_manager import StateManager, AchievementManager
from components.gamification import XPSystem, AchievementBadge, DailyChallenge, RewardSystem, ProgressRadar, LeaderboardSystem
from components.animations import AnimationStyles, MalteseDogFeedback, TransitionAnimations, ParticleEffects
from components.brain_drainers import get_brain_drainer_questions, display_brain_drainer_question
from components.minigames import display_minigame_menu
import config

# Page configuration
st.set_page_config(
    page_title="🌟 Aanya's Science Quest - Phase 2",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS animations
AnimationStyles.inject_styles()

# Initialize state
user_state = StateManager.init_user_state()
StateManager.update_streak()

# Check if a chapter is selected
if 'selected_chapter' in st.session_state and st.session_state.selected_chapter:
    chapter_key = st.session_state.selected_chapter

    if st.button("← Back to Chapters"):
        st.session_state.selected_chapter = None
        st.rerun()

    st.markdown("---")

    try:
        if chapter_key == 'Ch1_Reproduction':
            from modules import ch1_reproduction_new as chapter_module
        elif chapter_key == 'Ch2_Water':
            from modules import ch2_water_new as chapter_module
        elif chapter_key == 'Ch3_Plant':
            from modules import ch3_plant_new as chapter_module
        elif chapter_key == 'Ch4_Human':
            from modules import ch4_human_new as chapter_module
        elif chapter_key == 'Ch5_Electrical':
            from modules import ch5_electrical_new as chapter_module
        elif chapter_key == 'Ch6_Circuits':
            from modules import ch6_circuits_new as chapter_module

        # Display the chapter content
        if hasattr(chapter_module, 'show_chapter'):
            chapter_module.show_chapter()
        else:
            st.error(f"Chapter module does not have show_chapter() function")
    except ImportError as e:
        st.error(f"Chapter module not found: {e}")

    st.stop()

# ==================== SIDEBAR NAVIGATION ====================
with st.sidebar:
    try:
        st.image("https://via.placeholder.com/200?text=🌟+Science+Quest", use_container_width=True)
    except TypeError:
        st.image("https://via.placeholder.com/200?text=🌟+Science+Quest", use_column_width=True)

    st.markdown(f"# 🌟 {config.STUDENT_NAME}'s Science Quest")
    st.markdown("---")

    # User Profile
    st.markdown("### 👤 Profile")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Level", user_state['level'], f"⚡ {user_state['xp']} XP")
    with col2:
        st.metric("Streak", f"🔥 {user_state['streak']}", "days")

    st.progress(user_state['xp'] / user_state['xp_for_next_level'], text=f"{user_state['xp']}/{user_state['xp_for_next_level']} XP")

    st.markdown("---")

    # Navigation menu
    page = st.radio(
        "📚 Choose Your Journey:",
        ["🏠 Home", "📖 Chapters", "🧠 Brain Drainers", "🎮 Mini-Games", "🏆 Achievements", "📊 Progress", "⚙️ Settings"],
        index=0
    )

    st.markdown("---")

    # Pet evolution display
    st.markdown("### 🐕 Your Pet: Sparky")
    MalteseDogFeedback.show_pet_evolution(user_state['level'])

    st.markdown("---")

    # Daily challenge in sidebar
    st.markdown("### 🎯 Daily Challenge")
    if user_state.get('daily_challenge_completed'):
        st.success("✅ Completed!")
    else:
        st.info("📌 Answer 3 brain drainer questions correctly")

# ==================== MAIN CONTENT ====================

if page == "🏠 Home":
    welcome_msg = config.get_student_message('welcome')
    st.markdown(f"""
    <div class="fade-in">
        <h1 style="text-align: center; color: #2c3e50;">{welcome_msg}</h1>
        <p style="text-align: center; font-size: 18px; color: #7f8c8d;">
            📍 {config.get_student_message('dashboard_location')}
        </p>
        <p style="text-align: center; font-size: 14px; color: #7f8c8d;">
            Master Primary 5 Science through animations, mini-games, and PSLE brain drainers!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Dashboard widgets
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📚 Chapters", "6 Available", "P5 Curriculum")
    with col2:
        st.metric("🏆 Badges", len(user_state['achievements']), "Unlocked")
    with col3:
        st.metric("💯 Quizzes", sum(ch['quizzes_completed'] for ch in user_state['chapter_progress'].values()), "Completed")
    with col4:
        st.metric("🔥 Streak", user_state['streak'], "Days")

    st.markdown("---")

    # Quick start section
    st.subheader("🚀 Quick Start")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("### 📖 Learn")
        st.write("Master concepts with interactive flashcards and animated diagrams")
        if st.button("Start Learning →", key="quick_learn"):
            st.session_state.current_page = "📖 Chapters"
            st.rerun()

    with col2:
        st.write("### 🧠 Challenge")
        st.write("Test your knowledge with PSLE-style brain drainer questions")
        if st.button("Take Challenge →", key="quick_challenge"):
            st.session_state.current_page = "🧠 Brain Drainers"
            st.rerun()

    with col3:
        st.write("### 🎮 Play")
        st.write("Master concepts through engaging mini-games and timed challenges")
        if st.button("Play Games →", key="quick_games"):
            st.session_state.current_page = "🎮 Mini-Games"
            st.rerun()

    st.markdown("---")

    # Mastery radar
    st.subheader("📊 Your Mastery Levels")
    ProgressRadar.display_mastery_radar()

    st.markdown("---")

    # Tips and tricks
    st.subheader("💡 Did You Know?")
    tips = [
        "🔥 **Streaks:** Maintain daily streaks to unlock achievements and bonuses!",
        "⚡ **XP Multiplier:** Higher difficulty modes give 2x XP!",
        "🧠 **Brain Drainers:** These questions have traps - learn from explanations!",
        "🎮 **Mini-Games:** Speed bonuses give extra XP if you finish 30% faster!",
        "🏆 **Achievements:** Unlock cosmetic rewards at higher levels!",
    ]
    st.info(tips[hash(user_state['user_id']) % len(tips)])

elif page == "📖 Chapters":
    st.header("📚 Chapter Selection")

    chapters = {}
    for chapter_key, chapter_config in config.CHAPTERS.items():
        chapters[chapter_key] = {
            'title': chapter_config['title'],
            'description': chapter_config['description'],
            'emoji': chapter_config['emoji'],
            'progress': user_state['chapter_progress'].get(chapter_key, {'mastery_percentage': 0, 'quizzes_completed': 0, 'brain_drainer_completed': 0})
        }

    for chapter_key, chapter_info in chapters.items():
        with st.container(border=True):
            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                st.markdown(f"### {chapter_info['title']}")
                st.write(chapter_info['description'])

            with col2:
                progress = chapter_info['progress']
                st.metric("Mastery", f"{int(progress['mastery_percentage'])}%")
                st.metric("Quizzes", progress['quizzes_completed'])

            with col3:
                st.metric("Brain Drainers", progress['brain_drainer_completed'])
                if st.button(f"Open {chapter_key}", key=f"open_{chapter_key}"):
                    st.session_state.selected_chapter = chapter_key
                    st.rerun()

    st.markdown("---")
    st.info("💡 Tip: Select a chapter to access flashcards, matching games, quizzes, mini-games, and brain drainers!")

elif page == "🧠 Brain Drainers":
    st.header("🧠 PSLE Brain Drainers")
    st.write("Test your knowledge with exam-style tricky questions designed to catch common misconceptions!")

    # Chapter selection
    chapter_keys = list(config.CHAPTERS.keys())
    chapter = st.selectbox(
        "Select a chapter:",
        chapter_keys,
        format_func=lambda x: config.CHAPTERS[x]['title']
    )

    # Difficulty filter
    col1, col2 = st.columns([2, 1])
    with col1:
        difficulty = st.multiselect("Filter by difficulty:", ['easy', 'medium', 'hard'], default=['medium', 'hard'])
    with col2:
        num_questions = st.slider("Number of questions:", 1, 10, 3)

    st.markdown("---")

    # Get brain drainer questions
    questions = get_brain_drainer_questions(chapter)
    filtered_questions = [q for q in questions if q.get('difficulty') in difficulty]
    selected_questions = filtered_questions[:num_questions]

    if selected_questions:
        st.subheader(f"📝 {chapter.replace('_', ' ')} - {len(selected_questions)} Questions")

        # Quiz interface
        quiz_correct = 0
        quiz_total = 0

        for idx, question in enumerate(selected_questions, 1):
            with st.container(border=True):
                st.markdown(f"### Question {idx}/{len(selected_questions)}")
                result = display_brain_drainer_question(question)
                if result is not None:
                    quiz_correct += 1 if result else 0
                    quiz_total += 1

        # Summary
        if quiz_total > 0:
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Score", f"{quiz_correct}/{quiz_total}")
            with col2:
                percentage = (quiz_correct / quiz_total) * 100
                st.metric("Percentage", f"{percentage:.0f}%")
            with col3:
                xp_earned = int(quiz_correct * 5 * len(selected_questions) / 5)
                st.metric("XP Earned", xp_earned)

                if st.button("Claim XP Reward", key="claim_xp"):
                    XPSystem.award_xp(xp_earned, "brain drainer completion")
                    st.success("XP claimed!")
    else:
        st.warning("No questions found for the selected filters. Try different difficulty levels!")

elif page == "🎮 Mini-Games":
    st.header("🎮 Mini-Games")
    st.write("Master concepts through interactive games and timed challenges!")

    chapter_keys = list(config.CHAPTERS.keys())
    chapter = st.selectbox(
        "Select a chapter to play:",
        chapter_keys,
        format_func=lambda x: config.CHAPTERS[x]['title']
    )

    game_info = display_minigame_menu(chapter)

    if game_info:
        st.markdown(f"""
        <div class="slide-in-left" style="padding: 20px; border-left: 4px solid #3498db; background-color: #ecf0f1; margin: 20px 0; border-radius: 5px;">
            <h3>{game_info['name']}</h3>
            <p>{game_info['description']}</p>
            <p><strong>⚡ XP Reward: {game_info['xp_reward']} XP</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.info("🎮 Mini-games are coming soon! This feature will include drag-and-drop sorting, sequencing challenges, and timed quizzes.")

elif page == "🏆 Achievements":
    st.header("🏆 Achievements")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Unlocked", len(user_state['achievements']))
    with col2:
        st.metric("⭐ Total Available", "20+")
    with col3:
        unlock_percentage = (len(user_state['achievements']) / 20) * 100
        st.metric("Progress", f"{int(unlock_percentage)}%")

    st.progress(len(user_state['achievements']) / 20)

    st.markdown("---")
    AchievementBadge.display_achievements()

    st.markdown("---")
    st.subheader("🔓 Unlock More Achievements")
    st.write("""
    - 📚 **Chapter Master**: Complete all quizzes in a chapter at 90%+
    - 🧠 **Brain Drainer Expert**: Answer 50 brain drainer questions correctly
    - 🔥 **Week Warrior**: Maintain a 7-day learning streak
    - ⚡ **Speedrunner**: Complete a quiz in under 2 minutes
    - 💯 **Perfect Score**: Achieve 100% on any quiz
    - 🌟 **All-Rounder**: Complete all 6 chapters to 80%+
    """)

elif page == "📊 Progress":
    st.header("📊 Your Progress")

    tab1, tab2, tab3 = st.tabs(["📈 Overview", "📚 Chapter Details", "🔄 Export/Import"])

    with tab1:
        st.subheader("Overall Statistics")
        LeaderboardSystem.display_stats()

        st.markdown("---")
        st.subheader("Mastery by Chapter")
        ProgressRadar.display_mastery_radar()

    with tab2:
        st.subheader("Detailed Chapter Progress")
        chapter = st.selectbox("Select a chapter:", list(user_state['chapter_progress'].keys()))
        progress = user_state['chapter_progress'][chapter]

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mastery", f"{int(progress['mastery_percentage'])}%")
        with col2:
            st.metric("Quizzes", progress['quizzes_completed'])
        with col3:
            st.metric("Brain Drainers", progress['brain_drainer_completed'])
        with col4:
            st.metric("Mini-Games", progress['mini_games_played'])

        if progress['quiz_scores']:
            st.line_chart(progress['quiz_scores'], height=200)

    with tab3:
        st.subheader("Data Management")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("📥 Export Progress"):
                progress_json = StateManager.export_progress_json()
                st.download_button(
                    label="Download as JSON",
                    data=progress_json,
                    file_name="aanya_progress.json",
                    mime="application/json"
                )

        with col2:
            uploaded_file = st.file_uploader("📤 Import Progress", type=["json"])
            if uploaded_file:
                json_str = uploaded_file.read().decode('utf-8')
                if StateManager.import_progress_json(json_str):
                    st.rerun()

elif page == "⚙️ Settings":
    st.header("⚙️ Settings")

    # Theme settings
    st.subheader("🎨 Visual Settings")
    theme = st.selectbox(
        "Theme:",
        ['colorful', 'dark', 'light'],
        index=['colorful', 'dark', 'light'].index(user_state.get('theme', 'colorful'))
    )
    user_state['theme'] = theme

    animation_intensity = st.selectbox(
        "Animation Intensity:",
        ['minimal', 'moderate', 'full'],
        index=['minimal', 'moderate', 'full'].index(user_state.get('animation_intensity', 'full'))
    )
    user_state['animation_intensity'] = animation_intensity

    st.markdown("---")

    # Learning preferences
    st.subheader("📚 Learning Preferences")
    sound_effects = st.checkbox("Enable sound effects (coming soon)", value=True)
    notifications = st.checkbox("Enable notifications", value=True)

    st.markdown("---")

    # Account settings
    st.subheader("👤 Account")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📊 View All Stats"):
            st.json(user_state)

    with col2:
        if st.button("🗑️ Clear Progress"):
            if st.checkbox("I'm sure I want to reset my progress"):
                StateManager.init_user_state()
                st.success("Progress reset!")
                st.rerun()

    st.markdown("---")
    st.success("✅ Settings saved automatically!")

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #7f8c8d; font-size: 12px; padding: 20px;">
    <p>🌟 <strong>{config.STUDENT_NAME}'s Science Quest - Phase 2</strong> 🌟</p>
    <p>Designed for {config.STUDENT_NAME} | {config.CURRICULUM} | {config.SCHOOL_NAME}, {config.SCHOOL_LOCATION}</p>
    <p>✨ Keep learning, keep growing! ✨</p>
</div>
""", unsafe_allow_html=True)
