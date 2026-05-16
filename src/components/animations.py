import streamlit as st
import base64
import json

class AnimationStyles:
    """CSS animations and visual effects"""

    CUSTOM_CSS = """
    <style>
    /* Smooth transitions */
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .slide-in-left {
        animation: slideInLeft 0.5s ease-out;
    }

    @keyframes slideInLeft {
        from { transform: translateX(-100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .slide-in-right {
        animation: slideInRight 0.5s ease-out;
    }

    @keyframes slideInRight {
        from { transform: translateX(100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    /* Card flip animation */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 250px;
        perspective: 1000px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }

    .flip-card-inner.flipped {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        border-radius: 10px;
    }

    .flip-card-front {
        background-color: #3498db;
        color: white;
    }

    .flip-card-back {
        background-color: #2ecc71;
        color: white;
        transform: rotateY(180deg);
    }

    /* Pulsing badge */
    .pulse-badge {
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 107, 107, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0); }
    }

    /* Glowing button */
    .glow-button {
        animation: glow 2s ease-in-out infinite;
    }

    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px #ff6b6b; }
        50% { box-shadow: 0 0 20px #ff6b6b; }
    }

    /* Bounce animation */
    .bounce {
        animation: bounce 0.6s ease-out;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    /* Spin animation for loading */
    .spin {
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* Rainbow text */
    .rainbow-text {
        background: linear-gradient(90deg, #ff6b6b, #ffa502, #2ecc71, #3498db, #e74c3c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: bold;
    }

    /* Gradient progress bar */
    .gradient-bar {
        background: linear-gradient(90deg, #ff6b6b, #ffa502, #2ecc71);
        height: 10px;
        border-radius: 5px;
    }

    /* Maltese dog animations */
    @keyframes jump {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-30px); }
    }

    @keyframes wag {
        0%, 100% { transform: rotateZ(0deg); }
        25% { transform: rotateZ(15deg); }
        75% { transform: rotateZ(-15deg); }
    }

    @keyframes cry {
        0%, 100% { opacity: 0; transform: translateY(-20px); }
        50% { opacity: 1; transform: translateY(10px); }
    }

    @keyframes fallTears {
        0% { opacity: 0; transform: translateY(-20px); }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { opacity: 0; transform: translateY(40px); }
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }

    @keyframes slideInCenter {
        from {
            opacity: 0;
            transform: scale(0.9) translateY(-20px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }

    /* Celebrate animation */
    @keyframes celebrate {
        0%, 100% { transform: scale(1) rotateZ(0deg); }
        25% { transform: scale(1.1) rotateZ(-5deg); }
        75% { transform: scale(1.1) rotateZ(5deg); }
    }
    </style>
    """

    @staticmethod
    def inject_styles():
        """Inject custom CSS into Streamlit app"""
        st.markdown(AnimationStyles.CUSTOM_CSS, unsafe_allow_html=True)

    @staticmethod
    def animated_header(text, emoji=""):
        """Display animated header"""
        html = f"""
        <div class="fade-in">
            <h1 style="text-align: center; color: #2c3e50;">
                {emoji} {text}
            </h1>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

    @staticmethod
    def animated_metric(label, value, emoji=""):
        """Display animated metric"""
        html = f"""
        <div class="slide-in-left" style="padding: 10px; border-radius: 10px; background-color: #ecf0f1; margin: 10px 0;">
            <h3 style="margin: 0; color: #3498db;">{emoji} {label}</h3>
            <h2 style="margin: 5px 0; color: #2c3e50;">{value}</h2>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

class ParticleEffects:
    """Create particle and visual effects"""

    @staticmethod
    def confetti_burst():
        """Show confetti celebration"""
        st.balloons()

    @staticmethod
    def celebrate_achievement():
        """Show achievement celebration"""
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="font-size: 48px;">🎉🎊🏆🎉🎊</h1>
            <h2 style="color: #ff6b6b; animation: bounce 0.6s ease-out;">Achievement Unlocked!</h2>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

    @staticmethod
    def show_particle_effect(effect_type='stars'):
        """Show different particle effects"""
        particles = {
            'stars': '✨ ⭐ ✨ ⭐ ✨',
            'sparkles': '💫 💫 💫 💫 💫',
            'hearts': '💚 💛 💜 💗 💖',
            'celebration': '🎉 🎊 🎈 🎁 🏆'
        }
        st.markdown(f"<h1 style='text-align: center; animation: bounce 0.6s ease-out;'>{particles.get(effect_type, particles['sparkles'])}</h1>", unsafe_allow_html=True)

    @staticmethod
    def animated_progress_bar(progress, color='#ff6b6b'):
        """Display animated progress bar"""
        progress = min(max(progress, 0), 1)
        html = f"""
        <div style="width: 100%; background-color: #ecf0f1; border-radius: 10px; overflow: hidden; margin: 10px 0;">
            <div class="gradient-bar" style="width: {progress*100}%; transition: width 0.5s ease-out;"></div>
        </div>
        <p style="text-align: center; color: #2c3e50;"><strong>{int(progress*100)}%</strong></p>
        """
        st.markdown(html, unsafe_allow_html=True)

class MalteseDogFeedback:
    """Enhanced Maltese dog feedback system with emotional animations"""

    @staticmethod
    def show_feedback(is_correct, student_name="Aanya", score_percentage=0, animate=True):
        """Show Maltese dog feedback based on answer correctness with animations"""
        if is_correct:
            MalteseDogFeedback.show_happy_maltese(student_name)
            st.balloons()
        else:
            MalteseDogFeedback.show_sad_maltese(student_name)

    @staticmethod
    def show_happy_maltese(student_name="Aanya"):
        """Display happy Maltese with jumping and celebration animation"""
        st.markdown("""
        <style>
        .happy-maltese-container {
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            border-radius: 20px;
            border: 3px solid #FFD700;
            animation: slideInCenter 0.6s ease-out;
        }

        .maltese-emoji {
            font-size: 80px;
            display: inline-block;
            animation: jump 0.8s ease-in-out infinite;
        }

        .tail-wag {
            animation: wag 0.6s ease-in-out infinite;
        }

        .celebration-message {
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-top: 15px;
            animation: fadeIn 0.8s ease-in;
        }

        .celebration-stars {
            font-size: 40px;
            animation: spin 2s linear infinite;
        }
        </style>

        <div class="happy-maltese-container">
            <div class="maltese-emoji">🐕</div>
            <div class="celebration-message">
                🎉 WOOF WOOF! BRILLIANT """ + student_name + """! 🎉
            </div>
            <div style="font-size: 24px; margin-top: 10px;">
                ✨ 🐾 ✨ 🎊 🏆 🎊 ✨ 🐾 ✨
            </div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def show_sad_maltese(student_name="Aanya"):
        """Display sad Maltese with crying animation"""
        st.markdown("""
        <style>
        .sad-maltese-container {
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #87CEEB 0%, #B0E0E6 100%);
            border-radius: 20px;
            border: 3px solid #4169E1;
            animation: slideInCenter 0.6s ease-out;
        }

        .sad-maltese-emoji {
            font-size: 80px;
            display: inline-block;
            animation: shake 0.6s ease-in-out;
        }

        .teardrops {
            font-size: 30px;
            animation: fallTears 1.5s ease-in infinite;
        }

        .sad-message {
            color: #4169E1;
            font-size: 24px;
            font-weight: bold;
            margin-top: 15px;
            animation: fadeIn 0.8s ease-in;
        }

        .encouragement {
            color: #4169E1;
            font-size: 18px;
            margin-top: 10px;
            animation: fadeIn 1s ease-in;
        }
        </style>

        <div class="sad-maltese-container">
            <div class="sad-maltese-emoji">🐕</div>
            <div class="teardrops">💧 💧</div>
            <div class="sad-message">
                Ohhh no, """ + student_name + """! 😢
            </div>
            <div class="encouragement">
                But you'll get it next time! 💪
            </div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def show_pet_evolution(level):
        """Show pet evolution based on level"""
        pet_states = {
            'baby': ('🐕 Baby Sparky', 'Level 1-10'),
            'happy': ('🐕‍🦺 Happy Sparky', 'Level 11-25'),
            'champion': ('🏆 Champion Sparky', 'Level 26-50'),
            'legendary': ('👑 Legendary Sparky', 'Level 50+'),
        }

        if level >= 50:
            state = 'legendary'
        elif level >= 26:
            state = 'champion'
        elif level >= 11:
            state = 'happy'
        else:
            state = 'baby'

        pet_name, level_range = pet_states[state]
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; border: 2px solid #3498db; border-radius: 10px;">
            <h1 style="font-size: 64px; margin: 0;">{pet_name.split()[0]}</h1>
            <h3 style="color: #3498db; margin: 0;">{pet_name.split()[1] if len(pet_name.split()) > 1 else pet_name}</h3>
            <p style="color: #7f8c8d;">{level_range}</p>
        </div>
        """, unsafe_allow_html=True)

class TransitionAnimations:
    """Handle page transitions and content reveals"""

    @staticmethod
    def animated_section(title, content_func, emoji=""):
        """Display section with animation"""
        st.markdown(f"""
        <div class="slide-in-left" style="padding: 20px; border-left: 4px solid #3498db; background-color: #ecf0f1; margin: 20px 0; border-radius: 5px;">
            <h2>{emoji} {title}</h2>
        </div>
        """, unsafe_allow_html=True)
        content_func()

    @staticmethod
    def reveal_answer(question, answer, explanation=""):
        """Reveal answer with animation"""
        st.markdown(f"""
        <div style="padding: 15px; background-color: #2ecc71; border-radius: 10px; margin: 10px 0; animation: fadeIn 0.5s ease-in;">
            <h4 style="color: white; margin: 0;">✅ Correct Answer</h4>
            <p style="color: white; margin: 5px 0; font-weight: bold;">{answer}</p>
            {f'<p style="color: white; margin: 5px 0; font-size: 0.9em;">{explanation}</p>' if explanation else ''}
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def show_quiz_intro(chapter_name):
        """Show animated quiz introduction"""
        st.markdown(f"""
        <div class="fade-in" style="text-align: center; padding: 30px;">
            <h1 style="color: #3498db; font-size: 36px;">🚀 Ready to Learn?</h1>
            <h2 style="color: #2c3e50;">{chapter_name}</h2>
            <p style="color: #7f8c8d; font-size: 18px;">Answer questions to earn XP and unlock achievements!</p>
        </div>
        """, unsafe_allow_html=True)

class LottieAnimation:
    """Integrate Lottie animations"""

    @staticmethod
    def load_lottie_animation(url_or_path):
        """Load and display Lottie animation"""
        try:
            import requests
            import streamlit_lottie
            if url_or_path.startswith('http'):
                animation = requests.get(url_or_path).json()
            else:
                with open(url_or_path, 'r') as f:
                    animation = json.load(f)
            # Note: streamlit-lottie requires specific setup
            # This is a placeholder for the integration
            return animation
        except Exception as e:
            st.warning(f"Could not load animation: {e}")
            return None

    @staticmethod
    def show_loading_spinner():
        """Show loading spinner animation"""
        st.markdown("""
        <div style="text-align: center;">
            <h2>Loading...</h2>
            <p>⏳</p>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def show_success_animation():
        """Show success animation"""
        st.markdown("""
        <div style="text-align: center; animation: bounce 0.6s ease-out;">
            <h1 style="font-size: 64px; color: #2ecc71;">✅</h1>
            <h2 style="color: #2ecc71;">Success!</h2>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
