"""Chapter 5: Electrical Systems - Phase 2C Textbook-Aligned
Inspiring Science P5 Textbook, Pages 88-104
Theme: Systems
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import MalteseDogFeedback

# ==================== TEXTBOOK CONTENT ====================

FLASHCARDS = [
    {'concept': 'Battery', 'definition': 'Device that provides electrical energy to a circuit', 'ref': 'Pages 93-95'},
    {'concept': 'Bulb', 'definition': 'Electrical component that produces light when current flows through it', 'ref': 'Pages 93-95'},
    {'concept': 'Wire', 'definition': 'Conductor that carries electrical current from one component to another', 'ref': 'Pages 93-95'},
    {'concept': 'Switch', 'definition': 'Device that opens or closes the circuit path to control current flow', 'ref': 'Pages 93-95'},
    {'concept': 'Closed Circuit', 'definition': 'Complete path for current; switch is on; light is on', 'ref': 'Pages 94-96'},
    {'concept': 'Open Circuit', 'definition': 'Broken path for current; switch is off; light is off', 'ref': 'Pages 94-96'},
    {'concept': 'Current', 'definition': 'Flow of electrical charge through a circuit; measured in Amperes', 'ref': 'Page 97'},
    {'concept': 'Conductor', 'definition': 'Material that allows current to flow easily (metals like copper, iron, aluminum, silver)', 'ref': 'Page 98'},
    {'concept': 'Insulator', 'definition': 'Material that does not allow current to flow (rubber, plastic, wood, glass)', 'ref': 'Page 98'},
    {'concept': 'Ammeter', 'definition': 'Instrument used to measure current in a circuit', 'ref': 'Pages 102-103'},
    {'concept': 'Circuit Symbol', 'definition': 'Standardized diagram symbol representing a circuit component', 'ref': 'Pages 102-103'},
    {'concept': 'Electrical Safety', 'definition': 'Never touch wet appliances; always keep hands dry when using electrical devices', 'ref': 'Pages 101-102'},
    {'concept': 'Series Circuit', 'definition': 'Single path for current; components connected one after another', 'ref': 'Page 93'},
    {'concept': 'Parallel Circuit', 'definition': 'Multiple paths for current; components connected with separate paths', 'ref': 'Page 93'},
    {'concept': 'Electrical Appliance', 'definition': 'Device that uses electrical energy to perform a task (fan, lights, heater)', 'ref': 'Pages 100-101'},
]

MATCHING_PAIRS = [
    ('Battery', 'Provides electrical energy'),
    ('Bulb', 'Produces light'),
    ('Wire', 'Carries current'),
    ('Switch', 'Controls circuit on/off'),
    ('Closed circuit', 'Complete path; light on'),
    ('Open circuit', 'Broken path; light off'),
    ('Current', 'Flow of electrical charge'),
    ('Conductor', 'Metal that allows current'),
    ('Insulator', 'Material that blocks current'),
    ('Copper', 'Conductor used in wires'),
    ('Rubber', 'Insulator around wires'),
    ('Ammeter', 'Measures current'),
    ('Circuit symbol', 'Diagram representation'),
    ('Wet hands', 'Dangerous with electricity'),
    ('Series path', 'Single route for current'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What does a battery do in a circuit?',
        'options': ['Makes the bulb bright', 'Provides electrical energy', 'Measures current', 'Stores light'],
        'answer': 'Provides electrical energy',
        'explanation': 'A battery provides electrical energy that makes current flow in the circuit. (Textbook Pages 93-95)',
        'difficulty': 'easy'
    },
    {
        'q': 'What is the difference between a closed and an open circuit?',
        'options': ['Closed is bigger', 'Closed has complete path (light on); open has broken path (light off)', 'No difference', 'Open uses less energy'],
        'answer': 'Closed has complete path (light on); open has broken path (light off)',
        'explanation': 'A closed circuit has a complete path for current so the bulb lights up. An open circuit is broken, so no current flows and the bulb stays off. (Textbook Pages 94-96)',
        'difficulty': 'easy'
    },
    {
        'q': 'What does a switch do?',
        'options': ['Provides power', 'Makes light brighter', 'Opens or closes the circuit path', 'Measures current'],
        'answer': 'Opens or closes the circuit path',
        'explanation': 'A switch controls whether the circuit is open (off) or closed (on). (Textbook Pages 93-95)',
        'difficulty': 'easy'
    },
    {
        'q': 'Which of these is a good conductor?',
        'options': ['Rubber', 'Plastic', 'Copper', 'Glass'],
        'answer': 'Copper',
        'explanation': 'Copper is a metal and is a good conductor of electricity. It is used to make wires. (Textbook Page 98)',
        'difficulty': 'easy'
    },
    {
        'q': 'Why is rubber used on electrical wires?',
        'options': ['Makes it shiny', 'Rubber is an insulator that protects us from current', 'Makes it stronger', 'Prevents rust'],
        'answer': 'Rubber is an insulator that protects us from current',
        'explanation': 'Rubber is an insulator that does not conduct electricity. It wraps around copper wires to keep us safe. (Textbook Page 98)',
        'difficulty': 'medium'
    },
    {
        'q': 'What should you never do with electrical appliances?',
        'options': ['Use them when wet', 'Touch them with wet hands', 'Use them in the kitchen', 'All of the above'],
        'answer': 'Touch them with wet hands',
        'explanation': 'Water is a conductor of electricity. Touching electrical appliances with wet hands is very dangerous and can cause electric shock. (Textbook Pages 101-102)',
        'difficulty': 'medium'
    },
    {
        'q': 'How is current measured in a circuit?',
        'options': ['By the brightness of bulb', 'Using an ammeter in Amperes', 'By the size of the wire', 'By the battery voltage'],
        'answer': 'Using an ammeter in Amperes',
        'explanation': 'An ammeter is an instrument that measures current (electrical charge flow) in units called Amperes. (Textbook Pages 102-103)',
        'difficulty': 'hard'
    },
    {
        'q': 'In a series circuit, if one bulb burns out, what happens?',
        'options': ['Other bulbs stay bright', 'All bulbs go out', 'The circuit becomes parallel', 'Nothing happens'],
        'answer': 'All bulbs go out',
        'explanation': 'In a series circuit, there is only one path for current. If one bulb burns out, the path breaks and all bulbs go out. (Textbook Page 93)',
        'difficulty': 'hard'
    },
]

def show_flashcards():
    st.subheader("📇 Electrical Systems")

    if 'electrical_card' not in st.session_state:
        st.session_state.electrical_card = 0

    card = FLASHCARDS[st.session_state.electrical_card]

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️", key="elec_prev"):
            st.session_state.electrical_card = max(0, st.session_state.electrical_card - 1)
            st.rerun()

    with col2:
        st.markdown(f"""
        <div style="padding: 25px; background: linear-gradient(135deg, #f39c12, #e67e22); border-radius: 10px; color: white; text-align: center;">
            <h3>{card['concept']}</h3>
            <hr style="background-color: white;">
            <p>{card['definition']}</p>
            <small>{card['ref']}</small>
            <p style="margin-top: 10px; font-size: 12px;">{st.session_state.electrical_card + 1}/{len(FLASHCARDS)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("➡️", key="elec_next"):
            st.session_state.electrical_card = min(len(FLASHCARDS) - 1, st.session_state.electrical_card + 1)
            st.rerun()

def show_matching():
    st.subheader("🎯 Match Electrical Concepts")

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

    if st.button("Show Answers", key="elec_ans"):
        for t, d in MATCHING_PAIRS[:8]:
            st.write(f"✓ {t} → {d}")

def show_quiz():
    st.subheader("❓ Electrical Systems Quiz")

    if 'electrical_q' not in st.session_state:
        st.session_state.electrical_q = 0

    q = MCQ_QUESTIONS[st.session_state.electrical_q]
    st.write(f"**Q{st.session_state.electrical_q + 1}: {q['q']}**")

    ans = st.radio("Select:", q['options'], key=f"eq{st.session_state.electrical_q}")

    if st.button("Check", key="elec_check"):
        if ans == q['answer']:
            st.success("✅ Correct!")
            MalteseDogFeedback.show_happy_maltese("Aanya")
            st.balloons()
        else:
            st.error("❌ Try again")
            MalteseDogFeedback.show_sad_maltese("Aanya")

        st.write(f"**Explanation:** {q['explanation']}")

    if st.session_state.electrical_q < len(MCQ_QUESTIONS) - 1:
        if st.button("Next", key="elec_nxt"):
            st.session_state.electrical_q += 1
            st.rerun()

def show_chapter():
    st.header("⚡ Chapter 5: Electrical Systems")
    st.write("Learn how electrical circuits work and how to stay safe!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📇 Flashcards", "🎯 Matching", "❓ Quiz"])

    with tab1:
        show_flashcards()
    with tab2:
        show_matching()
    with tab3:
        show_quiz()

    st.markdown("---")
    st.info("📚 Content from: Inspiring Science P5, Pages 88-104")

if __name__ == "__main__":
    show_chapter()
