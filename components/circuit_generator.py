"""
Dynamic Circuit Generator for Chapter 6 - Electric Circuits
Generates random circuits, renders them, calculates properties, and creates questions
"""

import random
import streamlit as st
from typing import Dict, List, Tuple

class CircuitGenerator:
    """Generate random circuits and auto-create related questions"""

    # Circuit component properties
    COMPONENT_PROPS = {
        'battery': {'resistance': 0, 'voltage': 6, 'symbol': '⭕'},
        'bulb': {'resistance': 12, 'voltage': 6, 'brightness_base': 50, 'symbol': '💡'},
        'switch': {'resistance': 0, 'voltage': 6, 'symbol': '🔌'},
        'wire': {'resistance': 0, 'voltage': 6, 'symbol': '━'},
        'ammeter': {'resistance': 0, 'voltage': 6, 'symbol': 'A'},
    }

    @staticmethod
    def generate_random_circuit() -> Dict:
        """
        Generate a random valid circuit configuration.

        Returns:
            dict: Circuit configuration with type, bulbs, batteries, switches
        """
        circuit_config = {
            'type': random.choice(['series', 'series', 'series', 'parallel']),  # 75% series, 25% parallel
            'bulbs': random.randint(1, 4),
            'batteries': random.randint(1, 3),
            'switches': random.randint(0, 2),
            'id': random.randint(1000, 9999),
        }

        return circuit_config

    @staticmethod
    def calculate_circuit_properties(circuit_config: Dict) -> Dict:
        """
        Calculate electrical properties of the circuit (Ohm's Law: V = IR, P = I²R).

        Args:
            circuit_config: Circuit configuration dict

        Returns:
            dict: Properties including resistance, current, brightness
        """
        bulbs = circuit_config['bulbs']
        batteries = circuit_config['batteries']
        circuit_type = circuit_config['type']

        # Basic properties
        total_voltage = batteries * 6  # 6V per battery

        if circuit_type == 'series':
            # Series: Total resistance = sum of individual resistances
            bulb_resistance = 12  # Ω per bulb
            total_resistance = bulbs * bulb_resistance
            # Current = Voltage / Resistance (Ohm's Law)
            current = total_voltage / total_resistance if total_resistance > 0 else 0
            # Brightness per bulb decreases with more bulbs in series
            brightness_per_bulb = max(0, 100 * (current / 0.5))  # Normalized to max 100%
        else:  # parallel
            # Parallel: Each bulb gets full voltage
            current = bulbs * (total_voltage / 12)  # Each bulb at 6V = 0.5A
            # Brightness per bulb stays high in parallel
            brightness_per_bulb = 100
            total_resistance = 12 / bulbs  # Total resistance decreases

        properties = {
            'voltage': total_voltage,
            'resistance': total_resistance,
            'current': round(current, 2),
            'brightness_per_bulb': min(100, int(brightness_per_bulb)),
            'total_brightness': min(100, int(brightness_per_bulb)),  # Max brightness capped at 100
            'power_per_bulb': round(current ** 2 * 12, 2),  # P = I²R
        }

        return properties

    @staticmethod
    def generate_circuit_questions(circuit_config: Dict, properties: Dict) -> List[Dict]:
        """
        Auto-generate multiple-choice questions about the circuit.

        Args:
            circuit_config: Circuit configuration
            properties: Calculated circuit properties

        Returns:
            list: Generated MCQ questions about the circuit
        """
        questions = []
        circuit_type = circuit_config['type']
        bulbs = circuit_config['bulbs']
        batteries = circuit_config['batteries']

        # Question 1: Total voltage
        wrong_voltage_1 = batteries * 3
        wrong_voltage_2 = batteries * 12
        q1 = {
            'q': f"What is the total voltage in this {circuit_type} circuit with {batteries} batteries?",
            'options': [f"{properties['voltage']}V", f"{wrong_voltage_1}V", f"{wrong_voltage_2}V", "0V"],
            'answer': f"{properties['voltage']}V",
            'explanation': f"Each battery = 6V. {batteries} batteries × 6V = {properties['voltage']}V",
            'difficulty': 'easy'
        }
        questions.append(q1)

        # Question 2: Series vs Parallel behavior
        if circuit_type == 'series':
            q2 = {
                'q': f"In this SERIES circuit, if we add another bulb, what happens to the brightness?",
                'options': ['Stays the same', 'Gets brighter', 'Gets dimmer', 'Turns off'],
                'answer': 'Gets dimmer',
                'explanation': f"In series, more bulbs = more total resistance = less current = dimmer bulbs",
                'difficulty': 'hard'
            }
        else:  # parallel
            q2 = {
                'q': f"In this PARALLEL circuit, if we add another bulb, what happens to the brightness?",
                'options': ['Stays the same', 'Gets brighter', 'Gets dimmer', 'Turns off'],
                'answer': 'Stays the same',
                'explanation': f"In parallel, each bulb gets the full {properties['voltage']}V, so brightness stays constant",
                'difficulty': 'hard'
            }
        questions.append(q2)

        # Question 3: Current calculation
        q3 = {
            'q': f"Using Ohm's Law (I = V/R), what is the current in this circuit?",
            'options': [f"{properties['current']}A", f"{properties['current'] * 2}A", f"{properties['current'] / 2}A", "0A"],
            'answer': f"{properties['current']}A",
            'explanation': f"I = V/R = {properties['voltage']}V / {properties['resistance']}Ω = {properties['current']}A",
            'difficulty': 'hard'
        }
        questions.append(q3)

        # Question 4: Brightness comparison
        if circuit_type == 'series':
            q4 = {
                'q': f"If we replace this series circuit with a parallel circuit (same bulbs & batteries), what happens?",
                'options': ['Bulbs get brighter', 'Bulbs stay same brightness', 'Circuit breaks', 'Nothing changes'],
                'answer': 'Bulbs get brighter',
                'explanation': f"In parallel, each bulb gets full voltage, so they become much brighter than in series",
                'difficulty': 'hard'
            }
        else:
            q4 = {
                'q': f"If we convert this parallel circuit to series (same bulbs & batteries), what happens?",
                'options': ['Bulbs get brighter', 'Bulbs get dimmer', 'Bulbs stay same', 'They turn off'],
                'answer': 'Bulbs get dimmer',
                'explanation': f"In series, total resistance increases, current decreases, bulbs get dimmer",
                'difficulty': 'hard'
            }
        questions.append(q4)

        # Question 5: Effect of adding battery
        q5 = {
            'q': f"If we add another battery to this circuit, what would happen to bulb brightness?",
            'options': ['Stays the same', 'Gets brighter', 'Gets dimmer', 'Turns off completely'],
            'answer': 'Gets brighter',
            'explanation': f"More batteries = more voltage = more current = brighter bulbs",
            'difficulty': 'medium'
        }
        questions.append(q5)

        return questions

    @staticmethod
    def render_circuit_text(circuit_config: Dict, properties: Dict):
        """
        Render a text-based circuit diagram.

        Args:
            circuit_config: Circuit configuration
            properties: Circuit properties
        """
        circuit_type = circuit_config['type']
        bulbs = circuit_config['bulbs']
        batteries = circuit_config['batteries']

        if circuit_type == 'series':
            diagram = f"""
            **Series Circuit Diagram:**
            ```
            {batteries} Battery(ies) ─ {bulbs} Bulb(s) ─ {circuit_config['switches']} Switch(es)
            └─────────────────────────┘
                   Single Path
            ```
            """
        else:  # parallel
            bulb_branches = " ┬ ".join(['Bulb'] * bulbs)
            diagram = f"""
            **Parallel Circuit Diagram:**
            ```
            Battery ─┬─ Bulb 1 ─┬─ Back to Battery
                     ├─ Bulb 2 ─┤
                     ├─ Bulb ... ┤
                     └─ Bulb {bulbs} ─┘

                   Multiple Paths
            ```
            """

        st.markdown(diagram)

        # Display properties
        st.markdown("**Circuit Properties:**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Voltage", f"{properties['voltage']}V")
        with col2:
            st.metric("Resistance", f"{properties['resistance']}Ω")
        with col3:
            st.metric("Current", f"{properties['current']}A")
        with col4:
            st.metric("Brightness", f"{properties['brightness_per_bulb']}%")

    @staticmethod
    def display_full_simulator(circuit_config: Dict = None):
        """
        Display a complete circuit simulator with generation, rendering, and questions.

        Args:
            circuit_config: Optional pre-generated circuit config. If None, generates random.
        """
        # Generate circuit if not provided
        if circuit_config is None:
            circuit_config = CircuitGenerator.generate_random_circuit()

        # Calculate properties
        properties = CircuitGenerator.calculate_circuit_properties(circuit_config)

        # Render circuit
        CircuitGenerator.render_circuit_text(circuit_config, properties)

        st.markdown("---")

        # Generate questions
        st.subheader("🧠 Test Your Understanding:")
        questions = CircuitGenerator.generate_circuit_questions(circuit_config, properties)

        # Display questions (preview)
        for idx, q in enumerate(questions[:2], 1):
            with st.container(border=True):
                st.write(f"**Q{idx}: {q['q']}**")
                st.write(f"*Difficulty: {q['difficulty'].title()}*")

        st.info(f"💡 {len(questions)} auto-generated questions about this circuit are ready to test your knowledge!")


# Example usage function
def example_circuit_simulator():
    """Display example circuit simulator (for testing)"""
    st.write("## Dynamic Circuit Simulator Example")

    if st.button("Generate New Random Circuit"):
        st.session_state.current_circuit = CircuitGenerator.generate_random_circuit()

    if 'current_circuit' not in st.session_state:
        st.session_state.current_circuit = CircuitGenerator.generate_random_circuit()

    CircuitGenerator.display_full_simulator(st.session_state.current_circuit)
