"""Chapter 4: Human Respiratory & Circulatory Systems - Phase 2C Textbook-Aligned
Inspiring Science P5 Textbook, Pages 64-87
Theme: Systems
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Air', 'definition': 'Mixture of gases including oxygen, nitrogen, carbon dioxide, and water vapour', 'ref': 'Page 65'},
    {'concept': 'Oxygen', 'definition': 'Gas in air that living things need to survive (about 21%)', 'ref': 'Page 65'},
    {'concept': 'Carbon Dioxide', 'definition': 'Gas produced by living things; about 0.04% inhaled, 4.4% exhaled', 'ref': 'Pages 65, 70'},
    {'concept': 'Nose', 'definition': 'Allows air to enter and leave body; warms and moistens air; traps dust', 'ref': 'Page 69'},
    {'concept': 'Windpipe (Trachea)', 'definition': 'Carries air to and from lungs', 'ref': 'Page 69'},
    {'concept': 'Lungs', 'definition': 'Main respiratory organs where gaseous exchange happens', 'ref': 'Pages 69-71'},
    {'concept': 'Diaphragm', 'definition': 'Muscle below lungs that aids breathing by contracting and relaxing', 'ref': 'Page 70'},
    {'concept': 'Gaseous Exchange', 'definition': 'Oxygen enters blood, carbon dioxide leaves blood (in lungs)', 'ref': 'Page 71'},
    {'concept': 'Breathing', 'definition': 'Taking in air (inhale) and releasing air (exhale)', 'ref': 'Page 69'},
    {'concept': 'Inhaled Air', 'definition': 'Air breathed in; contains 21% oxygen, 0.04% carbon dioxide', 'ref': 'Page 70'},
    {'concept': 'Exhaled Air', 'definition': 'Air breathed out; contains 16% oxygen, 4.4% carbon dioxide', 'ref': 'Page 70'},
    {'concept': 'Heart', 'definition': 'Muscle that pumps blood to different parts of body', 'ref': 'Pages 75-76'},
    {'concept': 'Blood Vessels', 'definition': 'Tubes carrying blood; include arteries and veins', 'ref': 'Page 76'},
    {'concept': 'Pulse', 'definition': 'Heartbeat felt at wrist or neck; rhythm created by heart pumping', 'ref': 'Page 76'},
    {'concept': 'Heart Rate', 'definition': 'Number of times heart beats in one minute', 'ref': 'Page 76'},
]

MATCHING_PAIRS = [
    ('Oxygen', 'Gas needed for survival'),
    ('Carbon dioxide', 'Waste gas produced by living things'),
    ('Nose', 'Warms and moistens air'),
    ('Windpipe', 'Carries air to lungs'),
    ('Lungs', 'Gaseous exchange happens here'),
    ('Diaphragm', 'Muscle that aids breathing'),
    ('Breathing in', 'Inhale; diaphragm contracts'),
    ('Breathing out', 'Exhale; diaphragm relaxes'),
    ('Heart', 'Pumps blood'),
    ('Arteries', 'Carry oxygen-rich blood away'),
    ('Veins', 'Carry oxygen-poor blood back'),
    ('Pulse', 'Heartbeat rhythm'),
    ('Exercise', 'Increases breathing and heart rate'),
    ('Asthma', 'Narrowed airways due to swelling'),
    ('Smoking', 'Harms lungs and breathing'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What is the main gas that living things need from air?',
        'options': ['Nitrogen', 'Carbon dioxide', 'Oxygen', 'Water vapour'],
        'answer': 'Oxygen',
        'explanation': 'Living things need oxygen to survive. Air contains about 21% oxygen. (Textbook Page 65)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which organ is the main site for gaseous exchange?',
        'options': ['Nose', 'Windpipe', 'Lungs', 'Heart'],
        'answer': 'Lungs',
        'explanation': 'In the lungs, oxygen enters blood and carbon dioxide leaves blood. (Textbook Pages 69-71)',
        'difficulty': 'easy'
    },
    {
        'q': 'What does the diaphragm do?',
        'options': ['Filters air', 'Contracts and relaxes to aid breathing', 'Pumps blood', 'Makes food'],
        'answer': 'Contracts and relaxes to aid breathing',
        'explanation': 'The diaphragm is a muscle below the lungs. When it contracts, lungs expand (inhale). (Textbook Page 70)',
        'difficulty': 'easy'
    },
    {
        'q': 'How much oxygen is in exhaled air compared to inhaled air?',
        'options': ['More oxygen in exhaled', 'Less oxygen in exhaled (16% vs 21%)', 'Same amount', 'No oxygen in exhaled'],
        'answer': 'Less oxygen in exhaled (16% vs 21%)',
        'explanation': 'Inhaled air: 21% oxygen. Exhaled air: 16% oxygen. Our body uses the oxygen. (Textbook Page 70)',
        'difficulty': 'hard'
    },
    {
        'q': 'What is the main function of the heart?',
        'options': ['Make blood', 'Filter blood', 'Pump blood to different parts', 'Store blood'],
        'answer': 'Pump blood to different parts',
        'explanation': 'The heart is a muscle that pumps blood continuously throughout the body. (Textbook Pages 75-76)',
        'difficulty': 'easy'
    },
    {
        'q': 'Where can you feel your pulse?',
        'options': ['Only on wrist', 'Only on neck', 'On wrist or neck', 'Nowhere'],
        'answer': 'On wrist or neck',
        'explanation': 'You can feel pulse by placing fingers on wrist or side of neck. This shows heartbeat. (Textbook Page 76)',
        'difficulty': 'medium'
    },
    {
        'q': 'What happens to breathing and heart rate during exercise?',
        'options': ['Both stay same', 'Both decrease', 'Both increase', 'Breathing increases, heart decreases'],
        'answer': 'Both increase',
        'explanation': 'During exercise, body needs more oxygen. Breathing rate and heart rate increase to deliver oxygen. (Textbook Page 79-80)',
        'difficulty': 'medium'
    },
    {
        'q': 'During asthma attack, what happens to airways?',
        'options': ['Airways widen', 'Airways narrow/swell', 'Airways stay normal', 'Airways disappear'],
        'answer': 'Airways narrow/swell',
        'explanation': 'Asthma causes swelling and narrowing of airways, making breathing difficult. Inhaler medicine helps. (Textbook Page 71)',
        'difficulty': 'hard'
    },
]

def show_flashcards():
    st.subheader("📇 Respiratory & Circulatory System")

    if 'human_card' not in st.session_state:
        st.session_state.human_card = 0

    card = FLASHCARDS[st.session_state.human_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️", key="h_prev"):
            st.session_state.human_card = max(0, st.session_state.human_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #e74c3c, #c0392b); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p>{card['definition']}</p>
            <small>{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">{st.session_state.human_card + 1}/{len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("➡️", key="h_next"):
            st.session_state.human_card = min(len(FLASHCARDS) - 1, st.session_state.human_card + 1)
            st.rerun()

def show_matching():
    st.subheader("🎯 Match Respiratory & Circulatory Terms")

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

    if st.button("Show Answers", key="h_ans"):
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")

def show_quiz():
    st.subheader("❓ Human Systems Quiz")

    if 'human_q' not in st.session_state:
        st.session_state.human_q = 0

    q = MCQ_QUESTIONS[st.session_state.human_q]
    st.write(f"**Q{st.session_state.human_q + 1}: {q['q']}**")

    ans = st.radio("Select:", q['options'], key=f"hq{st.session_state.human_q}")

    if st.button("Check", key="h_check"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.human_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next", key="h_nxt"):
            st.session_state.human_q += 1
            st.rerun()

def show_chapter():
    st.header("❤️ Chapter 4: Human Respiratory & Circulatory Systems")
    st.write("Learn how your body breathes and circulates blood!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()
    with tab2:
        show_matching()
    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 Content from: Inspiring Science P5, Pages 64-87")

if __name__ == "__main__":
    show_chapter()
