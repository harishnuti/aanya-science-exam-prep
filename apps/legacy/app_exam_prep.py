"""
AANYA'S SCIENCE EXAM PREP - Comprehensive PSLE Training
Term 2 Review: Cycles in Water, Reproduction, Electrical Systems
45 minutes | MCQ + Structured Questions | Challenging Knowledge Test
"""

import streamlit as st
import time
from datetime import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from components.animations import MalteseDogFeedback
from components.brain_drainers_phase2c import BRAIN_DRAINERS_PHASE2C

# ==================== EXAM QUESTIONS DATABASE ====================

EXAM_QUESTIONS = {
    'Water_Cycles': {
        'mcq': [
            {
                'type': 'MCQ',
                'q': 'At what temperature does ice start melting?',
                'options': ['10°C', '0°C', '-10°C', '100°C'],
                'answer': '0°C',
                'ref': 'Page 31',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'Which process happens when wet clothes dry on a sunny day?',
                'options': ['Melting', 'Freezing', 'Evaporation', 'Condensation'],
                'answer': 'Evaporation',
                'ref': 'Page 42',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'What is water vapor?',
                'options': ['Visible steam', 'Invisible gas in air', 'Liquid water', 'Frozen water'],
                'answer': 'Invisible gas in air',
                'ref': 'Page 28',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'In the water cycle, after evaporation, what happens NEXT?',
                'options': ['Rain falls immediately', 'Water vapor condenses into clouds', 'Water freezes', 'More evaporation'],
                'answer': 'Water vapor condenses into clouds',
                'ref': 'Pages 43-44',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'Why does salt remain behind when seawater evaporates?',
                'options': ['Salt evaporates slower', 'Salt dissolves in vapor', 'Only water evaporates', 'Salt converts to minerals'],
                'answer': 'Only water evaporates',
                'ref': 'Page 43',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'If you boil water to 100°C and keep heating, what happens?',
                'options': ['Temperature rises above 100°C', 'Water evaporates at 100°C (latent heat)', 'Water freezes', 'Nothing changes'],
                'answer': 'Water evaporates at 100°C (latent heat)',
                'ref': 'Page 39',
                'difficulty': 'hard'
            },
            {
                'type': 'MCQ',
                'q': 'Why do puddles disappear faster on hot, windy days?',
                'options': ['Wind blows water away', 'Heat speeds evaporation; wind carries vapor', 'Puddles are shallower', 'Water moves to cooler places'],
                'answer': 'Heat speeds evaporation; wind carries vapor',
                'ref': 'Page 42',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'Explain why we cannot see water vapor but we can see steam. What is the difference?',
                'answer': 'Water vapor is invisible gas in air. Steam is visible mist formed when water vapor cools.',
                'ref': 'Pages 28-29',
                'difficulty': 'medium'
            },
            {
                'type': 'STRUCT',
                'q': 'How does the water cycle ensure that we always have clean water? Explain each stage.',
                'answer': 'Evaporation: Pure water rises as vapor, leaving salt/impurities behind. Condensation: Vapor cools and forms clouds. Precipitation: Water falls as rain. Collection: Water returns to oceans/lakes. The cycle purifies water.',
                'ref': 'Pages 43-44',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'Greenhouse gases trap heat. What effect does this have on the water cycle?',
                'answer': 'Trapped heat increases Earth\'s temperature, speeding up evaporation and intensifying rainfall. Ice caps also melt faster.',
                'ref': 'Page 33',
                'difficulty': 'hard'
            },
        ]
    },

    'Reproduction': {
        'mcq': [
            {
                'type': 'MCQ',
                'q': 'Which is a female reproductive cell?',
                'options': ['Pollen', 'Egg', 'Sperm', 'Seed'],
                'answer': 'Egg',
                'ref': 'Pages 5-7',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'What is needed for pollination to happen?',
                'options': ['Rain only', 'Pollen must reach stigma', 'Plant must be tall', 'Soil must be wet'],
                'answer': 'Pollen must reach stigma',
                'ref': 'Pages 14-15',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'Which plants reproduce using spores?',
                'options': ['Roses', 'Tomatoes', 'Ferns and mosses', 'Wheat'],
                'answer': 'Ferns and mosses',
                'ref': 'Pages 18-19',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'What does a seed need to germinate? (WOW)',
                'options': ['Water, Oil, Wind', 'Water, Oxygen, Warmth', 'Water, Oxygen, Sunlight', 'Wind, Oxygen, Warmth'],
                'answer': 'Water, Oxygen, Warmth',
                'ref': 'Page 17',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'Where does fertilization occur in humans?',
                'options': ['Ovary', 'Uterus', 'Fallopian tube', 'Stomach'],
                'answer': 'Fallopian tube',
                'ref': 'Pages 5-7',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'A plant is pollinated but NO seeds develop. What went wrong?',
                'options': ['Not enough rain', 'Fertilization didn\'t occur (fusion didn\'t happen)', 'Plant is too young', 'Too many insects'],
                'answer': 'Fertilization didn\'t occur (fusion didn\'t happen)',
                'ref': 'Pages 14-16',
                'difficulty': 'hard'
            },
            {
                'type': 'MCQ',
                'q': 'Why do identical twins look the same but fraternal twins may not?',
                'options': ['Identical share a bed', 'Identical = same egg+sperm (same DNA); Fraternal = two separate fertilizations', 'Fraternal aren\'t real siblings', 'It depends on diet'],
                'answer': 'Identical = same egg+sperm (same DNA); Fraternal = two separate fertilizations',
                'ref': 'Pages 5-7',
                'difficulty': 'hard'
            },
            {
                'type': 'MCQ',
                'q': 'If a seed has water and warmth but NO oxygen, will it germinate?',
                'options': ['Yes, slowly', 'No, cells need oxygen for respiration to release energy', 'Only if buried deep', 'Yes, but smaller'],
                'answer': 'No, cells need oxygen for respiration to release energy',
                'ref': 'Page 17',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'Explain the difference between pollination and fertilization. Why do we need both?',
                'answer': 'Pollination: Transfer of pollen to stigma (external process). Fertilization: Fusion of pollen nucleus with egg cell (creates seed). We need pollination to deliver pollen, then fertilization to create new life.',
                'ref': 'Pages 14-15',
                'difficulty': 'medium'
            },
            {
                'type': 'STRUCT',
                'q': 'Why do seeds need to scatter far from the parent plant? Give two reasons.',
                'answer': '1) Avoid competition for light, water, and nutrients. 2) Prevent overcrowding. Scattering by wind, water, or animals helps seeds colonize new areas.',
                'ref': 'Page 15',
                'difficulty': 'medium'
            },
            {
                'type': 'STRUCT',
                'q': 'A seed has everything (water, oxygen, warmth, soil, nutrients) but still won\'t germinate. Why? What could be missing?',
                'answer': 'The seed may be dormant (genetically programmed not to germinate yet). Some seeds need specific triggers like cold period (stratification) or light exposure before germinating.',
                'ref': 'Page 17',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'Explain how inherited traits are passed from parents to children using an example (e.g., dimples, eyelids).',
                'answer': 'During fertilization, genetic material from both sperm and egg combine. If both parents carry the gene for dimples, the child inherits it and has dimples. Some traits are recessive and skip generations.',
                'ref': 'Pages 4-5',
                'difficulty': 'hard'
            },
        ]
    },

    'Electrical_Systems': {
        'mcq': [
            {
                'type': 'MCQ',
                'q': 'What does a battery do in a circuit?',
                'options': ['Makes bulbs bright', 'Provides electrical energy (voltage)', 'Measures current', 'Controls the switch'],
                'answer': 'Provides electrical energy (voltage)',
                'ref': 'Pages 93-95',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'What is a closed circuit?',
                'options': ['Broken', 'Complete path for current to flow', 'Blocked', 'Empty'],
                'answer': 'Complete path for current to flow',
                'ref': 'Pages 94-96',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'Which of these is a good conductor?',
                'options': ['Rubber', 'Plastic', 'Copper', 'Wood'],
                'answer': 'Copper',
                'ref': 'Page 98',
                'difficulty': 'easy'
            },
            {
                'type': 'MCQ',
                'q': 'Why is rubber wrapped around copper wires?',
                'options': ['Makes it stronger', 'Rubber insulates; protects from current', 'Makes current faster', 'Prevents rusting'],
                'answer': 'Rubber insulates; protects from current',
                'ref': 'Page 98',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'Why is it dangerous to touch an appliance with wet hands?',
                'options': ['Hands get cold', 'Water conducts electricity; current flows through body', 'Appliances malfunction', 'Hands slip'],
                'answer': 'Water conducts electricity; current flows through body',
                'ref': 'Pages 101-102',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'What does an ammeter measure?',
                'options': ['Voltage', 'Current in Amperes', 'Resistance', 'Power'],
                'answer': 'Current in Amperes',
                'ref': 'Pages 102-103',
                'difficulty': 'medium'
            },
            {
                'type': 'MCQ',
                'q': 'In a series circuit with multiple bulbs, if one bulb breaks, what happens?',
                'options': ['Only that bulb goes dark', 'All bulbs go dark (circuit is broken)', 'Other bulbs brighten', 'Nothing'],
                'answer': 'All bulbs go dark (circuit is broken)',
                'ref': 'Page 93',
                'difficulty': 'hard'
            },
            {
                'type': 'MCQ',
                'q': 'In Ohm\'s Law (V = I × R), if voltage increases and resistance stays same, current:',
                'options': ['Decreases', 'Stays same', 'Increases', 'Becomes zero'],
                'answer': 'Increases',
                'ref': 'Pages 108-110',
                'difficulty': 'hard'
            },
            {
                'type': 'MCQ',
                'q': 'When you add more bulbs IN SERIES, what happens to brightness?',
                'options': ['All stay bright', 'All get dimmer', 'Only new ones dim', 'No change'],
                'answer': 'All get dimmer',
                'ref': 'Pages 110-113',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'A switch is "open." What does this mean? Can current flow?',
                'answer': 'Open switch means the circuit is broken (disconnected). Current CANNOT flow. Light is OFF.',
                'ref': 'Pages 94-96',
                'difficulty': 'medium'
            },
            {
                'type': 'STRUCT',
                'q': 'Explain why touching a live wire with bare hands is extremely dangerous. Use the term "circuit" in your answer.',
                'answer': 'Your body becomes part of the electrical circuit. Current flows through your body to the ground, causing dangerous electric shock or death.',
                'ref': 'Pages 101-102',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'Why does a circuit breaker trip when too much current flows? How does this protect your home?',
                'answer': 'High current creates dangerous heat in wires, risking fire. Circuit breaker automatically stops (trips) the flow, preventing overheating and fires.',
                'ref': 'Page 113',
                'difficulty': 'hard'
            },
            {
                'type': 'STRUCT',
                'q': 'In a series circuit (6V battery, 2 identical bulbs), how much voltage is across EACH bulb? Explain why.',
                'answer': 'Each bulb gets 3V. In series, voltage divides equally among identical resistances. 6V ÷ 2 bulbs = 3V each.',
                'ref': 'Page 110',
                'difficulty': 'hard'
            },
        ]
    }
}

# ==================== STREAMLIT APP ====================

def initialize_session():
    """Initialize all session state variables"""
    if 'exam_started' not in st.session_state:
        st.session_state.exam_started = False
    if 'exam_start_time' not in st.session_state:
        st.session_state.exam_start_time = None
    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'mode' not in st.session_state:
        st.session_state.mode = 'home'  # home, topic_select, practice, mock_exam, results

def get_all_questions(topic=None):
    """Get all questions for topic or all topics"""
    all_q = []
    topics = [topic] if topic else ['Water_Cycles', 'Reproduction', 'Electrical_Systems']

    for t in topics:
        if t in EXAM_QUESTIONS:
            all_q.extend(EXAM_QUESTIONS[t]['mcq'])

    return all_q

def display_question(question, question_num, total):
    """Display a single question"""
    st.markdown(f"**Question {question_num}/{total}**")
    st.markdown(f"**{question['q']}**")
    st.caption(f"📌 Ref: {question['ref']} | Difficulty: {question['difficulty'].upper()}")

    if question['type'] == 'MCQ':
        selected = st.radio(
            "Select your answer:",
            question['options'],
            key=f"q{question_num}"
        )
        return selected
    else:  # Structured
        response = st.text_area(
            "Write your answer (2-3 sentences):",
            key=f"q{question_num}",
            height=100
        )
        return response

def check_answer(question, user_answer):
    """Check if answer is correct"""
    if question['type'] == 'MCQ':
        return user_answer == question['answer']
    else:  # Structured - check if key terms present
        answer_lower = question['answer'].lower()
        response_lower = user_answer.lower()
        # Simple check: if key terms from answer appear in response
        key_terms = [word for word in answer_lower.split() if len(word) > 3]
        matches = sum(1 for term in key_terms if term in response_lower)
        return matches >= max(2, len(key_terms) // 2)  # At least 50% of key terms

def show_home():
    """Home page"""
    st.title("🧪 AANYA'S SCIENCE EXAM PREP")
    st.subheader("Term 2 Review - Comprehensive Training")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("📚 Topics", "3", "Water, Reproduction, Electrical")
        st.metric("❓ Questions", "38+", "MCQ + Structured")
    with col2:
        st.metric("⏱️ Exam Time", "45 min", "Official format")
        st.metric("🎓 Difficulty", "PSLE", "Hard training")

    st.markdown("---")
    st.write("**Choose your training mode:**")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📖 Topic Practice", use_container_width=True):
            st.session_state.mode = 'topic_select'
            st.rerun()

    with col2:
        if st.button("🎯 Full Mock Exam (45 min)", use_container_width=True):
            st.session_state.mode = 'mock_exam'
            st.session_state.exam_started = True
            st.session_state.exam_start_time = time.time()
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()

    with col3:
        if st.button("🚀 Challenge Mode", use_container_width=True):
            st.session_state.mode = 'challenge'
            st.rerun()

    st.markdown("---")
    st.info("💡 **Tip**: Start with Topic Practice to build confidence, then take the Mock Exam for realistic training!")

def show_topic_select():
    """Topic selection page"""
    st.title("📖 Topic Practice Mode")
    st.write("Master each topic before the exam!")

    topics = {
        '💧 Cycles in Water': 'Water_Cycles',
        '👶 Reproduction': 'Reproduction',
        '⚡ Electrical Systems': 'Electrical_Systems'
    }

    cols = st.columns(3)
    for idx, (name, key) in enumerate(topics.items()):
        with cols[idx]:
            if st.button(name, use_container_width=True, key=f"topic_{key}"):
                st.session_state.mode = 'practice'
                st.session_state.current_topic = key
                st.session_state.current_question_idx = 0
                st.session_state.score = 0
                st.session_state.answers = {}
                st.rerun()

    if st.button("← Back to Home"):
        st.session_state.mode = 'home'
        st.rerun()

def show_practice_mode():
    """Practice mode for single topic"""
    topic = st.session_state.current_topic
    topic_name = {'Water_Cycles': 'Cycles in Water', 'Reproduction': 'Reproduction', 'Electrical_Systems': 'Electrical Systems'}[topic]

    st.title(f"📖 {topic_name} Practice")

    questions = EXAM_QUESTIONS[topic]['mcq']
    current_idx = st.session_state.current_question_idx

    if current_idx >= len(questions):
        show_topic_results(topic, questions)
        return

    question = questions[current_idx]

    # Progress bar
    progress = (current_idx + 1) / len(questions)
    st.progress(progress)

    # Display question
    with st.container(border=True):
        user_answer = display_question(question, current_idx + 1, len(questions))

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=(current_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        if st.button("✓ Check Answer", use_container_width=True):
            if user_answer:
                is_correct = check_answer(question, user_answer)
                if is_correct:
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                    MalteseDogFeedback.show_happy_maltese("Aanya")
                else:
                    st.error("❌ Incorrect")
                    st.info(f"**Correct Answer**: {question['answer']}")
                    MalteseDogFeedback.show_sad_maltese("Aanya")

                st.session_state.answers[current_idx] = {
                    'question': question['q'],
                    'user_answer': user_answer,
                    'correct_answer': question['answer'],
                    'is_correct': is_correct
                }

    with col3:
        if st.button("Next ➡️", disabled=(current_idx >= len(questions) - 1)):
            st.session_state.current_question_idx += 1
            st.rerun()

def show_topic_results(topic, questions):
    """Show results for topic practice"""
    st.title("📊 Topic Results")

    topic_name = {'Water_Cycles': 'Cycles in Water', 'Reproduction': 'Reproduction', 'Electrical_Systems': 'Electrical Systems'}[topic]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score", f"{st.session_state.score}/{len(questions)}")
    with col2:
        percentage = (st.session_state.score / len(questions)) * 100
        st.metric("Percentage", f"{percentage:.0f}%")
    with col3:
        if percentage >= 80:
            st.metric("Grade", "🟢 Excellent")
        elif percentage >= 60:
            st.metric("Grade", "🟡 Good")
        else:
            st.metric("Grade", "🔴 Need Review")

    st.markdown("---")
    st.write("**Review your answers:**")

    for idx, answer in st.session_state.answers.items():
        with st.expander(f"Q{idx+1}: {answer['question'][:50]}..."):
            if answer['is_correct']:
                st.success("✅ Correct")
            else:
                st.error("❌ Incorrect")
                st.write(f"**Your answer**: {answer['user_answer']}")
                st.write(f"**Correct answer**: {answer['correct_answer']}")

    if st.button("← Back to Topics"):
        st.session_state.mode = 'topic_select'
        st.rerun()

def show_mock_exam():
    """Full 45-minute mock exam"""
    st.title("🎯 MOCK EXAM - 45 Minutes")

    # Timer
    elapsed = time.time() - st.session_state.exam_start_time
    remaining = max(0, 2700 - elapsed)  # 45 min = 2700 sec

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("All 3 topics (38+ questions)")
    with col2:
        if remaining > 0:
            mins = int(remaining // 60)
            secs = int(remaining % 60)
            st.metric("Time Remaining", f"{mins}:{secs:02d}", delta=-5)
            if remaining < 300:  # Less than 5 min
                st.warning("⚠️ Time running out!")
        else:
            st.error("⏰ TIME'S UP!")
            show_mock_results()
            return
    with col3:
        st.metric("Questions", f"{st.session_state.current_question_idx + 1}/38")

    # Get all questions
    all_questions = get_all_questions()

    if st.session_state.current_question_idx >= len(all_questions):
        show_mock_results()
        return

    question = all_questions[st.session_state.current_question_idx]

    st.markdown("---")
    with st.container(border=True):
        user_answer = display_question(
            question,
            st.session_state.current_question_idx + 1,
            len(all_questions)
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅️ Previous", disabled=(st.session_state.current_question_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        if st.button("✓ Submit Answer", use_container_width=True):
            if user_answer:
                is_correct = check_answer(question, user_answer)
                if is_correct:
                    st.session_state.score += 1
                    st.success("✅ Correct!")
                else:
                    st.info(f"**Answer**: {question['answer']}")

                st.session_state.answers[st.session_state.current_question_idx] = {
                    'question': question['q'],
                    'user_answer': user_answer,
                    'correct_answer': question['answer'],
                    'is_correct': is_correct
                }
                time.sleep(1)

    with col3:
        if st.button("Next ➡️"):
            st.session_state.current_question_idx += 1
            st.rerun()

def show_mock_results():
    """Show mock exam results"""
    all_questions = get_all_questions()
    st.title("📊 EXAM RESULTS")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Final Score", f"{st.session_state.score}/{len(all_questions)}")
    with col2:
        percentage = (st.session_state.score / len(all_questions)) * 100
        st.metric("Percentage", f"{percentage:.1f}%")
    with col3:
        if percentage >= 80:
            grade = "🟢 EXCELLENT"
        elif percentage >= 70:
            grade = "🟡 GOOD"
        elif percentage >= 60:
            grade = "🟠 FAIR"
        else:
            grade = "🔴 NEEDS WORK"
        st.metric("Grade", grade)
    with col4:
        st.metric("Questions Done", len(st.session_state.answers))

    st.markdown("---")

    if percentage >= 80:
        st.success("🎉 Excellent! You're ready for the exam!")
        MalteseDogFeedback.show_happy_maltese("Aanya")
    elif percentage >= 70:
        st.info("👍 Good! Review weak topics for polish.")
    else:
        st.warning("⚠️ Review failed topics before exam!")
        MalteseDogFeedback.show_sad_maltese("Aanya")

    # Detailed review
    st.write("**Detailed Review:**")
    col1, col2 = st.columns(2)

    correct_count = 0
    incorrect_count = 0

    with col1:
        for idx, answer in st.session_state.answers.items():
            if answer['is_correct']:
                correct_count += 1
                st.success(f"✅ Q{idx+1}: {answer['question'][:40]}...")

    with col2:
        for idx, answer in st.session_state.answers.items():
            if not answer['is_correct']:
                incorrect_count += 1
                st.error(f"❌ Q{idx+1}: {answer['question'][:40]}...")

    st.markdown("---")

    if st.button("📥 Download Results"):
        st.write("Save your results:")
        results_text = f"""
AANYA'S EXAM PREP RESULTS
========================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

SCORE: {st.session_state.score}/{len(all_questions)} ({percentage:.1f}%)
GRADE: {grade}

CORRECT: {correct_count}
INCORRECT: {incorrect_count}

Next Steps: {
    'Great work! You\'re ready!' if percentage >= 80
    else 'Review and practice weak areas'
}
"""
        st.download_button(
            label="Download Text Report",
            data=results_text,
            file_name=f"exam_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

    if st.button("🔄 Try Again"):
        st.session_state.exam_started = False
        st.session_state.mode = 'home'
        st.session_state.current_question_idx = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.rerun()

# ==================== MAIN APP ====================

def main():
    st.set_page_config(
        page_title="Aanya's Exam Prep",
        page_icon="🧪",
        layout="wide"
    )

    initialize_session()

    # Navigation
    if st.session_state.mode == 'home':
        show_home()
    elif st.session_state.mode == 'topic_select':
        show_topic_select()
    elif st.session_state.mode == 'practice':
        show_practice_mode()
    elif st.session_state.mode == 'mock_exam':
        show_mock_exam()

if __name__ == "__main__":
    main()
