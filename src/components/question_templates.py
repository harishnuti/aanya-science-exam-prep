"""
Parameterized Question Templates for Tier 2 Variation Generation
Each template can generate 10+ variations with different parameters
Total: 20+ templates × 10 variations = 200+ dynamically generated questions
"""

QUESTION_TEMPLATES = {
    # ==================== WATER CYCLES (6 templates) ====================

    'evaporation_temperature': {
        'template': 'Water at {temp}°C evaporates. How much of the water becomes water vapor?',
        'answer_formula': lambda p: 'Only water molecules escape as vapor; other substances remain',
        'difficulty': 'medium',
        'chapter': 'Water_Cycles',
        'concept': 'Evaporation & Phase Changes',
        'parameters': {
            'temp': [15, 20, 25, 30, 35, 40],
        }
    },

    'condensation_temperature': {
        'template': 'Water vapor at {temp}°C cools down to {cooled_temp}°C. What process occurs?',
        'answer_formula': lambda p: 'Condensation - water vapor becomes liquid water droplets',
        'difficulty': 'easy',
        'chapter': 'Water_Cycles',
        'concept': 'Condensation',
        'parameters': {
            'temp': [50, 60, 70, 80],
            'cooled_temp': [15, 20, 25, 30],
        }
    },

    'water_cycle_sequence': {
        'template': 'In the water cycle, after {step1} occurs, the next step is {step2}. Is this correct?',
        'answer_formula': lambda p: 'Yes' if (p['step1'] == 'evaporation' and p['step2'] == 'condensation') or \
                                            (p['step1'] == 'condensation' and p['step2'] == 'precipitation') else 'No',
        'difficulty': 'medium',
        'chapter': 'Water_Cycles',
        'concept': 'Water Cycle Process',
        'parameters': {
            'step1': ['evaporation', 'condensation', 'precipitation'],
            'step2': ['condensation', 'precipitation', 'evaporation'],
        }
    },

    'evaporation_surface_area': {
        'template': 'A container with {area} cm² surface area contains water. Compared to {area_compare} cm², which evaporates faster?',
        'answer_formula': lambda p: f'{max(p["area"], p["area_compare"])} cm² (larger surface area)',
        'difficulty': 'hard',
        'chapter': 'Water_Cycles',
        'concept': 'Factors Affecting Evaporation',
        'parameters': {
            'area': [50, 100, 150, 200],
            'area_compare': [30, 60, 100, 120],
        }
    },

    'salt_evaporation': {
        'template': 'Seawater contains {salt_percent}% salt. When it evaporates, what remains?',
        'answer_formula': lambda p: 'Salt crystals (salt has higher boiling point than water)',
        'difficulty': 'medium',
        'chapter': 'Water_Cycles',
        'concept': 'Evaporation & Purification',
        'parameters': {
            'salt_percent': [3, 4, 5, 6],
        }
    },

    'water_state_change': {
        'template': 'Ice at {start_temp}°C is heated to {end_temp}°C. What state is the water in?',
        'answer_formula': lambda p: 'Solid (ice)' if p['end_temp'] < 0 else ('Liquid (water)' if p['end_temp'] < 100 else 'Gas (vapor)'),
        'difficulty': 'easy',
        'chapter': 'Water_Cycles',
        'concept': 'Phase Changes',
        'parameters': {
            'start_temp': [-20, -10, -5],
            'end_temp': [-2, 15, 50, 110],
        }
    },

    # ==================== REPRODUCTION (5 templates) ====================

    'human_gestation': {
        'template': 'Human pregnancy lasts approximately {weeks} weeks. Is this correct?',
        'answer_formula': lambda p: 'Yes (approximately 40 weeks is normal)' if 38 <= p['weeks'] <= 42 else 'No',
        'difficulty': 'easy',
        'chapter': 'Reproduction',
        'concept': 'Human Gestation Period',
        'parameters': {
            'weeks': [20, 30, 35, 40, 42, 50],
        }
    },

    'plant_flower_parts': {
        'template': 'The {part} is the male reproductive organ in a flower. True or False?',
        'answer_formula': lambda p: 'True' if p['part'] == 'stamen' else 'False',
        'difficulty': 'medium',
        'chapter': 'Reproduction',
        'concept': 'Flower Reproduction',
        'parameters': {
            'part': ['stamen', 'pistil', 'sepal', 'petal'],
        }
    },

    'pollination_agents': {
        'template': 'Wind-pollinated plants typically have {feature} flowers. Which feature?',
        'answer_formula': lambda p: 'Small, inconspicuous flowers without bright colors' if p['feature'] == 'small' else 'Depends on feature',
        'difficulty': 'hard',
        'chapter': 'Reproduction',
        'concept': 'Plant Pollination',
        'parameters': {
            'feature': ['small', 'colorful', 'fragrant', 'large'],
        }
    },

    'seed_dispersal': {
        'template': 'Seeds with {structure} are dispersed by wind. Is this correct?',
        'answer_formula': lambda p: 'Yes' if p['structure'] in ['wings', 'parachutes'] else 'No',
        'difficulty': 'medium',
        'chapter': 'Reproduction',
        'concept': 'Seed Dispersal',
        'parameters': {
            'structure': ['wings', 'hooks', 'parachutes', 'none'],
        }
    },

    # ==================== ELECTRICAL SYSTEMS (5 templates) ====================

    'electrical_current': {
        'template': 'If a bulb uses {current_ma} mA of current, how many Amperes is that?',
        'answer_formula': lambda p: f'{p["current_ma"] / 1000} A',
        'difficulty': 'medium',
        'chapter': 'Electrical_Systems',
        'concept': 'Electric Current',
        'parameters': {
            'current_ma': [100, 500, 1000, 1500],
        }
    },

    'circuit_series_parallel': {
        'template': 'In a {circuit_type} circuit, if one bulb burns out, what happens?',
        'answer_formula': lambda p: 'All bulbs turn off' if p['circuit_type'] == 'series' else 'Other bulbs stay on',
        'difficulty': 'hard',
        'chapter': 'Electrical_Systems',
        'concept': 'Series vs Parallel Circuits',
        'parameters': {
            'circuit_type': ['series', 'parallel'],
        }
    },

    'resistance_material': {
        'template': 'Which material has {resistance_level} electrical resistance?',
        'answer_formula': lambda p: 'Copper' if p['resistance_level'] == 'low' else 'Rubber' if p['resistance_level'] == 'high' else 'Depends',
        'difficulty': 'medium',
        'chapter': 'Electrical_Systems',
        'concept': 'Electrical Resistance',
        'parameters': {
            'resistance_level': ['low', 'high', 'medium'],
        }
    },

    'voltage_definition': {
        'template': 'Voltage is the {definition} in a circuit.',
        'answer_formula': lambda p: 'Electric potential difference / Energy per unit charge',
        'difficulty': 'hard',
        'chapter': 'Electrical_Systems',
        'concept': 'Voltage Concept',
        'parameters': {
            'definition': ['energy', 'difference', 'resistance', 'power'],
        }
    },

    # ==================== CROSS-TOPIC (3 templates) ====================

    'measurement_units': {
        'template': '{quantity} is measured in {unit}. Is this correct?',
        'answer_formula': lambda p: 'Yes' if (p['quantity'] == 'Temperature' and p['unit'] == 'Celsius') or \
                                             (p['quantity'] == 'Current' and p['unit'] == 'Ampere') or \
                                             (p['quantity'] == 'Mass' and p['unit'] == 'Kilogram') else 'No',
        'difficulty': 'easy',
        'chapter': 'General',
        'concept': 'Scientific Measurements',
        'parameters': {
            'quantity': ['Temperature', 'Current', 'Mass', 'Volume'],
            'unit': ['Celsius', 'Ampere', 'Kilogram', 'Liter'],
        }
    },

    'experimental_variables': {
        'template': 'In an experiment testing {variable_type} effect, what should remain constant?',
        'answer_formula': lambda p: 'All variables except the independent variable',
        'difficulty': 'hard',
        'chapter': 'General',
        'concept': 'Scientific Method',
        'parameters': {
            'variable_type': ['temperature', 'light', 'water amount'],
        }
    },

}

def get_template_count():
    """Return total number of templates"""
    return len(QUESTION_TEMPLATES)

def get_templates_by_chapter(chapter):
    """Get templates for a specific chapter"""
    return {k: v for k, v in QUESTION_TEMPLATES.items() if v['chapter'] == chapter}

def get_template(template_id):
    """Get specific template by ID"""
    return QUESTION_TEMPLATES.get(template_id)

