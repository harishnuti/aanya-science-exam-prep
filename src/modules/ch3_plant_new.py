"""Chapter 3: Plant Transport System - Phase 2C Textbook-Aligned Version
Inspiring Science P5 Textbook, Pages 52-63
Theme: Systems
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Plant Transport System', 'definition': 'System that carries water, minerals, and food to all parts of a plant', 'ref': 'Page 52'},
    {'concept': 'Roots', 'definition': 'Plant part that absorbs water and mineral salts from soil', 'ref': 'Page 54'},
    {'concept': 'Root Hairs', 'definition': 'Tiny structures that increase surface area for water absorption', 'ref': 'Page 54'},
    {'concept': 'Xylem', 'definition': 'Water-carrying tubes; transports water and minerals from roots to leaves', 'ref': 'Pages 55-56'},
    {'concept': 'Phloem', 'definition': 'Food-carrying tubes; transports food (glucose) from leaves to all parts', 'ref': 'Pages 57-58'},
    {'concept': 'Mineral Salts', 'definition': 'Nutrients absorbed by roots and transported through xylem', 'ref': 'Page 55'},
    {'concept': 'Transpiration', 'definition': 'Process where water vapour escapes from leaves', 'ref': 'Page 59'},
    {'concept': 'Stem', 'definition': 'Plant part containing xylem and phloem tubes', 'ref': 'Pages 56-57'},
    {'concept': 'Leaves', 'definition': 'Plant part where food is made; loses water through transpiration', 'ref': 'Pages 57, 59'},
    {'concept': 'Photosynthesis', 'definition': 'Process where leaves make food using light and water', 'ref': 'Page 54'},
    {'concept': 'Woody Tubes', 'definition': 'Another name for xylem (appears as wood in stems)', 'ref': 'Page 55'},
    {'concept': 'Food Transport', 'definition': 'Movement of glucose from leaves to other plant parts through phloem', 'ref': 'Pages 57-58'},
    {'concept': 'Water Transport', 'definition': 'Movement of water from roots to all plant parts through xylem', 'ref': 'Pages 55-56'},
    {'concept': 'Bark Removal', 'definition': 'Cutting ring of bark removes phloem; plant above cut starves', 'ref': 'Page 59'},
    {'concept': 'Plant Wilting', 'definition': 'Plant droops when water-carrying tubes are cut; no water reaches leaves', 'ref': 'Page 60'},
]

MATCHING_PAIRS = [
    ('Xylem', 'Carries water and minerals'),
    ('Phloem', 'Carries food (glucose)'),
    ('Roots', 'Absorb water and minerals'),
    ('Leaves', 'Make food; lose water'),
    ('Stem', 'Contains transport tubes'),
    ('Root Hairs', 'Increase absorption surface'),
    ('Transpiration', 'Water vapour from leaves'),
    ('Photosynthesis', 'Leaves make food'),
    ('Mineral Salts', 'Travel in xylem'),
    ('Water Transport', 'From roots to all parts'),
    ('Food Transport', 'From leaves to all parts'),
    ('Woody tubes', 'Xylem tubes'),
    ('Cutting phloem', 'Plant starves (no food below)'),
    ('Cutting xylem', 'Plant wilts (no water)'),
    ('Plant death', 'When both xylem and phloem removed'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What is the main function of roots?',
        'options': ['Make food', 'Absorb water and minerals', 'Transport food', 'Release oxygen'],
        'answer': 'Absorb water and minerals',
        'explanation': 'Roots absorb water and mineral salts from soil. These are transported to other parts. (Textbook Page 54)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which tubes carry water through a plant?',
        'options': ['Phloem tubes', 'Xylem tubes', 'Both equally', 'Neither'],
        'answer': 'Xylem tubes',
        'explanation': 'Xylem tubes (water-carrying tubes) transport water from roots to leaves. (Textbook Pages 55-56)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which tubes carry food through a plant?',
        'options': ['Xylem tubes', 'Phloem tubes', 'Root hairs', 'Stems'],
        'answer': 'Phloem tubes',
        'explanation': 'Phloem tubes (food-carrying tubes) transport food made in leaves to all parts. (Textbook Pages 57-58)',
        'difficulty': 'easy'
    },
    {
        'q': 'Why do plants need a transport system?',
        'options': ['To look tall', 'To move water and food to all parts', 'To make seeds', 'To absorb sunlight'],
        'answer': 'To move water and food to all parts',
        'explanation': 'Plants need transport to move water (roots absorb it, leaves need it) and food (made in leaves, needed everywhere). (Textbook Pages 52-53)',
        'difficulty': 'medium'
    },
    {
        'q': 'What happens if a ring of bark is cut around a tree stem?',
        'options': ['Tree grows taller', 'Food cannot reach parts below; they starve', 'Tree gets more water', 'Nothing changes'],
        'answer': 'Food cannot reach parts below; they starve',
        'explanation': 'Bark contains phloem tubes. Removing it cuts food transport, so parts below receive no food and starve. (Textbook Page 59)',
        'difficulty': 'hard'
    },
    {
        'q': 'What does the term transpiration mean?',
        'options': ['Moving water upward', 'Losing water vapour from leaves', 'Making food', 'Absorbing minerals'],
        'answer': 'Losing water vapour from leaves',
        'explanation': 'Transpiration is when water vapour escapes from leaves into the air. (Textbook Page 59)',
        'difficulty': 'medium'
    },
    {
        'q': 'If water-carrying tubes (xylem) are cut, what happens to the plant?',
        'options': ['It grows faster', 'It wilts (droops)', 'It makes more food', 'Nothing happens'],
        'answer': 'It wilts (droops)',
        'explanation': 'When xylem is cut, water cannot reach leaves, so the plant wilts. (Textbook Page 60)',
        'difficulty': 'hard'
    },
    {
        'q': 'Where is food made in a plant?',
        'options': ['In roots', 'In stems', 'In leaves', 'In flowers'],
        'answer': 'In leaves',
        'explanation': 'Leaves make food through photosynthesis. This food is then transported to other parts via phloem. (Textbook Pages 54, 57)',
        'difficulty': 'medium'
    },
]

def show_flashcards():
    st.subheader("📇 Plant Transport System")

    if 'plant_card' not in st.session_state:
        st.session_state.plant_card = 0

    card = FLASHCARDS[st.session_state.plant_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Prev", key="plant_prev"):
            st.session_state.plant_card = max(0, st.session_state.plant_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #27ae60, #1e8449); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p style="font-size: 16px;">{card['definition']}</p>
            <small style="color: #abebc6;">{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">Card {st.session_state.plant_card + 1} of {len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("Next ➡️", key="plant_next"):
            st.session_state.plant_card = min(len(FLASHCARDS) - 1, st.session_state.plant_card + 1)
            st.rerun()

    st.progress((st.session_state.plant_card + 1) / len(FLASHCARDS))

def show_matching():
    st.subheader("🎯 Match Plant Transport Concepts")

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

    if st.button("Show Answers", key="plant_answers"):
        st.write("**Correct Matches:**")
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")

def show_quiz():
    st.subheader("❓ Plant Transport Quiz")

    if 'plant_q' not in st.session_state:
        st.session_state.plant_q = 0
        st.session_state.plant_score = 0

    q = MCQ_QUESTIONS[st.session_state.plant_q]
    st.write(f"**Q{st.session_state.plant_q + 1}: {q['q']}**")

    ans = st.radio("Choose:", q['options'], key=f"pq{st.session_state.plant_q}")

    if st.button("Submit", key="plant_submit"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            st.session_state.plant_score += 1
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.plant_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next", key="plant_nxt"):
            st.session_state.plant_q += 1
            st.rerun()
    else:
        st.info(f"Quiz Done! Score: {st.session_state.plant_score}/{len(MCQ_QUESTIONS)}")

def show_chapter():
    st.header("🌿 Chapter 3: Plant Transport System")
    st.write("Learn how plants transport water and food!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()
    with tab2:
        show_matching()
    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 Content from: Inspiring Science P5, Pages 52-63")

if __name__ == "__main__":
    show_chapter()
