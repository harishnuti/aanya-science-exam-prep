"""Chapter 6: Electric Circuits - Phase 2 Enhanced Version"""
import streamlit as st
from components.circuit_generator import CircuitGenerator
import random

def show_flashcards():
    """Display circuit flashcards"""
    st.subheader("📇 Circuit Flashcards")

    flashcards = [
        {"front": "Series Circuit", "back": "A circuit where components are connected in a single path. Current flows through one path only."},
        {"front": "Parallel Circuit", "back": "A circuit where components are connected in multiple branches. Current can flow through different paths."},
        {"front": "Ohm's Law", "back": "V = I × R (Voltage = Current × Resistance). Tells us how voltage, current, and resistance relate."},
        {"front": "Current", "back": "The flow of electrons through a circuit, measured in Amperes (A)."},
        {"front": "Resistance", "back": "Opposition to current flow, measured in Ohms (Ω). Higher resistance = less current."},
        {"front": "Voltage", "back": "Electrical pressure that pushes electrons, measured in Volts (V). Like water pressure in a pipe."},
        {"front": "Bulb in Series", "back": "In a series circuit, adding more bulbs increases resistance, so bulbs get dimmer."},
        {"front": "Bulb in Parallel", "back": "In a parallel circuit, each bulb gets full voltage independently, so they stay bright."},
    ]

    if 'flashcard_index' not in st.session_state:
        st.session_state.flashcard_index = 0

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % len(flashcards)

    with col2:
        card = flashcards[st.session_state.flashcard_index]
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background-color: #3498db; border-radius: 10px; color: white;">
            <h3>{card['front']}</h3>
            <hr style="background-color: white;">
            <p>{card['back']}</p>
            <small>Card {st.session_state.flashcard_index + 1} of {len(flashcards)}</small>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("Next ➡️"):
            st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(flashcards)


def show_matching_pairs():
    """Display matching pairs quiz"""
    st.subheader("🎯 Match the Following")

    pairs = [
        ("Series Circuit", "Components in single path"),
        ("Parallel Circuit", "Components in multiple branches"),
        ("Ohm's Law", "V = I × R"),
        ("Current (A)", "Flow of electrons"),
        ("Resistance (Ω)", "Opposition to current flow"),
        ("Voltage (V)", "Electrical pressure"),
        ("Ammeter", "Measures current"),
        ("Power Formula", "P = I²R"),
    ]

    st.write("**Match the terms on the left with their definitions on the right:**")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Terms:**")
        for term, _ in pairs:
            st.write(f"• {term}")

    with col2:
        st.write("**Definitions:**")
        # Shuffle definitions
        definitions = [df for _, df in pairs]
        random.shuffle(definitions)
        for df in definitions:
            st.write(f"• {df}")

    st.info("💡 Try matching them mentally, then click the button to reveal answers!")

    if st.button("Show Answers"):
        st.write("**Correct Matches:**")
        for term, definition in pairs:
            st.write(f"✓ {term} → {definition}")
        st.success("Great! You found all the matches! 🎉")


def show_circuit_quiz():
    """Display circuit multiple choice quiz"""
    st.subheader("❓ Circuit Quiz")

    questions = [
        {
            "q": "In a series circuit with 3 bulbs, what happens if one bulb breaks?",
            "options": ["All bulbs turn off", "The other bulbs stay on", "The circuit gets brighter", "Nothing happens"],
            "answer": "All bulbs turn off",
            "explanation": "In series, if one component breaks, the circuit is broken and no current flows.",
            "difficulty": "easy"
        },
        {
            "q": "Using Ohm's Law (V = IR), if voltage is 6V and resistance is 12Ω, what is the current?",
            "options": ["0.5A", "2A", "18A", "72A"],
            "answer": "0.5A",
            "explanation": "I = V/R = 6V / 12Ω = 0.5A",
            "difficulty": "hard"
        },
        {
            "q": "In a parallel circuit, if you add another bulb, what happens to the total current?",
            "options": ["Decreases", "Increases", "Stays same", "Becomes zero"],
            "answer": "Increases",
            "explanation": "In parallel, each bulb provides a path for current. More branches = more total current.",
            "difficulty": "medium"
        },
        {
            "q": "Which statement about series circuits is TRUE?",
            "options": ["All bulbs are equally bright", "Current is different through each bulb", "Adding bulbs increases brightness", "Voltage divides among components"],
            "answer": "Voltage divides among components",
            "explanation": "In series, voltage drops across each component. That's why bulbs get dimmer with more bulbs.",
            "difficulty": "hard"
        },
        {
            "q": "In a parallel circuit, if one branch is disconnected, what happens?",
            "options": ["Entire circuit stops", "Other branches still work", "Everything gets brighter", "No effect on anything"],
            "answer": "Other branches still work",
            "explanation": "Each branch in parallel is independent. Removing one doesn't affect the others.",
            "difficulty": "easy"
        },
    ]

    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0

    question = questions[st.session_state.quiz_index]
    st.write(f"**Q{st.session_state.quiz_index + 1}: {question['q']}**")
    st.write(f"*Difficulty: {question['difficulty'].title()}*")

    selected = st.radio("Choose your answer:", question['options'], key=f"quiz_{st.session_state.quiz_index}")

    if st.button("Submit Answer"):
        if selected == question['answer']:
            st.success("✅ Correct!")
            st.write(f"**Explanation:** {question['explanation']}")
            st.session_state.quiz_score += 1
        else:
            st.error("❌ Incorrect. Try again!")
            st.write(f"**Correct Answer:** {question['answer']}")
            st.write(f"**Explanation:** {question['explanation']}")

        if st.session_state.quiz_index < len(questions) - 1:
            if st.button("Next Question"):
                st.session_state.quiz_index += 1
                st.rerun()
        else:
            st.info(f"Quiz Complete! Your Score: {st.session_state.quiz_score}/{len(questions)}")
            if st.button("Restart Quiz"):
                st.session_state.quiz_index = 0
                st.session_state.quiz_score = 0
                st.rerun()


def show_lab_dynamic_circuit_builder():
    """Lab 1: Interactive circuit builder with real-time properties"""
    st.subheader("🔌 Lab 1: Dynamic Circuit Builder")

    st.write("**Challenge:** Build both series and parallel circuits. See how properties change in real-time!")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Series Circuit Builder**")
        series_bulbs = st.slider("Number of bulbs in series:", 1, 4, 2, key="series_bulbs")
        series_batteries = st.slider("Number of batteries in series:", 1, 3, 1, key="series_batteries")

        series_config = {
            'type': 'series',
            'bulbs': series_bulbs,
            'batteries': series_batteries,
            'switches': 0,
            'id': 1001
        }
        series_props = CircuitGenerator.calculate_circuit_properties(series_config)

        st.write("**Properties:**")
        st.metric("Voltage", f"{series_props['voltage']}V")
        st.metric("Current", f"{series_props['current']}A")
        st.metric("Brightness per Bulb", f"{series_props['brightness_per_bulb']}%")

    with col2:
        st.write("**Parallel Circuit Builder**")
        parallel_bulbs = st.slider("Number of bulbs in parallel:", 1, 4, 2, key="parallel_bulbs")
        parallel_batteries = st.slider("Number of batteries in parallel:", 1, 3, 1, key="parallel_batteries")

        parallel_config = {
            'type': 'parallel',
            'bulbs': parallel_bulbs,
            'batteries': parallel_batteries,
            'switches': 0,
            'id': 1002
        }
        parallel_props = CircuitGenerator.calculate_circuit_properties(parallel_config)

        st.write("**Properties:**")
        st.metric("Voltage", f"{parallel_props['voltage']}V")
        st.metric("Current", f"{parallel_props['current']}A")
        st.metric("Brightness per Bulb", f"{parallel_props['brightness_per_bulb']}%")

    st.markdown("---")
    st.write("**Key Learning Points:**")
    st.write("""
    ✓ **Series**: More bulbs = more resistance = dimmer bulbs (current decreases)
    ✓ **Parallel**: More bulbs = more current branches = brightness stays high
    ✓ Voltage stays same in parallel; divides in series
    """)

    if st.button("Complete Lab 1 - Earn 75 XP + Circuit Master Badge! 🏆"):
        st.success("🎉 Excellent work! You understand circuit basics!")
        st.balloons()


def show_lab_series_vs_parallel():
    """Lab 2: Side-by-side comparison of series vs parallel"""
    st.subheader("🔋 Lab 2: Series vs Parallel Comparison")

    st.write("**Challenge:** Explore how series and parallel circuits behave differently with the same components!")

    num_bulbs = st.slider("Add the same number of bulbs to both circuits:", 1, 4, 2)
    num_batteries = st.slider("Add the same number of batteries to both:", 1, 3, 1)

    series_config = {'type': 'series', 'bulbs': num_bulbs, 'batteries': num_batteries, 'switches': 0, 'id': 2001}
    parallel_config = {'type': 'parallel', 'bulbs': num_bulbs, 'batteries': num_batteries, 'switches': 0, 'id': 2002}

    series_props = CircuitGenerator.calculate_circuit_properties(series_config)
    parallel_props = CircuitGenerator.calculate_circuit_properties(parallel_config)

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Series Circuit")
        st.write(f"🔌 {num_batteries} Battery × 6V = **{series_props['voltage']}V**")
        st.write(f"💡 {num_bulbs} Bulbs × 12Ω = **{series_props['resistance']}Ω**")
        st.write(f"⚡ Current: **{series_props['current']}A**")
        st.write(f"🌟 Brightness: **{series_props['brightness_per_bulb']}%**")

        brightness_bar = "█" * (series_props['brightness_per_bulb'] // 10) + "░" * (10 - series_props['brightness_per_bulb'] // 10)
        st.write(f"Brightness Visual: {brightness_bar}")

    with col2:
        st.write("### Parallel Circuit")
        st.write(f"🔌 {num_batteries} Battery × 6V = **{parallel_props['voltage']}V**")
        st.write(f"💡 {num_bulbs} Bulbs = **{parallel_props['resistance']:.2f}Ω** total")
        st.write(f"⚡ Current: **{parallel_props['current']}A**")
        st.write(f"🌟 Brightness: **{parallel_props['brightness_per_bulb']}%**")

        brightness_bar = "█" * (parallel_props['brightness_per_bulb'] // 10) + "░" * (10 - parallel_props['brightness_per_bulb'] // 10)
        st.write(f"Brightness Visual: {brightness_bar}")

    st.markdown("---")
    st.write(f"**Observation:** With {num_bulbs} bulbs and {num_batteries} battery/batteries:")
    st.write(f"- **Series**: Total current = **{series_props['current']}A** (less current, dimmer)")
    st.write(f"- **Parallel**: Total current = **{parallel_props['current']}A** (more current, brighter)")
    st.write(f"- **Difference**: Parallel has **{parallel_props['current'] - series_props['current']:.2f}A** more current! ⚡")

    if st.button("Complete Lab 2 - Earn 50 XP! 🏅"):
        st.success("✅ You've mastered series vs parallel comparison!")
        st.info("💡 Remember: Parallel circuits are more practical for homes because each appliance works independently!")


def show_lab_break_the_circuit():
    """Lab 3: Troubleshooting broken circuits"""
    st.subheader("⚡ Lab 3: Break the Circuit Game")

    st.write("**Challenge:** A circuit is broken! Find out what's wrong and fix it.")

    if 'broken_circuit' not in st.session_state:
        # Randomly decide what's broken
        st.session_state.broken_circuit = random.choice(['battery', 'wire', 'switch', 'bulb'])
        st.session_state.circuit_attempts = 0

    st.write("**The Circuit Status:**")

    # Create a scenario
    problem_msg = {
        'battery': "⚠️ The batteries are disconnected (no voltage supplied)",
        'wire': "⚠️ One wire is broken (open circuit at the connection)",
        'switch': "⚠️ The switch is in the OFF position",
        'bulb': "⚠️ One bulb has burned out (broken filament)"
    }

    st.error(problem_msg[st.session_state.broken_circuit])
    st.write(f"Ammeter reading: **0.0A** (no current flowing!)")

    st.write("**What do you think is wrong?**")
    diagnosis = st.radio(
        "Select the problem:",
        ["Battery disconnected", "Wire broken", "Switch OFF", "Bulb burned out"],
        index=["battery", "wire", "switch", "bulb"].index(st.session_state.broken_circuit),
        key=f"diagnosis_{st.session_state.circuit_attempts}"
    )

    if st.button("Check Diagnosis"):
        st.session_state.circuit_attempts += 1

        diagnosis_map = {
            "Battery disconnected": "battery",
            "Wire broken": "wire",
            "Switch OFF": "switch",
            "Bulb burned out": "bulb"
        }

        if diagnosis_map[diagnosis] == st.session_state.broken_circuit:
            st.success("🎉 Correct! You diagnosed the problem!")
            st.write(f"**Solution:** {diagnosis}")
            st.write("✓ Ammeter now reads current flowing through circuit")
            st.write("✓ Bulbs light up! 💡")

            if st.button("Complete Lab 3 - Earn 40 XP + Troubleshooter Badge! 🔧"):
                st.success("⭐ Excellent troubleshooting skills!")
                st.balloons()
        else:
            st.error(f"❌ Not quite. Try again! (Attempt {st.session_state.circuit_attempts})")
            st.info("💡 Hint: Check the ammeter reading (0.0A = no current = broken path)")


def show_lab_voltage_drop_challenge():
    """Lab 4: Voltage drop and Ohm's Law challenge"""
    st.subheader("🎯 Lab 4: Voltage Drop Challenge")

    st.write("**Challenge:** Adjust resistors to achieve target brightness using Ohm's Law!")

    st.write("**Given:** 12V battery, need to light a bulb to exactly **60% brightness**")

    target_brightness = 60
    available_resistance = st.slider("Choose circuit resistance (Ω):", 10, 30, 12, step=2, key="resistance_slider")

    # Calculate current and brightness
    voltage = 12
    current = voltage / available_resistance
    brightness = min(100, int(100 * (current / 1.0)))  # Normalized to 1.0A = 100%

    st.write("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Voltage", f"{voltage}V")

    with col2:
        st.metric("Resistance", f"{available_resistance}Ω")

    with col3:
        st.metric("Current (I=V/R)", f"{current:.3f}A")

    st.write("---")
    st.write(f"**Bulb Brightness: {brightness}%**")

    brightness_bar = "🌟" * (brightness // 10) + "⭐" * (10 - brightness // 10)
    st.write(brightness_bar)

    if brightness == target_brightness:
        st.success(f"🎉 Perfect! You achieved exactly {target_brightness}% brightness!")
        st.write("**How you did it:**")
        st.write(f"✓ Used {available_resistance}Ω resistance")
        st.write(f"✓ Calculated current: I = {voltage}V ÷ {available_resistance}Ω = {current:.3f}A")
        st.write(f"✓ Achieved brightness: {brightness}%")

        if st.button("Complete Lab 4 - Earn 60 XP! 🎖️"):
            st.success("⭐ Mastered Ohm's Law and circuit optimization!")
            st.balloons()
    else:
        difference = abs(brightness - target_brightness)
        if difference <= 5:
            st.warning(f"Almost there! You're {difference}% off target.")
        elif difference <= 10:
            st.info(f"Getting closer! Adjust resistance to get {difference}% closer.")
        else:
            st.info(f"Adjust the slider to change resistance and match {target_brightness}%.")


def show_circuit_interactive_labs():
    """Display all circuit interactive labs"""
    st.subheader("🧪 Interactive Labs - Circuits in Action")

    lab_choice = st.selectbox(
        "Choose a lab:",
        ["📖 Lab Overview", "🔌 Lab 1: Dynamic Circuit Builder", "🔋 Lab 2: Series vs Parallel",
         "⚡ Lab 3: Break the Circuit", "🎯 Lab 4: Voltage Drop Challenge"]
    )

    if lab_choice == "📖 Lab Overview":
        st.write("""
        Welcome to Circuit Labs! In these interactive experiences, you'll:

        **🔌 Lab 1: Dynamic Circuit Builder**
        - Build series and parallel circuits in real-time
        - See how properties change instantly
        - Understand V, I, R, and brightness relationships

        **🔋 Lab 2: Series vs Parallel Comparison**
        - Compare same components in different configurations
        - Visualize current flow and brightness
        - Learn why parallel circuits are used in homes

        **⚡ Lab 3: Break the Circuit**
        - Diagnose what's wrong with broken circuits
        - Practice troubleshooting skills
        - Learn circuit failure modes

        **🎯 Lab 4: Voltage Drop Challenge**
        - Apply Ohm's Law to solve real problems
        - Adjust resistance for target brightness
        - Understand circuit optimization
        """)

    elif "Lab 1" in lab_choice:
        show_lab_dynamic_circuit_builder()
    elif "Lab 2" in lab_choice:
        show_lab_series_vs_parallel()
    elif "Lab 3" in lab_choice:
        show_lab_break_the_circuit()
    elif "Lab 4" in lab_choice:
        show_lab_voltage_drop_challenge()


# ==================== MAIN TAB STRUCTURE ====================

st.header("🔌 Chapter 6: Electric Circuits")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📇 Flashcards",
    "🎯 Matching",
    "❓ Quiz",
    "🧠 Brain Drainer",
    "📊 Progress",
    "🧪 Interactive Labs"
])

with tab1:
    show_flashcards()

with tab2:
    show_matching_pairs()

with tab3:
    show_circuit_quiz()

with tab4:
    st.subheader("🧠 Brain Drainer - PSLE Style Questions")
    st.info("🚧 Brain drainer questions coming soon! Complex circuit problems with trap answers.")
    st.write("Topics: Circuit analysis, Ohm's Law application, Series vs Parallel comparison")

with tab5:
    st.subheader("📊 Your Progress")
    st.info("✓ Flashcards: 8 reviewed")
    st.info("✓ Matching: 8 pairs learned")
    st.info("✓ Quiz: 5 questions completed")
    st.success("Current Mastery: 75%")

with tab6:
    show_circuit_interactive_labs()
