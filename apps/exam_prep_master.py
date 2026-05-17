"""
AANYA'S SCIENCE EXAM PREP MASTER - Phase 2 Complete Edition
Version 4.0: Unified Comprehensive Learning + Exam Preparation
Features: All 6 chapters, multi-user support, gamification, SQLite persistence, admin tools
"""

import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import sys
from pathlib import Path
import json
import sqlite3
import random

# Add src folder to path for imports (app is in apps/, src is in parent)
src_path = str(Path(__file__).parent.parent / "src")
sys.path.insert(0, src_path)

from components.animations import MalteseDogFeedback
from utils.database import (
    init_database, get_or_create_user, get_all_users, create_quiz_session,
    save_answer, end_quiz_session, get_user_sessions, get_user_stats,
    get_user_performance_by_difficulty, get_user_performance_by_concept,
    get_user_weak_areas, export_user_data_csv, init_user_gamification,
    add_xp, get_user_xp_and_level, update_streak, unlock_achievement,
    get_user_achievements, update_chapter_progress, get_chapter_progress,
    save_minigame_score
)

# Initialize database on app load
init_database()

# Database path (consistent with database.py)
DB_PATH = Path(__file__).parent.parent / "src" / "data" / "app.db"

# ==================== CHAPTER FLASHCARDS & MATCHING PAIRS ====================

CHAPTER_FLASHCARDS = {
    'Water_Cycles': [
        {'concept': 'Evaporation', 'definition': 'Process where liquid water changes to water vapor (gas) due to heat'},
        {'concept': 'Condensation', 'definition': 'Process where water vapor cools and changes back to liquid water'},
        {'concept': 'Precipitation', 'definition': 'Water falling from clouds as rain, snow, sleet, or hail'},
        {'concept': 'Melting', 'definition': 'Process where solid ice changes to liquid water when temperature rises above 0°C'},
        {'concept': 'Freezing', 'definition': 'Process where liquid water changes to solid ice when temperature drops below 0°C'},
        {'concept': 'Water Vapor', 'definition': 'Invisible gaseous form of water present in the air'},
        {'concept': 'Steam', 'definition': 'Visible water vapor that forms when boiling water rises and cools slightly'},
        {'concept': 'Water Cycle', 'definition': 'Continuous process of evaporation, condensation, and precipitation'},
        {'concept': 'Boiling', 'definition': 'Rapid evaporation that occurs at 100°C, with bubbles forming throughout liquid'},
        {'concept': 'Latent Heat', 'definition': 'Energy required for phase change without temperature change (e.g., melting or boiling)'},
    ],
    'Reproduction': [
        {'concept': 'Pollination', 'definition': 'Transfer of pollen from anther to stigma of a flower'},
        {'concept': 'Fertilization', 'definition': 'Fusion of male and female gametes to form a zygote'},
        {'concept': 'Seed Dispersal', 'definition': 'Spreading of seeds away from the parent plant'},
        {'concept': 'Germination', 'definition': 'Growth of a seed into a young plant'},
        {'concept': 'Reproduction', 'definition': 'Process of producing new organisms'},
        {'concept': 'Sexual Reproduction', 'definition': 'Reproduction requiring male and female gametes'},
        {'concept': 'Asexual Reproduction', 'definition': 'Reproduction without the need for a partner'},
        {'concept': 'Gametes', 'definition': 'Sex cells (sperm and egg)'},
    ],
    'Electrical_Systems': [
        {'concept': 'Voltage', 'definition': 'Electric potential difference measured in volts (V); the "push" that moves electrons'},
        {'concept': 'Current', 'definition': 'Flow of electric charge measured in amperes (A); amount of electrons moving through a wire'},
        {'concept': 'Resistance', 'definition': 'Opposition to current flow measured in ohms (Ω); how much a material opposes electric flow'},
        {'concept': 'Circuit', 'definition': 'Complete closed path that allows electric current to flow from + to - terminal'},
        {'concept': 'Conductor', 'definition': 'Material that allows electric current to flow easily (e.g., copper, aluminum)'},
        {'concept': 'Insulator', 'definition': 'Material that prevents or blocks electric current flow (e.g., rubber, plastic, wood)'},
        {'concept': 'Series Circuit', 'definition': 'Circuit where components are connected in a single path; same current flows through all'},
        {'concept': 'Parallel Circuit', 'definition': 'Circuit where components have separate paths; current can flow through multiple routes'},
    ],
    'Plant_Transport': [
        {'concept': 'Plant Transport System', 'definition': 'System that carries water, minerals, and food to all parts of a plant', 'ref': 'Page 52'},
        {'concept': 'Roots', 'definition': 'Plant part that absorbs water and mineral salts from soil', 'ref': 'Page 54'},
        {'concept': 'Root Hairs', 'definition': 'Tiny structures that increase surface area for water absorption', 'ref': 'Page 54'},
        {'concept': 'Xylem', 'definition': 'Water-carrying tubes; transports water and minerals from roots to leaves', 'ref': 'Pages 55-56'},
        {'concept': 'Phloem', 'definition': 'Food-carrying tubes; transports food (glucose) from leaves to all parts', 'ref': 'Pages 57-58'},
        {'concept': 'Mineral Salts', 'definition': 'Nutrients absorbed by roots and transported through xylem', 'ref': 'Page 55'},
        {'concept': 'Transpiration', 'definition': 'Process where water vapour escapes from leaves', 'ref': 'Page 59'},
        {'concept': 'Stem', 'definition': 'Plant part containing xylem and phloem tubes', 'ref': 'Pages 56-57'},
        {'concept': 'Leaves', 'definition': 'Plant part where food is made; loses water through transpiration', 'ref': 'Pages 57, 59'},
        {'concept': 'Photosynthesis', 'definition': 'Process where leaves make food using light and water', 'ref': 'Page 54'},
        {'concept': 'Woody Tubes', 'definition': 'Another name for xylem (appears as wood in stems)', 'ref': 'Page 55'},
        {'concept': 'Food Transport', 'definition': 'Movement of glucose from leaves to other plant parts through phloem', 'ref': 'Pages 57-58'},
        {'concept': 'Water Transport', 'definition': 'Movement of water from roots to all plant parts through xylem', 'ref': 'Pages 55-56'},
        {'concept': 'Bark Removal', 'definition': 'Cutting ring of bark removes phloem; plant above cut starves', 'ref': 'Page 59'},
        {'concept': 'Plant Wilting', 'definition': 'Plant droops when water-carrying tubes are cut; no water reaches leaves', 'ref': 'Page 60'},
    ],
    'Human_Systems': [
        {'concept': 'Air', 'definition': 'Mixture of gases including oxygen, nitrogen, carbon dioxide, and water vapour', 'ref': 'Page 65'},
        {'concept': 'Oxygen', 'definition': 'Gas in air that living things need to survive (about 21%)', 'ref': 'Page 65'},
        {'concept': 'Carbon Dioxide', 'definition': 'Gas produced by living things; about 0.04% inhaled, 4.4% exhaled', 'ref': 'Pages 65, 70'},
        {'concept': 'Nose', 'definition': 'Allows air to enter and leave body; warms and moistens air; traps dust', 'ref': 'Page 69'},
        {'concept': 'Windpipe (Trachea)', 'definition': 'Carries air to and from lungs', 'ref': 'Page 69'},
        {'concept': 'Lungs', 'definition': 'Main respiratory organs where gaseous exchange happens', 'ref': 'Pages 69-71'},
        {'concept': 'Diaphragm', 'definition': 'Muscle below lungs that aids breathing by contracting and relaxing', 'ref': 'Page 70'},
        {'concept': 'Gaseous Exchange', 'definition': 'Oxygen enters blood, carbon dioxide leaves blood (in lungs)', 'ref': 'Page 71'},
        {'concept': 'Breathing', 'definition': 'Taking in air (inhale) and releasing air (exhale)', 'ref': 'Page 69'},
        {'concept': 'Heart', 'definition': 'Muscle that pumps blood to different parts of body', 'ref': 'Pages 75-76'},
        {'concept': 'Blood Vessels', 'definition': 'Tubes carrying blood; include arteries and veins', 'ref': 'Page 76'},
        {'concept': 'Pulse', 'definition': 'Heartbeat felt at wrist or neck; rhythm created by heart pumping', 'ref': 'Page 76'},
        {'concept': 'Heart Rate', 'definition': 'Number of times heart beats in one minute', 'ref': 'Page 76'},
        {'concept': 'Inhaled Air', 'definition': 'Air breathed in; contains 21% oxygen, 0.04% carbon dioxide', 'ref': 'Page 70'},
        {'concept': 'Exhaled Air', 'definition': 'Air breathed out; contains 16% oxygen, 4.4% carbon dioxide', 'ref': 'Page 70'},
    ],
    'Electric_Circuits': [
        {'concept': 'Series Circuit', 'definition': 'Single path for current; components connected one after another', 'ref': 'Pages 105-107'},
        {'concept': 'Voltage', 'definition': 'Electrical pressure provided by battery; measured in Volts', 'ref': 'Pages 108-110'},
        {'concept': 'Current', 'definition': 'Flow of electrical charge through circuit; measured in Amperes', 'ref': 'Page 109'},
        {'concept': 'Resistance', 'definition': 'Opposition to current flow; measured in Ohms (unit R)', 'ref': 'Pages 110-111'},
        {'concept': 'Ohm\'s Law', 'definition': 'V = I × R (Voltage equals Current times Resistance)', 'ref': 'Pages 108-110'},
        {'concept': 'More Batteries', 'definition': 'More voltage → More current → Brighter bulbs', 'ref': 'Pages 108-110'},
        {'concept': 'More Bulbs (Series)', 'definition': 'More resistance → Less current → Dimmer bulbs', 'ref': 'Pages 110-113'},
        {'concept': 'Total Resistance', 'definition': 'In series: R_total = R₁ + R₂ + R₃ (sum of all resistances)', 'ref': 'Pages 110-113'},
        {'concept': 'Voltage Drop', 'definition': 'Voltage divides among components in series circuit', 'ref': 'Page 110'},
        {'concept': 'Circuit Breaker', 'definition': 'Safety device that trips when current is too high, preventing fires', 'ref': 'Page 113'},
        {'concept': 'Electrical Overload', 'definition': 'Too many appliances drawing too much current', 'ref': 'Pages 113-114'},
        {'concept': 'Fuse', 'definition': 'Safety device that melts when current is too high', 'ref': 'Page 113'},
        {'concept': 'Energy Conservation', 'definition': 'Saving electricity by turning off devices and using less power', 'ref': 'Pages 114-115'},
        {'concept': 'Fossil Fuels', 'definition': 'Coal, oil, gas burned to generate electricity', 'ref': 'Page 115'},
        {'concept': 'Renewable Energy', 'definition': 'Energy from sun, wind, water that does not run out', 'ref': 'Page 115'},
    ],
}

CHAPTER_MATCHING_PAIRS = {
    'Water_Cycles': [
        ('Evaporation', 'Liquid water becoming water vapor'),
        ('Condensation', 'Water vapor becoming liquid water'),
        ('Precipitation', 'Water falling from clouds as rain or snow'),
        ('Melting', 'Ice becoming liquid water'),
        ('Freezing', 'Liquid water becoming ice'),
        ('Boiling', 'Rapid evaporation at 100°C'),
        ('Water Vapor', 'Invisible gaseous water in the air'),
        ('Steam', 'Visible water vapor from boiling or hot water'),
    ],
    'Reproduction': [
        ('Bee', 'Transfers pollen between flowers'),
        ('Wind', 'Carries pollen and seeds'),
        ('Water', 'Disperses aquatic seeds'),
        ('Animal', 'Eats fruit and spreads seeds'),
        ('Stamen', 'Male part of flower'),
        ('Stigma', 'Female part of flower'),
        ('Seed Coat', 'Protects the embryo'),
        ('Cotyledon', 'Stores food for growing seed'),
    ],
    'Electrical_Systems': [
        ('Copper', 'Good conductor of electricity'),
        ('Rubber', 'Good insulator of electricity'),
        ('Voltage', 'Electric potential difference (V)'),
        ('Current', 'Flow of electric charge (A)'),
        ('Series Circuit', 'Components in single path'),
        ('Parallel Circuit', 'Components in multiple paths'),
        ('Resistance', 'Opposition to current flow (Ω)'),
        ('Ampere', 'Unit of electric current'),
    ],
    'Plant_Transport': [
        ('Xylem', 'Carries water and minerals'),
        ('Phloem', 'Carries food (glucose)'),
        ('Roots', 'Absorb water and minerals'),
        ('Leaves', 'Make food; lose water'),
        ('Stem', 'Contains transport tubes'),
        ('Root Hairs', 'Increase absorption surface'),
        ('Transpiration', 'Water vapour from leaves'),
        ('Photosynthesis', 'Leaves make food'),
        ('Mineral Salts', 'Travel in xylem'),
        ('Water Transport', 'From roots to all parts'),
        ('Food Transport', 'From leaves to all parts'),
        ('Woody tubes', 'Xylem tubes'),
        ('Cutting phloem', 'Plant starves (no food below)'),
        ('Cutting xylem', 'Plant wilts (no water)'),
        ('Plant death', 'When both xylem and phloem removed'),
    ],
    'Human_Systems': [
        ('Oxygen', 'Gas needed for survival'),
        ('Carbon dioxide', 'Waste gas produced by living things'),
        ('Nose', 'Warms and moistens air'),
        ('Windpipe', 'Carries air to lungs'),
        ('Lungs', 'Gaseous exchange happens here'),
        ('Diaphragm', 'Muscle that aids breathing'),
        ('Breathing in', 'Inhale; diaphragm contracts'),
        ('Breathing out', 'Exhale; diaphragm relaxes'),
        ('Heart', 'Pumps blood'),
        ('Arteries', 'Carry oxygen-rich blood away'),
        ('Veins', 'Carry oxygen-poor blood back'),
        ('Pulse', 'Heartbeat rhythm'),
        ('Exercise', 'Increases breathing and heart rate'),
        ('Asthma', 'Narrowed airways due to swelling'),
        ('Smoking', 'Harms lungs and breathing'),
    ],
    'Electric_Circuits': [
        ('Series circuit', 'Single path for current'),
        ('Voltage', 'Electrical pressure from battery'),
        ('Current', 'Flow of electrical charge'),
        ('Resistance', 'Opposition to current flow'),
        ('Ohm\'s Law', 'V = I × R'),
        ('More batteries', 'Brighter bulbs'),
        ('More bulbs in series', 'Dimmer bulbs'),
        ('Total resistance', 'R₁ + R₂ + R₃'),
        ('Voltage drop', 'Voltage divides among bulbs'),
        ('Circuit breaker', 'Prevents electrical fires'),
        ('Fuse', 'Safety device that melts'),
        ('Overload', 'Too much current'),
        ('Energy conservation', 'Save electricity'),
        ('Fossil fuels', 'Coal, oil, gas for power'),
        ('Renewable energy', 'Never runs out'),
    ],
}

# ==================== TIER 1: QUESTION HISTORY & QUEUE TABLES ====================

def create_question_history_table():
    """Create question_history table to track user questions"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            chapter TEXT,
            quiz_mode TEXT,
            first_seen_date TEXT,
            last_seen_date TEXT,
            times_seen INTEGER DEFAULT 1,
            times_correct INTEGER DEFAULT 0,
            times_incorrect INTEGER DEFAULT 0,
            max_difficulty_attempted TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            UNIQUE(user_id, question_id, quiz_mode)
        )
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_user_quiz
        ON question_history(user_id, quiz_mode)
    """)

    conn.commit()
    conn.close()


def create_question_queue_table():
    """Create question_queue table to manage next questions"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_queue (
            queue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            chapter TEXT,
            queue_type TEXT,
            difficulty_level TEXT,
            added_date TEXT,
            priority INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_queue_user
        ON question_queue(user_id)
    """)

    conn.commit()
    conn.close()


# Initialize new tables on app load
create_question_history_table()
create_question_queue_table()

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
                'concept': 'Phase Changes',
                'difficulty': 'easy'
            },
            {
                'id': 'w2',
                'type': 'MCQ',
                'q': 'Which process happens when wet clothes dry?',
                'options': ['Melting', 'Freezing', 'Evaporation', 'Condensation'],
                'answer': 'Evaporation',
                'explanation': 'Evaporation is liquid water changing to gas (vapor) without boiling. Heat from sun provides energy.',
                'ref': 'Page 42',
                'concept': 'Evaporation',
                'difficulty': 'easy'
            },
            {
                'id': 'w3',
                'type': 'MCQ',
                'q': 'What is water vapor?',
                'options': ['Visible steam', 'Invisible gas', 'Liquid water', 'Ice crystals'],
                'answer': 'Invisible gas',
                'explanation': 'Water vapor is invisible gas in air. Steam (visible mist) forms when vapor cools.',
                'ref': 'Page 28',
                'concept': 'Water States',
                'difficulty': 'easy'
            },
            {
                'id': 'w4',
                'type': 'MCQ',
                'q': 'In the water cycle, evaporation is followed by:',
                'options': ['Rain immediately', 'Condensation', 'Freezing', 'More evaporation'],
                'answer': 'Condensation',
                'explanation': 'Water vapor rises, cools in atmosphere, and condenses into water droplets forming clouds.',
                'ref': 'Pages 43-44',
                'concept': 'Water Cycle',
                'difficulty': 'easy'
            },
            {
                'id': 'w5',
                'type': 'MCQ',
                'q': 'Why does salt remain when seawater evaporates?',
                'options': ['Evaporates slowly', 'Dissolves in vapor', 'Only water evaporates', 'Freezes first'],
                'answer': 'Only water evaporates',
                'explanation': 'Salt molecules do not evaporate at normal temperatures. Only water vapor escapes, leaving salt behind.',
                'ref': 'Page 43',
                'concept': 'Evaporation Purification',
                'difficulty': 'easy'
            },
        ],
        'medium': [
            {
                'id': 'w6',
                'type': 'MCQ',
                'q': 'Which is an example of condensation?',
                'options': ['Boiling water', 'Dew forming on grass', 'Salt crystals forming', 'Ice melting'],
                'answer': 'Dew forming on grass',
                'explanation': 'Condensation is when water vapor in air cools and becomes liquid. Dew is a common example.',
                'ref': 'Page 44',
                'concept': 'Condensation',
                'difficulty': 'medium'
            },
            {
                'id': 'w7',
                'type': 'MCQ',
                'q': 'If you boil water continuously at 100°C, what happens to the temperature?',
                'options': ['Keeps rising', 'Stays at 100°C', 'Falls to 99°C', 'Drops suddenly'],
                'answer': 'Stays at 100°C',
                'explanation': 'At 100°C, all added heat goes to evaporation (latent heat), not temperature increase.',
                'ref': 'Page 39',
                'concept': 'Latent Heat',
                'difficulty': 'medium'
            },
            {
                'id': 'w8',
                'type': 'MCQ',
                'q': 'Why do puddles disappear faster on hot, windy days?',
                'options': ['Water flows away', 'Heat and wind speed up evaporation', 'Sun burns puddles', 'Temperature rises'],
                'answer': 'Heat and wind speed up evaporation',
                'explanation': 'Heat gives water molecules energy to evaporate. Wind carries away vapor, creating room for more evaporation.',
                'ref': 'Page 42',
                'concept': 'Evaporation Factors',
                'difficulty': 'medium'
            },
        ],
        'hard': [
            {
                'id': 'w9',
                'type': 'MCQ',
                'q': 'In a sealed jar, water evaporates but never rains. What is this process called?',
                'options': ['Freezing cycle', 'Dynamic equilibrium', 'Permanent evaporation', 'Closed melting'],
                'answer': 'Dynamic equilibrium',
                'explanation': 'Water molecules evaporate AND condense at equal rates. This is called dynamic equilibrium.',
                'ref': 'Pages 42-44',
                'concept': 'Dynamic Equilibrium',
                'difficulty': 'hard'
            },
            {
                'id': 'w10',
                'type': 'MCQ',
                'q': 'How does global warming affect evaporation?',
                'options': ['Decreases it', 'Stops it completely', 'Increases it due to warmer temperature', 'No effect'],
                'answer': 'Increases it due to warmer temperature',
                'explanation': 'Higher temperatures provide more energy for water molecules to evaporate. This accelerates the water cycle.',
                'ref': 'Pages 33, 43-44',
                'concept': 'Climate Impact',
                'difficulty': 'hard'
            },
            {
                'id': 'w11',
                'type': 'MCQ',
                'q': 'Why does water have different boiling points at different altitudes?',
                'options': ['It doesn\'t - boiling point is always 100°C', 'Air pressure is lower at high altitudes, so water boils at lower temperature', 'Temperature is colder, so water boils faster', 'Gravity pulls water molecules apart'],
                'answer': 'Air pressure is lower at high altitudes, so water boils at lower temperature',
                'explanation': 'At sea level, air pressure is 1 atm, water boils at 100°C. On mountains, lower air pressure means water boils at 95°C or lower. Boiling depends on air pressure, not just temperature.',
                'ref': 'Page 39',
                'concept': 'Boiling Point & Pressure',
                'difficulty': 'hard'
            },
            {
                'id': 'w12',
                'type': 'MCQ',
                'q': 'In a closed system with water and ice in equilibrium, what happens to the water level as ice melts?',
                'options': ['Water level rises', 'Water level stays the same', 'Water level drops', 'Unpredictable'],
                'answer': 'Water level stays the same',
                'explanation': 'Ice floats because it\'s less dense than water. When ice melts, it produces the same volume of water as the submerged part of the ice. Water level remains constant (this is why melting sea ice doesn\'t raise sea levels).',
                'ref': 'Pages 31, 40',
                'concept': 'Density of Water & Ice',
                'difficulty': 'hard'
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
                'concept': 'Reproductive Cells',
                'difficulty': 'easy'
            },
            {
                'id': 'r2',
                'type': 'MCQ',
                'q': 'What is needed for pollination?',
                'options': ['Rain only', 'Pollen reaches stigma', 'Tall plants', 'Wet soil'],
                'answer': 'Pollen reaches stigma',
                'explanation': 'Pollination is the transfer of pollen from anther to stigma. This is the first step in plant reproduction.',
                'ref': 'Pages 14-15',
                'concept': 'Pollination',
                'difficulty': 'easy'
            },
            {
                'id': 'r3',
                'type': 'MCQ',
                'q': 'Which reproduce using spores, not seeds?',
                'options': ['Roses', 'Tomatoes', 'Ferns', 'Wheat'],
                'answer': 'Ferns',
                'explanation': 'Ferns and mosses are non-flowering plants. They use spores (tiny cells) for reproduction, not seeds.',
                'ref': 'Pages 18-19',
                'concept': 'Non-Flowering Plants',
                'difficulty': 'easy'
            },
            {
                'id': 'r4',
                'type': 'MCQ',
                'q': 'What do seeds need to germinate? (WOW)',
                'options': ['Water, Oil, Wind', 'Water, Oxygen, Warmth', 'Water, Oxygen, Sun', 'Wind, Oxygen, Warmth'],
                'answer': 'Water, Oxygen, Warmth',
                'explanation': 'WOW = Water (dissolves nutrients), Oxygen (respiration energy), Warmth (enzyme activity). Sunlight is NOT needed initially (underground germination).',
                'ref': 'Page 17',
                'concept': 'Seed Germination',
                'difficulty': 'easy'
            },
            {
                'id': 'r5',
                'type': 'MCQ',
                'q': 'Where does fertilization occur in humans?',
                'options': ['Ovary', 'Uterus', 'Fallopian tube', 'Stomach'],
                'answer': 'Fallopian tube',
                'explanation': 'Sperm meets egg in fallopian tube. The fertilized egg then travels to uterus for development.',
                'ref': 'Pages 5-7',
                'concept': 'Human Fertilization',
                'difficulty': 'easy'
            },
        ],
        'medium': [
            {
                'id': 'r6',
                'type': 'MCQ',
                'q': 'A plant is pollinated but NO seeds form. Why?',
                'options': ['No rain', 'Fertilization did not occur', 'Plant was too old', 'Light was too weak'],
                'answer': 'Fertilization did not occur',
                'explanation': 'Pollination transfers pollen, but fertilization (fusion of pollen nucleus with egg cell) is needed for seeds. Without fertilization, no seed develops.',
                'ref': 'Pages 14-16',
                'concept': 'Pollination vs Fertilization',
                'difficulty': 'medium'
            },
            {
                'id': 'r7',
                'type': 'MCQ',
                'q': 'Why do identical twins look exactly alike?',
                'options': ['Same parents', 'One egg splits into 2 individuals = 100% same DNA', 'Eat same food', 'Born same day'],
                'answer': 'One egg splits into 2 individuals = 100% same DNA',
                'explanation': 'Identical twins come from one egg + one sperm that splits. They share all genes.',
                'ref': 'Pages 5-7',
                'concept': 'Twin Formation',
                'difficulty': 'medium'
            },
            {
                'id': 'r8',
                'type': 'MCQ',
                'q': 'Why are seeds scattered far from parent plants?',
                'options': ['Wind pushes them', 'Avoid competition and colonize new areas', 'Parent plants die', 'Seeds are too heavy'],
                'answer': 'Avoid competition and colonize new areas',
                'explanation': 'Dispersal prevents overcrowding near parent plant and helps species spread to new locations.',
                'ref': 'Page 15',
                'concept': 'Seed Dispersal',
                'difficulty': 'medium'
            },
        ],
        'hard': [
            {
                'id': 'r9',
                'type': 'MCQ',
                'q': 'A seed has water, oxygen, warmth but STILL won\'t germinate. What could be wrong?',
                'options': ['No nutrients', 'Seed is dormant (waiting for trigger)', 'Wrong pH', 'No bacteria'],
                'answer': 'Seed is dormant (waiting for trigger)',
                'explanation': 'Some seeds need triggers: cold period (winter), light exposure, or specific humidity. Dormancy ensures germination at best time.',
                'ref': 'Page 17',
                'concept': 'Seed Dormancy',
                'difficulty': 'hard'
            },
            {
                'id': 'r10',
                'type': 'MCQ',
                'q': 'How do inherited traits pass from parents to children?',
                'options': ['Through food', 'Genes combine during fertilization', 'Through blood', 'Through touch'],
                'answer': 'Genes combine during fertilization',
                'explanation': 'During fertilization, genes from both sperm and egg combine. Inherited traits follow this genetic inheritance.',
                'ref': 'Pages 4-5',
                'concept': 'Inheritance',
                'difficulty': 'hard'
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
                'concept': 'Battery Function',
                'difficulty': 'easy'
            },
            {
                'id': 'e2',
                'type': 'MCQ',
                'q': 'A closed circuit means:',
                'options': ['Broken path', 'Complete path for current', 'No path', 'Blocked path'],
                'answer': 'Complete path for current',
                'explanation': 'Closed = complete loop. Current can flow. Light turns ON. Open = broken, light OFF.',
                'ref': 'Pages 94-96',
                'concept': 'Circuit States',
                'difficulty': 'easy'
            },
            {
                'id': 'e3',
                'type': 'MCQ',
                'q': 'Which is a good conductor?',
                'options': ['Rubber', 'Plastic', 'Copper', 'Wood'],
                'answer': 'Copper',
                'explanation': 'Copper is a metal with free electrons. It conducts electricity well. Used in wires. Others are insulators.',
                'ref': 'Page 98',
                'concept': 'Conductors vs Insulators',
                'difficulty': 'easy'
            },
            {
                'id': 'e4',
                'type': 'MCQ',
                'q': 'Why is rubber wrapped around copper wires?',
                'options': ['Makes stronger', 'Insulates (protects)', 'Faster current', 'Prevents rust'],
                'answer': 'Insulates (protects)',
                'explanation': 'Rubber is insulator. It prevents accidental contact with live copper, protecting from electric shock.',
                'ref': 'Page 98',
                'concept': 'Electrical Safety',
                'difficulty': 'easy'
            },
            {
                'id': 'e5',
                'type': 'MCQ',
                'q': 'Why is touching wet appliances dangerous?',
                'options': ['Cold hands', 'Water conducts electricity', 'Appliances malfunction', 'Hands slip'],
                'answer': 'Water conducts electricity',
                'explanation': 'Water is conductor. Current flows through wet hands to ground. This causes electric shock.',
                'ref': 'Pages 101-102',
                'concept': 'Water Conductivity',
                'difficulty': 'easy'
            },
        ],
        'medium': [
            {
                'id': 'e6',
                'type': 'MCQ',
                'q': 'What measures electrical current and where should it be placed?',
                'options': ['Voltmeter, across components', 'Ammeter, in series with circuit', 'Thermometer, in bulbs', 'Ruler, on wires'],
                'answer': 'Ammeter, in series with circuit',
                'explanation': 'Ammeter measures current in Amperes. It must be placed IN SERIES (in the current path), not across components.',
                'ref': 'Pages 102-103',
                'concept': 'Ammeter Placement',
                'difficulty': 'medium'
            },
            {
                'id': 'e7',
                'type': 'MCQ',
                'q': 'In a series circuit with one 6V battery and 2 identical bulbs, what voltage is across EACH bulb?',
                'options': ['1.5V', '3V', '6V', '12V'],
                'answer': '3V',
                'explanation': 'In series, total voltage divides equally among identical resistances. 6V ÷ 2 bulbs = 3V per bulb.',
                'ref': 'Page 110',
                'concept': 'Voltage Division',
                'difficulty': 'medium'
            },
            {
                'id': 'e8',
                'type': 'MCQ',
                'q': 'When you add more bulbs IN SERIES, what happens to brightness?',
                'options': ['All stay same', 'All get brighter', 'All get dimmer', 'No change'],
                'answer': 'All get dimmer',
                'explanation': 'More bulbs = more resistance. More resistance with same voltage = less current (I = V/R). Less current = dimmer light.',
                'ref': 'Pages 110-113',
                'concept': 'Series Resistance',
                'difficulty': 'medium'
            },
            {
                'id': 'e9_new',
                'type': 'MCQ',
                'q': 'What is the difference between voltmeter and ammeter placement?',
                'options': ['Voltmeter in series, ammeter across', 'Voltmeter across, ammeter in series', 'Both placed the same way', 'Depends on circuit'],
                'answer': 'Voltmeter across, ammeter in series',
                'explanation': 'Voltmeter measures potential difference ACROSS components (parallel). Ammeter measures current THROUGH circuit (series). Wrong placement damages instruments.',
                'ref': 'Pages 102-105',
                'concept': 'Meter Placement',
                'difficulty': 'medium'
            },
            {
                'id': 'e10_new',
                'type': 'MCQ',
                'q': 'In a parallel circuit with 3 identical bulbs, compared to a series circuit, what happens?',
                'options': ['Bulbs are dimmer', 'Bulbs are brighter', 'No change in brightness', 'Only middle bulb is bright'],
                'answer': 'Bulbs are brighter',
                'explanation': 'Parallel: Each bulb gets full voltage (6V). Less total resistance = more current. Series: Voltage divides, less current per bulb. Parallel = brighter.',
                'ref': 'Pages 112-115',
                'concept': 'Parallel Advantages',
                'difficulty': 'medium'
            },
        ],
        'hard': [
            {
                'id': 'e9',
                'type': 'MCQ',
                'q': 'What danger does a circuit breaker prevent?',
                'options': ['Bulbs breaking', 'Wire fire from high current heat', 'Battery draining', 'Switches failing'],
                'answer': 'Wire fire from high current heat',
                'explanation': 'High current causes power loss: P = I²R. This creates dangerous heat that can melt wires and start fires. Breaker cuts current.',
                'ref': 'Page 113',
                'concept': 'Circuit Breaker',
                'difficulty': 'hard'
            },
            {
                'id': 'e10',
                'type': 'MCQ',
                'q': 'Why does touching a live wire with bare hands cause shock?',
                'options': ['Wire is hot', 'Your body completes the circuit', 'Electricity jumps out', 'Muscles contract from cold'],
                'answer': 'Your body completes the circuit',
                'explanation': 'Your body becomes a conductor. Current flows: wire → body → ground. This shock causes injury.',
                'ref': 'Pages 101-102',
                'concept': 'Electric Shock',
                'difficulty': 'hard'
            },
            {
                'id': 'e11',
                'type': 'MCQ',
                'q': 'Using Ohm\'s Law (V = IR), if voltage stays constant but resistance doubles, what happens to current?',
                'options': ['Doubles', 'Stays same', 'Halves', 'Becomes zero'],
                'answer': 'Halves',
                'explanation': 'I = V/R. If V is constant and R doubles, then I = V/(2R) = (V/R)/2. Current is halved. This shows inverse relationship between resistance and current.',
                'ref': 'Pages 108-110',
                'concept': 'Ohm\'s Law Application',
                'difficulty': 'hard'
            },
            {
                'id': 'e12',
                'type': 'MCQ',
                'q': 'Which circuit arrangement would use the LEAST amount of electrical energy (power)?',
                'options': ['3 bulbs in series', '3 bulbs in parallel', 'Both use same energy', 'Depends on bulb brightness'],
                'answer': '3 bulbs in series',
                'explanation': 'Series: Higher total resistance, less current, less power (P=VI). Parallel: Lower total resistance, more current, more power. Series uses LESS energy.',
                'ref': 'Pages 112-115',
                'concept': 'Power Efficiency',
                'difficulty': 'hard'
            },
            {
                'id': 'e13',
                'type': 'MCQ',
                'q': 'In a circuit with resistance R, if you halve the resistance, the power dissipated (P = I²R with constant V) will:',
                'options': ['Double', 'Halve', 'Quadruple', 'Stay the same'],
                'answer': 'Double',
                'explanation': 'With constant voltage, halving R doubles the current: I = V/R. Power P = I²R. New power = (2I)² × (R/2) = 4I² × (R/2) = 2I²R. Power doubles.',
                'ref': 'Pages 113-115',
                'concept': 'Power Dissipation',
                'difficulty': 'hard'
            },
        ]
    },

    'Plant_Transport': {
        'easy': [
            {'id': 'pt1', 'type': 'MCQ', 'q': 'What is the main function of roots?', 'options': ['Make food', 'Absorb water and minerals', 'Transport food', 'Release oxygen'], 'answer': 'Absorb water and minerals', 'explanation': 'Roots absorb water and mineral salts from soil. These are transported to other parts. (Textbook Page 54)', 'difficulty': 'easy'},
            {'id': 'pt2', 'type': 'MCQ', 'q': 'Which tubes carry water through a plant?', 'options': ['Phloem tubes', 'Xylem tubes', 'Both equally', 'Neither'], 'answer': 'Xylem tubes', 'explanation': 'Xylem tubes (water-carrying tubes) transport water from roots to leaves. (Textbook Pages 55-56)', 'difficulty': 'easy'},
            {'id': 'pt3', 'type': 'MCQ', 'q': 'Which tubes carry food through a plant?', 'options': ['Xylem tubes', 'Phloem tubes', 'Root hairs', 'Stems'], 'answer': 'Phloem tubes', 'explanation': 'Phloem tubes (food-carrying tubes) transport food made in leaves to all parts. (Textbook Pages 57-58)', 'difficulty': 'easy'},
            {'id': 'pt4', 'type': 'MCQ', 'q': 'Where is food made in a plant?', 'options': ['In roots', 'In stems', 'In leaves', 'In flowers'], 'answer': 'In leaves', 'explanation': 'Leaves make food through photosynthesis. This food is then transported to other parts via phloem. (Textbook Pages 54, 57)', 'difficulty': 'easy'},
            {'id': 'pt5', 'type': 'MCQ', 'q': 'What do root hairs help with?', 'options': ['Making food', 'Increasing water absorption surface area', 'Transporting minerals', 'Storing water'], 'answer': 'Increasing water absorption surface area', 'explanation': 'Root hairs are tiny extensions that greatly increase the surface area for absorbing water and minerals. (Textbook Page 54)', 'difficulty': 'easy'},
        ],
        'medium': [
            {'id': 'pt6', 'type': 'MCQ', 'q': 'Why do plants need a transport system?', 'options': ['To look tall', 'To move water and food to all parts', 'To make seeds', 'To absorb sunlight'], 'answer': 'To move water and food to all parts', 'explanation': 'Plants need transport to move water (roots absorb it, leaves need it) and food (made in leaves, needed everywhere). (Textbook Pages 52-53)', 'difficulty': 'medium'},
            {'id': 'pt7', 'type': 'MCQ', 'q': 'What does the term transpiration mean?', 'options': ['Moving water upward', 'Losing water vapour from leaves', 'Making food', 'Absorbing minerals'], 'answer': 'Losing water vapour from leaves', 'explanation': 'Transpiration is when water vapour escapes from leaves into the air. (Textbook Page 59)', 'difficulty': 'medium'},
            {'id': 'pt8', 'type': 'MCQ', 'q': 'Which part of the plant contains both xylem and phloem tubes?', 'options': ['Roots', 'Leaves', 'Stem', 'Flowers'], 'answer': 'Stem', 'explanation': 'The stem contains both xylem (water) and phloem (food) tubes running through it. (Textbook Pages 56-57)', 'difficulty': 'medium'},
            {'id': 'pt9', 'type': 'MCQ', 'q': 'What are mineral salts used for in plants?', 'options': ['Making water', 'Growing and staying healthy', 'Making flowers', 'Preventing wilting'], 'answer': 'Growing and staying healthy', 'explanation': 'Mineral salts from soil are nutrients that plants need to grow and stay healthy. They travel through xylem. (Textbook Page 55)', 'difficulty': 'medium'},
            {'id': 'pt10', 'type': 'MCQ', 'q': 'In which direction does food travel through phloem?', 'options': ['Downward only', 'Upward only', 'From leaves to other parts', 'From roots to leaves'], 'answer': 'From leaves to other parts', 'explanation': 'Food is made in leaves and transported by phloem to all other parts that need it. (Textbook Pages 57-58)', 'difficulty': 'medium'},
        ],
        'hard': [
            {'id': 'pt11', 'type': 'MCQ', 'q': 'What happens if a ring of bark is cut around a tree stem?', 'options': ['Tree grows taller', 'Food cannot reach parts below; they starve', 'Tree gets more water', 'Nothing changes'], 'answer': 'Food cannot reach parts below; they starve', 'explanation': 'Bark contains phloem tubes. Removing it cuts food transport, so parts below receive no food and starve. (Textbook Page 59)', 'difficulty': 'hard'},
            {'id': 'pt12', 'type': 'MCQ', 'q': 'If water-carrying tubes (xylem) are cut, what happens to the plant?', 'options': ['It grows faster', 'It wilts (droops)', 'It makes more food', 'Nothing happens'], 'answer': 'It wilts (droops)', 'explanation': 'When xylem is cut, water cannot reach leaves, so the plant wilts. (Textbook Page 60)', 'difficulty': 'hard'},
            {'id': 'pt13', 'type': 'MCQ', 'q': 'Which would have a greater impact on plant survival: cutting all phloem or cutting all xylem?', 'options': ['Cutting phloem is worse', 'Cutting xylem is worse', 'Both equally harmful', 'Neither matters'], 'answer': 'Cutting xylem is worse', 'explanation': 'Without water (xylem), the plant dies within days. Without food (phloem), it takes longer. Water is immediately critical. (Textbook Pages 55-59)', 'difficulty': 'hard'},
            {'id': 'pt14', 'type': 'MCQ', 'q': 'What is the relationship between photosynthesis and food transport?', 'options': ['Unrelated', 'Photosynthesis makes food; phloem transports it', 'Photosynthesis uses food from phloem', 'Xylem carries photosynthesis products'], 'answer': 'Photosynthesis makes food; phloem transports it', 'explanation': 'Leaves use photosynthesis to make food. This food is then transported through phloem to other parts. (Textbook Pages 54, 57-58)', 'difficulty': 'hard'},
            {'id': 'pt15', 'type': 'MCQ', 'q': 'If a plant is in very dry soil, why does it wilt even if water is below ground?', 'options': ['Roots are blocked', 'Root hairs cannot absorb dry soil water fast enough', 'Transpiration is faster than absorption', 'Xylem stops working'], 'answer': 'Root hairs cannot absorb dry soil water fast enough', 'explanation': 'In dry soil, water is harder for roots to absorb. Transpiration from leaves happens faster than roots can absorb water, causing wilting. (Textbook Pages 54, 59)', 'difficulty': 'hard'},
        ]
    },

    'Human_Systems': {
        'easy': [
            {'id': 'hs1', 'type': 'MCQ', 'q': 'What is the main gas that living things need from air?', 'options': ['Nitrogen', 'Carbon dioxide', 'Oxygen', 'Water vapour'], 'answer': 'Oxygen', 'explanation': 'Living things need oxygen to survive. Air contains about 21% oxygen. (Textbook Page 65)', 'difficulty': 'easy'},
            {'id': 'hs2', 'type': 'MCQ', 'q': 'Which organ is the main site for gaseous exchange?', 'options': ['Nose', 'Windpipe', 'Lungs', 'Heart'], 'answer': 'Lungs', 'explanation': 'In the lungs, oxygen enters blood and carbon dioxide leaves blood. (Textbook Pages 69-71)', 'difficulty': 'easy'},
            {'id': 'hs3', 'type': 'MCQ', 'q': 'What does the diaphragm do?', 'options': ['Filters air', 'Contracts and relaxes to aid breathing', 'Pumps blood', 'Makes food'], 'answer': 'Contracts and relaxes to aid breathing', 'explanation': 'The diaphragm is a muscle below the lungs. When it contracts, lungs expand (inhale). (Textbook Page 70)', 'difficulty': 'easy'},
            {'id': 'hs4', 'type': 'MCQ', 'q': 'What is the main function of the heart?', 'options': ['Make blood', 'Filter blood', 'Pump blood to different parts', 'Store blood'], 'answer': 'Pump blood to different parts', 'explanation': 'The heart is a muscle that pumps blood continuously throughout the body. (Textbook Pages 75-76)', 'difficulty': 'easy'},
            {'id': 'hs5', 'type': 'MCQ', 'q': 'Where can you feel your pulse?', 'options': ['Only on wrist', 'Only on neck', 'On wrist or neck', 'Nowhere'], 'answer': 'On wrist or neck', 'explanation': 'You can feel pulse by placing fingers on wrist or side of neck. This shows heartbeat. (Textbook Page 76)', 'difficulty': 'easy'},
        ],
        'medium': [
            {'id': 'hs6', 'type': 'MCQ', 'q': 'How much oxygen is in exhaled air compared to inhaled air?', 'options': ['More oxygen in exhaled', 'Less oxygen in exhaled (16% vs 21%)', 'Same amount', 'No oxygen in exhaled'], 'answer': 'Less oxygen in exhaled (16% vs 21%)', 'explanation': 'Inhaled air: 21% oxygen. Exhaled air: 16% oxygen. Our body uses the oxygen. (Textbook Page 70)', 'difficulty': 'medium'},
            {'id': 'hs7', 'type': 'MCQ', 'q': 'What happens to breathing and heart rate during exercise?', 'options': ['Both stay same', 'Both decrease', 'Both increase', 'Breathing increases, heart decreases'], 'answer': 'Both increase', 'explanation': 'During exercise, body needs more oxygen. Breathing rate and heart rate increase to deliver oxygen. (Textbook Page 79-80)', 'difficulty': 'medium'},
            {'id': 'hs8', 'type': 'MCQ', 'q': 'What is the function of blood vessels?', 'options': ['Make blood', 'Carry blood throughout body', 'Filter waste', 'Store oxygen'], 'answer': 'Carry blood throughout body', 'explanation': 'Blood vessels (arteries and veins) form a network to transport blood to and from all body parts. (Textbook Page 76)', 'difficulty': 'medium'},
            {'id': 'hs9', 'type': 'MCQ', 'q': 'What gases are exchanged in the lungs?', 'options': ['Nitrogen and oxygen', 'Oxygen in, carbon dioxide out', 'Carbon dioxide in, oxygen out', 'Only oxygen'], 'answer': 'Oxygen in, carbon dioxide out', 'explanation': 'In gaseous exchange, oxygen from inhaled air enters the blood, and carbon dioxide (waste) leaves the blood. (Textbook Page 71)', 'difficulty': 'medium'},
            {'id': 'hs10', 'type': 'MCQ', 'q': 'How can you measure heart rate?', 'options': ['Feel pulse and count for 1 minute', 'Count breaths per minute', 'Measure lung capacity', 'Check oxygen levels'], 'answer': 'Feel pulse and count for 1 minute', 'explanation': 'Heart rate is measured by feeling the pulse at wrist or neck and counting heartbeats in one minute. (Textbook Page 76)', 'difficulty': 'medium'},
        ],
        'hard': [
            {'id': 'hs11', 'type': 'MCQ', 'q': 'During asthma attack, what happens to airways?', 'options': ['Airways widen', 'Airways narrow/swell', 'Airways stay normal', 'Airways disappear'], 'answer': 'Airways narrow/swell', 'explanation': 'Asthma causes swelling and narrowing of airways, making breathing difficult. Inhaler medicine helps. (Textbook Page 71)', 'difficulty': 'hard'},
            {'id': 'hs12', 'type': 'MCQ', 'q': 'How does carbon dioxide reach the lungs to be exhaled?', 'options': ['Through arteries', 'Through veins from body cells', 'Made in lungs', 'Through nose'], 'answer': 'Through veins from body cells', 'explanation': 'Body cells produce CO₂ as waste. It dissolves in blood and returns to lungs via veins for exhalation. (Textbook Page 71)', 'difficulty': 'hard'},
            {'id': 'hs13', 'type': 'MCQ', 'q': 'Why is the nose important in the respiratory system?', 'options': ['Just allows air entry', 'Warms, moistens, and filters air', 'Makes oxygen', 'Exchanges gases'], 'answer': 'Warms, moistens, and filters air', 'explanation': 'The nose warms cold air, adds moisture, and traps dust/particles before air reaches lungs. (Textbook Page 69)', 'difficulty': 'hard'},
            {'id': 'hs14', 'type': 'MCQ', 'q': 'What would happen to body cells if they received blood with too little oxygen?', 'options': ['Cells thrive', 'Cells work slowly or die', 'Cells grow faster', 'No effect'], 'answer': 'Cells work slowly or die', 'explanation': 'Oxygen is essential for cell respiration and energy production. Insufficient oxygen causes cells to dysfunction or die. (Textbook Pages 65, 71)', 'difficulty': 'hard'},
            {'id': 'hs15', 'type': 'MCQ', 'q': 'How does smoking harm the respiratory system?', 'options': ['No effect', 'Damages lungs and reduces oxygen absorption', 'Makes lungs stronger', 'Increases air flow'], 'answer': 'Damages lungs and reduces oxygen absorption', 'explanation': 'Smoking damages lung tissue and makes it harder for lungs to absorb oxygen, reducing oxygen in blood. (Textbook Page 71)', 'difficulty': 'hard'},
        ]
    },

    'Electric_Circuits': {
        'easy': [
            {'id': 'ec1', 'type': 'MCQ', 'q': 'What is a series circuit?', 'options': ['Many paths for current', 'Single path for current with components in a line', 'No path for current', 'Random paths'], 'answer': 'Single path for current with components in a line', 'explanation': 'A series circuit has one path for current; all components are connected in a line. (Textbook Pages 105-107)', 'difficulty': 'easy'},
            {'id': 'ec2', 'type': 'MCQ', 'q': 'What happens when you add more batteries in a series circuit?', 'options': ['Bulbs get dimmer', 'Bulbs get brighter', 'No change', 'Circuit breaks'], 'answer': 'Bulbs get brighter', 'explanation': 'More batteries provide more voltage, which increases current, making bulbs brighter. (Textbook Pages 108-110)', 'difficulty': 'easy'},
            {'id': 'ec3', 'type': 'MCQ', 'q': 'What happens when you add more bulbs in a series circuit?', 'options': ['All stay bright', 'All get dimmer', 'One gets brighter', 'Nothing happens'], 'answer': 'All get dimmer', 'explanation': 'More bulbs add resistance. More resistance means less current, so all bulbs get dimmer. (Textbook Pages 110-113)', 'difficulty': 'easy'},
            {'id': 'ec4', 'type': 'MCQ', 'q': 'What does Ohm\'s Law state?', 'options': ['V = I + R', 'V = I × R', 'V = I ÷ R', 'V = R - I'], 'answer': 'V = I × R', 'explanation': 'Ohm\'s Law: Voltage = Current × Resistance. This relates the three key quantities in a circuit. (Textbook Pages 108-110)', 'difficulty': 'easy'},
            {'id': 'ec5', 'type': 'MCQ', 'q': 'What is a circuit breaker?', 'options': ['Something that breaks circuits', 'A device that prevents electrical fires', 'A type of bulb', 'A power source'], 'answer': 'A device that prevents electrical fires', 'explanation': 'A circuit breaker is a safety device that automatically trips (opens) when current is too high, preventing fires and damage. (Textbook Page 113)', 'difficulty': 'easy'},
        ],
        'medium': [
            {'id': 'ec6', 'type': 'MCQ', 'q': 'In a series circuit, what happens to voltage across each bulb?', 'options': ['Each bulb gets full voltage', 'Voltage divides among bulbs', 'Bulbs get no voltage', 'Voltage stays same everywhere'], 'answer': 'Voltage divides among bulbs', 'explanation': 'In series, total voltage divides among components. With 3 bulbs and 6V, each bulb gets about 2V. (Textbook Page 110)', 'difficulty': 'hard'},
            {'id': 'ec7', 'type': 'MCQ', 'q': 'In a series circuit with 2 identical bulbs and 6V battery, what voltage is across each bulb?', 'options': ['0V', '6V', '3V', '12V'], 'answer': '3V', 'explanation': 'In series, voltage divides equally among identical resistances. 6V ÷ 2 bulbs = 3V per bulb. (Textbook Page 110)', 'difficulty': 'hard'},
            {'id': 'ec8', 'type': 'MCQ', 'q': 'What is the total resistance in a series circuit with bulbs of 2Ω, 3Ω, and 5Ω?', 'options': ['3Ω', '5Ω', '10Ω', '2Ω'], 'answer': '10Ω', 'explanation': 'In series, total resistance = sum of all resistances. R_total = 2Ω + 3Ω + 5Ω = 10Ω. (Textbook Pages 110-113)', 'difficulty': 'medium'},
            {'id': 'ec9', 'type': 'MCQ', 'q': 'How does a fuse differ from a circuit breaker?', 'options': ['Same thing', 'Fuse melts; breaker trips and can be reset', 'Breaker melts; fuse trips', 'No real difference'], 'answer': 'Fuse melts; breaker trips and can be reset', 'explanation': 'Fuse: melts and breaks (one-time use). Breaker: trips and can be manually reset multiple times. (Textbook Page 113)', 'difficulty': 'medium'},
            {'id': 'ec10', 'type': 'MCQ', 'q': 'Why is energy conservation important?', 'options': ['Saves money', 'Reduces fossil fuel use and environmental impact', 'Makes bulbs brighter', 'Prevents circuit breaks'], 'answer': 'Reduces fossil fuel use and environmental impact', 'explanation': 'Saving electricity reduces the need to burn fossil fuels, which protects the environment. (Textbook Pages 114-115)', 'difficulty': 'medium'},
        ],
        'hard': [
            {'id': 'ec11', 'type': 'MCQ', 'q': 'If you have a 12V battery and want current of 2A, what resistance is needed?', 'options': ['6Ω', '12Ω', '24Ω', '2Ω'], 'answer': '6Ω', 'explanation': 'Using Ohm\'s Law: V = IR, so R = V/I = 12V ÷ 2A = 6Ω. (Textbook Pages 108-110)', 'difficulty': 'hard'},
            {'id': 'ec12', 'type': 'MCQ', 'q': 'In a series circuit, if one bulb burns out, what happens?', 'options': ['Other bulbs stay on', 'All bulbs turn off', 'Brightness increases', 'Circuit resets'], 'answer': 'All bulbs turn off', 'explanation': 'In series, the broken bulb breaks the single path, stopping all current. All bulbs turn off. (Textbook Pages 105-107)', 'difficulty': 'hard'},
            {'id': 'ec13', 'type': 'MCQ', 'q': 'What causes an electrical overload?', 'options': ['Not enough wires', 'Too many appliances using too much current', 'Too much insulation', 'Low battery voltage'], 'answer': 'Too many appliances using too much current', 'explanation': 'Overload occurs when total current demand exceeds circuit capacity, creating dangerously high heat. (Textbook Pages 113-114)', 'difficulty': 'hard'},
            {'id': 'ec14', 'type': 'MCQ', 'q': 'How does renewable energy differ from fossil fuels?', 'options': ['Same thing', 'Renewables never run out; fossil fuels are limited', 'Fossil fuels are unlimited', 'Both run out at same rate'], 'answer': 'Renewables never run out; fossil fuels are limited', 'explanation': 'Renewable energy (sun, wind, water) continuously replenishes. Fossil fuels (coal, oil) are finite and will run out. (Textbook Page 115)', 'difficulty': 'hard'},
            {'id': 'ec15', 'type': 'MCQ', 'q': 'What is power dissipation in a circuit?', 'options': ['Voltage used up', 'Current converted to heat (P = I²R)', 'Resistance disappearing', 'Battery draining'], 'answer': 'Current converted to heat (P = I²R)', 'explanation': 'Power dissipation is the rate at which electrical energy converts to heat in a resistor. P = I²R or P = VI. (Textbook Pages 113-115)', 'difficulty': 'hard'},
        ]
    }
}

# ==================== CHALLENGE QUESTIONS (PSLE BRAIN DRAINERS) ====================
# These are tricky questions where all answers seem correct but only ONE is right!
# Designed to test deeper understanding and catch common misconceptions

CHALLENGE_QUESTIONS = {
    'Water_Cycles': [
        {
            'id': 'ch_w1',
            'type': 'MCQ',
            'q': 'During evaporation from the ocean, salt crystals form on the water surface. Why does this NOT happen?',
            'options': [
                'Salt molecules are too heavy to evaporate',
                'Salt water has a lower boiling point than fresh water',
                'Only water molecules have enough energy to escape as vapor',
                'Salt dissolves more in hot water and cannot crystallize'
            ],
            'answer': 'Only water molecules have enough energy to escape as vapor',
            'explanation': 'In evaporation, ONLY water molecules turn into vapor because salt is non-volatile. Salt molecules cannot escape into vapor form at normal temperatures - only liquid water molecules can evaporate. This is why salt can be extracted from seawater through evaporation!',
            'ref': 'Pages 43-44',
            'concept': 'Evaporation & Separation',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_w2',
            'type': 'MCQ',
            'q': 'A glass of water left in direct sunlight disappears in 3 days. A glass of water left in the shade takes 10 days to disappear. Which statement best explains this difference?',
            'options': [
                'The sunlight heats the water, giving water molecules more energy to evaporate',
                'The sunlight destroys the water molecules making them lighter',
                'The shade prevents air movement which is needed for evaporation',
                'Sunlight increases the boiling point of water'
            ],
            'answer': 'The sunlight heats the water, giving water molecules more energy to evaporate',
            'explanation': 'Temperature is the KEY factor! Sun-heated water has molecules with MORE kinetic energy, so MORE molecules can escape as vapor. It\'s not about light destroying water or air movement - it\'s pure thermal energy. Same reason puddles dry faster on hot days!',
            'ref': 'Page 42',
            'concept': 'Temperature & Evaporation Rate',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_w3',
            'type': 'MCQ',
            'q': 'Rain clouds contain water droplets. But when these droplets form through condensation, where do the LATENT HEAT go during this process?',
            'options': [
                'Released into the atmosphere as heat',
                'Absorbed from the atmosphere as heat',
                'Stored in the water droplets',
                'Converted to light energy'
            ],
            'answer': 'Released into the atmosphere as heat',
            'explanation': 'Condensation is EXOTHERMIC - it RELEASES latent heat into atmosphere! This released heat is why clouds warm air around them. This is opposite to evaporation (endothermic). Remember: Condensation = heat OUT, Evaporation = heat IN!',
            'ref': 'Page 44',
            'concept': 'Latent Heat in Phase Changes',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_w4',
            'type': 'MCQ',
            'q': 'In the water cycle, water from rivers flows to the ocean. But 99% of ocean water doesn\'t "flow out" again as rivers. Why is this possible without the ocean shrinking or overflowing?',
            'options': [
                'Rivers bring more water than evaporation removes',
                'Evaporation removes water from ocean as vapor, and precipitation returns it as rain over land and ocean',
                'Groundwater keeps the ocean level constant',
                'The ocean is so large that water addition doesn\'t matter'
            ],
            'answer': 'Evaporation removes water from ocean as vapor, and precipitation returns it as rain over land and ocean',
            'explanation': 'The water cycle is BALANCED! Water input (rivers + precipitation on ocean) = Water output (evaporation). Even though rivers bring water IN, evaporation takes water OUT equally. Ocean level stays constant through this perfect balance!',
            'ref': 'Pages 43-44',
            'concept': 'Water Cycle Balance',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_w5',
            'type': 'MCQ',
            'q': 'A puddle dries faster on a windy day than a calm day. Which statement BEST explains why wind helps evaporation?',
            'options': [
                'Wind cools the water surface, making evaporation easier',
                'Wind removes the "saturated layer" of water vapor above the surface, allowing more evaporation',
                'Wind adds thermal energy to the water',
                'Wind converts water into vapor directly'
            ],
            'answer': 'Wind removes the "saturated layer" of water vapor above the surface, allowing more evaporation',
            'explanation': 'Above water surfaces, a thin layer of air becomes "saturated" with water vapor. Wind blows this away, creating "room" for MORE water to evaporate. Without wind, evaporation eventually stops as the layer becomes saturated. This is why fans dry things faster!',
            'ref': 'Page 42',
            'concept': 'Evaporation & Air Movement',
            'difficulty': 'hard'
        }
    ],
    'Reproduction': [
        {
            'id': 'ch_r1',
            'type': 'MCQ',
            'q': 'A flower is pollinated and seeds develop. But the seeds never germinate even with water, oxygen, and warmth. What is the MOST LIKELY reason?',
            'options': [
                'The flower was not fully mature',
                'The seeds are dormant and waiting for a specific trigger (cold period/light)',
                'The pollination was unsuccessful',
                'The seeds need fertilizer to germinate'
            ],
            'answer': 'The seeds are dormant and waiting for a specific trigger (cold period/light)',
            'explanation': 'Dormancy is a survival strategy! Seeds don\'t germinate immediately even with optimal conditions. They wait for triggers (winter cold, spring light) to ensure germination happens at the BEST time for survival. This is not a failure - it\'s smart biology!',
            'ref': 'Page 17',
            'concept': 'Seed Dormancy & Germination Triggers',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_r2',
            'type': 'MCQ',
            'q': 'In flowering plants, the pollen grain contains the male gamete, and the ovule contains the female gamete. After fertilization, the ovule develops into a seed. What happens to the pollen grain?',
            'options': [
                'It grows into the root of the new plant',
                'It dissolves after releasing the male gamete',
                'It becomes part of the seed coat',
                'It develops into the embryo'
            ],
            'answer': 'It dissolves after releasing the male gamete',
            'explanation': 'The pollen grain\'s ONLY job is to deliver the male gamete to the ovule. Once fertilization happens, the pollen grain is no longer needed and dissolves. The embryo comes from the fertilized egg INSIDE the ovule, not from the pollen!',
            'ref': 'Pages 10-12',
            'concept': 'Pollination & Fertilization',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_r3',
            'type': 'MCQ',
            'q': 'Identical twins have 100% the same DNA, but fraternal twins share only ~50% DNA (like siblings). If both sets of twins are raised in the SAME environment, which pair will be MORE alike in appearance?',
            'options': [
                'Fraternal twins (same environment overrides DNA differences)',
                'Identical twins (same DNA makes them look identical)',
                'Both pairs will be equally alike (environment matters more)',
                'It depends on the parents\' genes'
            ],
            'answer': 'Identical twins (same DNA makes them look identical)',
            'explanation': 'DNA is the PRIMARY factor for appearance! Even in the same environment, identical twins look virtually identical because they have identical genetics. Fraternal twins look different because they have different DNA. This shows genetics > environment for appearance!',
            'ref': 'Pages 4-5',
            'concept': 'Genetics vs Environment',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_r4',
            'type': 'MCQ',
            'q': 'An insect has 8 legs and feeds on plants. A mammal has 4 legs and feeds on meat. Both are animals. Which characteristic is used to classify them into DIFFERENT groups?',
            'options': [
                'Number of legs (8 vs 4)',
                'Presence of a backbone and warm blood (mammals have both)',
                'Diet (herbivore vs carnivore)',
                'Size and shape'
            ],
            'answer': 'Presence of a backbone and warm blood (mammals have both)',
            'explanation': 'Scientific classification uses BIOLOGICAL characteristics, not diet or leg count! Insects are invertebrates (no backbone), mammals are vertebrates (have backbone) and warm-blooded. These fundamental differences determine classification, not diet or appearance.',
            'ref': 'Page 2',
            'concept': 'Classification & Characteristics',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_r5',
            'type': 'MCQ',
            'q': 'A plant grows taller when given more sunlight. A plant grows taller when given more water. A plant grows taller when given fertilizer. Which statement is MOST ACCURATE?',
            'options': [
                'Sunlight is the most important factor',
                'Water is the most important factor',
                'Fertilizer is the most important factor',
                'All three factors are needed in BALANCE for optimal growth'
            ],
            'answer': 'All three factors are needed in BALANCE for optimal growth',
            'explanation': 'Plant growth requires ALL three: Sunlight (energy), Water (transport & structure), Nutrients (building materials). Missing ANY one limits growth. It\'s not "which is best" - it\'s that ALL are necessary! Growth requires the factor that\'s in SHORTEST supply.',
            'ref': 'Pages 21-25',
            'concept': 'Plant Growth Factors',
            'difficulty': 'hard'
        }
    ],
    'Electrical_Systems': [
        {
            'id': 'ch_e1',
            'type': 'MCQ',
            'q': 'In a series circuit with 2 bulbs and 1 battery, adding another identical bulb in series makes the circuit dimmer. What is the MAIN reason?',
            'options': [
                'The battery voltage decreases when more bulbs are added',
                'Adding a bulb increases total resistance, so current decreases',
                'The electrons move slower through more bulbs',
                'The battery loses power faster with more bulbs'
            ],
            'answer': 'Adding a bulb increases total resistance, so current decreases',
            'explanation': 'Series means bulbs are "in line" - each adds resistance. More resistance = Less current (Ohm\'s Law: I=V/R). Less current = dimmer bulbs! The battery voltage stays the same, but the resistance blocking the flow increases. This is why series circuits are good for high resistance, parallel for bright lights!',
            'ref': 'Pages 68-70',
            'concept': 'Series Circuits & Resistance',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_e2',
            'type': 'MCQ',
            'q': 'In a parallel circuit with 2 identical bulbs, if one bulb breaks (opens circuit), the other bulb stays lit. But in a series circuit with 2 identical bulbs, if one breaks, both go dark. Why does this happen?',
            'options': [
                'Parallel circuits have more voltage than series',
                'In parallel, each bulb has its OWN path to the battery; in series, all share ONE path',
                'The broken bulb drains energy in series but not in parallel',
                'Parallel bulbs are brighter so they continue despite breakage'
            ],
            'answer': 'In parallel, each bulb has its OWN path to the battery; in series, all share ONE path',
            'explanation': 'STRUCTURE is everything! Parallel = Multiple independent paths to battery. One break doesn\'t affect others. Series = Single path. One break = entire circuit broken! This is why homes use parallel wiring (each outlet independent) not series!',
            'ref': 'Pages 69-70',
            'concept': 'Series vs Parallel Circuit Design',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_e3',
            'type': 'MCQ',
            'q': 'An ammeter in a circuit reads 2A when connected in series. If you connect the SAME ammeter in parallel with a bulb, what happens?',
            'options': [
                'The ammeter reads the same 2A',
                'The ammeter reads half the current (1A)',
                'The ammeter short-circuits and breaks',
                'The ammeter reads the full circuit current'
            ],
            'answer': 'The ammeter short-circuits and breaks',
            'explanation': 'AMMETERS MUST be in SERIES! They have near-zero resistance. In parallel, they become a "short circuit" - all current bypasses the bulb and flows through the low-resistance ammeter, burning it out! This is a MAJOR safety rule in circuits!',
            'ref': 'Pages 71-72',
            'concept': 'Correct Ammeter Connection',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_e4',
            'type': 'MCQ',
            'q': 'A bulb is connected to a battery with a switch. When you close the switch, current flows and the bulb lights. When you open the switch, current stops and the bulb goes dark. What is actually happening to the flow of electrons?',
            'options': [
                'Electrons stop moving completely when switch opens',
                'Electrons bounce back when the switch opens',
                'The switch breaks the complete circuit, preventing electron flow',
                'Electrons leak out through the switch'
            ],
            'answer': 'The switch breaks the complete circuit, preventing electron flow',
            'explanation': 'A COMPLETE CIRCUIT is needed for electron flow! Electrons don\'t "stop" or "bounce" - the physical break (open switch) breaks the PATH. No path = No flow = No current = No light. It\'s all about the physical circuit being complete!',
            'ref': 'Page 52',
            'concept': 'Complete vs Incomplete Circuits',
            'difficulty': 'hard'
        },
        {
            'id': 'ch_e5',
            'type': 'MCQ',
            'q': 'Two identical bulbs: Bulb A in series with a 6V battery, Bulb B in parallel with a 6V battery (just one bulb, not a complete parallel circuit yet). Which bulb receives 6V?',
            'options': [
                'Both bulbs receive 6V',
                'Bulb A receives 6V, Bulb B receives 3V (split)',
                'Bulb B receives 6V, Bulb A receives less',
                'It depends on the bulb resistance'
            ],
            'answer': 'Bulb B receives 6V, Bulb A receives less',
            'explanation': 'In series with 2+ components, voltage is SHARED. But one bulb in parallel with battery gets the FULL battery voltage! Wait - you said "one bulb" so it\'s not sharing with anything. A single bulb in parallel gets full voltage. This confuses many students!',
            'ref': 'Pages 66-70',
            'concept': 'Voltage in Series vs Parallel',
            'difficulty': 'hard'
        }
    ]
}

# ==================== INITIALIZE SESSION ====================

def init_session():
    """Initialize all session variables including user tracking"""
    defaults = {
        'mode': 'login',  # Start with login screen
        'user_id': None,
        'user_name': None,
        'current_session_id': None,
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
        'challenge_question_idx': 0,
        'challenge_score': 0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ==================== USER LOGIN ====================

def show_login():
    """User login/identification screen with professional styling"""
    st.set_page_config(page_title="Exam Prep - Login", page_icon="🧪", layout="wide")

    # Apply custom styling
    st.markdown("""
    <style>
    .login-header {
        background: linear-gradient(135deg, #3B82F6 0%, #A855F7 100%);
        padding: 40px 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .login-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 700;
    }
    .login-header p {
        margin: 10px 0 0 0;
        font-size: 1.1em;
        opacity: 0.9;
    }
    .login-card {
        background: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .input-label {
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 8px;
        display: block;
    }
    .recent-users-section {
        background: #F9FAFB;
        border-radius: 12px;
        padding: 20px;
        margin-top: 25px;
    }
    .recent-users-title {
        font-size: 1.1em;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Header banner
        st.markdown("""
        <div class="login-header">
            <h1>🧪 Science Exam Prep</h1>
            <p>Master Your Science Skills</p>
        </div>
        """, unsafe_allow_html=True)

        # Login card
        st.markdown('<div class="login-card">', unsafe_allow_html=True)

        st.markdown("<label class='input-label'>What's your name?</label>", unsafe_allow_html=True)
        user_name = st.text_input(
            "Enter your name:",
            placeholder="e.g., Aanya, Chan Chan, or your name",
            key="login_name",
            label_visibility="collapsed"
        )

        # Start Learning button
        col_btn1, col_btn2 = st.columns([2, 1])
        with col_btn1:
            if st.button("🚀 Start Learning", use_container_width=True, type="primary"):
                if user_name and user_name.strip():
                    # Get or create user in database
                    user_id = get_or_create_user(user_name.strip())
                    if user_id:
                        st.session_state.user_id = user_id
                        st.session_state.user_name = user_name.strip()
                        st.session_state.mode = 'home'
                        st.success(f"Welcome, {user_name.strip()}! 🎉")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Error creating user. Please try again.")
                else:
                    st.error("Please enter your name to continue!")

        st.markdown('</div>', unsafe_allow_html=True)

        # Recent users section
        st.markdown('<div class="recent-users-section">', unsafe_allow_html=True)
        st.markdown('<div class="recent-users-title">🔄 Quick Login - Recent Users</div>', unsafe_allow_html=True)
        existing_users = get_all_users()
        if existing_users:
            cols = st.columns(min(3, len(existing_users)))
            for idx, user in enumerate(existing_users[:3]):
                with cols[idx % 3]:
                    if st.button(f"{user['name']}", use_container_width=True, key=f"quick_login_{user['user_id']}"):
                        st.session_state.user_id = user['user_id']
                        st.session_state.user_name = user['name']
                        st.session_state.mode = 'home'
                        st.rerun()
        else:
            st.caption("💡 No previous users yet. Enter your name above to get started!")
        st.markdown('</div>', unsafe_allow_html=True)

        # Admin access (collapsed by default)
        with st.expander("🔑 Admin Access"):
            st.caption("Admin-only section for progress monitoring")
            admin_password = st.text_input("Admin Password:", type="password", key="admin_pass")
            if st.button("Access Admin Dashboard", use_container_width=True):
                if admin_password == "admin123":  # Simple password - change in production
                    st.session_state.user_id = -1  # Special admin ID
                    st.session_state.user_name = "ADMIN"
                    st.session_state.mode = 'admin'
                    st.rerun()
                elif admin_password:
                    st.error("❌ Incorrect password")

# ==================== ADMIN DASHBOARD ====================

def show_admin_dashboard():
    """Admin view for monitoring all users and their progress"""
    st.set_page_config(page_title="Admin Dashboard", page_icon="👨‍💼", layout="wide")

    st.title("👨‍💼 ADMIN DASHBOARD - User Progress Monitoring")
    st.subheader("Track all users and their learning progress")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("← Back to Login"):
            st.session_state.mode = 'login'
            st.session_state.user_id = None
            st.session_state.user_name = None
            st.rerun()

    st.markdown("---")

    # Get all users
    all_users = get_all_users()

    if not all_users:
        st.info("📊 No users yet. The app is ready to use!")
        return

    # Summary stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Users", len(all_users))
    with col2:
        total_sessions = sum(u['total_sessions'] for u in all_users)
        st.metric("Total Sessions", total_sessions)
    with col3:
        total_score = sum(u['total_score'] for u in all_users)
        st.metric("Combined Score", int(total_score))
    with col4:
        avg_sessions = total_sessions / len(all_users) if all_users else 0
        st.metric("Avg Sessions/User", f"{avg_sessions:.1f}")

    st.markdown("---")

    # User list with filtering
    st.write("### 📋 User List")

    user_names = [u['name'] for u in all_users]
    selected_user_name = st.selectbox("Select a user to view details:", user_names)

    selected_user = next((u for u in all_users if u['name'] == selected_user_name), None)

    if selected_user:
        st.markdown(f"## {selected_user['name']}'s Progress")

        user_id = selected_user['user_id']
        user_stats = get_user_stats(user_id)
        user_sessions = get_user_sessions(user_id)

        # User stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Questions Answered", user_stats['total_questions'])
        with col2:
            st.metric("Correct Answers", user_stats['correct_answers'])
        with col3:
            st.metric("Overall Accuracy", f"{user_stats['overall_accuracy']:.1f}%")
        with col4:
            st.metric("Total Sessions", user_stats['total_sessions'])

        st.markdown("---")

        # Performance by difficulty
        st.write("### Performance by Difficulty")
        diff_perf = get_user_performance_by_difficulty(user_id)
        if diff_perf:
            diff_df = pd.DataFrame([
                {
                    'Difficulty': d.upper(),
                    'Correct': diff_perf[d]['correct'],
                    'Total': diff_perf[d]['total'],
                    'Accuracy': f"{diff_perf[d]['accuracy']:.1f}%"
                }
                for d in ['easy', 'medium', 'hard']
                if d in diff_perf
            ])
            st.dataframe(diff_df, use_container_width=True)

        st.markdown("---")

        # Performance by concept
        st.write("### Performance by Concept")
        concept_perf = get_user_performance_by_concept(user_id)
        if concept_perf:
            concept_df = pd.DataFrame([
                {
                    'Concept': c,
                    'Correct': concept_perf[c]['correct'],
                    'Total': concept_perf[c]['total'],
                    'Accuracy': f"{concept_perf[c]['accuracy']:.1f}%"
                }
                for c in sorted(concept_perf.keys())
            ])
            st.dataframe(concept_df, use_container_width=True)

        st.markdown("---")

        # Session history
        st.write("### Session History")
        if user_sessions:
            session_df = pd.DataFrame([
                {
                    'Date': s['start_time'][:10],
                    'Type': s['quiz_type'],
                    'Topic': s['topic'] or '-',
                    'Score': f"{s['score']}/{s['total_questions']}",
                    'Accuracy': f"{s['accuracy']:.1f}%" if s['accuracy'] else '-'
                }
                for s in user_sessions
            ])
            st.dataframe(session_df, use_container_width=True)
        else:
            st.info("No sessions yet for this user")

        # Export data button
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Export User Data as CSV"):
                csv_data = export_user_data_csv(user_id)
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name=f"{selected_user['name']}_progress.csv",
                    mime="text/csv"
                )

    st.markdown("---")
    st.write("### 📊 All Users Comparison")

    all_users_df = pd.DataFrame([
        {
            'Name': u['name'],
            'Sessions': u['total_sessions'],
            'Total Score': u['total_score'],
            'Joined': u['created_date'][:10]
        }
        for u in sorted(all_users, key=lambda x: x['total_sessions'], reverse=True)
    ])
    st.dataframe(all_users_df, use_container_width=True)

# ==================== QUESTIONS HELPER ====================

def get_all_questions_flat(topic=None, difficulty=None):
    """Get flat list of all MCQ questions only"""
    all_q = []
    topics = [topic] if topic else ['Water_Cycles', 'Reproduction', 'Electrical_Systems']

    for t in topics:
        if t in COMPREHENSIVE_QUESTIONS:
            diffs = [difficulty] if difficulty else ['easy', 'medium', 'hard']
            for d in diffs:
                if d in COMPREHENSIVE_QUESTIONS[t]:
                    # Filter for MCQ only
                    for q in COMPREHENSIVE_QUESTIONS[t][d]:
                        if q.get('type') == 'MCQ':
                            all_q.append(q)

    return all_q

def get_challenge_questions(topic=None):
    """Get challenge questions (PSLE brain drainers)"""
    all_q = []
    topics = [topic] if topic else ['Water_Cycles', 'Reproduction', 'Electrical_Systems']

    for t in topics:
        if t in CHALLENGE_QUESTIONS:
            for q in CHALLENGE_QUESTIONS[t]:
                if q.get('type') == 'MCQ':
                    all_q.append(q)

    return all_q

def get_question_by_id(q_id):
    """Get specific question by ID"""
    for topic in COMPREHENSIVE_QUESTIONS:
        for difficulty in COMPREHENSIVE_QUESTIONS[topic]:
            for q in COMPREHENSIVE_QUESTIONS[topic][difficulty]:
                if q['id'] == q_id:
                    return q
    return None

# ==================== TIER 1: QUESTION TRACKING FUNCTIONS ====================

def get_harder_difficulty(current_difficulty):
    """Get next difficulty level"""
    difficulty_levels = {
        'easy': 'medium',
        'medium': 'hard',
        'hard': 'hard'  # Stay at hard
    }
    return difficulty_levels.get(current_difficulty, 'hard')


def track_question_answer(user_id, question_id, is_correct, difficulty, chapter='', quiz_mode=''):
    """Track user's answer and update question history + queue"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()

        # Check if question history already exists
        cursor.execute("""
            SELECT times_seen, times_correct, times_incorrect
            FROM question_history
            WHERE user_id=? AND question_id=? AND quiz_mode=?
        """, (user_id, question_id, quiz_mode))

        existing = cursor.fetchone()

        if existing:
            # Update existing record
            times_seen, times_correct, times_incorrect = existing
            new_times_seen = times_seen + 1
            new_times_correct = times_correct + (1 if is_correct else 0)
            new_times_incorrect = times_incorrect + (0 if is_correct else 1)

            cursor.execute("""
                UPDATE question_history
                SET times_seen=?, times_correct=?, times_incorrect=?,
                    last_seen_date=?, max_difficulty_attempted=?
                WHERE user_id=? AND question_id=? AND quiz_mode=?
            """, (new_times_seen, new_times_correct, new_times_incorrect,
                  datetime.now().isoformat(), difficulty,
                  user_id, question_id, quiz_mode))
        else:
            # Insert new record
            cursor.execute("""
                INSERT INTO question_history
                (user_id, question_id, chapter, quiz_mode, first_seen_date,
                 last_seen_date, times_seen, times_correct, times_incorrect,
                 max_difficulty_attempted)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (user_id, question_id, chapter, quiz_mode,
                  datetime.now().isoformat(), datetime.now().isoformat(),
                  1, (1 if is_correct else 0), (0 if is_correct else 1),
                  difficulty))

        # If wrong answer, add to queue with higher difficulty
        if not is_correct:
            new_difficulty = get_harder_difficulty(difficulty)
            cursor.execute("""
                INSERT INTO question_queue
                (user_id, question_id, chapter, queue_type, difficulty_level,
                 added_date, priority)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, question_id, chapter, 'wrong_answer', new_difficulty,
                  datetime.now().isoformat(), 10))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        st.error(f"Database error in track_question_answer: {e}")
        pass  # Silently fail to avoid breaking quiz flow


def queue_next_question(user_id, chapter, quiz_mode):
    """Get next question from queue (priority order)"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()

        cursor.execute("""
            SELECT question_id, queue_type, difficulty_level
            FROM question_queue
            WHERE user_id = ? AND chapter = ?
            ORDER BY
                CASE queue_type
                    WHEN 'wrong_answer' THEN 1
                    WHEN 'review' THEN 2
                    WHEN 'new' THEN 3
                END,
                priority DESC,
                added_date ASC
            LIMIT 1
        """, (user_id, chapter))

        result = cursor.fetchone()
        conn.close()

        return result  # Returns (question_id, queue_type, difficulty_level) or None

    except sqlite3.Error as e:
        return None


def get_next_question(user_id, chapter, quiz_mode, all_questions):
    """Smart question selection with history tracking and variations
    Returns: (question_dict, difficulty_level) or (None, None)
    """
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()

        # Step 1: Check queue first (wrong answers get priority)
        queued = queue_next_question(user_id, chapter, quiz_mode)
        if queued:
            question_id, queue_type, difficulty = queued
            # Find the actual question
            for q in all_questions:
                if q['id'] == question_id:
                    conn.close()
                    return q, difficulty

        # Step 2: Get list of seen questions
        cursor.execute("""
            SELECT question_id FROM question_history
            WHERE user_id = ? AND quiz_mode = ?
        """, (user_id, quiz_mode))

        seen_questions = {row[0] for row in cursor.fetchall()}
        conn.close()

        # Step 3: Filter out seen questions
        unseen = [q for q in all_questions
                  if q['id'] not in seen_questions]

        if unseen:
            return random.choice(unseen), 'easy'

        # Step 4: All base questions seen, generate variations (Tier 2)
        # Only do this if we've seen many questions
        if len(seen_questions) > 50:
            try:
                variations = get_all_variations_cached()
                if variations:
                    return random.choice(variations), 'easy'
            except:
                pass  # Fallback if variations fail

        # Step 5: Restart from beginning of base questions
        if all_questions:
            return random.choice(all_questions), 'easy'

        return None, None

    except sqlite3.Error as e:
        # Fallback to random if database fails
        if all_questions:
            return random.choice(all_questions), 'easy'
        return None, None


# ==================== TIER 2: QUESTION VARIATION GENERATOR ====================

def generate_question_variation(template, variation_num=1):
    """Generate a single variation from a parameterized template
    Args:
        template: Template dict with template, answer_formula, parameters, etc.
        variation_num: Which variation number (for generating unique questions)
    Returns:
        Dictionary with generated question text, answer, difficulty, etc.
    """
    import itertools

    # Get all parameter combinations
    param_names = list(template.get('parameters', {}).keys())
    if not param_names:
        # No parameters, return template as-is
        return {
            'id': f"{template.get('template_id', 'unknown')}_v0",
            'type': 'MCQ',
            'q': template['template'],
            'answer': template['answer_formula']({}),
            'explanation': f"Based on concept: {template.get('concept', 'Unknown')}",
            'ref': template.get('chapter', 'General'),
            'concept': template.get('concept', 'Unknown'),
            'difficulty': template.get('difficulty', 'medium'),
            'options': ['Yes', 'No', 'Sometimes', 'Cannot determine'],
        }

    # Sample random values from parameter ranges
    params = {}
    for param_name in param_names:
        param_values = template['parameters'][param_name]
        # Use variation_num to pick different values for each variation
        if isinstance(param_values, list):
            idx = (variation_num + hash(param_name)) % len(param_values)
            params[param_name] = param_values[idx]

    # Generate question text
    question_text = template['template'].format(**params)

    # Compute answer using the formula
    answer = str(template['answer_formula'](params))

    # Create variation object
    variation = {
        'id': f"{template.get('template_id', 'unknown')}_v{variation_num}",
        'type': 'MCQ',
        'q': question_text,
        'answer': answer,
        'explanation': f"Concept: {template.get('concept', 'Unknown')} | Parameters: {params}",
        'ref': f"Template: {template.get('chapter', 'General')}",
        'concept': template.get('concept', 'Unknown'),
        'difficulty': template.get('difficulty', 'medium'),
        'parameters': params,
    }

    return variation


def generate_all_variations(num_per_template=10):
    """Generate all variations from templates
    Args:
        num_per_template: How many variations to generate per template
    Returns:
        List of all generated variation questions
    """
    try:
        from components.question_templates import QUESTION_TEMPLATES
    except ImportError:
        # Fallback if import path is different
        try:
            from src.components.question_templates import QUESTION_TEMPLATES
        except ImportError:
            return []  # Return empty if can't import

    all_variations = []

    for template_id, template in QUESTION_TEMPLATES.items():
        template['template_id'] = template_id  # Add ID to template

        for var_num in range(num_per_template):
            try:
                variation = generate_question_variation(template, var_num)
                all_variations.append(variation)
            except Exception as e:
                # Skip templates that fail
                continue

    return all_variations


# Cache for generated variations (to avoid regenerating)
_variation_cache = {}

def get_all_variations_cached(force_refresh=False):
    """Get all variations, using cache if available"""
    if not _variation_cache or force_refresh:
        _variation_cache['variations'] = generate_all_variations()
        _variation_cache['count'] = len(_variation_cache['variations'])

    return _variation_cache.get('variations', [])


# ==================== DISPLAY FUNCTIONS ====================

def display_question(question, num, total):
    """Display a question with all details"""
    st.markdown(f"## Q{num}/{total}: {question['q']}")

    # Safe difficulty access
    difficulty = question.get('difficulty', 'medium')
    st.caption(f"📌 **Concept**: {question['concept']} | **Ref**: {question['ref']} | **Difficulty**: {difficulty.upper()}")

    if question['type'] == 'MCQ':
        # BUG FIX: Restore previous answer if it exists (so students can't cheat by going back)
        previous_answer = None
        previous_confidence = 3
        if question['id'] in st.session_state.answers:
            previous_answer = st.session_state.answers[question['id']].get('user_answer')
            previous_confidence = st.session_state.answers[question['id']].get('confidence', 3)

        # Find index of previous answer in options (if exists)
        answer_index = 0
        if previous_answer and previous_answer in question['options']:
            answer_index = question['options'].index(previous_answer)

        answer = st.radio(
            "Select your answer:",
            question['options'],
            index=answer_index,  # ← RESTORED: Show previous selection
            key=f"q_{question['id']}"
        )
        confidence = st.slider(
            "How confident are you? (1=Guess, 5=Very Sure)",
            1, 5, previous_confidence,  # ← RESTORED: Show previous confidence
            key=f"conf_{question['id']}"
        )
        return answer, confidence
    else:
        # BUG FIX: Restore previous answer for text input
        previous_answer = ""
        previous_confidence = 3
        if question['id'] in st.session_state.answers:
            previous_answer = st.session_state.answers[question['id']].get('user_answer', "")
            previous_confidence = st.session_state.answers[question['id']].get('confidence', 3)

        answer = st.text_area(
            "Write your answer (2-3 sentences with key terms):",
            value=previous_answer,  # ← RESTORED: Show previous answer
            key=f"q_{question['id']}",
            height=120
        )
        confidence = st.slider(
            "How confident are you?",
            1, 5, previous_confidence,  # ← RESTORED: Show previous confidence
            key=f"conf_{question['id']}"
        )
        return answer, confidence

def check_answer(question, user_answer):
    """Check answer correctness"""
    if question['type'] == 'MCQ':
        return user_answer == question['answer'], question['answer']
    else:
        answer_lower = question['answer'].lower()
        response_lower = user_answer.lower()
        key_terms = [w for w in answer_lower.split() if len(w) > 3]
        matches = sum(1 for term in key_terms if term in response_lower)
        threshold = max(2, len(key_terms) // 2)
        is_correct = matches >= threshold
        return is_correct, question['answer']

# ==================== MAIN APP ====================

def show_home():
    """Home page with learning paths"""
    st.set_page_config(page_title="Exam Prep Pro", page_icon="🧪", layout="wide")

    # ============ HEADER WITH USER INFO ============
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.title("🧪 SCIENCE EXAM PREP PRO")
        st.subheader("MCQ-Focused PSLE Training System")
    with col2:
        st.metric("📚 Total MCQs", "25+", "All PSLE Format")
    with col3:
        col3a, col3b = st.columns(2)
        with col3a:
            st.write(f"👤 **{st.session_state.user_name}**")
        with col3b:
            if st.button("🚪 Logout"):
                st.session_state.mode = 'login'
                st.session_state.user_id = None
                st.session_state.user_name = None
                st.rerun()

    # ============ ATTRACTIVE WELCOME BANNER ============
    user_name = st.session_state.user_name
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px;
                padding: 30px;
                text-align: center;
                color: white;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h1 style="margin: 0; font-size: 2.5em;">🌟 Welcome, {user_name}! 🌟</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.2em; opacity: 0.95;">
            🚀 Ready to ace your PSLE Science exam? Let's get started!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ============ KEY STATS ============
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

    # ============ LEARNING PATHS ============
    st.markdown("""
    <div style="text-align: center; margin: 30px 0 20px 0;">
        <h2 style="color: #667eea; margin: 0;">🎯 Choose Your Learning Path</h2>
        <p style="color: #666; margin-top: 5px;">Pick the learning style that works best for you</p>
    </div>
    """, unsafe_allow_html=True)

    # Three main modes with enhanced styling
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    color: white;
                    min-height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;">
            <div>
                <h3 style="margin-top: 0;">📖 Topic Mastery</h3>
                <p>Learn one topic at a time. No timer, focus on understanding.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Topic Practice →", key="topic_btn", use_container_width=True):
            st.session_state.mode = 'topic_select'
            st.rerun()

    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    color: white;
                    min-height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;">
            <div>
                <h3 style="margin-top: 0;">🎯 Mock Exam</h3>
                <p>Full 45-minute realistic test. All 25+ MCQ questions.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Mock Exam →", key="mock_btn", use_container_width=True):
            st.session_state.mode = 'mock_exam'
            st.session_state.exam_started = True
            st.session_state.exam_start_time = time.time()
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.session_state.current_session_id = None  # Reset for new session
            st.rerun()

    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    color: white;
                    min-height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;">
            <div>
                <h3 style="margin-top: 0;">📊 Performance Review</h3>
                <p>Analyze your strengths and weaknesses.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Analytics →", key="analytics_btn", use_container_width=True):
            st.session_state.mode = 'analytics'
            st.rerun()

    st.markdown("---")

    # ============ CHALLENGE SECTION ============
    st.markdown("""
    <div style="text-align: center; margin: 30px 0 20px 0;">
        <h2 style="color: #764ba2; margin: 0;">🧠 Challenge Yourself!</h2>
        <p style="color: #666; margin-top: 5px;">Test your deeper understanding with PSLE brain drainers</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                border-radius: 10px;
                padding: 25px;
                text-align: center;
                color: white;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h3 style="margin-top: 0; font-size: 1.8em;">🎯 Challenge to {user_name}!</h3>
        <p style="font-size: 1.1em; margin: 10px 0;">
            🧠 <strong>PSLE-Style Brain Drainers</strong> - Tricky questions with similar-looking options!
        </p>
        <p style="margin: 10px 0 0 0; opacity: 0.95;">
            Test your DEEPER understanding with confusing questions designed to catch misconceptions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start Brain Drain Challenge →", key="challenge_btn", use_container_width=True):
        st.session_state.mode = 'challenge'
        st.session_state.challenge_question_idx = 0
        st.session_state.challenge_score = 0
        st.rerun()

    st.markdown("---")
    st.write("## 📊 Manage Your Learning")

    # Progress and Settings
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📈 **Progress Tracker**")
        st.write("View detailed statistics and learning history.")
        if st.button("View Progress →", key="progress_btn", use_container_width=True):
            st.session_state.mode = 'progress'
            st.rerun()

    with col2:
        st.markdown("### ⚙️ **Settings**")
        st.write("Manage progress, reset data, and customize settings.")
        if st.button("Open Settings →", key="settings_btn", use_container_width=True):
            st.session_state.mode = 'settings'
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


# ==================== CHAPTER CONTENT DISPLAY (v4.4) ====================

def show_chapter_content(chapter_name):
    """Display comprehensive chapter learning interface with tabs"""
    st.title(f"📚 {chapter_name} | {st.session_state.user_name}")

    # Initialize session state for chapter
    if f"{chapter_name}_tab" not in st.session_state:
        st.session_state[f"{chapter_name}_tab"] = 0

    # Tab interface based on chapter
    tabs = st.tabs(["📖 Learn", "🎯 Match", "❓ Practice", "🎮 Game", "🧠 Challenge", "📊 Progress"])

    with tabs[0]:  # Learn Tab
        st.subheader(f"Flashcards - {chapter_name}")
        show_chapter_flashcards(chapter_name)

    with tabs[1]:  # Match Tab
        st.subheader(f"Concept Matching - {chapter_name}")
        show_chapter_matching(chapter_name)

    with tabs[2]:  # Practice Tab
        st.subheader(f"Practice Quiz - {chapter_name}")
        show_chapter_quiz(chapter_name)

    with tabs[3]:  # Game Tab
        st.subheader(f"Interactive Game - {chapter_name}")
        show_chapter_minigame(chapter_name)

    with tabs[4]:  # Challenge Tab
        st.subheader(f"Challenge Mode - {chapter_name}")
        show_chapter_brain_drainers(chapter_name)

    with tabs[5]:  # Progress Tab
        st.subheader(f"Your Progress - {chapter_name}")
        show_chapter_progress(chapter_name)

    # Back button
    col1, col2, col3 = st.columns([4, 1, 1])
    with col3:
        if st.button("← Back to Chapters", key=f"back_{chapter_name}"):
            st.session_state.mode = 'topic_select'
            st.rerun()


def show_chapter_flashcards(chapter_name):
    """Display flashcards for chapter"""
    try:
        # Get topic key from chapter name
        if "Ch 1" in chapter_name or "Reproduction" in chapter_name:
            topic_key = "Reproduction"
        elif "Ch 2" in chapter_name or "Water" in chapter_name:
            topic_key = "Water_Cycles"
        elif "Ch 3" in chapter_name or "Plant" in chapter_name:
            topic_key = "Plant_Transport"
        elif "Ch 4" in chapter_name or "Human" in chapter_name:
            topic_key = "Human_Systems"
        elif "Ch 5" in chapter_name or "Electrical" in chapter_name:
            topic_key = "Electrical_Systems"
        elif "Ch 6" in chapter_name or "Circuit" in chapter_name:
            topic_key = "Electric_Circuits"
        else:
            st.warning("Chapter not found")
            return

        # Get flashcards from dict
        flashcards = CHAPTER_FLASHCARDS.get(topic_key, [])

        if not flashcards:
            st.info("Flashcards coming soon for this chapter!")
            return

        # Initialize flashcard state
        card_key = f"flashcard_index_{chapter_name}"
        if card_key not in st.session_state:
            st.session_state[card_key] = 0

        # Display current card
        current_idx = st.session_state[card_key]
        if current_idx < len(flashcards):
            card = flashcards[current_idx]
            concept = card.get('concept', 'Unknown')
            definition = card.get('definition', 'No definition')

            # Flashcard display
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                <div style="
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    padding: 30px;
                    text-align: center;
                    background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
                    color: white;
                    min-height: 200px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                ">
                    <h2>{concept}</h2>
                    <hr style="margin: 20px 0;">
                    <p style="font-size: 18px;">{definition}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.metric("Card", f"{current_idx + 1}/{len(flashcards)}")

            # Navigation
            nav_col1, nav_col2, nav_col3 = st.columns(3)
            with nav_col1:
                if st.button("⬅️ Previous", disabled=(current_idx == 0), key=f"prev_flash_{chapter_name}"):
                    st.session_state[card_key] = max(0, current_idx - 1)
                    st.rerun()

            with nav_col2:
                if st.button("Next ➡️", disabled=(current_idx >= len(flashcards) - 1), key=f"next_flash_{chapter_name}"):
                    st.session_state[card_key] = min(len(flashcards) - 1, current_idx + 1)
                    st.rerun()

            with nav_col3:
                if st.button("Reset", key=f"reset_flash_{chapter_name}"):
                    st.session_state[card_key] = 0
                    st.rerun()

    except ImportError as e:
        st.error(f"Could not load flashcards: {e}")


def show_chapter_matching(chapter_name):
    """Display matching pairs for chapter"""
    try:
        # Get topic key from chapter name
        if "Ch 1" in chapter_name or "Reproduction" in chapter_name:
            topic_key = "Reproduction"
        elif "Ch 2" in chapter_name or "Water" in chapter_name:
            topic_key = "Water_Cycles"
        elif "Ch 3" in chapter_name or "Plant" in chapter_name:
            topic_key = "Plant_Transport"
        elif "Ch 4" in chapter_name or "Human" in chapter_name:
            topic_key = "Human_Systems"
        elif "Ch 5" in chapter_name or "Electrical" in chapter_name:
            topic_key = "Electrical_Systems"
        elif "Ch 6" in chapter_name or "Circuit" in chapter_name:
            topic_key = "Electric_Circuits"
        else:
            st.warning("Chapter not found")
            return

        # Get matching pairs from dict
        pairs = CHAPTER_MATCHING_PAIRS.get(topic_key, [])

        if not pairs:
            st.info("Matching pairs coming soon for this chapter!")
            return

        st.write("**Match the concepts on the left with their definitions on the right.**")
        st.info(f"There are {len(pairs)} pairs to match.")

        # Display all pairs in two columns
        col1, col2 = st.columns(2)

        # Get first half and shuffle second half to make it challenging
        import random
        left_items = [item[0] for item in pairs]
        right_items = [item[1] for item in pairs]
        right_shuffled = right_items.copy()
        random.shuffle(right_shuffled)

        with col1:
            st.subheader("Concepts")
            for i, item in enumerate(left_items, 1):
                st.write(f"{i}. {item}")

        with col2:
            st.subheader("Definitions")
            for i, item in enumerate(right_shuffled, 1):
                st.write(f"• {item}")

        # Show answer button
        if st.button("Show Correct Answers", key=f"show_matching_{chapter_name}"):
            st.success("**Correct Matches:**")
            for concept, definition in pairs:
                st.write(f"✓ **{concept}** → *{definition}*")

        # Track completion
        if st.button("Mark as Completed", key=f"complete_matching_{chapter_name}"):
            st.success("✅ Matching exercise completed!")
            track_question_answer(
                st.session_state.user_id,
                f'{topic_key}_matching',
                True,
                'easy',
                chapter=topic_key,
                quiz_mode='matching'
            )

    except Exception as e:
        st.error(f"Error loading matching pairs: {e}")


def show_chapter_quiz(chapter_name):
    """Display practice quiz for chapter - answers hidden until shown"""
    try:
        # Get questions for chapter from COMPREHENSIVE_QUESTIONS
        if "🌱 Ch 1" in chapter_name or "Reproduction" in chapter_name:
            topic_key = "Reproduction"
        elif "💧 Ch 2" in chapter_name or "Water" in chapter_name:
            topic_key = "Water_Cycles"
        elif "🌿 Ch 3" in chapter_name or "Plant" in chapter_name:
            topic_key = "Plant_Transport"
        elif "❤️ Ch 4" in chapter_name or "Human" in chapter_name:
            topic_key = "Human_Systems"
        elif "⚡ Ch 5" in chapter_name or "Electrical" in chapter_name:
            topic_key = "Electrical_Systems"
        elif "🔌 Ch 6" in chapter_name or "Circuit" in chapter_name:
            topic_key = "Electric_Circuits"
        else:
            st.warning("Chapter not found in question bank")
            return

        questions = get_all_questions_flat(topic_key)
        if not questions:
            st.info("Questions coming soon for this chapter!")
            return

        quiz_key = f"quiz_idx_{chapter_name}"
        answer_key = f"quiz_answered_{chapter_name}"

        if quiz_key not in st.session_state:
            st.session_state[quiz_key] = 0
            st.session_state[answer_key] = False

        current_idx = st.session_state[quiz_key]
        if current_idx >= len(questions):
            # Show summary
            score = st.session_state.get(f"quiz_score_{chapter_name}", 0)
            total = len(questions)
            accuracy = round((score / total * 100) if total > 0 else 0, 1)

            st.success(f"🎉 Quiz Complete! Score: {score}/{total} ({accuracy}%)")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Retake Quiz", key=f"restart_quiz_{chapter_name}"):
                    st.session_state[quiz_key] = 0
                    st.session_state[answer_key] = False
                    st.session_state[f"quiz_score_{chapter_name}"] = 0
                    st.rerun()
            with col2:
                if st.button("Back to Chapter", key=f"back_chapter_{chapter_name}"):
                    st.session_state.mode = 'chapter_content'
                    st.rerun()
            return

        question = questions[current_idx]

        # Initialize score if not exists
        if f"quiz_score_{chapter_name}" not in st.session_state:
            st.session_state[f"quiz_score_{chapter_name}"] = 0

        # Display question
        st.progress((current_idx + 1) / len(questions))
        st.write(f"**Question {current_idx + 1}/{len(questions)}**")
        st.write(f"**Concept**: {question.get('concept', 'General')}")

        user_answer, confidence = display_question(question, current_idx + 1, len(questions))

        # Create answer tracking state
        if f"user_answer_{chapter_name}_{current_idx}" not in st.session_state:
            st.session_state[f"user_answer_{chapter_name}_{current_idx}"] = None

        # Store user answer
        if user_answer:
            st.session_state[f"user_answer_{chapter_name}_{current_idx}"] = user_answer

        st.markdown("---")

        # Action buttons
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Submit Answer", key=f"submit_{chapter_name}_{current_idx}"):
                if user_answer:
                    st.session_state[answer_key] = True
                else:
                    st.warning("Please select an answer first")

        # Show answer button - only if submitted
        if st.session_state.get(answer_key, False):
            with col2:
                if st.button("📖 Show Answer & Explanation", key=f"show_answer_{chapter_name}_{current_idx}"):
                    is_correct, correct_answer = check_answer(question, user_answer)

                    if is_correct:
                        st.success("✅ CORRECT! Great job!")
                        st.session_state[f"quiz_score_{chapter_name}"] += 1
                    else:
                        st.error(f"❌ Not quite right. Correct answer: **{correct_answer}**")

                    st.info(f"**Explanation**: {question['explanation']}")

                    # Track the answer
                    track_question_answer(
                        st.session_state.user_id,
                        question['id'],
                        is_correct,
                        question.get('difficulty', 'medium'),
                        chapter=topic_key,
                        quiz_mode='chapter_quiz'
                    )

        with col3:
            if st.button("Next Question ➡️", key=f"next_quiz_{chapter_name}_{current_idx}"):
                st.session_state[quiz_key] = current_idx + 1
                st.session_state[answer_key] = False
                st.rerun()

    except Exception as e:
        st.error(f"Error loading quiz: {e}")


def show_chapter_minigame(chapter_name):
    """Display mini-game for chapter"""
    try:
        from components.minigames import SequencingGame, DragDropGame

        if "Ch 1" in chapter_name or "Reproduction" in chapter_name:
            st.write("🎮 **Plant the Seed Game**: Arrange plant life cycle stages in correct order")

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
                st.success("✅ Perfect! You've completed the Plant the Seed game!")
                # Track the game completion
                track_question_answer(
                    st.session_state.user_id,
                    'ch1_minigame_plant',
                    True,
                    'medium',
                    chapter='Reproduction',
                    quiz_mode='minigame'
                )

        elif "Ch 2" in chapter_name or "Water" in chapter_name:
            st.write("🎮 **Water Cycle Sorter**: Categorize water cycle processes")

            # Water cycle items to categorize
            items = [
                "Sun heats ocean water",
                "Water becomes invisible gas",
                "Vapor rises into atmosphere",
                "Cool air cools water vapor",
                "Droplets form clouds",
                "Clouds become heavy",
                "Water falls as rain",
                "Rain flows into rivers and lakes",
                "Water returns to ocean",
                "Cycle begins again",
                "Plants release water vapor",
                "Animals drink water"
            ]

            categories = ["Evaporation", "Condensation", "Precipitation", "Accumulation"]

            st.info("📝 Drag each item to the correct water cycle stage:")
            st.write("- **Evaporation**: Water becomes vapor")
            st.write("- **Condensation**: Vapor becomes water droplets")
            st.write("- **Precipitation**: Water falls from clouds")
            st.write("- **Accumulation**: Water collects in oceans/lakes")

            # Store game state
            game_key = f"water_cycle_game_{st.session_state.user_id}"
            if game_key not in st.session_state:
                st.session_state[game_key] = {'completed': False}

            if not st.session_state[game_key]['completed']:
                st.warning("🎮 Interactive drag-and-drop game coming soon! For now, practice with the quiz above.")

        elif "Ch 5" in chapter_name or "Electrical" in chapter_name:
            st.write("🎮 **Circuit Builder**: Arrange electrical components in correct circuit order")

            components = [
                'Battery (energy source)',
                'Switch (control)',
                'Wire (conductor)',
                'Light Bulb (load)',
                'Resistor (reduces current)',
                'Ground (complete circuit)'
            ]

            correct_order = components.copy()

            st.info("📝 A complete circuit needs these components in order:")
            st.write("1. **Battery**: Provides electrical energy")
            st.write("2. **Switch**: Controls the circuit on/off")
            st.write("3. **Wire**: Carries current as conductor")
            st.write("4. **Light Bulb**: Uses energy (load)")
            st.write("5. **Resistor**: Controls current flow")
            st.write("6. **Ground**: Completes the circuit")

            is_correct = SequencingGame.create_sequence_game(components, correct_order, "Build a Complete Circuit")

            if is_correct:
                st.success("✅ Perfect! You've built a complete circuit!")
                # Track the game completion
                track_question_answer(
                    st.session_state.user_id,
                    'ch5_minigame_circuit',
                    True,
                    'hard',
                    chapter='Electrical_Systems',
                    quiz_mode='minigame'
                )

        elif "Ch 3" in chapter_name or "Plant" in chapter_name:
            st.write("🎮 **Plant Transport Puzzle**: Match plant systems to their functions")

            concepts = ['Xylem', 'Phloem', 'Roots', 'Leaves', 'Stem', 'Root Hairs']
            functions = ['Carries water and minerals', 'Carries food (glucose)', 'Absorbs water and minerals',
                        'Make food; lose water', 'Contains transport tubes', 'Increase absorption surface']

            st.info("📝 Match each plant system (left) to its function (right):")

            cols = st.columns(2)
            with cols[0]:
                st.write("**Plant Parts:**")
                for c in concepts:
                    st.write(f"• {c}")
            with cols[1]:
                st.write("**Functions:**")
                for f in functions:
                    st.write(f"• {f}")

            st.success("✅ Review the flashcards and matching section for the answers!")
            track_question_answer(
                st.session_state.user_id,
                'ch3_minigame_transport',
                True,
                'medium',
                chapter='Plant_Transport',
                quiz_mode='minigame'
            )

        elif "Ch 4" in chapter_name or "Human" in chapter_name:
            st.write("🎮 **Respiratory System Journey**: Trace air through your body")

            st.info("📝 Follow the path of air through your respiratory system:")
            st.write("1. **Nose**: Warms and moistens air; filters dust")
            st.write("2. **Windpipe (Trachea)**: Carries air to lungs")
            st.write("3. **Lungs**: Oxygen enters blood; CO₂ leaves blood")
            st.write("4. **Heart**: Pumps oxygen-rich blood throughout body")
            st.write("5. **Body Cells**: Use oxygen; produce CO₂")
            st.write("6. **Veins**: Return deoxygenated blood with CO₂")
            st.write("7. **Back to Lungs**: Cycle repeats!")

            col1, col2 = st.columns(2)
            with col1:
                pulse_visible = st.checkbox("Can you feel your pulse?")
                if pulse_visible:
                    st.success("Great! That's your heart pumping blood!")
            with col2:
                breathing_rate = st.slider("How many breaths per minute (at rest)?", 10, 30, 15)
                st.info(f"Normal breathing rate: 12-20 breaths/minute. Yours: {breathing_rate}")

            st.success("✅ Respiratory System Journey Completed!")
            track_question_answer(
                st.session_state.user_id,
                'ch4_minigame_respiratory',
                True,
                'medium',
                chapter='Human_Systems',
                quiz_mode='minigame'
            )

        elif "Ch 6" in chapter_name or "Circuit" in chapter_name:
            st.write("🎮 **Series vs Parallel Challenge**: Design the right circuit")

            st.info("📝 Let's design circuits with different behaviors:")

            design = st.radio("Choose a circuit design:",
                             ["Series: One path, dimmer bulbs", "Parallel: Multiple paths, brighter bulbs"])

            if design:
                if "Series" in design:
                    st.write("✓ **Series Circuit** chosen:")
                    st.write("- Single path for current")
                    st.write("- Same current through all bulbs")
                    st.write("- Voltage divides among bulbs")
                    st.write("- If one bulb burns out → all go off")
                    st.write("- Used in: String lights, some old decorations")
                else:
                    st.write("✓ **Parallel Circuit** chosen:")
                    st.write("- Multiple paths for current")
                    st.write("- Each bulb gets full voltage")
                    st.write("- Brightness stays same")
                    st.write("- If one bulb burns out → others stay on")
                    st.write("- Used in: Home wiring, most modern electronics")

            st.success("✅ Circuit Design Challenge Complete!")
            track_question_answer(
                st.session_state.user_id,
                'ch6_minigame_circuits',
                True,
                'medium',
                chapter='Electric_Circuits',
                quiz_mode='minigame'
            )

        else:
            st.info("Mini-games coming soon for this chapter!")

    except ImportError as e:
        st.error(f"Could not load mini-games: {e}")


def show_chapter_brain_drainers(chapter_name):
    """Display brain drainer challenge questions"""
    st.write("PSLE-style tricky questions designed to test deeper understanding!")

    try:
        # Get brain drainer questions from CHALLENGE_QUESTIONS
        if "🌱 Ch 1" in chapter_name or "Reproduction" in chapter_name:
            topic_key = "Reproduction"
        elif "💧 Ch 2" in chapter_name or "Water" in chapter_name:
            topic_key = "Water_Cycles"
        elif "🌿 Ch 3" in chapter_name or "Plant" in chapter_name:
            topic_key = "Plant_Transport"
        elif "❤️ Ch 4" in chapter_name or "Human" in chapter_name:
            topic_key = "Human_Systems"
        elif "⚡ Ch 5" in chapter_name or "Electrical" in chapter_name:
            topic_key = "Electrical_Systems"
        elif "🔌 Ch 6" in chapter_name or "Circuit" in chapter_name:
            topic_key = "Electric_Circuits"
        else:
            st.warning("Chapter not found")
            return

        if topic_key not in CHALLENGE_QUESTIONS:
            st.info(f"🧠 Brain drainers for {chapter_name} coming soon! Practice with the regular quiz for now.")
            return

        questions = CHALLENGE_QUESTIONS[topic_key]
        if not questions:
            st.info("No brain drainers available yet for this chapter.")
            return

        drainer_key = f"drainer_idx_{chapter_name}"
        if drainer_key not in st.session_state:
            st.session_state[drainer_key] = 0

        current_idx = st.session_state[drainer_key]
        if current_idx >= len(questions):
            st.success("🎉 Challenge Complete!")
            if st.button("Start Over", key=f"restart_drainer_{chapter_name}"):
                st.session_state[drainer_key] = 0
                st.rerun()
            return

        question = questions[current_idx]
        st.progress((current_idx + 1) / len(questions))
        st.write(f"**Challenge {current_idx + 1}/{len(questions)}**")

        user_answer, confidence = display_question(question, current_idx + 1, len(questions))

        if st.button("Submit Answer", key=f"submit_drainer_{chapter_name}_{current_idx}"):
            if user_answer:
                is_correct, correct_answer = check_answer(question, user_answer)

                if is_correct:
                    st.success("🎉 Correct! Well done!")
                else:
                    st.warning("Not quite right. Read the explanation carefully.")
                    st.info(f"**Correct Answer**: {correct_answer}")
                    st.write(f"**Explanation**: {question['explanation']}")

                if st.button("Next Challenge ➡️", key=f"next_drainer_{chapter_name}_{current_idx}"):
                    st.session_state[drainer_key] = current_idx + 1
                    st.rerun()

    except Exception as e:
        st.error(f"Error loading brain drainers: {e}")


def show_chapter_progress(chapter_name):
    """Display chapter progress and mastery stats"""
    st.write("### Your Chapter Progress")

    try:
        # Get topic key
        if "🌱 Ch 1" in chapter_name:
            topic_key = "Reproduction"
        elif "💧 Ch 2" in chapter_name:
            topic_key = "Water_Cycles"
        elif "⚡ Ch 5" in chapter_name:
            topic_key = "Electrical_Systems"
        else:
            return

        import sqlite3

        # Query progress from database
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*) as questions_seen,
                   SUM(CASE WHEN times_correct > 0 THEN 1 ELSE 0 END) as questions_correct
            FROM question_history
            WHERE user_id=? AND chapter=?
        """, (st.session_state.user_id, topic_key))

        result = cursor.fetchone()
        conn.close()

        questions_seen, questions_correct = result if result else (0, 0)
        questions_correct = questions_correct or 0

        # Display stats
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Questions Seen", questions_seen)

        with col2:
            st.metric("Correct", questions_correct)

        with col3:
            accuracy = (questions_correct / questions_seen * 100) if questions_seen > 0 else 0
            st.metric("Accuracy", f"{accuracy:.0f}%")

        with col4:
            mastery = min(100, (accuracy + (questions_seen / 20) * 10))
            st.metric("Mastery", f"{mastery:.0f}%")

        st.progress(mastery / 100)
        st.write("Keep practicing to master this chapter!")

    except Exception as e:
        st.info(f"Progress tracking: {e}")


def show_topic_select():
    """All 6 chapters learning mode - comprehensive learning experience"""
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(f"📚 Master All Chapters | {st.session_state.user_name}")
    with col2:
        if st.button("← Back"):
            st.session_state.mode = 'home'
            st.rerun()

    st.write("Learn concepts with **flashcards, matching games, mini-games, and PSLE brain drainers**")

    # All 6 chapters with descriptions
    chapters = [
        {
            'name': 'Ch 1: Reproduction in Animals & Plants',
            'emoji': '🌱',
            'key': 'Reproduction',
            'topics': ['Pollination', 'Fertilization', 'Germination', 'Animal Reproduction']
        },
        {
            'name': 'Ch 2: Cycles in Water',
            'emoji': '💧',
            'key': 'Water_Cycles',
            'topics': ['Evaporation', 'Condensation', 'Freezing', 'Melting']
        },
        {
            'name': 'Ch 3: Plant Transport',
            'emoji': '🌿',
            'key': 'Plant_Transport',
            'topics': ['Xylem', 'Phloem', 'Osmosis', 'Transpiration']
        },
        {
            'name': 'Ch 4: Human Systems',
            'emoji': '❤️',
            'key': 'Human_Systems',
            'topics': ['Circulatory', 'Respiratory', 'Digestive', 'Excretory']
        },
        {
            'name': 'Ch 5: Electrical Systems',
            'emoji': '⚡',
            'key': 'Electrical_Systems',
            'topics': ['Circuits', 'Components', 'Series', 'Parallel']
        },
        {
            'name': 'Ch 6: Electric Circuits',
            'emoji': '🔌',
            'key': 'Electric_Circuits',
            'topics': ['Conductors', 'Insulators', 'Safety', 'Applications']
        },
    ]

    # Display chapters in 2x3 grid
    cols = st.columns(2, gap="large")
    for idx, chapter in enumerate(chapters):
        column = cols[idx % 2]
        with column:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 10px;
                        padding: 20px;
                        color: white;
                        margin-bottom: 15px;">
                <h3 style="margin-top: 0; font-size: 1.3em;">{chapter['emoji']} {chapter['name']}</h3>
                <p style="margin: 10px 0;">Topics: {', '.join(chapter['topics'])}</p>
                <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.95;">
                    📖 Flashcards • 🎯 Matching • 🎮 Mini-Games • 🧠 Brain Drainers
                </p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Learn {chapter['name'].split(':')[0].strip()} →", use_container_width=True, key=f"ch_{idx}"):
                st.session_state.mode = 'chapter_content'
                st.session_state.chapter_name = f"{chapter['emoji']} {chapter['name']}"
                st.session_state.current_topic = chapter['key']
                st.rerun()

def show_practice_mode():
    """Topic practice mode"""
    topic = st.session_state.current_topic
    topic_display = {'Water_Cycles': '💧 Water Cycles', 'Reproduction': '👶 Reproduction', 'Electrical_Systems': '⚡ Electrical Systems'}

    st.title(f"{topic_display.get(topic, topic)} - Practice Mode | {st.session_state.user_name}")

    questions = get_all_questions_flat(topic)
    current_idx = st.session_state.current_question_idx

    if current_idx >= len(questions):
        show_topic_results(questions)
        return

    question = questions[current_idx]

    # Create a session for this topic practice if not exists
    if not st.session_state.current_session_id:
        st.session_state.current_session_id = create_quiz_session(
            st.session_state.user_id, 'practice', topic
        )

    # Progress
    progress = (current_idx + 1) / len(questions)
    st.progress(progress)
    st.write(f"Progress: {current_idx + 1}/{len(questions)}")

    # Display question
    with st.container(border=True):
        user_answer, confidence = display_question(question, current_idx + 1, len(questions))

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("⬅️ Previous", disabled=(current_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        if st.button("✓ Check Answer", use_container_width=True):
            if user_answer:
                # Check if this question was already answered to avoid double-counting
                question_already_answered = question['id'] in st.session_state.answers

                is_correct, correct_answer = check_answer(question, user_answer)

                # Only increment score if this is the first time answering this question
                if is_correct and not question_already_answered:
                    st.success("✅ CORRECT!")
                    st.session_state.score += 1
                    MalteseDogFeedback.show_happy_maltese(st.session_state.user_name)
                elif is_correct and question_already_answered:
                    st.success("✅ CORRECT! (Already submitted)")
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

                # Save answer to database
                save_answer(
                    st.session_state.current_session_id,
                    question['id'],
                    question['q'],
                    user_answer,
                    correct_answer,
                    is_correct,
                    confidence,
                    question.get('difficulty', 'medium'),
                    question.get('concept', 'Unknown')
                )

                # Track question for intelligent selection (Tier 1)
                track_question_answer(
                    st.session_state.user_id,
                    question['id'],
                    is_correct,
                    question.get('difficulty', 'medium'),
                    chapter=topic,
                    quiz_mode='practice'
                )

    with col3:
        # Only allow Next if current question has been answered
        question_answered = question['id'] in st.session_state.answers
        if st.button("Next ➡️", disabled=(current_idx >= len(questions) - 1 or not question_answered), help="Answer the question first" if not question_answered else ""):
            st.session_state.current_question_idx += 1
            st.rerun()

    with col4:
        if st.button("🔄 Reset", help="Start topic over"):
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()

    with col5:
        if st.button("🏠 Exit to Home", help="Go back to home page"):
            st.session_state.mode = 'home'
            st.rerun()

def show_topic_results(questions):
    """Topic results and review with summary table"""
    st.title("📊 Topic Results")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score", f"{st.session_state.score}/{len(questions)}")
    with col2:
        if len(questions) > 0:
            percentage = (st.session_state.score / len(questions)) * 100
            st.metric("Percentage", f"{percentage:.0f}%")
        else:
            percentage = 0
            st.metric("Percentage", "-")
    with col3:
        if percentage >= 80:
            st.metric("Status", "🟢 Excellent")
        elif percentage >= 70:
            st.metric("Status", "🟡 Good")
        else:
            st.metric("Status", "🔴 Review Needed")

    st.markdown("---")
    st.write("### Summary Table")

    # Create summary dataframe
    summary_data = []
    for q_id, answer in st.session_state.answers.items():
        summary_data.append({
            'Question': answer['question'][:50] + "...",
            'Your Answer': answer['user_answer'][:30],
            'Correct Answer': answer['correct_answer'][:30],
            'Result': '✅ Correct' if answer['is_correct'] else '❌ Wrong',
            'Confidence': f"{answer['confidence']}/5",
            'Concept': answer['concept']
        })

    if summary_data:
        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.write("### Detailed Review")

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
                difficulty = question.get('difficulty', 'medium')
                st.caption(f"Concept: {question['concept']} | Difficulty: {difficulty.upper()}")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Retry Topic"):
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()
    with col2:
        if st.button("🏠 Back to Topics"):
            st.session_state.mode = 'topic_select'
            st.rerun()
    with col3:
        if st.button("🏠 Home"):
            st.session_state.mode = 'home'
            st.rerun()

def show_mock_exam():
    """Full mock exam - MCQ Only"""
    st.title(f"🎯 FULL MOCK EXAM - 45 Minutes | {st.session_state.user_name}")

    # Create a mock exam session if not exists
    if not st.session_state.current_session_id:
        st.session_state.current_session_id = create_quiz_session(
            st.session_state.user_id, 'mock_exam', None
        )

    # Timer
    elapsed = time.time() - st.session_state.exam_start_time
    remaining = max(0, 2700 - elapsed)

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write("**All 3 Topics - 25+ MCQ Questions**")
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

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("⬅️ Previous", disabled=(st.session_state.current_question_idx == 0)):
            st.session_state.current_question_idx -= 1
            st.rerun()
    with col2:
        if st.button("✓ Submit Answer", use_container_width=True):
            if user_answer:
                # Check if this question was already answered to avoid double-counting
                question_already_answered = question['id'] in st.session_state.answers

                is_correct, correct_answer = check_answer(question, user_answer)

                # Only increment score if this is the first time answering this question
                if is_correct and not question_already_answered:
                    st.session_state.score += 1
                    st.success("✅ Correct!")
                elif is_correct and question_already_answered:
                    st.success("✅ Correct! (Already submitted)")
                else:
                    st.info(f"Answer: {correct_answer}")

                st.session_state.answers[question['id']] = {
                    'question': question['q'],
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct,
                    'confidence': confidence,
                    'difficulty': question.get('difficulty', 'medium'),
                    'concept': question.get('concept', 'Unknown')
                }

                # Save answer to database
                save_answer(
                    st.session_state.current_session_id,
                    question['id'],
                    question['q'],
                    user_answer,
                    correct_answer,
                    is_correct,
                    confidence,
                    question.get('difficulty', 'medium'),
                    question.get('concept', 'Unknown')
                )

                # Track question for intelligent selection (Tier 1)
                track_question_answer(
                    st.session_state.user_id,
                    question['id'],
                    is_correct,
                    question.get('difficulty', 'medium'),
                    chapter='All',
                    quiz_mode='mock_exam'
                )

                time.sleep(1)
                st.session_state.current_question_idx += 1
                st.rerun()
    with col3:
        # Only allow Next if current question has been answered
        question_answered = question['id'] in st.session_state.answers
        if st.button("Next ➡️", disabled=not question_answered, help="Answer the question first" if not question_answered else ""):
            st.session_state.current_question_idx += 1
            st.rerun()
    with col4:
        if st.button("🔄 Reset", help="Start exam over"):
            st.session_state.exam_started = True
            st.session_state.exam_start_time = time.time()
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()
    with col5:
        if st.button("🏠 Exit to Home", help="Exit exam and go home"):
            st.session_state.exam_started = False
            st.session_state.mode = 'home'
            st.rerun()

def show_mock_results():
    """Mock exam results with summary table"""
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
        MalteseDogFeedback.show_happy_maltese(st.session_state.user_name)
    elif percentage >= 70:
        st.info("👍 Good score! Focus on weak areas for final polish.")
    else:
        st.warning("⚠️ Keep practicing! Review weak topics before exam.")
        MalteseDogFeedback.show_sad_maltese(st.session_state.user_name)

    st.markdown("---")
    st.write("### Summary Table")

    # Create comprehensive summary table
    summary_data = []
    for q_id, answer in st.session_state.answers.items():
        summary_data.append({
            'Question': answer['question'][:45] + "...",
            'Your Answer': answer['user_answer'][:25],
            'Correct': answer['correct_answer'][:25],
            'Result': '✅' if answer['is_correct'] else '❌',
            'Confidence': f"{answer['confidence']}/5",
            'Difficulty': answer['difficulty'].upper(),
            'Concept': answer['concept']
        })

    if summary_data:
        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True)

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

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Try Again"):
            st.session_state.exam_started = False
            st.session_state.mode = 'home'
            st.session_state.current_question_idx = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.rerun()
    with col2:
        if st.button("📖 Topic Practice"):
            st.session_state.mode = 'topic_select'
            st.rerun()
    with col3:
        if st.button("🏠 Back to Home"):
            st.session_state.mode = 'home'
            st.rerun()

def show_challenge_mode():
    """Challenge to Aanya - PSLE Brain Drainers with tricky similar options"""
    st.title("🧠 CHALLENGE TO AANYA - Brain Drain Mode")
    st.subheader("🎯 PSLE-Style Tricky Questions (All answers look similar but only ONE is correct!)")

    # Topic selection
    topics = {
        '💧 Water Cycles': 'Water_Cycles',
        '👶 Reproduction in Animals & Plants': 'Reproduction',
        '⚡ Electrical Systems': 'Electrical_Systems'
    }

    col1, col2 = st.columns(2)
    with col1:
        selected_topic_name = st.selectbox(
            "Choose a topic to challenge yourself:",
            list(topics.keys())
        )
        selected_topic = topics[selected_topic_name]

    with col2:
        st.info("💡 **Hint**: Read carefully! These questions test DEEPER understanding and have similar-looking wrong answers!")

    st.markdown("---")

    # Get challenge questions for selected topic
    questions = get_challenge_questions(selected_topic)
    current_idx = st.session_state.get('challenge_question_idx', 0)

    if current_idx >= len(questions):
        show_challenge_results(questions)
        return

    question = questions[current_idx]

    # Progress bar and counter
    progress = (current_idx + 1) / len(questions)
    st.progress(progress)
    st.write(f"**Challenge Progress**: {current_idx + 1}/{len(questions)} | **Score**: {st.session_state.get('challenge_score', 0)}/{current_idx}")

    st.markdown("---")

    # Display question with styling
    st.markdown(f"### Q{current_idx + 1}: {question['q']}")
    st.caption(f"📌 **Concept**: {question['concept']} | **Difficulty**: HARD ⚠️ | **Ref**: {question['ref']}")

    # BUG FIX: Restore previous answer if it exists (so students can't cheat by going back)
    previous_answer = None
    previous_confidence = 2
    challenge_key = f"challenge_{question['id']}"
    if challenge_key in st.session_state:
        previous_answer = st.session_state[challenge_key].get('user_answer')
        previous_confidence = st.session_state[challenge_key].get('confidence', 2)

    # Find index of previous answer in options (if exists)
    answer_index = 0
    if previous_answer and previous_answer in question['options']:
        answer_index = question['options'].index(previous_answer)

    # Options with visual styling
    answer = st.radio(
        "Select your answer (Read carefully - all look similar!):",
        question['options'],
        index=answer_index,  # ← RESTORED: Show previous selection
        key=f"ch_q_{question['id']}"
    )

    confidence = st.slider(
        "How confident are you? (1=Just guessing, 5=Very sure)",
        1, 5, previous_confidence,  # ← RESTORED: Show previous confidence
        key=f"ch_conf_{question['id']}"
    )

    st.markdown("---")

    # Navigation buttons for challenge mode
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("⬅️ Previous", disabled=(current_idx == 0), key="ch_prev"):
            st.session_state.challenge_question_idx -= 1
            st.rerun()

    with col2:
        if st.button("✓ Check Answer", use_container_width=True, key="ch_check"):
            if answer:
                # Check if question already answered (challenge_key already defined above)
                question_already_answered = challenge_key in st.session_state

                is_correct = answer == question['answer']

                # Only increment score if first time answering
                if is_correct and not question_already_answered:
                    st.session_state.challenge_score = st.session_state.get('challenge_score', 0) + 1
                    st.success("🎉 CORRECT! You found the right answer among the tricky options!")
                    MalteseDogFeedback.show_happy_maltese(st.session_state.user_name)
                elif is_correct and question_already_answered:
                    st.success("✅ Correct! (Already submitted)")
                else:
                    st.error("❌ Not quite right. Read the explanation carefully!")
                    st.warning(f"**Your answer**: {answer}")
                    st.info(f"**Correct answer**: {question['answer']}")
                    st.write(f"**Why?** {question['explanation']}")

                # Store answer
                st.session_state[challenge_key] = {
                    'question': question['q'],
                    'user_answer': answer,
                    'correct_answer': question['answer'],
                    'is_correct': is_correct,
                    'confidence': confidence,
                    'concept': question['concept']
                }

                # Track question for intelligent selection (Tier 1)
                track_question_answer(
                    st.session_state.user_id,
                    question['id'],
                    is_correct,
                    'hard',  # Challenge mode is always hard difficulty
                    chapter=selected_topic,
                    quiz_mode='challenge'
                )

    with col3:
        question_answered = f"challenge_{question['id']}" in st.session_state
        if st.button("Next ➡️", disabled=(current_idx >= len(questions) - 1 or not question_answered), key="ch_next"):
            st.session_state.challenge_question_idx = current_idx + 1
            st.rerun()

    with col4:
        if st.button("🔄 Reset Challenge", key="ch_reset"):
            st.session_state.challenge_question_idx = 0
            st.session_state.challenge_score = 0
            # Clear all challenge answers
            for key in list(st.session_state.keys()):
                if key.startswith('challenge_'):
                    del st.session_state[key]
            st.rerun()

    with col5:
        if st.button("🏠 Exit", key="ch_exit"):
            st.session_state.mode = 'home'
            # Clear challenge session
            st.session_state.challenge_question_idx = 0
            st.session_state.challenge_score = 0
            st.rerun()

def show_challenge_results(questions):
    """Challenge results and analysis"""
    st.title("📊 CHALLENGE RESULTS - How Did You Do?")

    challenge_score = st.session_state.get('challenge_score', 0)
    total_questions = len(questions)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🧠 Challenge Score", f"{challenge_score}/{total_questions}")
    with col2:
        if total_questions > 0:
            percentage = (challenge_score / total_questions) * 100
            st.metric("Accuracy", f"{percentage:.0f}%")
        else:
            st.metric("Accuracy", "-")
    with col3:
        if percentage >= 80:
            st.metric("Brain Power", "🟢 Excellent!")
        elif percentage >= 70:
            st.metric("Brain Power", "🟡 Good!")
        elif percentage >= 50:
            st.metric("Brain Power", "🟠 Getting there")
        else:
            st.metric("Brain Power", "🔴 Keep trying")
    with col4:
        st.metric("Difficulty", "⚠️ HARD MODE")

    st.markdown("---")

    if percentage >= 80:
        st.success("🎉 AMAZING! You have a sharp mind and read questions carefully!")
        MalteseDogFeedback.show_happy_maltese(st.session_state.user_name)
    elif percentage >= 70:
        st.info("👍 Great job! These were PSLE-level tricky questions!")
    else:
        st.warning("⚠️ These brain drainers are meant to be HARD! Don't worry - they're designed to confuse!")

    st.markdown("---")
    st.write("### Your Challenge Answers")

    # Show detailed review
    challenge_answers = []
    for key, value in st.session_state.items():
        if key.startswith('challenge_'):
            challenge_answers.append(value)

    if challenge_answers:
        # Summary table
        summary_data = []
        for answer in challenge_answers:
            summary_data.append({
                'Question': answer['question'][:50] + "...",
                'Your Answer': answer['user_answer'][:30],
                'Correct': answer['correct_answer'][:30],
                'Result': '✅ Correct' if answer['is_correct'] else '❌ Wrong',
                'Concept': answer['concept']
            })

        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True)

        st.markdown("---")
        st.write("### Detailed Explanations")

        for answer in challenge_answers:
            q_id = [q['id'] for q in questions if q['q'] == answer['question']]
            if q_id:
                question = next((q for q in questions if q['id'] == q_id[0]), None)
                if question:
                    with st.expander(f"{'✅' if answer['is_correct'] else '❌'} {answer['question'][:70]}..."):
                        st.write(f"**Your Answer**: {answer['user_answer']}")
                        st.write(f"**Correct Answer**: {answer['correct_answer']}")
                        st.write(f"**Why?** {question['explanation']}")
                        st.caption(f"Concept: {question['concept']}")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Try Again", key="ch_retry"):
            st.session_state.challenge_question_idx = 0
            st.session_state.challenge_score = 0
            for key in list(st.session_state.keys()):
                if key.startswith('challenge_'):
                    del st.session_state[key]
            st.rerun()
    with col2:
        if st.button("🧠 Try Different Topic", key="ch_other_topic"):
            st.session_state.challenge_question_idx = 0
            st.session_state.challenge_score = 0
            for key in list(st.session_state.keys()):
                if key.startswith('challenge_'):
                    del st.session_state[key]
            st.session_state.mode = 'challenge'
            st.rerun()
    with col3:
        if st.button("🏠 Back to Home", key="ch_home"):
            st.session_state.mode = 'home'
            st.session_state.challenge_question_idx = 0
            st.session_state.challenge_score = 0
            st.rerun()

def show_progress_tracker():
    """Comprehensive progress tracking page"""
    st.title("📈 Progress Tracker")
    st.subheader("Your Learning Journey - Detailed Statistics")

    if len(st.session_state.answers) == 0:
        st.info("📊 No data yet. Complete some practice sessions first!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📖 Start Practice"):
                st.session_state.mode = 'topic_select'
                st.rerun()
        with col2:
            if st.button("🏠 Back to Home"):
                st.session_state.mode = 'home'
                st.rerun()
        return

    # Overall Stats - Top Row
    st.markdown("## 📊 Overall Statistics")
    col1, col2, col3, col4 = st.columns(4)

    total_attempted = len(st.session_state.answers)
    total_correct = sum(1 for a in st.session_state.answers.values() if a['is_correct'])
    accuracy = (total_correct / total_attempted * 100) if total_attempted > 0 else 0
    avg_confidence = sum(a['confidence'] for a in st.session_state.answers.values()) / total_attempted if total_attempted > 0 else 0

    with col1:
        st.metric("Questions Answered", total_attempted)
    with col2:
        st.metric("✅ Correct", total_correct)
    with col3:
        st.metric("Overall Accuracy", f"{accuracy:.1f}%")
    with col4:
        st.metric("Avg Confidence", f"{avg_confidence:.1f}/5")

    st.markdown("---")

    # Performance by Difficulty
    st.markdown("## 🎯 Performance by Difficulty Level")
    diff_data = {'easy': [], 'medium': [], 'hard': []}
    for answer in st.session_state.answers.values():
        diff = answer.get('difficulty', 'medium')
        diff_data[diff].append(answer['is_correct'])

    df_data = []
    for diff, scores in diff_data.items():
        if scores:
            correct = sum(scores)
            total = len(scores)
            acc = (correct / total) * 100
            df_data.append({
                'Difficulty': diff.upper(),
                'Correct': f"{correct}/{total}",
                'Accuracy': f"{acc:.0f}%",
                'Status': "🟢 Strong" if acc >= 80 else "🟡 Good" if acc >= 70 else "🔴 Needs Work"
            })
        else:
            df_data.append({
                'Difficulty': diff.upper(),
                'Correct': '0/0',
                'Accuracy': '-',
                'Status': '⚪ No data'
            })

    if df_data:
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # Performance by Concept/Topic
    st.markdown("## 📚 Performance by Concept")
    concept_perf = {}
    for answer in st.session_state.answers.values():
        concept = answer.get('concept', 'Unknown')
        if concept not in concept_perf:
            concept_perf[concept] = {'correct': 0, 'total': 0}
        concept_perf[concept]['total'] += 1
        if answer['is_correct']:
            concept_perf[concept]['correct'] += 1

    concept_df_data = []
    for concept, data in sorted(concept_perf.items()):
        accuracy = (data['correct'] / data['total'] * 100) if data['total'] > 0 else 0
        concept_df_data.append({
            'Concept': concept,
            'Correct': f"{data['correct']}/{data['total']}",
            'Accuracy': f"{accuracy:.0f}%",
            'Status': "🟢" if accuracy >= 80 else "🟡" if accuracy >= 70 else "🔴"
        })

    if concept_df_data:
        concept_df = pd.DataFrame(concept_df_data)
        st.dataframe(concept_df, use_container_width=True)

    st.markdown("---")

    # Weak Areas Needing Review
    st.markdown("## ⚠️ Areas for Improvement")
    weak_concepts = []
    for concept, data in concept_perf.items():
        if data['total'] > 0:
            accuracy = (data['correct'] / data['total']) * 100
            if accuracy < 70:
                weak_concepts.append((concept, accuracy, data['total']))

    if weak_concepts:
        for concept, accuracy, count in sorted(weak_concepts, key=lambda x: x[1]):
            st.warning(f"📌 **{concept}**: {accuracy:.0f}% accuracy ({data['correct']}/{count} correct)")
    else:
        st.success("✅ All topics performing well! (70%+ accuracy)")

    st.markdown("---")

    # All Answers Summary Table
    st.markdown("## 📋 Complete Answer History")
    summary_data = []
    for q_id, answer in st.session_state.answers.items():
        summary_data.append({
            'Question': answer['question'][:50] + "...",
            'Your Answer': answer['user_answer'][:25],
            'Correct': answer['correct_answer'][:25],
            'Result': '✅' if answer['is_correct'] else '❌',
            'Confidence': f"{answer['confidence']}/5",
            'Difficulty': answer['difficulty'].upper(),
            'Concept': answer['concept']
        })

    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)

    st.markdown("---")

    # Action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📖 More Practice"):
            st.session_state.mode = 'topic_select'
            st.rerun()
    with col2:
        if st.button("⚙️ Settings"):
            st.session_state.mode = 'settings'
            st.rerun()
    with col3:
        if st.button("🏠 Back to Home"):
            st.session_state.mode = 'home'
            st.rerun()

def show_settings():
    """Settings page with progress management"""
    st.title("⚙️ Settings & Progress Management")

    # Tabs for different settings
    tab1, tab2 = st.tabs(["Progress Management", "App Settings"])

    with tab1:
        st.markdown("## 🗂️ Progress Management")

        # Current progress summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions Answered", len(st.session_state.answers))
        with col2:
            if len(st.session_state.answers) > 0:
                correct = sum(1 for a in st.session_state.answers.values() if a['is_correct'])
                st.metric("Correct Answers", correct)
            else:
                st.metric("Correct Answers", 0)
        with col3:
            if len(st.session_state.answers) > 0:
                accuracy = (correct / len(st.session_state.answers)) * 100
                st.metric("Accuracy", f"{accuracy:.1f}%")
            else:
                st.metric("Accuracy", "-")

        st.markdown("---")

        st.markdown("### 🔄 Reset Progress")
        st.warning("⚠️ **WARNING**: This action will permanently delete all your progress data including:")
        st.write("- All answers you've submitted")
        st.write("- Your accuracy scores")
        st.write("- Your practice history")
        st.write("- Your confidence ratings")

        st.markdown("---")

        # Reset confirmation
        if st.checkbox("I understand that resetting will delete all progress", key="reset_confirm"):
            st.info("✅ Confirmation enabled. Click the button below to reset.")

            if st.button("🔴 RESET ALL PROGRESS", use_container_width=True):
                # Reset all progress
                st.session_state.answers = {}
                st.session_state.score = 0
                st.session_state.current_question_idx = 0
                st.session_state.total_questions_attempted = 0
                st.success("✅ All progress has been reset successfully!")
                st.info("You can now start fresh. Redirecting to home in 2 seconds...")
                time.sleep(2)
                st.session_state.mode = 'home'
                st.rerun()

    with tab2:
        st.markdown("## 🎨 Display Settings")

        st.info("📱 These settings help customize your learning experience:")

        # Theme preference (can be added later)
        st.write("- **Dark Mode** support (coming soon)")
        st.write("- **Animation Speed** adjustment (coming soon)")
        st.write("- **Sound Effects** toggle (coming soon)")
        st.write("- **Notification Preferences** (coming soon)")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 View Progress"):
            st.session_state.mode = 'progress'
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
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📖 Start Practice"):
                st.session_state.mode = 'topic_select'
                st.rerun()
        with col2:
            if st.button("🏠 Back to Home"):
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

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 More Practice"):
            st.session_state.mode = 'topic_select'
            st.rerun()
    with col2:
        if st.button("🏠 Back to Home"):
            st.session_state.mode = 'home'
            st.rerun()

# ==================== MAIN ====================

def main():
    init_session()

    # Authentication check
    if st.session_state.mode != 'login' and st.session_state.user_id is None:
        st.session_state.mode = 'login'

    if st.session_state.mode == 'login':
        show_login()
    elif st.session_state.mode == 'admin':
        show_admin_dashboard()
    elif st.session_state.mode == 'home':
        show_home()
    elif st.session_state.mode == 'topic_select':
        show_topic_select()
    elif st.session_state.mode == 'chapter_content':
        show_chapter_content(st.session_state.chapter_name)
    elif st.session_state.mode == 'practice':
        show_practice_mode()
    elif st.session_state.mode == 'mock_exam':
        show_mock_exam()
    elif st.session_state.mode == 'challenge':
        show_challenge_mode()
    elif st.session_state.mode == 'analytics':
        show_analytics()
    elif st.session_state.mode == 'progress':
        show_progress_tracker()
    elif st.session_state.mode == 'settings':
        show_settings()

if __name__ == "__main__":
    main()
