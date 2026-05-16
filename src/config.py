"""
Configuration file for Aanya's Science Quest Phase 2
Personalization settings for student, school, and app preferences
"""

# ==================== STUDENT PROFILE ====================
STUDENT_NAME = "Aanya"
STUDENT_EMOJI = "👧"
STUDENT_AGE = 10

# ==================== SCHOOL INFORMATION ====================
SCHOOL_NAME = "Waterway Primary School"
SCHOOL_LOCATION = "Punggol, Singapore"
SCHOOL_EMOJI = "📍"
SCHOOL_REGION = "Tampines"
CURRICULUM = "MOE Primary 5 Science"

# ==================== PERSONALIZED MESSAGES ====================
MESSAGES = {
    'welcome': f"🌟 Welcome, {STUDENT_NAME}! Ready to master science? 🌟",
    'home_header': f"🌟 {STUDENT_NAME}'s Science Quest - Waterway Primary Edition",
    'dashboard_location': f"{SCHOOL_EMOJI} {SCHOOL_NAME}, {SCHOOL_LOCATION}",
    'chapter_intro': lambda topic: f"{STUDENT_NAME} from Waterway Primary learns about {topic}...",
    'quiz_complete': lambda xp: f"Excellent work, {STUDENT_NAME}! You earned {xp} XP! 🎉",
    'achievement_unlock': lambda badge: f"{STUDENT_NAME} becomes a {badge}! 👑",
    'daily_challenge': f"{STUDENT_NAME}, complete today's challenge for 20 XP!",
    'streak_milestone': lambda days: f"{STUDENT_NAME} is on fire! 🔥 {days}-day streak!",
    'chapter_master': lambda chapter: f"{STUDENT_NAME} - Waterway Primary {chapter} Master! 📚",
    'school_champion': f"Waterway Primary Science Champion! 🏆",
    'legend_status': f"🌟 WATERWAY PRIMARY LEGEND! 👑",
    'perfect_score': f"{STUDENT_NAME} achieved PERFECT SCORE! 💯",
    'maltese_happy': f"WOOF WOOF! BRILLIANT {STUDENT_NAME}! 🐾",
    'maltese_sad': f"Ohhh no, {STUDENT_NAME}! Try again! 🐕",
}

# ==================== MALTESE DOG FEEDBACK ====================
MALTESE_CONFIG = {
    'happy': {
        'emoji': '🐕',
        'expression': 'Happy',
        'color': '#FFD700',  # Gold
        'animation': 'jump',
        'sound': 'celebration',  # Optional
        'message_prefix': '🎉',
        'tail_wag': True,
    },
    'sad': {
        'emoji': '🐕',
        'expression': 'Sad',
        'color': '#87CEEB',  # Sky blue
        'animation': 'cry',
        'sound': 'whimper',  # Optional
        'message_prefix': '😢',
        'head_shake': True,
    }
}

# ==================== DIFFICULTY SETTINGS ====================
DIFFICULTY_LEVELS = {
    'beginner': {
        'emoji': '🟡',
        'label': 'Beginner',
        'target_audience': 'Initial learning',
        'xp_multiplier': 1.0,
        'estimated_time': '5-10 min',
        'content_scope': 'Flashcards + matching + basic MCQ',
    },
    'intermediate': {
        'emoji': '🟠',
        'label': 'Intermediate',
        'target_audience': 'Consolidation',
        'xp_multiplier': 1.5,
        'estimated_time': '15-20 min',
        'content_scope': 'Flashcards + MCQ + 1 mini-game + 10 brain drainers',
    },
    'advanced': {
        'emoji': '🔴',
        'label': 'Advanced',
        'target_audience': 'Mastery + Exam Prep',
        'xp_multiplier': 2.0,
        'estimated_time': '25-40 min',
        'content_scope': 'All content + full brain drainer set + timed challenges',
    }
}

# ==================== CHAPTER CONFIGURATION ====================
CHAPTERS = {
    'Ch1_Reproduction': {
        'title': '🌱 Chapter 1: Reproduction in Animals & Plants',
        'emoji': '🌱',
        'description': 'Pollination, fertilization, seed dispersal, germination, and animal reproduction',
        'color': '#2ECC71',  # Green
    },
    'Ch2_Water': {
        'title': '💧 Chapter 2: Cycles in Water',
        'emoji': '💧',
        'description': 'States of matter, phase changes, evaporation, condensation, and the water cycle',
        'color': '#3498DB',  # Blue
    },
    'Ch3_Plant': {
        'title': '🌿 Chapter 3: Plant Transport',
        'emoji': '🌿',
        'description': 'Xylem, phloem, water transport, food transport, and transpiration',
        'color': '#27AE60',  # Dark Green
    },
    'Ch4_Human': {
        'title': '❤️ Chapter 4: Human Systems',
        'emoji': '❤️',
        'description': 'Respiratory system, circulatory system, and gaseous exchange',
        'color': '#E74C3C',  # Red
    },
    'Ch5_Electrical': {
        'title': '⚡ Chapter 5: Electrical Systems',
        'emoji': '⚡',
        'description': 'Circuits, batteries, conductors, insulators, and switches',
        'color': '#F39C12',  # Orange
    },
    'Ch6_Circuits': {
        'title': '🔌 Chapter 6: Electric Circuits',
        'emoji': '🔌',
        'description': 'Series and parallel circuits, circuit diagrams, and problem-solving',
        'color': '#E67E22',  # Dark Orange
    },
}

# ==================== ACHIEVEMENT BADGES ====================
ACHIEVEMENT_BADGES = {
    'first_steps': {'name': 'First Steps', 'icon': '👶', 'requirement': 'Complete first quiz'},
    'chapter_master': {'name': 'Chapter Master', 'icon': '📚', 'requirement': '90%+ mastery in chapter'},
    'brain_drainer_10': {'name': 'Brain Drainer 10', 'icon': '🧠', 'requirement': '10 correct brain drainers'},
    'brain_drainer_master': {'name': 'Brain Drainer Master', 'icon': '🧠💪', 'requirement': '50 correct brain drainers'},
    'week_warrior': {'name': 'Week Warrior', 'icon': '🔥', 'requirement': '7-day learning streak'},
    'speedrunner': {'name': 'Speedrunner', 'icon': '⚡', 'requirement': 'Complete quiz in 2 minutes'},
    'perfect_score': {'name': 'Perfect Score', 'icon': '💯', 'requirement': '100% on any quiz'},
    'all_rounder': {'name': 'All-Rounder', 'icon': '🌟', 'requirement': '80%+ mastery in all 6 chapters'},
    'pollinator_expert': {'name': 'Pollinator Expert', 'icon': '🐝', 'requirement': 'Complete Ch1 Lab 1'},
    'seed_scientist': {'name': 'Seed Scientist', 'icon': '🌱', 'requirement': 'Complete Ch1 Lab 2'},
    'twin_expert': {'name': 'Twin Expert', 'icon': '👯', 'requirement': 'Complete Ch1 Lab 3'},
    'circuit_master': {'name': 'Circuit Master', 'icon': '⚡', 'requirement': 'Complete Ch6 Lab 1'},
    'troubleshooter': {'name': 'Troubleshooter', 'icon': '🔧', 'requirement': 'Complete Ch6 Lab 3'},
    'waterway_champion': {'name': 'Waterway Primary Champion', 'icon': '🏆', 'requirement': 'Unlock 10+ badges'},
    'legend': {'name': 'Waterway Primary Legend', 'icon': '👑', 'requirement': 'Reach level 50'},
}

# ==================== XP SYSTEM ====================
XP_CONFIG = {
    'base_xp_per_level': 100,
    'level_multiplier': 1.1,
    'max_levels': 50,
    'daily_login_bonus': 5,
    'daily_challenge_reward': 20,
    'quiz_rewards': {
        'beginner': 15,
        'intermediate': 25,
        'advanced': 50,
    },
    'brain_drainer_reward_correct': 20,
    'brain_drainer_reward_incorrect': 10,
    'minigame_reward': {
        'beginner': 30,
        'intermediate': 40,
        'advanced': 50,
    }
}

# ==================== STREAK SETTINGS ====================
STREAK_CONFIG = {
    'daily_login_bonus': 5,
    'streak_freeze_cost': 10,  # XP cost to freeze streak for 1 day
    'milestone_rewards': {
        3: {'name': '3-day Streak', 'bonus_xp': 25},
        7: {'name': 'Week Warrior', 'bonus_xp': 50},
        14: {'name': '2-Week Champion', 'bonus_xp': 100},
        30: {'name': 'Month Master', 'bonus_xp': 200},
    }
}

# ==================== INTERACTIVE LAB SETTINGS ====================
INTERACTIVE_LABS = {
    'Ch1_Reproduction': {
        'Lab1_Pollination': {
            'name': '🌸 Flower Pollination Simulator',
            'difficulty': 'medium',
            'xp_reward': 50,
            'badge': 'pollinator_expert',
        },
        'Lab2_Germination': {
            'name': '🌱 Seed Germination Timeline',
            'difficulty': 'easy',
            'xp_reward': 40,
            'badge': 'seed_scientist',
        },
        'Lab3_Twins': {
            'name': '👯 Twin Formation Visualizer',
            'difficulty': 'hard',
            'xp_reward': 60,
            'badge': 'twin_expert',
        },
    },
    'Ch6_Circuits': {
        'Lab1_CircuitBuilder': {
            'name': '🔌 Dynamic Circuit Builder',
            'difficulty': 'hard',
            'xp_reward': 75,
            'badge': 'circuit_master',
        },
        'Lab2_Comparison': {
            'name': '🔋 Series vs Parallel Comparison',
            'difficulty': 'medium',
            'xp_reward': 50,
            'badge': None,
        },
        'Lab3_Troubleshooting': {
            'name': '⚡ Break the Circuit Game',
            'difficulty': 'medium',
            'xp_reward': 40,
            'badge': 'troubleshooter',
        },
        'Lab4_VoltageChallenge': {
            'name': '🎯 Voltage Drop Challenge',
            'difficulty': 'hard',
            'xp_reward': 60,
            'badge': None,
        },
    }
}

# ==================== THEME & UI SETTINGS ====================
THEMES = {
    'colorful': {
        'name': 'Colorful (Default)',
        'primary_color': '#3498DB',
        'secondary_color': '#2ECC71',
        'accent_color': '#E74C3C',
    },
    'dark': {
        'name': 'Dark Mode',
        'primary_color': '#1C1C1C',
        'secondary_color': '#333333',
        'accent_color': '#FFD700',
    },
    'light': {
        'name': 'Light Mode',
        'primary_color': '#FFFFFF',
        'secondary_color': '#F5F5F5',
        'accent_color': '#2ECC71',
    }
}

ANIMATION_INTENSITIES = ['minimal', 'moderate', 'full']

# ==================== HELPER FUNCTIONS ====================

def get_student_message(message_key, *args):
    """Get personalized message for the student"""
    if message_key in MESSAGES:
        msg = MESSAGES[message_key]
        if callable(msg):
            return msg(*args)
        return msg
    return f"Welcome, {STUDENT_NAME}!"

def get_difficulty_config(difficulty):
    """Get configuration for a difficulty level"""
    return DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS['beginner'])

def get_chapter_config(chapter_key):
    """Get configuration for a chapter"""
    return CHAPTERS.get(chapter_key, {})

def get_xp_for_level(level):
    """Calculate XP needed to reach a specific level"""
    return int(XP_CONFIG['base_xp_per_level'] * (XP_CONFIG['level_multiplier'] ** (level - 1)))

# ==================== EXPORT ====================
__all__ = [
    'STUDENT_NAME',
    'SCHOOL_NAME',
    'SCHOOL_LOCATION',
    'MESSAGES',
    'MALTESE_CONFIG',
    'DIFFICULTY_LEVELS',
    'CHAPTERS',
    'ACHIEVEMENT_BADGES',
    'XP_CONFIG',
    'STREAK_CONFIG',
    'INTERACTIVE_LABS',
    'THEMES',
    'ANIMATION_INTENSITIES',
    'get_student_message',
    'get_difficulty_config',
    'get_chapter_config',
    'get_xp_for_level',
]
