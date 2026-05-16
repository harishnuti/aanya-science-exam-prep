"""Chapter 1: Reproduction in Animals & Plants - Phase 2C Textbook-Aligned
Inspiring Science P5 Textbook, Pages 2-25
Theme: Cycles
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Reproduction', 'definition': 'Process by which living organisms produce offspring', 'ref': 'Page 2'},
    {'concept': 'Sperm', 'definition': 'Male reproductive cell; contributes to offspring in animals', 'ref': 'Pages 5-7'},
    {'concept': 'Egg', 'definition': 'Female reproductive cell; needed for reproduction in animals', 'ref': 'Pages 5-7'},
    {'concept': 'Fertilization', 'definition': 'When sperm and egg join to form a zygote', 'ref': 'Pages 5-7'},
    {'concept': 'Inherited Traits', 'definition': 'Characteristics passed from parents to offspring (eyelids, earlobes, dimples)', 'ref': 'Pages 4-5'},
    {'concept': 'Puberty', 'definition': 'Stage when sperms and eggs begin to mature in young animals', 'ref': 'Page 5'},
    {'concept': 'Flower', 'definition': 'Reproductive part of a flowering plant; contains stamen and pistil', 'ref': 'Pages 12-13'},
    {'concept': 'Pollination', 'definition': 'Transfer of pollen from anther (male) to stigma (female)', 'ref': 'Pages 14-15'},
    {'concept': 'Pollen', 'definition': 'Fine powder containing male cells; produced in anther', 'ref': 'Page 14'},
    {'concept': 'Stigma', 'definition': 'Female part of flower that receives pollen', 'ref': 'Page 13'},
    {'concept': 'Seed', 'definition': 'Result of fertilization in plants; contains embryo and food store', 'ref': 'Pages 16-17'},
    {'concept': 'Seed Dispersal', 'definition': 'Movement of seeds away from parent plant (wind, water, animals)', 'ref': 'Page 15'},
    {'concept': 'Germination', 'definition': 'Process when seed grows into a seedling; needs WOW (Water, Oxygen, Warmth)', 'ref': 'Page 17'},
    {'concept': 'Non-flowering Plants', 'definition': 'Plants that reproduce using spores, not seeds (ferns, mosses)', 'ref': 'Pages 18-19'},
    {'concept': 'Spores', 'definition': 'Tiny reproductive cells of non-flowering plants; dispersed by wind or water', 'ref': 'Pages 18-19'},
]

MATCHING_PAIRS = [
    ('Sperm', 'Male reproductive cell'),
    ('Egg', 'Female reproductive cell'),
    ('Fertilization', 'Sperm and egg join'),
    ('Inherited traits', 'Passed from parents'),
    ('Puberty', 'When reproduction begins'),
    ('Flower', 'Plant reproductive part'),
    ('Pollen', 'Male reproductive powder'),
    ('Stigma', 'Receives pollen'),
    ('Seed', 'Contains baby plant'),
    ('Germination', 'Seed grows into seedling'),
    ('Water, Oxygen, Warmth', 'Needed for germination'),
    ('Seed dispersal', 'Moving seeds away'),
    ('Non-flowering plants', 'Use spores'),
    ('Spores', 'Tiny cells for reproduction'),
    ('Pollination', 'Pollen transfer'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What is reproduction?',
        'options': ['Growing bigger', 'Process of producing offspring', 'Moving around', 'Finding food'],
        'answer': 'Process of producing offspring',
        'explanation': 'Reproduction is when living organisms produce offspring (babies). (Textbook Page 2)',
        'difficulty': 'easy'
    },
    {
        'q': 'What do we call the female reproductive cell?',
        'options': ['Sperm', 'Egg', 'Seed', 'Pollen'],
        'answer': 'Egg',
        'explanation': 'An egg is the female reproductive cell. In plants, it is inside the ovule. (Textbook Pages 5-7)',
        'difficulty': 'easy'
    },
    {
        'q': 'What happens during fertilization?',
        'options': ['Egg grows alone', 'Sperm and egg join together', 'Seed is made', 'Nothing happens'],
        'answer': 'Sperm and egg join together',
        'explanation': 'Fertilization is when sperm (male cell) and egg (female cell) join to form a zygote. (Textbook Pages 5-7)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which of these is an inherited trait?',
        'options': ['Height you grow', 'Language you speak', 'Dimples on your face', 'Clothes you wear'],
        'answer': 'Dimples on your face',
        'explanation': 'Inherited traits like dimples, earlobes, and eyelids are passed from parents to offspring. (Textbook Pages 4-5)',
        'difficulty': 'medium'
    },
    {
        'q': 'What is pollination?',
        'options': ['Making the flower bigger', 'Transfer of pollen from anther to stigma', 'Planting seeds', 'Growing roots'],
        'answer': 'Transfer of pollen from anther to stigma',
        'explanation': 'Pollination is when pollen moves from the anther (male part) to the stigma (female part) of a flower. (Textbook Pages 14-15)',
        'difficulty': 'medium'
    },
    {
        'q': 'What does a seed contain?',
        'options': ['Only water', 'Embryo and food store', 'Only soil', 'Only air'],
        'answer': 'Embryo and food store',
        'explanation': 'A seed contains an embryo (baby plant) and a food store to help it grow. (Textbook Pages 16-17)',
        'difficulty': 'medium'
    },
    {
        'q': 'Why are seeds dispersed (moved away from parent plant)?',
        'options': ['To have more room', 'To find new places to grow away from parent plant', 'To get wet', 'No reason'],
        'answer': 'To find new places to grow away from parent plant',
        'explanation': 'Seeds are dispersed by wind, water, or animals to colonize new areas away from the parent plant. (Textbook Page 15)',
        'difficulty': 'hard'
    },
    {
        'q': 'What does WOW stand for in seed germination?',
        'options': ['Water, Oil, Wood', 'Water, Oxygen, Warmth', 'Wind, Oil, Warmth', 'Water, Oxygen, Wind'],
        'answer': 'Water, Oxygen, Warmth',
        'explanation': 'WOW (Water, Oxygen, Warmth) are the three things seeds need to germinate (start growing). (Textbook Page 17)',
        'difficulty': 'hard'
    },
]

def show_flashcards():
    st.subheader("📇 Reproduction in Animals & Plants")

    if 'repro_card' not in st.session_state:
        st.session_state.repro_card = 0

    card = FLASHCARDS[st.session_state.repro_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️", key="repro_prev"):
            st.session_state.repro_card = max(0, st.session_state.repro_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #9b59b6, #8e44ad); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p>{card['definition']}</p>
            <small>{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">{st.session_state.repro_card + 1}/{len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("➡️", key="repro_next"):
            st.session_state.repro_card = min(len(FLASHCARDS) - 1, st.session_state.repro_card + 1)
            st.rerun()

def show_matching():
    st.subheader("🎯 Match Reproduction Concepts")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Terms:**")
        for t, _ in MATCHING_PAIRS[:8]:
            st.write(f"• {t}")

    with col2:
        st.write("**Definitions:**")
        import random
        defs = [d for _, d in MATCHING_PAIRS[:8]]
        random.shuffle(defs)
        for d in defs:
            st.write(f"• {d}")

    if st.button("Show Answers", key="repro_ans"):
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")

def show_quiz():
    st.subheader("❓ Reproduction Quiz")

    if 'repro_q' not in st.session_state:
        st.session_state.repro_q = 0

    q = MCQ_QUESTIONS[st.session_state.repro_q]
    st.write(f"**Q{st.session_state.repro_q + 1}: {q['q']}**")

    ans = st.radio("Select:", q['options'], key=f"rq{st.session_state.repro_q}")

    if st.button("Check", key="repro_check"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.repro_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next", key="repro_nxt"):
            st.session_state.repro_q += 1
            st.rerun()

def show_chapter():
    st.header("👶 Chapter 1: Reproduction in Animals & Plants")
    st.write("Learn how animals and plants create offspring!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()
    with tab2:
        show_matching()
    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 Content from: Inspiring Science P5, Pages 2-25")

if __name__ == "__main__":
    show_chapter()
