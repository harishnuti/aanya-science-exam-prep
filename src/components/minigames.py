"""Mini-games for Phase 2 - drag-drop, sequencing, and timed challenges"""

import streamlit as st
import random
import time

class DragDropGame:
    """Template for drag-and-drop games"""

    @staticmethod
    def create_sorter_game(items, categories, game_name):
        """Create a categorization game where items are dragged into categories"""
        st.subheader(f"🎮 {game_name}")

        # Initialize game state
        if 'sorter_state' not in st.session_state:
            st.session_state.sorter_state = {
                'items': items.copy(),
                'categories': {cat: [] for cat in categories},
                'completed': False,
                'score': 0
            }

        # Display categories as dropzones
        cols = st.columns(len(categories))
        for idx, category in enumerate(categories):
            with cols[idx]:
                st.write(f"**{category}**")
                items_in_cat = st.session_state.sorter_state['categories'].get(category, [])
                if items_in_cat:
                    for item in items_in_cat:
                        st.info(f"✓ {item}")
                else:
                    st.write("_(Drop items here)_")

        # Display remaining items to sort
        st.write("**Items to Sort:**")
        remaining_items = [item for item in items if item not in [i for cat_items in st.session_state.sorter_state['categories'].values() for i in cat_items]]

        if remaining_items:
            for item in remaining_items:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(item)
                with col2:
                    selected_cat = st.selectbox(f"Category for {item}", categories, key=f"item_{item}")
                    if st.button("Place", key=f"place_{item}"):
                        if selected_cat not in st.session_state.sorter_state['categories']:
                            st.session_state.sorter_state['categories'][selected_cat] = []
                        st.session_state.sorter_state['categories'][selected_cat].append(item)
                        st.rerun()

        # Check if completed
        if not remaining_items and not st.session_state.sorter_state['completed']:
            st.success("✅ All items sorted! Check your answers.")
            st.session_state.sorter_state['completed'] = True

        return st.session_state.sorter_state['categories']

class SequencingGame:
    """Template for sequencing/ordering games"""

    @staticmethod
    def create_sequence_game(items, correct_order, game_name):
        """Create a game where items must be ordered correctly"""
        st.subheader(f"🎮 {game_name}")

        if 'sequence_state' not in st.session_state:
            shuffled = items.copy()
            random.shuffle(shuffled)
            st.session_state.sequence_state = {
                'items': shuffled,
                'user_order': [],
                'completed': False,
                'correct': False
            }

        st.write("**Arrange items in the correct order:**")

        # Display items with numbered buttons to order them
        cols = st.columns(len(st.session_state.sequence_state['items']))
        for idx, item in enumerate(st.session_state.sequence_state['items']):
            with cols[idx]:
                if st.button(f"{idx+1}. {item}", key=f"seq_item_{idx}_{item}"):
                    if item not in st.session_state.sequence_state['user_order']:
                        st.session_state.sequence_state['user_order'].append(item)
                        st.rerun()

        # Display user's current order
        st.write("**Your Order:**")
        if st.session_state.sequence_state['user_order']:
            for idx, item in enumerate(st.session_state.sequence_state['user_order'], 1):
                st.write(f"{idx}. {item}")

            # Check button
            if len(st.session_state.sequence_state['user_order']) == len(items):
                if st.button("Check Answer", key="check_sequence"):
                    is_correct = st.session_state.sequence_state['user_order'] == correct_order
                    if is_correct:
                        st.success("✅ Perfect sequence! You got it right!")
                        st.session_state.sequence_state['correct'] = True
                    else:
                        st.error("❌ Incorrect sequence. Try again!")
                        st.session_state.sequence_state['user_order'] = []
                        st.rerun()

        return st.session_state.sequence_state['correct']

class TimedChallenge:
    """Template for timed challenge games"""

    @staticmethod
    def create_timed_quiz(questions, time_limit=45):
        """Create a timed quiz challenge"""
        st.subheader("⏱️ Timed Challenge")
        st.write(f"Answer as many questions as you can in {time_limit} seconds!")

        if 'timed_challenge' not in st.session_state:
            st.session_state.timed_challenge = {
                'start_time': time.time(),
                'current_question': 0,
                'score': 0,
                'completed': False
            }

        # Calculate remaining time
        elapsed = time.time() - st.session_state.timed_challenge['start_time']
        remaining = max(0, time_limit - elapsed)

        # Display timer
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.metric("Time Remaining", f"{int(remaining)}s")
        with col2:
            st.metric("Score", st.session_state.timed_challenge['score'])
        with col3:
            st.metric("Question", f"{st.session_state.timed_challenge['current_question'] + 1}/{len(questions)}")

        if remaining <= 0:
            st.success(f"⏰ Time's up! Final Score: {st.session_state.timed_challenge['score']}/{len(questions)}")
            st.session_state.timed_challenge['completed'] = True
            return st.session_state.timed_challenge['score']

        # Display current question
        q_idx = st.session_state.timed_challenge['current_question']
        if q_idx < len(questions):
            q = questions[q_idx]
            st.write(f"**{q['question']}**")

            # Radio buttons for options
            answer = st.radio("Select an answer:", q['options'], key=f"timed_q_{q_idx}")

            if st.button("Next", key=f"next_timed_{q_idx}"):
                if answer == q['answer']:
                    st.session_state.timed_challenge['score'] += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. The answer is: {q['answer']}")

                st.session_state.timed_challenge['current_question'] += 1
                time.sleep(1)  # Brief pause before next question
                st.rerun()

        return None

class MatchingGame:
    """Template for enhanced matching games"""

    @staticmethod
    def create_matching_game(pairs, game_name):
        """Create a matching game with visual feedback"""
        st.subheader(f"🎮 {game_name}")

        if 'matching_state' not in st.session_state:
            shuffled_values = [pair[1] for pair in pairs]
            random.shuffle(shuffled_values)
            st.session_state.matching_state = {
                'pairs': pairs,
                'shuffled': shuffled_values,
                'matches': {},
                'completed': False
            }

        # Display pairs with dropdown for matching
        st.write("**Match each term with its definition:**")

        for term, correct_match in st.session_state.matching_state['pairs']:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write(f"**{term}**")
            with col2:
                selected = st.selectbox(
                    f"Match for {term}",
                    st.session_state.matching_state['shuffled'],
                    key=f"match_{term}"
                )
                st.session_state.matching_state['matches'][term] = selected

        # Check button
        if st.button("Check Matches", key="check_matches"):
            all_correct = all(
                st.session_state.matching_state['matches'].get(term) == correct
                for term, correct in st.session_state.matching_state['pairs']
            )

            if all_correct:
                st.success("✅ Perfect! All matches are correct!")
                st.session_state.matching_state['completed'] = True
            else:
                st.error("❌ Some matches are incorrect. Try again!")

        return st.session_state.matching_state['completed']

class PuzzleGame:
    """Template for puzzle/building games"""

    @staticmethod
    def create_circuit_builder(components, game_name):
        """Create a simple circuit builder game"""
        st.subheader(f"🎮 {game_name}")

        if 'circuit_state' not in st.session_state:
            st.session_state.circuit_state = {
                'selected_components': [],
                'completed': False,
                'target_brightness': 100
            }

        st.write("**Drag components to build the circuit:**")

        # Display available components
        st.write("Available Components:")
        cols = st.columns(len(components))
        for idx, comp in enumerate(components):
            with cols[idx]:
                if st.button(f"+ {comp['name']}", key=f"add_comp_{comp['name']}"):
                    st.session_state.circuit_state['selected_components'].append(comp)
                    st.rerun()

        # Display selected components
        st.write("**Your Circuit:**")
        if st.session_state.circuit_state['selected_components']:
            for idx, comp in enumerate(st.session_state.circuit_state['selected_components']):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"→ {comp['name']} (Resistance: {comp.get('resistance', 1)}Ω)")
                with col2:
                    if st.button("Remove", key=f"remove_{idx}_{comp['name']}"):
                        st.session_state.circuit_state['selected_components'].pop(idx)
                        st.rerun()

            # Calculate circuit properties
            total_resistance = sum(c.get('resistance', 1) for c in st.session_state.circuit_state['selected_components'])
            voltage = 6  # Example voltage
            brightness = max(0, min(100, voltage / total_resistance * 10))

            st.metric("Brightness", f"{int(brightness)}%")
            st.progress(brightness / 100)

            if brightness >= st.session_state.circuit_state['target_brightness']:
                st.success("✅ Circuit brightness target reached!")
                st.session_state.circuit_state['completed'] = True

        return st.session_state.circuit_state['completed']

def display_minigame_menu(chapter):
    """Display available mini-games for a chapter"""
    games = {
        'Ch1_Reproduction': {
            'name': '🌱 Plant the Seed',
            'description': 'Arrange plant life stages in order',
            'xp_reward': 30
        },
        'Ch2_Water': {
            'name': '💧 State Sorter',
            'description': 'Categorize water states correctly',
            'xp_reward': 30
        },
        'Ch3_Plant': {
            'name': '🚀 Transport Race',
            'description': 'Guide water and food through plant systems',
            'xp_reward': 40
        },
        'Ch4_Human': {
            'name': '❤️ Body Match Pro',
            'description': 'Match organs to their systems',
            'xp_reward': 30
        },
        'Ch5_Electrical': {
            'name': '⚡ Circuit Constructor',
            'description': 'Build working circuits',
            'xp_reward': 40
        },
        'Ch6_Circuits': {
            'name': '💡 Light It Up',
            'description': 'Achieve target brightness with components',
            'xp_reward': 50
        },
    }

    if chapter in games:
        game = games[chapter]
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.subheader(game['name'])
        with col2:
            st.write(game['description'])
        with col3:
            st.metric("XP Reward", game['xp_reward'])
        return game
    return None
