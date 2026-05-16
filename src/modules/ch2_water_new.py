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

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Ice', 'definition': 'Water in the solid state; melts at 0°C', 'ref': 'Page 27'},
    {'concept': 'Water', 'definition': 'Water in its liquid state', 'ref': 'Page 28'},
    {'concept': 'Water Vapour', 'definition': 'Water in the gaseous state; invisible', 'ref': 'Page 28'},
    {'concept': 'Melting', 'definition': 'Solid ice changes to liquid water at 0°C', 'ref': 'Pages 33-34'},
    {'concept': 'Freezing', 'definition': 'Liquid water changes to solid ice at 0°C', 'ref': 'Pages 33-35'},
    {'concept': 'Boiling', 'definition': 'Liquid water changes to gas at 100°C', 'ref': 'Pages 35-39'},
    {'concept': 'Condensation', 'definition': 'Gas changes to liquid when it loses heat', 'ref': 'Pages 35, 40'},
    {'concept': 'Evaporation', 'definition': 'Liquid changes to gas without boiling', 'ref': 'Page 42'},
    {'concept': 'Melting Point', 'definition': 'Temperature at which ice melts: 0 degrees C', 'ref': 'Page 31'},
    {'concept': 'Boiling Point', 'definition': 'Temperature at which water boils: 100 degrees C', 'ref': 'Page 39'},
    {'concept': 'Water Cycle', 'definition': 'Process: Evaporation, Condensation, Precipitation, Collection', 'ref': 'Pages 43-44'},
    {'concept': 'Greenhouse gases', 'definition': 'Trap heat and cause ice caps to melt', 'ref': 'Page 33'},
    {'concept': 'Desalination', 'definition': 'Process to remove salt from seawater', 'ref': 'Page 44'},
    {'concept': 'Impurities', 'definition': 'Dirt left behind when water evaporates', 'ref': 'Page 43'},
    {'concept': 'Precipitation', 'definition': 'Water falling from clouds as rain or snow', 'ref': 'Page 44'},
]

MATCHING_PAIRS = [
    ('Ice', 'Solid water'),
    ('Water', 'Liquid state'),
    ('Water Vapour', 'Gaseous state'),
    ('0°C', 'Melting and freezing point'),
    ('100°C', 'Boiling point'),
    ('Melting', 'Solid to liquid'),
    ('Freezing', 'Liquid to solid'),
    ('Boiling', 'Liquid to gas'),
    ('Condensation', 'Gas to liquid'),
    ('Evaporation', 'Liquid to gas (no boiling)'),
    ('Heat', 'Causes melting and boiling'),
    ('Loss of heat', 'Causes freezing and condensation'),
    ('Polar bears', 'Threatened by melting ice'),
    ('Greenhouse effect', 'Causes global warming'),
    ('Water cycle', 'Provides clean water supply'),
]

MCQ_QUESTIONS = [
    {
        'q': 'At what temperature does ice melt?',
        'options': ['0°C', '50°C', '100°C', '-10°C'],
        'answer': '0°C',
        'explanation': 'Ice melts at 0°C (melting point). When ice is left on a warm table, it melts. (Textbook Page 31)',
        'difficulty': 'easy'
    },
    {
        'q': 'At what temperature does water boil?',
        'options': ['0°C', '50°C', '100°C', '150°C'],
        'answer': '100°C',
        'explanation': 'Water boils at 100°C (boiling point). Bubbles form throughout the water. (Textbook Page 39)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which process happens when water changes from liquid to ice?',
        'options': ['Melting', 'Freezing', 'Boiling', 'Evaporation'],
        'answer': 'Freezing',
        'explanation': 'Freezing is liquid changing to solid at 0°C. Water in a freezer becomes ice. (Textbook Page 35)',
        'difficulty': 'easy'
    },
    {
        'q': 'When steam cools and becomes water droplets, what is this process?',
        'options': ['Melting', 'Evaporation', 'Boiling', 'Condensation'],
        'answer': 'Condensation',
        'explanation': 'Condensation is gas changing to liquid when it loses heat. (Textbook Page 40)',
        'difficulty': 'medium'
    },
    {
        'q': 'What causes water on wet clothes to disappear?',
        'options': ['Freezing', 'Melting', 'Evaporation', 'Boiling'],
        'answer': 'Evaporation',
        'explanation': 'Evaporation is liquid changing to gas without boiling. (Textbook Page 42)',
        'difficulty': 'medium'
    },
    {
        'q': 'In the water cycle, after evaporation, what happens next?',
        'options': ['Rain falls immediately', 'Condensation forms clouds', 'Water freezes', 'Nothing happens'],
        'answer': 'Condensation forms clouds',
        'explanation': 'Water vapour rises, cools, and condenses into droplets that form clouds. (Textbook Pages 43-44)',
        'difficulty': 'medium'
    },
    {
        'q': 'Why is the water cycle important?',
        'options': ['Only plants need it', 'Provides clean water for all life', 'Has no importance', 'Prevents rain'],
        'answer': 'Provides clean water for all life',
        'explanation': 'The water cycle ensures continuous clean water. Impurities are left behind during evaporation. (Textbook Pages 26, 43-44)',
        'difficulty': 'hard'
    },
    {
        'q': 'How do greenhouse gases affect ice caps?',
        'options': ['Preserve ice caps', 'Trap heat and melt ice faster', 'Have no effect', 'Create more ice'],
        'answer': 'Trap heat and melt ice faster',
        'explanation': 'Greenhouse gases trap heat, raising Earths temperature and melting ice in Arctic/Antarctica. (Textbook Page 33)',
        'difficulty': 'hard'
    },
]

def show_flashcards():
    st.subheader("📇 Water States and Phase Changes")

    if 'water_card' not in st.session_state:
        st.session_state.water_card = 0

    card = FLASHCARDS[st.session_state.water_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Prev"):
            st.session_state.water_card = max(0, st.session_state.water_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #3498db, #2980b9); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p style="font-size: 16px;">{card['definition']}</p>
            <small style="color: #ecf0f1;">{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">Card {st.session_state.water_card + 1} of {len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("Next ➡️"):
            st.session_state.water_card = min(len(FLASHCARDS) - 1, st.session_state.water_card + 1)
            st.rerun()

    st.progress((st.session_state.water_card + 1) / len(FLASHCARDS))

def show_matching():
    st.subheader("🎯 Match Water Concepts")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Concepts:**")
        for t, _ in MATCHING_PAIRS[:8]:
            st.write(f"• {t}")

    with col2:
        st.write("**Definitions:**")
        import random
        defs = [d for _, d in MATCHING_PAIRS[:8]]
        random.shuffle(defs)
        for d in defs:
            st.write(f"• {d}")

    if st.button("Show Correct Answers"):
        st.write("**Answers:**")
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")
        st.success("Great job!")

def show_quiz():
    st.subheader("❓ Water Cycle Knowledge Quiz")

    if 'water_q' not in st.session_state:
        st.session_state.water_q = 0
        st.session_state.water_score = 0

    q = MCQ_QUESTIONS[st.session_state.water_q]
    st.write(f"**Q{st.session_state.water_q + 1}: {q['q']}**")
    st.write(f"*Difficulty: {q['difficulty'].title()}*")

    ans = st.radio("Choose answer:", q['options'], key=f"wq{st.session_state.water_q}")

    if st.button("Submit"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            st.session_state.water_score += 1
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.water_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next Question"):
            st.session_state.water_q += 1
            st.rerun()
    else:
        st.info(f"Quiz Done! Score: {st.session_state.water_score}/{len(MCQ_QUESTIONS)}")
        if st.button("Restart"):
            st.session_state.water_q = 0
            st.session_state.water_score = 0
            st.rerun()

def show_chapter():
    st.header("💧 Chapter 2: Cycles in Water")
    st.write("Understand states of water and the water cycle!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()

    with tab2:
        show_matching()

    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 All content from: Inspiring Science P5 Textbook, Pages 26-49")

if __name__ == "__main__":
    show_chapter()
