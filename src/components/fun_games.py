"""
Fun, Interactive Games for Children (P5 Students)
Games designed to be engaging, educational, and age-appropriate
"""

import streamlit as st
import random
import time


class PlantGrowthGame:
    """Ch 1: Interactive plant growth game - watch your plant grow"""

    @staticmethod
    def play():
        """Plant growth progression game"""
        st.markdown("""
        <style>
        .game-title { font-size: 2em; text-align: center; }
        .plant { font-size: 3em; text-align: center; }
        .score { font-size: 1.5em; text-align: center; color: #22C55E; }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<div class='game-title'>🌱 Plant Growth Challenge</div>", unsafe_allow_html=True)
        st.write("Help your plant grow! Click the water button and give it sunlight to reach full growth!")

        # Game state
        game_key = "plant_game"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'growth': 0,  # 0-100%
                'water_count': 0,
                'sun_count': 0,
                'completed': False
            }

        state = st.session_state[game_key]

        # Display plant growth stages
        stages = ["🌰", "🌱", "🌿", "🌳", "🌲", "🎉 FULLY GROWN!"]
        current_stage = min(int(state['growth'] / 20), 5)

        col1, col2, col3 = st.columns(3)
        with col2:
            st.markdown(f"<div class='plant'>{stages[current_stage]}</div>", unsafe_allow_html=True)
            progress_value = min(state['growth'] / 100, 1.0)
            display_growth = min(state['growth'], 100)
            st.progress(progress_value, text=f"Growth: {display_growth}%")

        st.write("---")

        # Game buttons
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("💧 Water (30% growth)", key="water_btn", use_container_width=True):
                if state['growth'] < 100:
                    state['growth'] += 30
                    state['water_count'] += 1
                    st.rerun()

        with col2:
            if st.button("☀️ Sunlight (20% growth)", key="sun_btn", use_container_width=True):
                if state['growth'] < 100:
                    state['growth'] += 20
                    state['sun_count'] += 1
                    st.rerun()

        with col3:
            if st.button("🌍 Nutrients (10% growth)", key="nutrients_btn", use_container_width=True):
                if state['growth'] < 100:
                    state['growth'] += 10
                    st.rerun()

        st.write("---")

        # Cap growth at 100%
        if state['growth'] >= 100 and not state['completed']:
            state['growth'] = 100
            state['completed'] = True
            st.balloons()
            st.success("🎉 Your plant is fully grown! Congratulations!")
            st.write(f"You used: {state['water_count']} water, {state['sun_count']} sunlight clicks")
            return True

        return state['completed']


class WaterCycleRace:
    """Ch 2: Water droplet race through the water cycle"""

    @staticmethod
    def play():
        st.markdown("<h2 style='text-align: center;'>💧 Water Cycle Race</h2>", unsafe_allow_html=True)
        st.write("Help the water droplet complete its journey through the water cycle! Click the stages in order.")

        game_key = "water_race"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'current_stage': 0,
                'completed': False,
                'time': time.time()
            }

        stages = [
            ("☀️ EVAPORATION", "Sun heats water in ocean"),
            ("⬆️ RISING", "Water vapor rises into atmosphere"),
            ("❄️ CONDENSATION", "Cool air cools water vapor into droplets"),
            ("☁️ CLOUD FORMATION", "Droplets form clouds"),
            ("🌧️ PRECIPITATION", "Water falls as rain"),
            ("🌊 ACCUMULATION", "Water returns to ocean")
        ]

        state = st.session_state[game_key]

        # Display progress
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.progress((state['current_stage'] + 1) / len(stages),
                       text=f"Stage {state['current_stage'] + 1}/{len(stages)}")

        # Display current stage
        emoji, description = stages[state['current_stage']]
        st.markdown(f"<h3 style='text-align: center; color: #06B6D4;'>{emoji}</h3>", unsafe_allow_html=True)
        st.write(f"**{description}**")

        # Action button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("➡️ Move Forward", key="cycle_btn", use_container_width=True, type="primary"):
                state['current_stage'] += 1
                if state['current_stage'] >= len(stages):
                    state['completed'] = True
                    elapsed = round(time.time() - state['time'], 1)
                    st.balloons()
                    st.success(f"🎉 Water cycle complete in {elapsed} seconds! Great job!")
                    return True
                st.rerun()

        return state['completed']


class PlantPartBuilder:
    """Ch 3: Build a plant by identifying parts"""

    @staticmethod
    def play():
        st.markdown("<h2 style='text-align: center;'>🌿 Plant Part Builder</h2>", unsafe_allow_html=True)
        st.write("Match the plant parts with their functions. Get them all right to complete your plant!")

        parts = {
            "🌱 Roots": "Absorbs water and nutrients",
            "🌿 Stem": "Supports leaves and carries water",
            "🍃 Leaves": "Makes food using sunlight",
            "🌸 Flower": "Makes seeds and attracts bees",
            "🌾 Seeds": "Grows into new plants"
        }

        game_key = "plant_builder"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'correct': 0,
                'total': len(parts),
                'answered': set()
            }

        state = st.session_state[game_key]

        # Progress
        st.progress(state['correct'] / state['total'],
                   text=f"Score: {state['correct']}/{state['total']}")

        # Quiz
        for part, function in parts.items():
            if part not in state['answered']:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.write(f"**{part}**")
                with col2:
                    selected = st.selectbox(f"Function of {part}",
                                           ["Select..."] + list(parts.values()),
                                           key=f"part_{part}")
                    if selected == function:
                        st.success(f"✅ Correct!")
                        state['answered'].add(part)
                        state['correct'] += 1

        if state['correct'] == state['total']:
            st.balloons()
            st.success("🎉 Perfect! You've built a complete plant!")
            return True

        return False


class HeartbeatGame:
    """Ch 4: Heartbeat rhythm game - tap to the beat"""

    @staticmethod
    def play():
        st.markdown("<h2 style='text-align: center;'>❤️ Heartbeat Rhythm</h2>", unsafe_allow_html=True)
        st.write("Click the heart to match the heartbeat rhythm! Tap: LUB-DUB... LUB-DUB...")

        game_key = "heartbeat"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'score': 0,
                'rhythm': [1, 1, 0],  # LUB-DUB-pause pattern
                'sequence': [],
                'target_beats': 5
            }

        state = st.session_state[game_key]

        st.progress(state['score'] / state['target_beats'],
                   text=f"Beats: {state['score']}/{state['target_beats']}")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("❤️", key="heart_btn", use_container_width=True):
                state['score'] += 1
                if state['score'] >= state['target_beats']:
                    st.balloons()
                    st.success("🎉 Perfect heartbeat rhythm! Your heart is healthy!")
                    return True
                st.rerun()

        # Rhythm display
        st.write("Pattern: **LUB** - **DUB** - *(pause)*")
        st.caption(f"Current rhythm: {state['score']} beats collected")

        return False


class CircuitBuilder:
    """Ch 5: Build a working electrical circuit"""

    @staticmethod
    def play():
        st.markdown("<h2 style='text-align: center;'>⚡ Circuit Builder</h2>", unsafe_allow_html=True)
        st.write("Build a circuit by selecting components. Make the light bulb shine!")

        components = ["Battery 🔋", "Wire 〰️", "Bulb 💡", "Switch 🔌"]

        game_key = "circuit"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'selected': [],
                'completed': False
            }

        state = st.session_state[game_key]

        st.write("**Components needed:** Battery → Wire → Bulb → Switch")
        st.write("**Your circuit:**")

        # Display selected components
        if state['selected']:
            circuit_display = " → ".join(state['selected'])
            st.markdown(f"<h3 style='text-align: center;'>{circuit_display}</h3>", unsafe_allow_html=True)
        else:
            st.write("Click components below to build your circuit...")

        # Component buttons
        cols = st.columns(len(components))
        for idx, component in enumerate(components):
            with cols[idx]:
                if st.button(component, key=f"comp_{component}", use_container_width=True):
                    state['selected'].append(component)
                    st.rerun()

        # Check circuit
        if state['selected']:
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("✓ Test Circuit", key="test_circuit", use_container_width=True):
                    correct_order = ["Battery 🔋", "Wire 〰️", "Bulb 💡", "Switch 🔌"]
                    if state['selected'] == correct_order:
                        st.balloons()
                        st.success("💡 SUCCESS! Your circuit works! The light is on!")
                        state['completed'] = True
                        return True
                    else:
                        st.error("⚠️ Circuit not complete. Check the order!")

            with col3:
                if st.button("Reset", key="reset_circuit", use_container_width=True):
                    state['selected'] = []
                    st.rerun()

        return state['completed']


class BrainQuiz:
    """Ch 6: Quick brain quiz game"""

    @staticmethod
    def play():
        st.markdown("<h2 style='text-align: center;'>🧠 Brain Teaser Quiz</h2>", unsafe_allow_html=True)
        st.write("Test your knowledge with quick electricity questions!")

        questions = [
            {
                "q": "What flows through a circuit?",
                "a": "Electric current",
                "opts": ["Electric current", "Water", "Air", "Light"]
            },
            {
                "q": "What stops electricity flow?",
                "a": "A break in the circuit",
                "opts": ["A break in the circuit", "A battery", "A wire", "A light"]
            },
            {
                "q": "What provides power to a circuit?",
                "a": "Battery",
                "opts": ["Wire", "Switch", "Battery", "Bulb"]
            }
        ]

        game_key = "brain_quiz"
        if game_key not in st.session_state:
            st.session_state[game_key] = {
                'score': 0,
                'current': 0,
                'completed': False
            }

        state = st.session_state[game_key]

        if state['current'] >= len(questions):
            st.balloons()
            st.success(f"🎉 Quiz Complete! Score: {state['score']}/{len(questions)}")
            return True

        # Display current question
        q = questions[state['current']]
        st.progress(state['current'] / len(questions),
                   text=f"Q{state['current'] + 1}/{len(questions)}")
        st.write(f"**{q['q']}**")

        answer = st.radio("Choose your answer:", q['opts'], key=f"q_{state['current']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✓ Submit", key="submit_q", use_container_width=True):
                if answer == q['a']:
                    st.success("✅ Correct!")
                    state['score'] += 1
                else:
                    st.error(f"❌ Wrong! Answer: {q['a']}")
                time.sleep(1)
                state['current'] += 1
                st.rerun()

        return False


def play_game_for_chapter(chapter_name):
    """Route to appropriate game based on chapter"""
    if "Ch 1" in chapter_name or "Reproduction" in chapter_name:
        return PlantGrowthGame.play()
    elif "Ch 2" in chapter_name or "Water" in chapter_name:
        return WaterCycleRace.play()
    elif "Ch 3" in chapter_name or "Plant" in chapter_name:
        return PlantPartBuilder.play()
    elif "Ch 4" in chapter_name or "Human" in chapter_name:
        return HeartbeatGame.play()
    elif "Ch 5" in chapter_name or "Electrical" in chapter_name:
        return CircuitBuilder.play()
    elif "Ch 6" in chapter_name or "Circuit" in chapter_name:
        return BrainQuiz.play()
    else:
        st.warning("Game not available for this chapter")
        return False
