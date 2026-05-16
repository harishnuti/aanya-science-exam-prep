"""Chapter 6: Simple Series Electric Circuits - Phase 2C Textbook-Aligned
Inspiring Science P5 Textbook, Pages 105-120
Theme: Systems
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Series Circuit', 'definition': 'Single path for current; components connected one after another', 'ref': 'Pages 105-107'},
    {'concept': 'Voltage', 'definition': 'Electrical pressure provided by battery; measured in Volts', 'ref': 'Pages 108-110'},
    {'concept': 'Current', 'definition': 'Flow of electrical charge through circuit; measured in Amperes', 'ref': 'Page 109'},
    {'concept': 'Resistance', 'definition': 'Opposition to current flow; measured in Ohms (unit R)', 'ref': 'Pages 110-111'},
    {'concept': 'Ohm\'s Law', 'definition': 'V = I × R (Voltage equals Current times Resistance)', 'ref': 'Pages 108-110'},
    {'concept': 'More Batteries', 'definition': 'More voltage → More current → Brighter bulbs', 'ref': 'Pages 108-110'},
    {'concept': 'More Bulbs (Series)', 'definition': 'More resistance → Less current → Dimmer bulbs', 'ref': 'Pages 110-113'},
    {'concept': 'Total Resistance', 'definition': 'In series: R_total = R₁ + R₂ + R₃ (sum of all resistances)', 'ref': 'Pages 110-113'},
    {'concept': 'Voltage Drop', 'definition': 'Voltage divides among components in series circuit', 'ref': 'Page 110'},
    {'concept': 'Circuit Breaker', 'definition': 'Safety device that trips when current is too high, preventing fires', 'ref': 'Page 113'},
    {'concept': 'Electrical Overload', 'definition': 'Too many appliances drawing too much current', 'ref': 'Pages 113-114'},
    {'concept': 'Fuse', 'definition': 'Safety device that melts when current is too high', 'ref': 'Page 113'},
    {'concept': 'Energy Conservation', 'definition': 'Saving electricity by turning off devices and using less power', 'ref': 'Pages 114-115'},
    {'concept': 'Fossil Fuels', 'definition': 'Coal, oil, gas burned to generate electricity', 'ref': 'Page 115'},
    {'concept': 'Renewable Energy', 'definition': 'Energy from sun, wind, water that does not run out', 'ref': 'Page 115'},
]

MATCHING_PAIRS = [
    ('Series circuit', 'Single path for current'),
    ('Voltage', 'Electrical pressure from battery'),
    ('Current', 'Flow of electrical charge'),
    ('Resistance', 'Opposition to current flow'),
    ('Ohm\'s Law', 'V = I × R'),
    ('More batteries', 'Brighter bulbs'),
    ('More bulbs in series', 'Dimmer bulbs'),
    ('Total resistance', 'R₁ + R₂ + R₃'),
    ('Voltage drop', 'Voltage divides among bulbs'),
    ('Circuit breaker', 'Prevents electrical fires'),
    ('Fuse', 'Safety device that melts'),
    ('Overload', 'Too much current'),
    ('Energy conservation', 'Save electricity'),
    ('Fossil fuels', 'Coal, oil, gas for power'),
    ('Renewable energy', 'Never runs out'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What is a series circuit?',
        'options': ['Many paths for current', 'Single path for current with components in a line', 'No path for current', 'Random paths'],
        'answer': 'Single path for current with components in a line',
        'explanation': 'A series circuit has one path for current; all components are connected in a line. (Textbook Pages 105-107)',
        'difficulty': 'easy'
    },
    {
        'q': 'What happens when you add more batteries in a series circuit?',
        'options': ['Bulbs get dimmer', 'Bulbs get brighter', 'No change', 'Circuit breaks'],
        'answer': 'Bulbs get brighter',
        'explanation': 'More batteries provide more voltage, which increases current, making bulbs brighter. (Textbook Pages 108-110)',
        'difficulty': 'easy'
    },
    {
        'q': 'What happens when you add more bulbs in a series circuit?',
        'options': ['All stay bright', 'All get dimmer', 'One gets brighter', 'Nothing happens'],
        'answer': 'All get dimmer',
        'explanation': 'More bulbs add resistance. More resistance means less current, so all bulbs get dimmer. (Textbook Pages 110-113)',
        'difficulty': 'medium'
    },
    {
        'q': 'What does Ohm\'s Law state?',
        'options': ['V = I + R', 'V = I × R', 'V = I ÷ R', 'V = R - I'],
        'answer': 'V = I × R',
        'explanation': 'Ohm\'s Law: Voltage = Current × Resistance. This relates the three key quantities in a circuit. (Textbook Pages 108-110)',
        'difficulty': 'medium'
    },
    {
        'q': 'What is a circuit breaker?',
        'options': ['Something that breaks circuits', 'A device that prevents electrical fires', 'A type of bulb', 'A power source'],
        'answer': 'A device that prevents electrical fires',
        'explanation': 'A circuit breaker is a safety device that automatically trips (opens) when current is too high, preventing fires and damage. (Textbook Page 113)',
        'difficulty': 'medium'
    },
    {
        'q': 'In a series circuit, what happens to voltage across each bulb?',
        'options': ['Each bulb gets full voltage', 'Voltage divides among bulbs', 'Bulbs get no voltage', 'Voltage stays same everywhere'],
        'answer': 'Voltage divides among bulbs',
        'explanation': 'In series, total voltage divides among components. With 3 bulbs and 6V, each bulb gets about 2V. (Textbook Page 110)',
        'difficulty': 'hard'
    },
    {
        'q': 'Why is energy conservation important?',
        'options': ['Saves money', 'Reduces fossil fuel use and environmental impact', 'Makes bulbs brighter', 'Prevents circuit breaks'],
        'answer': 'Reduces fossil fuel use and environmental impact',
        'explanation': 'Saving electricity reduces the need to burn fossil fuels, which protects the environment. (Textbook Pages 114-115)',
        'difficulty': 'hard'
    },
    {
        'q': 'In a series circuit with 2 identical bulbs and 6V battery, what voltage is across each bulb?',
        'options': ['0V', '6V', '3V', '12V'],
        'answer': '3V',
        'explanation': 'In series, voltage divides equally among identical resistances. 6V ÷ 2 bulbs = 3V per bulb. (Textbook Page 110)',
        'difficulty': 'hard'
    },
]

def show_flashcards():
    st.subheader("📇 Simple Series Electric Circuits")

    if 'circuits_card' not in st.session_state:
        st.session_state.circuits_card = 0

    card = FLASHCARDS[st.session_state.circuits_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️", key="circ_prev"):
            st.session_state.circuits_card = max(0, st.session_state.circuits_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #e74c3c, #c0392b); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p>{card['definition']}</p>
            <small>{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">{st.session_state.circuits_card + 1}/{len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("➡️", key="circ_next"):
            st.session_state.circuits_card = min(len(FLASHCARDS) - 1, st.session_state.circuits_card + 1)
            st.rerun()

def show_matching():
    st.subheader("🎯 Match Circuit Concepts")

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

    if st.button("Show Answers", key="circ_ans"):
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")

def show_quiz():
    st.subheader("❓ Simple Series Circuits Quiz")

    if 'circuits_q' not in st.session_state:
        st.session_state.circuits_q = 0

    q = MCQ_QUESTIONS[st.session_state.circuits_q]
    st.write(f"**Q{st.session_state.circuits_q + 1}: {q['q']}**")

    ans = st.radio("Select:", q['options'], key=f"cq{st.session_state.circuits_q}")

    if st.button("Check", key="circ_check"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.circuits_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next", key="circ_nxt"):
            st.session_state.circuits_q += 1
            st.rerun()

def show_chapter():
    st.header("⚡ Chapter 6: Simple Series Electric Circuits")
    st.write("Master voltage, current, resistance, and circuit safety!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()
    with tab2:
        show_matching()
    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 Content from: Inspiring Science P5, Pages 105-120")

if __name__ == "__main__":
    show_chapter()
