"""
Extended PSLE Brain Drainer Questions for Exam Prep
Additional challenging questions to test mastery
"""

EXTENDED_QUESTIONS = {
    'Water_Cycles_Hard': [
        {
            'type': 'STRUCT',
            'q': 'In a sealed jar, water evaporates but never rains. Why? What is this called?',
            'answer': 'This is dynamic equilibrium. Water molecules evaporate AND condense at equal rates, creating a closed water cycle inside the jar.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'Why can\'t you heat liquid water above 100°C by boiling at sea level? Explain using latent heat.',
            'answer': 'At 100°C, all added heat goes to evaporation (phase change), not temperature rise. This energy is called latent heat. Temperature remains 100°C until all water evaporates.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'If global warming increases ocean temperatures, what TWO effects occur in the water cycle?',
            'answer': '1) More evaporation = more water vapor in air. 2) More condensation = heavier rainfall and more extreme weather.',
            'difficulty': 'hard'
        },
        {
            'type': 'MCQ',
            'q': 'At the same temperature, which has the FASTEST-moving particles?',
            'options': ['Ice (solid)', 'Water (liquid)', 'Water vapor (gas)', 'All same speed'],
            'answer': 'Water vapor (gas)',
            'difficulty': 'hard'
        },
        {
            'type': 'MCQ',
            'q': 'Desert plants have waxy leaves. This is an adaptation to:',
            'options': ['Attract insects', 'Reduce transpiration (water loss)', 'Absorb more sunlight', 'Store food'],
            'answer': 'Reduce transpiration (water loss)',
            'difficulty': 'hard'
        },
    ],

    'Reproduction_Hard': [
        {
            'type': 'STRUCT',
            'q': 'Explain why pollination (pollen on stigma) does NOT guarantee seed formation. What must happen next?',
            'answer': 'Pollination only transfers pollen. Fertilization (fusion of pollen nucleus with egg cell) must follow for seed formation. Without fertilization, no seed develops.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'A flower has both male and female parts. Can it self-pollinate? What is the advantage?',
            'answer': 'Yes, it can self-pollinate (pollen from own anther reaches own stigma). Advantage: doesn\'t rely on insects/wind, guarantees reproduction.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'Seeds scatter far from parent plants. Give three DIFFERENT dispersal methods and one example for each.',
            'answer': '1) Wind: Winged seeds (maple) or light seeds (dandelion). 2) Water: Floating seeds (coconut). 3) Animals: Hooked seeds (burdock) or eaten fruits (berries).',
            'difficulty': 'hard'
        },
        {
            'type': 'MCQ',
            'q': 'A seed has water, oxygen, warmth, and soil but still won\'t germinate. What\'s likely?',
            'options': ['It\'s a dead seed', 'It\'s dormant (needs trigger like cold or light)', 'Soil is wrong pH', 'Too many nutrients'],
            'answer': 'It\'s dormant (needs trigger like cold or light)',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'Why do identical twins share 100% DNA but fraternal twins share only ~50%?',
            'answer': 'Identical: One egg + one sperm splits into 2 individuals = exact same DNA. Fraternal: Two eggs + two sperm fertilize separately = genetically different (like regular siblings).',
            'difficulty': 'hard'
        },
    ],

    'Electrical_Hard': [
        {
            'type': 'STRUCT',
            'q': 'In a circuit, current flows from positive to negative. But electrons actually flow opposite direction. Why is this not a problem?',
            'answer': 'This is called "conventional current" vs "electron flow." Conventional current direction (+ to -) is just a labeling convention. Both directions give correct circuit analysis.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'A series circuit has 12V battery, 2Ω resistor, 4Ω resistor. Calculate: 1) Total resistance, 2) Current, 3) Voltage across each resistor.',
            'answer': '1) Total R = 2 + 4 = 6Ω (series = sum). 2) I = V/R = 12/6 = 2A. 3) V₁ = 2A×2Ω = 4V, V₂ = 2A×4Ω = 8V.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'Why does a circuit breaker trip? Explain the danger it prevents.',
            'answer': 'Circuit breaker trips when current exceeds safe level. High current causes P = I²R power loss, creating dangerous heat in wires that can start fires.',
            'difficulty': 'hard'
        },
        {
            'type': 'MCQ',
            'q': 'In an overloaded home circuit, which happens FIRST?',
            'options': ['Breaker trips', 'Wires heat up', 'Lights flicker', 'Bulbs burn out'],
            'answer': 'Wires heat up',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'If you connect two identical 6V batteries in series (positive of one to negative of other), what\'s the total voltage?',
            'answer': 'Total voltage = 6V + 6V = 12V. In series, voltages add. Both batteries push in the same direction.',
            'difficulty': 'hard'
        },
        {
            'type': 'STRUCT',
            'q': 'If you connect two 6V batteries the WRONG way (positive to positive), what happens to voltage?',
            'answer': 'Voltage is CANCELED (0V or very low). The batteries oppose each other. The one with higher internal resistance may be damaged.',
            'difficulty': 'hard'
        },
    ]
}

# Additional PSLE Trick Questions
TRICK_QUESTIONS = [
    {
        'type': 'MCQ',
        'topic': 'Water',
        'q': 'A teacher heats water to 100°C. The thermometer reads 100°C and stays there for 5 minutes despite continuous heating. Is the thermometer broken?',
        'options': ['Yes, broken', 'No, latent heat is being used for evaporation', 'Yes, needs recalibration', 'No, water cooled down'],
        'answer': 'No, latent heat is being used for evaporation',
        'explanation': 'At 100°C, all heat goes to phase change (evaporation). Temperature stays constant until all water evaporates.'
    },
    {
        'type': 'MCQ',
        'topic': 'Reproduction',
        'q': 'A plant is pollinated by bees. 2 weeks later, NO seeds formed. Did the pollination fail?',
        'options': ['Yes', 'No, fertilization failed even though pollination succeeded', 'No, seeds take 2 weeks', 'Yes, bees were bad'],
        'answer': 'No, fertilization failed even though pollination succeeded',
        'explanation': 'Pollination transfers pollen (✓). But fertilization (nucleus fusion) may have failed, so no seed develops.'
    },
    {
        'type': 'MCQ',
        'topic': 'Electrical',
        'q': 'A circuit has 2 bulbs in series + 2V battery. Adding a 3rd identical bulb makes... (pick one)',
        'options': ['Only 3rd bulb dim', 'All bulbs equally bright (more power)', 'All bulbs dimmer', 'No change in brightness'],
        'answer': 'All bulbs dimmer',
        'explanation': 'More bulbs = more resistance. More R with same V = less I (current). All bulbs get less current = all dimmer.'
    },
    {
        'type': 'MCQ',
        'topic': 'Water',
        'q': 'If you heat a pot of water and then turn off the stove, the water continues to boil for a few seconds. Why?',
        'options': ['Stove still hot', 'Latent heat in steam keeps water bubbling', 'Water temperature rising', 'Residual heat in pot'],
        'answer': 'Residual heat in pot',
        'explanation': 'The pot retains heat from the stove. This heat keeps some water evaporating for a few more seconds.'
    },
    {
        'type': 'STRUCT',
        'topic': 'Reproduction',
        'q': 'Two plants look identical but produce offspring with different traits. Explain how this is possible.',
        'answer': 'Even identical-looking plants have different genes inside. During fertilization, different gene combinations create varied offspring.',
        'explanation': 'Phenotype (appearance) ≠ Genotype (genes). Same parents, different inheritance combinations.'
    },
]
