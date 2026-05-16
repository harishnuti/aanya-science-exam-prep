"""Chapter 1: Reproduction in Animals & Plants - Phase 2 Enhanced Version"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.animations import AnimationStyles, MalteseDogFeedback, TransitionAnimations, ParticleEffects
from components.gamification import XPSystem, AchievementBadge
from components.brain_drainers import get_brain_drainer_questions, display_brain_drainer_question
from components.minigames import DragDropGame, SequencingGame, MatchingGame
from utils.state_manager import StateManager

# Chapter data
FLASHCARDS = [
    {'concept': 'Pollination', 'definition': 'Transfer of pollen from the stamen to the stigma of a flower'},
    {'concept': 'Fertilization', 'definition': 'Fusion of the male and female gametes to form a zygote'},
    {'concept': 'Seed Dispersal', 'definition': 'Spreading of seeds away from the parent plant'},
    {'concept': 'Germination', 'definition': 'Growth of a seed into a young plant'},
    {'concept': 'Twin Embryos', 'definition': 'When a single seed contains two embryos, producing identical twins'},
    {'concept': 'Reproduction', 'definition': 'Process of producing new organisms'},
    {'concept': 'Sexual Reproduction', 'definition': 'Reproduction requiring male and female gametes'},
    {'concept': 'Asexual Reproduction', 'definition': 'Reproduction without the need for a partner'},
    {'concept': 'Gametes', 'definition': 'Sex cells (sperm and egg)'},
    {'concept': 'Zygote', 'definition': 'Fertilized egg cell that develops into an organism'},
]

MATCHING_PAIRS = [
    ('Bee', 'Transfers pollen between flowers'),
    ('Wind', 'Carries pollen and seeds'),
    ('Water', 'Disperses aquatic seeds'),
    ('Animal', 'Eats fruit and spreads seeds'),
    ('Stamen', 'Male part of flower'),
    ('Stigma', 'Female part of flower'),
    ('Seed Coat', 'Protects the embryo'),
    ('Cotyledon', 'Stores food for growing seed'),
]

MCQ_QUESTIONS = [
    {
        'q': 'What is the role of a bee in flower pollination?',
        'options': ['It eats the nectar', 'It transfers pollen between flowers', 'It waters the plant', 'It protects seeds'],
        'answer': 'It transfers pollen between flowers',
        'explanation': 'Bees collect nectar and pollen, and while doing so, transfer pollen between flowers.'
    },
    {
        'q': 'Which part of the flower contains the ovules?',
        'options': ['Stamen', 'Stigma', 'Ovary', 'Sepal'],
        'answer': 'Ovary',
        'explanation': 'The ovary is the female part of the flower that contains ovules, which develop into seeds.'
    },
    {
        'q': 'What happens after fertilization in a flower?',
        'options': ['Pollination occurs', 'A seed develops', 'The flower dies', 'The petal falls'],
        'answer': 'A seed develops',
        'explanation': 'After fertilization, the ovule develops into a seed containing an embryo and stored food.'
    },
    {
        'q': 'How do coconut seeds travel to new locations?',
        'options': ['By wind', 'By water', 'By animals', 'By insects'],
        'answer': 'By water',
        'explanation': 'Coconut seeds have a thick, water-resistant coat and float on ocean currents.'
    },
    {
        'q': 'What is asexual reproduction?',
        'options': ['Reproduction with two parents', 'Reproduction without a partner', 'Reproduction with gametes', 'Reproduction by seeds'],
        'answer': 'Reproduction without a partner',
        'explanation': 'Asexual reproduction creates genetically identical offspring from one parent (like from runners or bulbs).'
    },
]

def show_chapter():
    """Main chapter display function"""
    st.header("🌱 Chapter 1: Reproduction in Animals & Plants")

    # Difficulty mode selector
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Master the concept of reproduction across the plant and animal kingdoms!")
    with col2:
        difficulty = st.selectbox("Difficulty:", ['beginner', 'intermediate', 'advanced'], key='ch1_difficulty')

    st.markdown("---")

    # Tab interface
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📚 Flashcards", "🎯 Matching", "❓ Quiz", "🎮 Mini-Game", "🧪 Interactive Labs", "🧠 Brain Drainer"])

    with tab1:
        show_flashcards(difficulty)

    with tab2:
        show_matching_game()

    with tab3:
        show_quiz(difficulty)

    with tab4:
        show_minigame()

    with tab5:
        show_interactive_labs()

    with tab6:
        show_brain_drainer()

def show_flashcards(difficulty):
    """Display flashcard learning interface"""
    st.subheader("📚 Flashcards: Learning Concepts")

    if 'flashcard_index' not in st.session_state:
        st.session_state.flashcard_index = 0

    cards_to_show = FLASHCARDS[:5] if difficulty == 'beginner' else FLASHCARDS[:8] if difficulty == 'intermediate' else FLASHCARDS

    current_card = cards_to_show[st.session_state.flashcard_index]

    # Flashcard display with animation
    st.markdown(f"""
    <div class="flip-card">
        <div class="flip-card-inner" id="flipCard">
            <div class="flip-card-front">
                <h2 style="color: white;">{current_card['concept']}</h2>
            </div>
            <div class="flip-card-back">
                <p style="color: white; font-size: 18px;">{current_card['definition']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("*Click the card to flip it! (In interactive mode)*")

    # Navigation
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("⏮️ First", key="first_card"):
            st.session_state.flashcard_index = 0
            st.rerun()
    with col2:
        if st.button("⬅️ Previous", key="prev_card"):
            st.session_state.flashcard_index = max(0, st.session_state.flashcard_index - 1)
            st.rerun()
    with col3:
        st.metric("Card", f"{st.session_state.flashcard_index + 1}/{len(cards_to_show)}")
    with col4:
        if st.button("Next ➡️", key="next_card"):
            st.session_state.flashcard_index = min(len(cards_to_show) - 1, st.session_state.flashcard_index + 1)
            st.rerun()

    # Progress indicator
    progress = (st.session_state.flashcard_index + 1) / len(cards_to_show)
    st.progress(progress)

    if st.button("✅ Mark as Learned", key="learned_flashcards"):
        StateManager.init_user_state()['chapter_progress']['Ch1_Reproduction']['flashcards_learned'] = len(cards_to_show)
        st.success("Great! Move on to the matching game to reinforce your learning!")

def show_matching_game():
    """Display matching game"""
    st.subheader("🎯 Matching Game: Terms & Definitions")
    st.write("Match each term with its correct definition!")

    completed = MatchingGame.create_matching_game(MATCHING_PAIRS, "Reproduction Matching")

    if completed:
        st.success("✅ Excellent matching! You've earned 25 XP!")
        StateManager.init_user_state()['chapter_progress']['Ch1_Reproduction']['quizzes_completed'] += 1
        XPSystem.award_xp(25, "matching game")

def show_quiz(difficulty):
    """Display MCQ quiz"""
    st.subheader("❓ Quiz: Test Your Knowledge")

    if difficulty == 'beginner':
        quiz_questions = MCQ_QUESTIONS[:2]
    elif difficulty == 'intermediate':
        quiz_questions = MCQ_QUESTIONS[:3]
    else:
        quiz_questions = MCQ_QUESTIONS

    correct_count = 0

    for idx, question in enumerate(quiz_questions, 1):
        with st.container(border=True):
            st.write(f"**Question {idx}/{len(quiz_questions)}**")
            st.write(question['q'])

            answer = st.radio(
                "Select your answer:",
                question['options'],
                key=f"ch1_q{idx}",
                label_visibility="collapsed"
            )

            if st.button("Check", key=f"check_ch1_q{idx}"):
                if answer == question['answer']:
                    st.success("✅ Correct!")
                    st.info(f"💡 {question['explanation']}")
                    correct_count += 1
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {question['answer']}")
                    st.warning(f"📖 {question['explanation']}")

    # Summary
    if len(quiz_questions) > 0:
        st.markdown("---")
        percentage = (correct_count / len(quiz_questions)) * 100 if correct_count > 0 else 0
        st.metric("Quiz Score", f"{correct_count}/{len(quiz_questions)} ({percentage:.0f}%)")

        if correct_count >= len(quiz_questions) * 0.7:
            st.success("Great job! You can try the Brain Drainer for a harder challenge!")

def show_minigame():
    """Display mini-game section"""
    st.subheader("🎮 Mini-Game: Plant the Seed")
    st.write("Arrange the stages of plant growth in the correct order!")

    stages = [
        'Germination: Seed sprouts',
        'Growth: Plant develops leaves',
        'Photosynthesis: Plant makes food',
        'Flowering: Plant produces flowers',
        'Pollination: Pollen transferred',
        'Fertilization: Seed development begins'
    ]

    correct_order = stages.copy()

    is_correct = SequencingGame.create_sequence_game(stages, correct_order, "Plant Life Cycle Sequencing")

    if is_correct:
        st.success("✅ Perfect! You've earned 40 XP!")
        XPSystem.award_xp(40, "mini-game completion")

def show_interactive_labs():
    """Display Interactive Labs with simulators and challenges"""
    st.subheader("🧪 Interactive Labs: Learn by Doing!")

    # Lab selector
    lab = st.selectbox(
        "Choose a lab to explore:",
        [
            "🌸 Lab 1: Flower Pollination Simulator",
            "🌱 Lab 2: Seed Germination Timeline",
            "👯 Lab 3: Twin Formation Visualizer"
        ]
    )

    st.markdown("---")

    if "🌸 Lab 1" in lab:
        show_lab_pollination()
    elif "🌱 Lab 2" in lab:
        show_lab_germination()
    elif "👯 Lab 3" in lab:
        show_lab_twins()

def show_lab_pollination():
    """Interactive Lab 1: Flower Pollination Simulator"""
    st.write("### 🌸 Flower Pollination Simulator")
    st.write("Learn how bees help plants reproduce by transferring pollen!")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        **How Pollination Works:**

        1️⃣ **Pollen Production** - The flower's anther (male part) produces yellow pollen grains
        2️⃣ **Bee Landing** - A bee lands on the flower to collect nectar
        3️⃣ **Pollen Sticks** - Pollen grains stick to the bee's fuzzy body
        4️⃣ **Bee Travels** - The bee flies to another flower
        5️⃣ **Pollen Transfer** - Pollen rubs off on the stigma (female part)
        6️⃣ **Fertilization** - A pollen tube grows down to the ovule, allowing fertilization

        **Challenge:** Click the buttons below to simulate the pollination process!
        """)

    with col2:
        st.metric("Pollen Collected", "0", "grains")

    # Interactive challenge
    st.markdown("---")

    if 'pollination_stage' not in st.session_state:
        st.session_state.pollination_stage = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌸 Step 1: Flower", key="poll_step1"):
            st.session_state.pollination_stage = 1
    with col2:
        if st.button("🐝 Step 2: Bee Lands", key="poll_step2"):
            st.session_state.pollination_stage = 2
    with col3:
        if st.button("✈️ Step 3: Bee Travels", key="poll_step3"):
            st.session_state.pollination_stage = 3

    # Show current stage
    if st.session_state.pollination_stage >= 1:
        st.success("✅ Step 1: Pollen produced in anther 🟡")
    if st.session_state.pollination_stage >= 2:
        st.success("✅ Step 2: Bee collects pollen 🐝")
    if st.session_state.pollination_stage >= 3:
        st.success("✅ Step 3: Pollen transferred to stigma ✨")

        if st.button("Complete Lab: Pollinator Expert 🏆", key="complete_poll"):
            st.success("🎉 Congratulations! You've earned 50 XP and the 'Pollinator Expert' badge!")
            XPSystem.award_xp(50, "interactive lab completion")

def show_lab_germination():
    """Interactive Lab 2: Seed Germination Timeline"""
    st.write("### 🌱 Seed Germination Timeline")
    st.write("Follow a seed's journey from dormancy to a growing plant!")

    st.markdown("""
    **The Magic of Germination (WOW):**

    Seeds need three things to germinate:
    - 💧 **Water** - Activates the seed's growth machinery
    - 💨 **Oxygen** - Needed for respiration and energy
    - 🌡️ **Warmth** - Provides the right conditions for growth
    """)

    st.markdown("---")

    # Timeline visualization
    timeline_data = {
        "Day 1": "Seed soaks in water and absorbs moisture",
        "Day 3": "Root emerges downward to find water",
        "Day 5": "Shoot emerges upward toward sunlight",
        "Day 10": "First leaves appear (seed leaves)",
        "Day 20": "True leaves develop and plant grows taller"
    }

    for day, event in timeline_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"**{day}**")
        with col2:
            st.info(event)

    st.markdown("---")

    # Interactive challenge
    if st.button("Complete Lab: Seed Scientist 🌱", key="complete_germ"):
        st.success("🎉 Congratulations! You've earned 40 XP and the 'Seed Scientist' badge!")
        XPSystem.award_xp(40, "interactive lab completion")

    st.write("**Key Learning:** Without WOW (Water, Oxygen, Warmth), seeds remain dormant and won't grow!")

def show_lab_twins():
    """Interactive Lab 3: Twin Formation Visualizer"""
    st.write("### 👯 Twin Formation Visualizer")
    st.write("Discover the difference between identical and fraternal twins!")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Identical Twins (Monozygotic)**

        1️⃣ **One** egg + **One** sperm fuse

        2️⃣ The fertilized egg **splits into two** after fertilization

        3️⃣ Result: **Two genetically identical babies**

        🧬 DNA Match: **100%** (exact clones!)

        👥 Always same sex

        ✨ About 1 in 300 births
        """)

    with col2:
        st.markdown("""
        **Fraternal Twins (Dizygotic)**

        1️⃣ **Two** eggs + **Two** sperm fuse

        2️⃣ Two separate fertilizations happen

        3️⃣ Result: **Two genetically different babies**

        🧬 DNA Match: **50%** (like regular siblings)

        👥 Can be same or different sex

        ✨ About 1 in 30 births
        """)

    st.markdown("---")

    st.info("💡 **Fun Fact:** Identical twins can come from the same placenta or separate ones. Fraternal twins have separate placentas!")

    st.markdown("---")

    # Challenge
    col1, col2 = st.columns(2)

    with col1:
        if st.button("I can identify Identical Twins! ✓", key="twin_identical"):
            st.success("✅ Correct! One egg + One sperm = 100% identical DNA")

    with col2:
        if st.button("I can identify Fraternal Twins! ✓", key="twin_fraternal"):
            st.success("✅ Correct! Two eggs + Two sperm = Only 50% shared DNA")

    if st.button("Complete Lab: Twin Expert 👯", key="complete_twins"):
        st.success("🎉 Congratulations! You've earned 60 XP and the 'Twin Expert' badge!")
        XPSystem.award_xp(60, "interactive lab completion")

def show_brain_drainer():
    """Display PSLE brain drainer questions"""
    st.subheader("🧠 Brain Drainer: PSLE-Style Questions")
    st.write("Test your knowledge with exam-style questions that include tricky answers!")

    # Get brain drainer questions
    questions = get_brain_drainer_questions('Ch1_Reproduction', limit=5)

    if questions:
        st.write(f"**{len(questions)} challenging questions selected**")
        st.markdown("---")

        for idx, question in enumerate(questions, 1):
            with st.container(border=True):
                st.markdown(f"### Question {idx}/{len(questions)}")
                result = display_brain_drainer_question(question)

                if result is not None:
                    xp_reward = 20 if result else 10
                    if result:
                        XPSystem.award_xp(xp_reward, "brain drainer correct")
                    st.write(f"Gained {xp_reward} XP")

        st.markdown("---")
        st.success("💪 Brain Drainer completed! You've earned valuable exam preparation experience!")

if __name__ == "__main__":
    show_chapter()
