"""
AANYA'S SCIENCE EXAM PREP PRO - Comprehensive PSLE Training System
Advanced features: Analytics, Spaced Repetition, Adaptive Difficulty, Performance Tracking
"""

import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent))

from components.animations import MalteseDogFeedback

# ==================== COMPREHENSIVE QUESTION BANK ====================

COMPREHENSIVE_QUESTIONS = {
    'Water_Cycles': {
        'easy': [
            {
                'id': 'w1',
                'type': 'MCQ',
                'q': 'At what temperature does ice melt?',
                'options': ['10°C', '0°C', '-10°C', '100°C'],
                'answer': '0°C',
                'explanation': 'Ice melts at 0°C (melting point). This is when solid water transforms to liquid water.',
                'ref': 'Page 31',
                'concept': 'Phase Changes'
            },
            {
                'id': 'w2',
                'type': 'MCQ',
                'q': 'Which process happens when wet clothes dry?',
                'options': ['Melting', 'Freezing', 'Evaporation', 'Condensation'],
                'answer': 'Evaporation',
                'explanation': 'Evaporation is liquid water changing to gas (vapor) without boiling. Heat from sun provides energy.',
                'ref': 'Page 42',
                'concept': 'Evaporation'
            },
            {
                'id': 'w3',
                'type': 'MCQ',
                'q': 'What is water vapor?',
                'options': ['Visible steam', 'Invisible gas', 'Liquid water', 'Ice crystals'],
                'answer': 'Invisible gas',
                'explanation': 'Water vapor is invisible gas in air. Steam (visible mist) forms when vapor cools.',
                'ref': 'Page 28',
                'concept': 'Water States'
            },
            {
                'id': 'w4',
                'type': 'MCQ',
                'q': 'In the water cycle, evaporation is followed by:',
                'options': ['Rain immediately', 'Condensation', 'Freezing', 'More evaporation'],
                'answer': 'Condensation',
                'explanation': 'Water vapor rises, cools in atmosphere, and condenses into water droplets forming clouds.',
                'ref': 'Pages 43-44',
                'concept': 'Water Cycle'
            },
            {
                'id': 'w5',
                'type': 'MCQ',
                'q': 'Why does salt remain when seawater evaporates?',
                'options': ['Evaporates slowly', 'Dissolves in vapor', 'Only water evaporates', 'Freezes first'],
                'answer': 'Only water evaporates',
                'explanation': 'Salt molecules do not evaporate at normal temperatures. Only water vapor escapes, leaving salt behind.',
                'ref': 'Page 43',
                'concept': 'Evaporation Purification'
            },
        ],
        'medium': [
            {
                'id': 'w6',
                'type': 'STRUCT',
                'q': 'Explain why steam (from boiling water) is VISIBLE but water vapor (in air) is INVISIBLE.',
                'answer': 'Steam is tiny water droplets (liquid) that reflect light. Water vapor is gas molecules (invisible). When vapor cools, it condenses into droplets (steam).',
                'explanation': 'State of matter determines visibility. Droplets scatter light; gas molecules do not.',
                'ref': 'Pages 28-29',
                'concept': 'Water States'
            },
            {
                'id': 'w7',
                'type': 'STRUCT',
                'q': 'If you boil water continuously at 100°C, why does temperature NOT rise above 100°C?',
                'answer': 'At 100°C, all added heat is used for evaporation (latent heat), not temperature increase. Temperature stays at 100°C until water fully evaporates.',
                'explanation': 'Phase change requires energy (latent heat). This energy goes to breaking bonds, not increasing motion.',
                'ref': 'Page 39',
                'concept': 'Latent Heat'
            },
            {
                'id': 'w8',
                'type': 'STRUCT',
                'q': 'Why do puddles disappear faster on hot, windy days compared to cool, still days?',
                'answer': 'Heat speeds evaporation (gives water molecules more energy). Wind carries away water vapor, making room for more evaporation.',
                'explanation': 'Both temperature and air movement increase evaporation rate.',
                'ref': 'Page 42',
                'concept': 'Evaporation Factors'
            },
        ],
        'hard': [
            {
                'id': 'w9',
                'type': 'STRUCT',
                'q': 'In a sealed jar, water evaporates but never rains. Explain what happens and name the process.',
                'answer': 'Water molecules evaporate AND simultaneously condense at equal rates. This is dynamic equilibrium - a closed water cycle where no net water gain/loss occurs.',
                'explanation': 'In closed systems, evaporation and condensation reach balance.',
                'ref': 'Pages 42-44',
                'concept': 'Dynamic Equilibrium'
            },
            {
                'id': 'w10',
                'type': 'STRUCT',
                'q': 'How does global warming affect the water cycle? Explain with specific effects.',
                'answer': 'Greenhouse gases trap heat, warming Earth. This causes: (1) Faster evaporation = more water vapor in air, (2) Heavier rainfall = extreme weather, (3) Melting ice caps = rising seas.',
                'explanation': 'Climate change accelerates entire water cycle.',
                'ref': 'Pages 33, 43-44',
                'concept': 'Climate Impact'
            },
        ]
    },

    'Reproduction': {
        'easy': [
            {
                'id': 'r1',
                'type': 'MCQ',
                'q': 'Which is a female reproductive cell?',
                'options': ['Pollen', 'Egg', 'Sperm', 'Seed'],
                'answer': 'Egg',
                'explanation': 'Egg is the female cell. Sperm is male. Pollen carries male cells in plants. Seed forms after fertilization.',
                'ref': 'Pages 5-7',
                'concept': 'Reproductive Cells'
            },
            {
                'id': 'r2',
                'type': 'MCQ',
                'q': 'What is needed for pollination?',
                'options': ['Rain only', 'Pollen reaches stigma', 'Tall plants', 'Wet soil'],
                'answer': 'Pollen reaches stigma',
                'explanation': 'Pollination is the transfer of pollen from anther to stigma. This is the first step in plant reproduction.',
                'ref': 'Pages 14-15',
                'concept': 'Pollination'
            },
            {
                'id': 'r3',
                'type': 'MCQ',
                'q': 'Which reproduce using spores, not seeds?',
                'options': ['Roses', 'Tomatoes', 'Ferns', 'Wheat'],
                'answer': 'Ferns',
                'explanation': 'Ferns and mosses are non-flowering plants. They use spores (tiny cells) for reproduction, not seeds.',
                'ref': 'Pages 18-19',
                'concept': 'Non-Flowering Plants'
            },
            {
                'id': 'r4',
                'type': 'MCQ',
                'q': 'What do seeds need to germinate? (WOW)',
                'options': ['Water, Oil, Wind', 'Water, Oxygen, Warmth', 'Water, Oxygen, Sun', 'Wind, Oxygen, Warmth'],
                'answer': 'Water, Oxygen, Warmth',
                'explanation': 'WOW = Water (dissolves nutrients), Oxygen (respiration energy), Warmth (enzyme activity). Sunlight is NOT needed initially (underground germination).',
                'ref': 'Page 17',
                'concept': 'Seed Germination'
            },
            {
                'id': 'r5',
                'type': 'MCQ',
                'q': 'Where does fertilization occur in humans?',
                'options': ['Ovary', 'Uterus', 'Fallopian tube', 'Stomach'],
                'answer': 'Fallopian tube',
                'explanation': 'Sperm meets egg in fallopian tube. The fertilized egg then travels to uterus for development.',
                'ref': 'Pages 5-7',
                'concept': 'Human Fertilization'
            },
        ],
        'medium': [
            {
                'id': 'r6',
                'type': 'STRUCT',
                'q': 'A plant is pollinated (pollen lands on stigma) but NO seeds form. What went wrong? Explain.',
                'answer': 'Pollination transferred pollen, but fertilization (fusion of pollen nucleus with egg cell) did not occur. Without fertilization, no seed develops.',
                'explanation': 'Pollination ≠ Fertilization. Pollination is delivery; fertilization is the actual fusion.',
                'ref': 'Pages 14-16',
                'concept': 'Pollination vs Fertilization'
            },
            {
                'id': 'r7',
                'type': 'STRUCT',
                'q': 'Why do identical twins look exactly alike but fraternal twins may look different?',
                'answer': 'Identical: One egg + one sperm → splits into 2 individuals = 100% same DNA. Fraternal: Two eggs + two sperm → two separate fertilizations = ~50% DNA similarity (like siblings).',
                'explanation': 'Identical share all genes; fraternal share half.',
                'ref': 'Pages 5-7',
                'concept': 'Twin Formation'
            },
            {
                'id': 'r8',
                'type': 'STRUCT',
                'q': 'Why are seeds scattered far from parent plants? Give TWO reasons.',
                'answer': '1) Avoid competition: Overcrowding with parent plant means fighting for light, water, nutrients. 2) Colonize new areas: Seeds reach new locations for species survival.',
                'explanation': 'Dispersal is survival strategy.',
                'ref': 'Page 15',
                'concept': 'Seed Dispersal'
            },
        ],
        'hard': [
            {
                'id': 'r9',
                'type': 'STRUCT',
                'q': 'A seed has water, oxygen, warmth, nutrients, and correct pH but STILL won\'t germinate. What could be wrong?',
                'answer': 'Seed is dormant (genetically programmed not to germinate yet). Some seeds need triggers: cold period (winter), light exposure, or specific humidity. Dormancy ensures germination at best time.',
                'explanation': 'Dormancy is an evolutionary adaptation.',
                'ref': 'Page 17',
                'concept': 'Seed Dormancy'
            },
            {
                'id': 'r10',
                'type': 'STRUCT',
                'q': 'Explain how inherited traits pass from parents to children using dimples as example.',
                'answer': 'During fertilization, genes from both sperm and egg combine. If both parents carry dimple gene, child inherits it and has dimples. Some traits are dominant (show up); others recessive (hidden).',
                'explanation': 'Genetic inheritance follows Mendelian patterns.',
                'ref': 'Pages 4-5',
                'concept': 'Inheritance'
            },
            {
                'id': 'r11',
                'type': 'STRUCT',
                'q': 'Two plants with identical appearance produce offspring with different traits. How is this possible?',
                'answer': 'Phenotype (appearance) ≠ Genotype (genes). Both plants may carry different hidden genes. During reproduction, different gene combinations create varied offspring.',
                'explanation': 'Same parents, different inheritance combinations.',
                'ref': 'Pages 4-5',
                'concept': 'Phenotype vs Genotype'
            },
        ]
    },

    'Electrical_Systems': {
        'easy': [
            {
                'id': 'e1',
                'type': 'MCQ',
                'q': 'What does a battery do in a circuit?',
                'options': ['Makes bulbs bright', 'Provides electrical energy', 'Measures current', 'Controls switch'],
                'answer': 'Provides electrical energy',
                'explanation': 'Battery converts chemical energy to electrical energy. It pushes electrons (current) through the circuit.',
                'ref': 'Pages 93-95',
                'concept': 'Battery Function'
            },
            {
                'id': 'e2',
                'type': 'MCQ',
                'q': 'A closed circuit means:',
                'options': ['Broken path', 'Complete path for current', 'No path', 'Blocked path'],
                'answer': 'Complete path for current',
                'explanation': 'Closed = complete loop. Current can flow. Light turns ON. Open = broken, light OFF.',
                'ref': 'Pages 94-96',
                'concept': 'Circuit States'
            },
            {
                'id': 'e3',
                'type': 'MCQ',
                'q': 'Which is a good conductor?',
                'options': ['Rubber', 'Plastic', 'Copper', 'Wood'],
                'answer': 'Copper',
                'explanation': 'Copper is a metal with free electrons. It conducts electricity well. Used in wires. Others are insulators.',
                'ref': 'Page 98',
                'concept': 'Conductors vs Insulators'
            },
            {
                'id': 'e4',
                'type': 'MCQ',
                'q': 'Why is rubber wrapped around copper wires?',
                'options': ['Makes stronger', 'Insulates (protects)', 'Faster current', 'Prevents rust'],
                'answer': 'Insulates (protects)',
                'explanation': 'Rubber is insulator. It prevents accidental contact with live copper, protecting from electric shock.',
                'ref': 'Page 98',
                'concept': 'Electrical Safety'
            },
            {
                'id': 'e5',
                'type': 'MCQ',
                'q': 'Why is touching wet appliances dangerous?',
                'options': ['Cold hands', 'Water conducts electricity', 'Appliances malfunction', 'Hands slip'],
                'answer': 'Water conducts electricity',
                'explanation': 'Water is conductor. Current flows through wet hands to ground. This causes electric shock.',
                'ref': 'Pages 101-102',
                'concept': 'Water Conductivity'
            },
        ],
        'medium': [
            {
                'id': 'e6',
                'type': 'STRUCT',
                'q': 'What does an ammeter measure and where should it be placed in a circuit?',
                'answer': 'Ammeter measures electrical current in Amperes. It must be placed IN SERIES with the circuit (in the current path), not across components.',
                'explanation': 'Ammeters have low resistance and must not bypass circuit.',
                'ref': 'Pages 102-103',
                'concept': 'Ammeter Placement'
            },
            {
                'id': 'e7',
                'type': 'STRUCT',
                'q': 'In a series circuit with one 6V battery and 2 identical bulbs, how much voltage is across EACH bulb?',
                'answer': 'Each bulb gets 3V. In series, total voltage divides equally among identical resistances. 6V ÷ 2 bulbs = 3V per bulb.',
                'explanation': 'Voltage division in series: V_total = V_1 + V_2 + ...',
                'ref': 'Page 110',
                'concept': 'Voltage Division'
            },
            {
                'id': 'e8',
                'type': 'STRUCT',
                'q': 'When you add more bulbs IN SERIES, what happens to brightness? Why?',
                'answer': 'All bulbs get dimmer. More bulbs = more resistance. More resistance with same voltage = less current (I = V/R). Less current = dimmer light.',
                'explanation': 'Series resistance adds: R_total = R_1 + R_2 + R_3...',
                'ref': 'Pages 110-113',
                'concept': 'Series Resistance'
            },
        ],
        'hard': [
            {
                'id': 'e9',
                'type': 'STRUCT',
                'q': 'A circuit breaker trips when too much current flows. Explain the danger it prevents.',
                'answer': 'High current causes power loss in wires: P = I²R (current squared). This creates dangerous heat that can melt wires and start fires. Breaker trips to cut current before fire occurs.',
                'explanation': 'Current is squared because heat depends on I².',
                'ref': 'Page 113',
                'concept': 'Circuit Breaker'
            },
            {
                'id': 'e10',
                'type': 'STRUCT',
                'q': 'Why does touching a live wire with bare hands cause electric shock? Use "circuit" in your answer.',
                'answer': 'Your body completes the electrical circuit. Current flows from wire → through your body → to ground. This shock can cause injury or death.',
                'explanation': 'Body becomes conductor in the circuit path.',
                'ref': 'Pages 101-102',
                'concept': 'Electric Shock'
            },
            {
                'id': 'e11',
                'type': 'STRUCT',
                'q': 'In Ohm\'s Law (V = I × R), if voltage increases but resistance stays same, what happens to current and why?',
                'answer': 'Current INCREASES. Mathematically: I = V/R. If V increases and R is constant, I must increase. Physically: higher voltage pushes more electrons through.',
                'explanation': 'Direct proportional relationship between voltage and current.',
                'ref': 'Pages 108-110',
                'concept': 'Ohm\'s Law'
            },
        ]
    }
}

# ==================== INITIALIZE SESSION ====================

def init_session():
    """Initialize all session variables"""
    defaults = {
        'mode': 'home',
        'current_question_idx': 0,
        'score': 0,
        'answers': {},
        'exam_started': False,
        'exam_start_time': None,
        'current_topic': None,
        'performance_history': [],
        'weak_topics': [],
        'total_questions_attempted': 0,
        'accuracy_by_difficulty': {'easy': [], 'medium': [], 'hard': []},
        'confidence_ratings': {},
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ==================== QUESTIONS HELPER ====================

def get_all_questions_flat(topic=None, difficulty=None):
    """Get flat list of all questions"""
    all_q = []
    topics = [topic] if topic else ['Water_Cycles', 'Reproduction', 'Electrical_Systems']

    for t in topics:
        if t in COMPREHENSIVE_QUESTIONS:
            diffs = [difficulty] if difficulty else ['easy', 'medium', 'hard']
            for d in diffs:
                if d in COMPREHENSIVE_QUESTIONS[t]:
                    all_q.extend(COMPREHENSIVE_QUESTIONS[t][d])

    return all_q

def get_question_by_id(q_id):
    """Get specific question by ID"""
    for topic in COMPREHENSIVE_QUESTIONS:
        for difficulty in COMPREHENSIVE_QUESTIONS[topic]:
            for q in COMPREHENSIVE_QUESTIONS[topic][difficulty]:
                if q['id'] == q_id:
                    return q
    return None

# ==================== DISPLAY FUNCTIONS ====================

def display_question(question, num, total):
    """Display a question with all details"""
    st.markdown(f"## Q{num}/{total}: {question['q']}")
    st.caption(f"📌 **Concept**: {question['concept']} | **Ref**: {question['ref']} | **Difficulty**: {question['difficulty'].upper()}")

    if question['type'] == 'MCQ':
        answer = st.radio(
            "Select your answer:",
            question['options'],
            key=f"q_{question['id']}"
        )
        confidence = st.slider(
            "How confident are you? (1=Guess, 5=Very Sure)",
            1, 5, 3,
            key=f"conf_{question['id']}"
        )
        return answer, confidence
    else:  # Structured
        answer = st.text_area(
            "Write your answer (2-3 sentences with key terms):",
            key=f"q_{question['id']}",
            height=120
        )
        confidence = st.slider(
            "How confident are you?",
            1, 5, 3,
            key=f"conf_{question['id']}"
        )
        return answer, confidence

def check_answer(question, user_answer):
    """Check answer correctness"""
    if question['type'] == 'MCQ':
        return user_answer == question['answer'], question['answer']
    else:  # Structured
        answer_lower = question['answer'].lower()
        response_lower = user_answer.lower()

        # Check if key concepts present
        key_terms = [w for w in answer_lower.split() if len(w) > 3]
        matches = sum(1 for term in key_terms if term in response_lower)

        # Need at least 50% of key terms
        threshold = max(2, len(key_terms) // 2)
        is_correct = matches >= threshold

        return is_correct, question['answer']

# ==================== MAIN APP ====================

def show_home():
    """Home page with learning paths"""
    st.set_page_config(page_title="Aanya's Exam Prep Pro", page_icon="🧪", layout="wide")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🧪 AANYA'S SCIENCE EXAM PREP PRO")
        st.subheader("Advanced PSLE Training System")
    with col2:
        st.metric("📚 Total Questions", "38+", "All PSLE Format")

    st.markdown("---")

    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Attempted", st.session_state.total_questions_attempted)
    with col2:
        if st.session_state.total_questions_attempted > 0:
            accuracy = (sum(1 for a in st.session_state.answers.values() if a.get('is_correct')) / len(st.session_state.answers)) * 100
            st.metric("Overall Accuracy", f"{accuracy:.0f}%")
        else:
            st.metric("Overall Accuracy", "-")
    with col3:
        st.metric("⏰ Exam Date", "T2W9", "This Week")
    with col4:
        st.metric("⏱️ Exam Time", "45 min", "Official Format")

    st.markdown("---")
    st.write("## 🎯 Choose Your Learning Path")

    # Three main modes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📖 **Topic Mastery**")
        st.write("Learn one topic at a time. No timer, focus on understanding.")
        if st.button("Start Topic Practice →", key="topic_btn", use_container_width=True):
            st.session_state.mode = 'topic_select'
            st.rerun()

    with col2:
        st.markdown("### 🎯 **Mock Exam**")
        st.write("Full 45-minute realistic test. All 38+ questions.")
        if st.button("Start Mock Exam →", key="mock_btn", use_container_width=True):
            st.session_state.mode = 'mock_exam'
            st.session_state.exam_started = True
            st.session_state.exam_start_time = time.time()
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()

    with col3:
        st.markdown("### 📊 **Performance Review**")
        st.write("Analyze your strengths and weaknesses.")
        if st.button("View Analytics →", key="analytics_btn", use_container_width=True):
            st.session_state.mode = 'analytics'
            st.rerun()

    st.markdown("---")

    # Study recommendations
    if st.session_state.total_questions_attempted > 0:
        st.info("💡 **Study Recommendation**:")
        weak = get_weak_topics()
        if weak:
            st.write(f"Focus on: **{', '.join(weak)}**")
        else:
            st.write("You're doing well! Keep practicing to reach 80%+")

def get_weak_topics():
    """Identify weak topics based on performance"""
    if len(st.session_state.answers) < 5:
        return []

    topic_scores = {'Water': [], 'Reproduction': [], 'Electrical': []}
    topic_map = {'w': 'Water', 'r': 'Reproduction', 'e': 'Electrical'}

    for q_id, answer_data in st.session_state.answers.items():
        prefix = q_id.split('_')[0] if '_' in q_id else q_id[0]
        topic = topic_map.get(prefix)
        if topic:
            topic_scores[topic].append(answer_data.get('is_correct', False))

    weak = []
    for topic, scores in topic_scores.items():
        if scores and (sum(scores) / len(scores)) < 0.7:
            weak.append(topic)

    return weak

def show_topic_select():
    """Topic selection"""
    st.title("📖 Topic Mastery Mode")
    st.write("Master each topic before the mock exam!")

    topics = {
        '💧 Cycles in Water': 'Water_Cycles',
        '👶 Reproduction in Animals & Plants': 'Reproduction',
        '⚡ Electrical Systems': 'Electrical_Systems'
    }

    cols = st.columns(3)
    for idx, (name, key) in enumerate(topics.items()):
        with cols[idx]:
            q_count = len(get_all_questions_flat(key))
            if st.button(f"{name}\n\n({q_count} questions)", use_container_width=True, key=f"topic_{key}"):
                st.session_state.mode = 'practice'
                st.session_state.current_topic = key
                st.session_state.current_question_idx = 0
                st.session_state.score = 0
                st.session_state.answers = {}
                st.rerun()

    st.markdown("---")
    if st.button("← Back to Home"):
        st.session_state.mode = 'home'
        st.rerun()

def show_practice_mode():
    """Topic practice mode"""
    topic = st.session_state.current_topic
    topic_display = {'Water_Cycles': '💧 Water Cycles', 'Reproduction': '👶 Reproduction', 'Electrical_Systems': '⚡ Electrical Systems'}

    st.title(f"{topic_display.get(topic, topic)} - Practice Mode")

    questions = get_all_questions_flat(topic)
    current_idx = st.session_state.current_question_idx

    if current_idx >= len(questions):
        show_topic_results(questions)
        return

    question = questions[current_idx]

    # Progress
    progress = (current_idx + 1) / len(questions)
    st.progress(progress)
    st.write(f"Progress: {current_idx + 1}/{len(questions)}")

    # Display question
    with st.container(border=True):
        user_answer, confidence = display_question(question, current_idx + 1, len(questions))

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=(current_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        if st.button("✓ Check Answer", use_container_width=True):
            if user_answer:
                is_correct, correct_answer = check_answer(question, user_answer)

                if is_correct:
                    st.success("✅ CORRECT!")
                    st.session_state.score += 1
                    MalteseDogFeedback.show_happy_maltese("Aanya")
                else:
                    st.error("❌ Not quite right")
                    st.info(f"**Correct Answer**: {correct_answer}")
                    st.write(f"**Explanation**: {question['explanation']}")

                st.session_state.answers[question['id']] = {
                    'question': question['q'],
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct,
                    'confidence': confidence,
                    'difficulty': question.get('difficulty', 'medium'),
                    'concept': question.get('concept', 'Unknown')
                }

    with col3:
        if st.button("Next ➡️", disabled=(current_idx >= len(questions) - 1)):
            st.session_state.current_question_idx += 1
            st.rerun()

def show_topic_results(questions):
    """Topic results and review"""
    st.title("📊 Topic Results")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score", f"{st.session_state.score}/{len(questions)}")
    with col2:
        if len(questions) > 0:
            percentage = (st.session_state.score / len(questions)) * 100
            st.metric("Percentage", f"{percentage:.0f}%")
        else:
            st.metric("Percentage", "-")
    with col3:
        if percentage >= 80:
            st.metric("Status", "🟢 Excellent")
        elif percentage >= 70:
            st.metric("Status", "🟡 Good")
        else:
            st.metric("Status", "🔴 Review Needed")

    st.markdown("---")
    st.write("### Review Your Answers")

    correct_count = 0
    incorrect_count = 0

    for q_id, answer in st.session_state.answers.items():
        with st.expander(f"{'✅' if answer['is_correct'] else '❌'} Q: {answer['question'][:60]}... (Confidence: {answer['confidence']}/5)"):
            if answer['is_correct']:
                st.success("Correct!")
            else:
                st.error(f"Your answer: {answer['user_answer']}")
                st.write(f"Correct answer: {answer['correct_answer']}")

            question = get_question_by_id(q_id)
            if question:
                st.write(f"**Explanation**: {question['explanation']}")
                st.caption(f"Concept: {question['concept']} | Difficulty: {question.get('difficulty', 'N/A').upper()}")

            if answer['is_correct']:
                correct_count += 1
            else:
                incorrect_count += 1

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Retry Topic"):
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()
    with col2:
        if st.button("← Back to Topics"):
            st.session_state.mode = 'topic_select'
            st.rerun()

def show_mock_exam():
    """Full mock exam"""
    st.title("🎯 FULL MOCK EXAM - 45 Minutes")

    # Timer
    elapsed = time.time() - st.session_state.exam_start_time
    remaining = max(0, 2700 - elapsed)

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("**All 3 Topics - 38+ Questions**")
    with col2:
        if remaining > 0:
            mins = int(remaining // 60)
            secs = int(remaining % 60)
            st.metric("⏱️ Time Left", f"{mins}:{secs:02d}")
            if remaining < 300:
                st.warning("⚠️ Less than 5 minutes!")
        else:
            st.error("⏰ TIME'S UP!")
            show_mock_results()
            return
    with col3:
        all_questions = get_all_questions_flat()
        st.metric("Progress", f"{st.session_state.current_question_idx + 1}/{len(all_questions)}")

    st.progress(min(st.session_state.current_question_idx / len(all_questions), 1.0))

    # Get all questions in order
    all_questions = get_all_questions_flat()

    if st.session_state.current_question_idx >= len(all_questions):
        show_mock_results()
        return

    question = all_questions[st.session_state.current_question_idx]

    st.markdown("---")
    with st.container(border=True):
        user_answer, confidence = display_question(question, st.session_state.current_question_idx + 1, len(all_questions))

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Previous", disabled=(st.session_state.current_question_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()
    with col2:
        if st.button("✓ Submit Answer", use_container_width=True):
            if user_answer:
                is_correct, correct_answer = check_answer(question, user_answer)
                if is_correct:
                    st.session_state.score += 1
                    st.success("✅ Correct!")
                else:
                    st.info(f"Answer: {correct_answer}")

                st.session_state.answers[question['id']] = {
                    'question': question['q'],
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct,
                    'confidence': confidence,
                    'difficulty': question.get('difficulty'),
                    'concept': question.get('concept')
                }

                time.sleep(1)
                st.session_state.current_question_idx += 1
                st.rerun()
    with col3:
        if st.button("Next ➡️"):
            st.session_state.current_question_idx += 1
            st.rerun()

def show_mock_results():
    """Mock exam results"""
    st.title("📊 EXAM RESULTS")

    all_questions = get_all_questions_flat()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Final Score", f"{st.session_state.score}/{len(all_questions)}")
    with col2:
        percentage = (st.session_state.score / len(all_questions)) * 100
        st.metric("Percentage", f"{percentage:.1f}%")
    with col3:
        if percentage >= 80:
            st.metric("Grade", "🟢 EXCELLENT")
        elif percentage >= 70:
            st.metric("Grade", "🟡 GOOD")
        elif percentage >= 60:
            st.metric("Grade", "🟠 FAIR")
        else:
            st.metric("Grade", "🔴 NEEDS WORK")
    with col4:
        st.metric("Questions Done", len(st.session_state.answers))

    st.markdown("---")

    if percentage >= 80:
        st.success("🎉 EXCELLENT! You're ready for the real exam!")
        MalteseDogFeedback.show_happy_maltese("Aanya")
    elif percentage >= 70:
        st.info("👍 Good score! Focus on weak areas for final polish.")
    else:
        st.warning("⚠️ Keep practicing! Review weak topics before exam.")
        MalteseDogFeedback.show_sad_maltese("Aanya")

    st.markdown("---")
    st.write("### Detailed Performance by Difficulty")

    diff_perf = {'easy': [], 'medium': [], 'hard': []}
    for q_id, answer in st.session_state.answers.items():
        diff = answer.get('difficulty', 'medium')
        diff_perf[diff].append(answer['is_correct'])

    cols = st.columns(3)
    for idx, (diff, scores) in enumerate(diff_perf.items()):
        with cols[idx]:
            if scores:
                perc = (sum(scores) / len(scores)) * 100
                st.metric(f"{diff.upper()}", f"{perc:.0f}% ({sum(scores)}/{len(scores)})")
            else:
                st.metric(f"{diff.upper()}", "No questions")

    st.markdown("---")
    st.write("### Answer Review")

    tabs = st.tabs(["All Answers", "Correct", "Incorrect"])

    with tabs[0]:
        for q_id, answer in st.session_state.answers.items():
            with st.expander(f"{'✅' if answer['is_correct'] else '❌'} {answer['question'][:70]}..."):
                st.write(f"**Your Answer**: {answer['user_answer']}")
                st.write(f"**Correct Answer**: {answer['correct_answer']}")
                question = get_question_by_id(q_id)
                if question:
                    st.write(f"**Explanation**: {question['explanation']}")

    with tabs[1]:
        for q_id, answer in st.session_state.answers.items():
            if answer['is_correct']:
                st.success(f"✅ {answer['question'][:70]}...")

    with tabs[2]:
        for q_id, answer in st.session_state.answers.items():
            if not answer['is_correct']:
                with st.expander(f"❌ {answer['question'][:70]}..."):
                    st.write(f"Your Answer: {answer['user_answer']}")
                    st.write(f"Correct: {answer['correct_answer']}")
                    question = get_question_by_id(q_id)
                    if question:
                        st.write(f"Explanation: {question['explanation']}")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Try Again"):
            st.session_state.exam_started = False
            st.session_state.mode = 'home'
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()
    with col2:
        if st.button("🏠 Back to Home"):
            st.session_state.mode = 'home'
            st.rerun()

def show_analytics():
    """Performance analytics"""
    st.title("📊 Performance Analytics")

    if len(st.session_state.answers) == 0:
        st.info("No data yet. Complete some practice sessions first!")
        if st.button("← Back to Home"):
            st.session_state.mode = 'home'
            st.rerun()
        return

    # Overall stats
    col1, col2, col3 = st.columns(3)
    with col1:
        total_correct = sum(1 for a in st.session_state.answers.values() if a['is_correct'])
        st.metric("Total Correct", f"{total_correct}/{len(st.session_state.answers)}")
    with col2:
        accuracy = (total_correct / len(st.session_state.answers)) * 100
        st.metric("Accuracy", f"{accuracy:.1f}%")
    with col3:
        avg_confidence = sum(a['confidence'] for a in st.session_state.answers.values()) / len(st.session_state.answers)
        st.metric("Avg Confidence", f"{avg_confidence:.1f}/5")

    st.markdown("---")

    # Performance by difficulty
    st.write("### Performance by Difficulty")
    diff_data = {'easy': [], 'medium': [], 'hard': []}
    for answer in st.session_state.answers.values():
        diff = answer.get('difficulty', 'medium')
        diff_data[diff].append(answer['is_correct'])

    df_data = []
    for diff, scores in diff_data.items():
        if scores:
            df_data.append({
                'Difficulty': diff.upper(),
                'Correct': sum(scores),
                'Total': len(scores),
                'Accuracy': f"{(sum(scores)/len(scores))*100:.0f}%"
            })

    if df_data:
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # Weak concepts
    st.write("### Concepts to Review")
    concept_perf = {}
    for answer in st.session_state.answers.values():
        concept = answer.get('concept', 'Unknown')
        if concept not in concept_perf:
            concept_perf[concept] = []
        concept_perf[concept].append(answer['is_correct'])

    weak_concepts = []
    for concept, scores in concept_perf.items():
        if scores and (sum(scores) / len(scores)) < 0.7:
            accuracy = (sum(scores) / len(scores)) * 100
            weak_concepts.append((concept, accuracy, len(scores)))

    if weak_concepts:
        for concept, accuracy, count in sorted(weak_concepts, key=lambda x: x[1]):
            st.warning(f"📌 **{concept}**: {accuracy:.0f}% accuracy ({count} questions)")
    else:
        st.success("✅ All concepts strong!")

    if st.button("← Back to Home"):
        st.session_state.mode = 'home'
        st.rerun()

# ==================== MAIN ====================

def main():
    init_session()

    if st.session_state.mode == 'home':
        show_home()
    elif st.session_state.mode == 'topic_select':
        show_topic_select()
    elif st.session_state.mode == 'practice':
        show_practice_mode()
    elif st.session_state.mode == 'mock_exam':
        show_mock_exam()
    elif st.session_state.mode == 'analytics':
        show_analytics()

if __name__ == "__main__":
    main()
