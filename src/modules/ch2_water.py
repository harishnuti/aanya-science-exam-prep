"""Chapter 2: Cycles in Water - Phase 2C Textbook-Aligned Version
Inspiring Science P5 Textbook, Pages 26-49
Theme: Cycles
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback
from components.gamification import XPSystem
from utils.state_manager import StateManager

# ==================== CHAPTER 2: TEXTBOOK CONTENT ====================
# Learning Objectives:
# - What are the states of matter that water can exist in?
# - How does water change from one state to another?
# - What is the water cycle and its importance?

FLASHCARDS = [
    {'concept': 'Matter', 'definition': 'Anything that has mass and takes up space; can exist in solid, liquid, and gas states', 'textbook_ref': 'Page 21'},
    {'concept': 'Ice', 'definition': 'Water in the solid state; found in freezers, Antarctica, and when snow falls in winter', 'textbook_ref': 'Page 27'},
    {'concept': 'Water (Liquid)', 'definition': 'Water in its liquid state; flows from taps, falls as rain, found in seas, lakes, and rivers', 'textbook_ref': 'Page 28'},
    {'concept': 'Water Vapour', 'definition': 'Water in the gaseous state; invisible, colorless gas found everywhere in the air', 'textbook_ref': 'Page 28'},
    {'concept': 'Steam', 'definition': 'Water vapour formed when water boils; visible mist from boiling water', 'textbook_ref': 'Page 29'},
    {'concept': 'Melting', 'definition': 'Process when ice (solid) changes to water (liquid) by gaining heat at 0°C', 'textbook_ref': 'Pages 33-34'},
    {'concept': 'Freezing', 'definition': 'Process where liquid water turns into solid ice'},
    {'concept': 'Boiling', 'definition': 'Rapid evaporation that occurs at a specific temperature'},
    {'concept': 'Water Cycle', 'definition': 'Continuous cycle of water evaporating, condensing, and precipitating'},
    {'concept': 'Latent Heat', 'definition': 'Energy absorbed or released during phase changes'},
]

MCQ_QUESTIONS = [
    {
        'q': 'What is the primary source of water that evaporates in the water cycle?',
        'options': ['Lakes', 'Oceans', 'Rivers', 'All of the above'],
        'answer': 'All of the above',
        'explanation': 'Water evaporates from all bodies of water, though oceans are the largest source.'
    },
    {
        'q': 'At what temperature does water boil?',
        'options': ['50°C', '100°C', '0°C', '150°C'],
        'answer': '100°C',
        'explanation': 'Water boils at 100°C at sea level. This is when the vapor pressure equals atmospheric pressure.'
    },
    {
        'q': 'What happens when water vapor cools?',
        'options': ['Evaporation', 'Condensation', 'Sublimation', 'Freezing'],
        'answer': 'Condensation',
        'explanation': 'Condensation is when water vapor cools and turns back into liquid water.'
    },
    {
        'q': 'Why do puddles disappear on sunny days?',
        'options': ['They sink into the ground', 'They evaporate into water vapor', 'They freeze', 'They become plants'],
        'answer': 'They evaporate into water vapor',
        'explanation': 'The sun\'s heat provides energy for water to evaporate from puddles.'
    },
    {
        'q': 'Which process releases water into the atmosphere from plants?',
        'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Absorption'],
        'answer': 'Transpiration',
        'explanation': 'Transpiration is the release of water vapor through stomata in plant leaves.'
    },
]

def show_chapter():
    """Main chapter display function"""
    st.header("💧 Chapter 2: Cycles in Water")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Explore the continuous journey of water through Earth's atmosphere, land, and oceans!")
    with col2:
        difficulty = st.selectbox("Difficulty:", ['beginner', 'intermediate', 'advanced'], key='ch2_difficulty')

    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Flashcards", "🎯 Matching", "❓ Quiz", "🎮 Mini-Game", "🧠 Brain Drainer"])

    with tab1:
        show_flashcards(difficulty)
    with tab2:
        st.info("💧 Water state matching game coming soon!")
    with tab3:
        show_quiz(difficulty)
    with tab4:
        st.info("🎮 Water cycle state sorter game coming soon!")
    with tab5:
        show_brain_drainer()

def show_flashcards(difficulty):
    """Display flashcard learning interface"""
    st.subheader("📚 Flashcards: Water Cycle Concepts")

    if 'flashcard_index' not in st.session_state:
        st.session_state.flashcard_index = 0

    cards_to_show = FLASHCARDS[:5] if difficulty == 'beginner' else FLASHCARDS[:8] if difficulty == 'intermediate' else FLASHCARDS

    current_card = cards_to_show[st.session_state.flashcard_index]

    st.markdown(f"""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h2 style="color: white;">{current_card['concept']}</h2>
            </div>
            <div class="flip-card-back">
                <p style="color: white; font-size: 18px;">{current_card['definition']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("⏮️ First", key="first_card_ch2"):
            st.session_state.flashcard_index = 0
            st.rerun()
    with col2:
        if st.button("⬅️ Previous", key="prev_card_ch2"):
            st.session_state.flashcard_index = max(0, st.session_state.flashcard_index - 1)
            st.rerun()
    with col3:
        st.metric("Card", f"{st.session_state.flashcard_index + 1}/{len(cards_to_show)}")
    with col4:
        if st.button("Next ➡️", key="next_card_ch2"):
            st.session_state.flashcard_index = min(len(cards_to_show) - 1, st.session_state.flashcard_index + 1)
            st.rerun()

    progress = (st.session_state.flashcard_index + 1) / len(cards_to_show)
    st.progress(progress)

def show_quiz(difficulty):
    """Display MCQ quiz"""
    st.subheader("❓ Quiz: Test Your Knowledge")

    if difficulty == 'beginner':
        quiz_questions = MCQ_QUESTIONS[:2]
    elif difficulty == 'intermediate':
        quiz_questions = MCQ_QUESTIONS[:3]
    else:
        quiz_questions = MCQ_QUESTIONS

    correct_count = 0

    for idx, question in enumerate(quiz_questions, 1):
        with st.container(border=True):
            st.write(f"**Question {idx}/{len(quiz_questions)}**")
            st.write(question['q'])

            answer = st.radio(
                "Select your answer:",
                question['options'],
                key=f"ch2_q{idx}",
                label_visibility="collapsed"
            )

            if st.button("Check", key=f"check_ch2_q{idx}"):
                if answer == question['answer']:
                    st.success("✅ Correct!")
                    st.info(f"💡 {question['explanation']}")
                    correct_count += 1
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {question['answer']}")

def show_brain_drainer():
    """Display PSLE brain drainer questions"""
    st.subheader("🧠 Brain Drainer: PSLE-Style Questions")

    questions = get_brain_drainer_questions('Ch2_Water', limit=5)

    if questions:
        st.write(f"**{len(questions)} challenging questions**")
        st.markdown("---")

        for idx, question in enumerate(questions, 1):
            with st.container(border=True):
                st.markdown(f"### Question {idx}/{len(questions)}")
                result = display_brain_drainer_question(question)

                if result is not None:
                    xp_reward = 20 if result else 10
                    if result:
                        XPSystem.award_xp(xp_reward, "brain drainer")

if __name__ == "__main__":
    show_chapter()
