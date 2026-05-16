"""PSLE Brain Drainer Questions for all 6 chapters"""

BRAIN_DRAINERS = {
    'Ch1_Reproduction': [
        # Phase 1 Ported Content - 50 PSLE Brain Drainer Questions
        {'q': 'How are Identical Twins formed?', 'options': ['One sperm fuses with one egg, and it splits.', 'Two sperms fuse with two eggs.', 'One sperm fuses with two eggs.', 'Two eggs split before fertilisation.'], 'answer': 'One sperm fuses with one egg, and it splits.', 'trap': 'IDENTICAL = 1 Egg + 1 Sperm that splits in half!', 'difficulty': 'easy'},
        {'q': 'How are Fraternal Twins formed?', 'options': ['One sperm fuses with one egg.', 'One sperm fuses with two eggs.', 'Two separate sperms fuse with two separate eggs.', 'One egg splits into two.'], 'answer': 'Two separate sperms fuse with two separate eggs.', 'trap': 'Fraternal = 2 eggs and 2 sperms. They are just like regular siblings!', 'difficulty': 'easy'},
        {'q': 'Function of fibrous husk in Pong Pong?', 'options': ['Nutrients.', 'Attract animals.', 'Trap air to float.', 'Parachute.'], 'answer': 'Trap air to float.', 'trap': 'Fibrous husks trap air like a life jacket for water dispersal.', 'difficulty': 'medium'},
        {'q': 'First part of plant to appear in germination?', 'options': ['Stem', 'Leaves', 'Roots', 'Seed coat'], 'answer': 'Roots', 'trap': 'Roots anchor the plant and get water first!', 'difficulty': 'easy'},
        {'q': 'Where does a young plant get its nutrients before true leaves appear?', 'options': ['From soil', 'From seed leaves', 'From Sun', 'From rain'], 'answer': 'From seed leaves', 'trap': 'Seed leaves store food. True leaves make food later via photosynthesis.', 'difficulty': 'medium'},
        {'q': 'Duration of baby in womb?', 'options': ['9 weeks', '40 weeks (9 months)', '20 weeks', '12 months'], 'answer': '40 weeks (9 months)', 'trap': 'It is 40 weeks or roughly 9 months. Don\'t mix up weeks and months!', 'difficulty': 'easy'},
        {'q': 'Definition of Pollination?', 'options': ['Fusion of cells.', 'Transfer of pollen from anther to stigma.', 'Transfer of pollen from stigma to anther.', 'Turning ovule into seed.'], 'answer': 'Transfer of pollen from anther to stigma.', 'trap': 'Pollination is only the TRAVEL. Fertilisation is the FUSION.', 'difficulty': 'medium'},
        {'q': 'Which part becomes the FRUIT?', 'options': ['Ovule', 'Ovary', 'Stigma', 'Anther'], 'answer': 'Ovary', 'trap': 'The Ovary swells into the fruit. The Ovule becomes the seed.', 'difficulty': 'easy'},
        {'q': 'Wind-pollinated flowers usually have:', 'options': ['Bright petals', 'Feathery stigmas', 'Nectar', 'Sweet scent'], 'answer': 'Feathery stigmas', 'trap': 'Wind flowers need \'nets\' (feathery stigmas) to catch flying pollen.', 'difficulty': 'hard'},
        {'q': 'Why scatter seeds far away?', 'options': ['To feed animals.', 'To avoid competition for light, water, and space.', 'To keep them dry.', 'To help pollination.'], 'answer': 'To avoid competition for light, water, and space.', 'trap': 'Competition for resources makes young plants weak. Distance is key!', 'difficulty': 'medium'},
        {'q': 'Where is the egg produced in a human?', 'options': ['Womb', 'Ovary', 'Testis', 'Stomach'], 'answer': 'Ovary', 'trap': 'Eggs are made in the ovary. The baby grows in the womb.', 'difficulty': 'easy'},
        {'q': 'Human male reproductive cell?', 'options': ['Pollen', 'Testis', 'Sperm', 'Spore'], 'answer': 'Sperm', 'trap': 'Sperm is the cell. Testis is the organ that makes it.', 'difficulty': 'easy'},
        {'q': 'Human fertilisation involves:', 'options': ['Millions of sperms and one egg.', 'One sperm and one egg.', 'One sperm and millions of eggs.', 'Two eggs and one sperm.'], 'answer': 'One sperm and one egg.', 'trap': 'Even if millions swim, only ONE fuses with the egg!', 'difficulty': 'medium'},
        {'q': 'Seeds with hooks/hairs are dispersed by:', 'options': ['Wind', 'Water', 'Animals', 'Explosive action'], 'answer': 'Animals', 'trap': 'Hooks latch onto fur or human socks!', 'difficulty': 'medium'},
        {'q': 'Fleshy, sweet fruits are dispersed by:', 'options': ['Wind', 'Animals eating them', 'Splitting', 'Gravity'], 'answer': 'Animals eating them', 'trap': 'Animals eat the fruit and poop the seeds out elsewhere.', 'difficulty': 'medium'},
        {'q': 'Seed needs for germination (WOW):', 'options': ['Water, Oxygen, Sunlight', 'Water, Oxygen, Warmth', 'Soil, Sunlight, Water', 'Soil, Oxygen, Warmth'], 'answer': 'Water, Oxygen, Warmth', 'trap': 'Sunlight is NOT needed until the plant has leaves!', 'difficulty': 'easy'},
        {'q': 'Function of the Anther?', 'options': ['Receive pollen.', 'Produce pollen grains.', 'Protect the bud.', 'Make nectar.'], 'answer': 'Produce pollen grains.', 'trap': 'Anther makes pollen. Stigma catches it.', 'difficulty': 'easy'},
        {'q': 'Sticky surface to catch pollen?', 'options': ['Style', 'Filament', 'Stigma', 'Ovary'], 'answer': 'Stigma', 'trap': 'Sticky Stigma!', 'difficulty': 'easy'},
        {'q': 'Pollen tube\'s purpose?', 'options': ['To grow leaves.', 'To reach the ovule for fertilisation.', 'To attract bees.', 'To store water.'], 'answer': 'To reach the ovule for fertilisation.', 'trap': 'It is a path for the male cell to travel to the female cell.', 'difficulty': 'medium'},
        {'q': 'Reproduction ensures species:', 'options': ['Die out.', 'Grow taller.', 'Continue their kind.', 'Make food.'], 'answer': 'Continue their kind.', 'trap': 'Reproduction prevents extinction.', 'difficulty': 'easy'},
        {'q': 'Genetic traits are stored in the:', 'options': ['Cell wall', 'Nucleus', 'Cytoplasm', 'Tail'], 'answer': 'Nucleus', 'trap': 'The nucleus is the command center with the blueprints (DNA).', 'difficulty': 'medium'},
        {'q': 'Stigma removed = immediately stops:', 'options': ['Photosynthesis', 'Pollination', 'Dispersal', 'Water intake'], 'answer': 'Pollination', 'trap': 'No stigma = no place for pollen to land.', 'difficulty': 'hard'},
        {'q': 'Heredity means:', 'options': ['Learning tricks.', 'Passing traits from parents to young.', 'Growing bigger.', 'Eating healthy.'], 'answer': 'Passing traits from parents to young.', 'trap': 'Biological traits (hair color, eye color) are inherited.', 'difficulty': 'easy'},
        {'q': 'Winged seeds are dispersed by:', 'options': ['Water', 'Animals', 'Wind', 'Splitting'], 'answer': 'Wind', 'trap': 'Wings help them glide in the air.', 'difficulty': 'easy'},
        {'q': 'Human Testis function?', 'options': ['Make eggs.', 'Make sperms.', 'Protect baby.', 'Digest food.'], 'answer': 'Make sperms.', 'trap': 'Testis = Male factory. Ovary = Female factory.', 'difficulty': 'easy'},
        {'q': 'Style connects the:', 'options': ['Anther to filament', 'Stigma to ovary', 'Ovary to roots', 'Petal to stem'], 'answer': 'Stigma to ovary', 'trap': 'The style is the long tube connecting the top and bottom female parts.', 'difficulty': 'medium'},
        {'q': 'Bright, large flowers are for:', 'options': ['Wind', 'Water', 'Insects', 'None'], 'answer': 'Insects', 'trap': 'Color attracts pollinators like bees and butterflies.', 'difficulty': 'easy'},
        {'q': 'Splitting action is used by:', 'options': ['Coconuts', 'Mangoes', 'Balsam/Saga', 'Dandelions'], 'answer': 'Balsam/Saga', 'trap': 'Their pods dry up and snap open!', 'difficulty': 'medium'},
        {'q': 'After fertilisation, petals usually:', 'options': ['Turn green', 'Grow bigger', 'Wither and fall off', 'Become seeds'], 'answer': 'Wither and fall off', 'trap': 'Their job is done once the flower is fertilised.', 'difficulty': 'medium'},
        {'q': 'Water dispersed fruits are often:', 'options': ['Heavy', 'Waterproof and buoyant', 'Sweet', 'Small and hairy'], 'answer': 'Waterproof and buoyant', 'trap': 'They need to float and not rot!', 'difficulty': 'hard'},
        {'q': 'Stamen includes:', 'options': ['Stigma and style', 'Anther and filament', 'Ovary and ovule', 'Petal and sepal'], 'answer': 'Anther and filament', 'trap': 'Sta-MEN (male parts).', 'difficulty': 'medium'},
        {'q': 'Pistil/Carpel includes:', 'options': ['Anther and filament', 'Stigma, style, ovary', 'Petal and stem', 'Roots'], 'answer': 'Stigma, style, ovary', 'trap': 'The entire female structure.', 'difficulty': 'hard'},
        {'q': 'Traits passed down include:', 'options': ['Scars', 'Eye color', 'Language', 'Knowledge'], 'answer': 'Eye color', 'trap': 'Acquired skills are not passed down genetically.', 'difficulty': 'medium'},
        {'q': 'Millions of sperm are needed because:', 'options': ['They are small.', 'Many die on the way to the egg.', 'To make more babies.', 'To fight insects.'], 'answer': 'Many die on the way to the egg.', 'trap': 'It is a difficult journey; only the strongest makes it.', 'difficulty': 'hard'},
        {'q': 'Seed leaves (Cotyledons) function?', 'options': ['Protect from wind.', 'Store food for germination.', 'Make oxygen.', 'Attract bees.'], 'answer': 'Store food for germination.', 'trap': 'The \'lunchbox\' for the baby plant.', 'difficulty': 'medium'},
        {'q': 'Dispersal helps prevent:', 'options': ['Pollination', 'Overcrowding', 'Photosynthesis', 'Rain'], 'answer': 'Overcrowding', 'trap': 'Too many plants in one spot = not enough food for all.', 'difficulty': 'easy'},
        {'q': 'Zanzibar Yam is removed because it:', 'options': ['Is a native plant.', 'Competes for space and sunlight.', 'Has no seeds.', 'Smells bad.'], 'answer': 'Competes for space and sunlight.', 'trap': 'It is invasive and smothers other plants.', 'difficulty': 'medium'},
        {'q': 'Human fertilisation happens in the:', 'options': ['Ovary', 'Womb', 'Fallopian tube', 'Stomach'], 'answer': 'Fallopian tube', 'trap': 'This is the tube where the sperm meets the egg before it moves to the womb.', 'difficulty': 'hard'},
        {'q': 'Waterproof covering is for:', 'options': ['Wind', 'Animals', 'Water dispersal', 'Fire'], 'answer': 'Water dispersal', 'trap': 'Prevents water from entering the seed.', 'difficulty': 'medium'},
        {'q': 'Common goal of reproduction?', 'options': ['Oxygen', 'Species survival', 'Food production', 'Growth'], 'answer': 'Species survival', 'trap': 'To ensure life continues.', 'difficulty': 'easy'},
        {'q': 'Identical twins share the same:', 'options': ['Parents but different DNA.', 'DNA because they came from the same cell.', 'Birthdays only.', 'Sperm only.'], 'answer': 'DNA because they came from the same cell.', 'trap': 'One egg + One sperm = Exact same blueprints!', 'difficulty': 'hard'},
        {'q': 'Fraternal twins are formed by:', 'options': ['One egg splitting.', 'Two separate fertilised eggs.', 'One sperm and two eggs.', 'A mistake.'], 'answer': 'Two separate fertilised eggs.', 'trap': 'Two eggs were released and both were fertilised independently.', 'difficulty': 'hard'},
        {'q': 'Pollen is the:', 'options': ['Female cell.', 'Male cell (in plants).', 'Food for bees.', 'Part of the root.'], 'answer': 'Male cell (in plants).', 'trap': 'Pollen contains the male reproductive cells.', 'difficulty': 'easy'},
        {'q': 'Ovule contains the:', 'options': ['Pollen.', 'Female cell (egg).', 'Fruit juice.', 'Sunlight.'], 'answer': 'Female cell (egg).', 'trap': 'The female cell is inside the ovule.', 'difficulty': 'easy'},
        {'q': 'Once pollen lands on stigma, it:', 'options': ['Dies.', 'Explodes.', 'Grows a tube.', 'Falls off.'], 'answer': 'Grows a tube.', 'trap': 'The start of the fertilisation process.', 'difficulty': 'medium'},
        {'q': 'Baby in womb gets food from:', 'options': ['Mouth.', 'Mother via the umbilical cord.', 'Ovary.', 'Stomach.'], 'answer': 'Mother via the umbilical cord.', 'trap': 'The lifeline between mother and baby.', 'difficulty': 'easy'},
        {'q': 'Germination: WOW acronym stands for:', 'options': ['Wind, Oxygen, Water', 'Water, Oxygen, Warmth', 'Water, Oil, Wind', 'Warmth, Oil, Water'], 'answer': 'Water, Oxygen, Warmth', 'trap': 'The three requirements for a seed to wake up.', 'difficulty': 'easy'},
        {'q': 'Does a seed need soil to germinate?', 'options': ['Yes, always.', 'No, it just needs WOW.', 'Only if it is a tree.', 'Only in winter.'], 'answer': 'No, it just needs WOW.', 'trap': 'You can germinate seeds on wet cotton wool!', 'difficulty': 'medium'},
        {'q': 'Do humans have a "seed stage"?', 'options': ['Yes.', 'No, we have a fertilised egg stage.', 'Only in the womb.', 'Yes, called pollen.'], 'answer': 'No, we have a fertilised egg stage.', 'trap': 'We don\'t use seeds, we use internal fertilisation and development.', 'difficulty': 'hard'},
        {'q': 'Which part of the plant makes food after germination?', 'options': ['Roots', 'True leaves', 'Seed leaves', 'Stem'], 'answer': 'True leaves', 'trap': 'True leaves perform photosynthesis once they appear.', 'difficulty': 'medium'},
    ],

    'Ch2_Water': [
        {'q': 'A glass of hot water left on a table evaporates completely in 3 days. Where did the water go?', 'options': ['Into the ground', 'Into the air as water vapor', 'Absorbed by the glass', 'It did not actually evaporate'], 'answer': 'Into the air as water vapor', 'trap': 'We cannot see water vapor, so some think it disappears', 'difficulty': 'easy'},
        {'q': 'During the water cycle, which process requires energy from the sun?', 'options': ['Condensation', 'Evaporation and Transpiration', 'Precipitation', 'Freezing'], 'answer': 'Evaporation and Transpiration', 'trap': 'Condensation releases energy, not requires it', 'difficulty': 'hard'},
        {'q': 'Ice melts into water at 0°C. Is this a physical or chemical change?', 'options': ['Chemical - water is now different', 'Physical - water molecules remain the same', 'Both physical and chemical', 'Neither - it is a state change only'], 'answer': 'Physical - water molecules remain the same', 'trap': 'The substance looks different but is still H₂O', 'difficulty': 'medium'},
        {'q': 'A kettle of water is heated. Bubbles form at the bottom before reaching the top. What is happening?', 'options': ['Air is escaping from the water', 'Water is evaporating from the bottom', 'Heat is being trapped at the bottom', 'The water is dissolving the kettle'], 'answer': 'Water is evaporating from the bottom', 'trap': 'Bubbles could be dissolved air, but they are primarily water vapor', 'difficulty': 'hard'},
        {'q': 'When water vapor condenses, it releases heat. Where does this heat come from?', 'options': ['The environment', 'Energy stored during evaporation', 'Chemical reactions in water', 'Pressure changes'], 'answer': 'Energy stored during evaporation', 'trap': 'The heat seems to appear from nothing, but it was stored as latent heat', 'difficulty': 'hard'},
        {'q': 'Rain falls from clouds. Before reaching the cloud, water evaporated from the sea. What is the name of the complete process?', 'options': ['Distillation', 'The Water Cycle', 'Sublimation', 'Crystallization'], 'answer': 'The Water Cycle', 'trap': 'Distillation is similar but usually refers to heating liquid to produce vapor', 'difficulty': 'easy'},
        {'q': 'A puddle dries faster on a hot, windy day than on a cool, still day. Why?', 'options': ['Wind blows the water away', 'Heat increases evaporation, wind carries vapor away', 'The puddle is shallower', 'Water is attracted to cool temperatures'], 'answer': 'Heat increases evaporation, wind carries vapor away', 'trap': 'Wind alone cannot make water disappear', 'difficulty': 'medium'},
        {'q': 'What happens to the mass of water during the water cycle?', 'options': ['Mass increases as it evaporates', 'Mass decreases as it condenses', 'Mass remains the same throughout', 'Mass varies with temperature'], 'answer': 'Mass remains the same throughout', 'trap': 'Water changes state, not amount (ignoring tiny losses to space)', 'difficulty': 'hard'},
    ],

    'Ch3_Plant': [
        {'q': 'Xylem vessels transport water. What is the driving force for water to move UP against gravity?', 'options': ['Turgor pressure', 'Root pressure and transpiration pull', 'Osmosis from roots', 'The plant\'s heartbeat'], 'answer': 'Root pressure and transpiration pull', 'trap': 'Turgor pressure helps, but the main forces are root pressure + transpiration pull', 'difficulty': 'hard'},
        {'q': 'A plant leaf wilts even though the soil is wet. What could cause this?', 'options': ['Roots are rotting (cannot absorb)', 'The plant does not need water', 'Xylem is blocked or damaged', 'The soil pH is wrong'], 'answer': 'Roots are rotting (cannot absorb)', 'trap': 'A blocked xylem would have the same symptom, but wet soil suggests root damage', 'difficulty': 'hard'},
        {'q': 'Why do plants have more xylem than phloem?', 'options': ['Xylem is thinner', 'Water transport is more critical than food transport', 'Xylem is easier to make', 'Phloem is a newer discovery'], 'answer': 'Water transport is more critical than food transport', 'trap': 'Xylem vessels are actually thicker-walled, not thinner', 'difficulty': 'medium'},
        {'q': 'Phloem transports sugars from the leaves to the roots. How do we know sugars are moving BOTH ways in different tissues?', 'options': ['The plant told us', 'Different phloem vessels point different directions', 'Root cells also photosynthesize', 'Scientists traced radioactive sugars'], 'answer': 'Scientists traced radioactive sugars', 'trap': 'Different directions are in the same phloem, but using different tubes', 'difficulty': 'hard'},
        {'q': 'A tree is ringed (bark removed in a circle). It will eventually die. Why?', 'options': ['Xylem is cut, water cannot reach leaves', 'Phloem is cut, sugars cannot reach roots', 'Roots receive no air', 'Sunlight is blocked'], 'answer': 'Phloem is cut, sugars cannot reach roots', 'trap': 'Xylem is still intact below the ring, so water can reach the leaves', 'difficulty': 'hard'},
        {'q': 'Why do plants need mineral ions in addition to water and sunlight?', 'options': ['For color', 'To make proteins, chlorophyll, and other organic compounds', 'For taste', 'To float in water'], 'answer': 'To make proteins, chlorophyll, and other organic compounds', 'trap': 'Minerals are absorbed by roots but students often forget their importance', 'difficulty': 'medium'},
        {'q': 'The guard cells on a leaf stoma close at night. Why?', 'options': ['To rest', 'To conserve water (transpiration decreases)', 'To trap CO₂', 'To produce more glucose'], 'answer': 'To conserve water (transpiration decreases)', 'trap': 'Trapping CO₂ would happen during the day', 'difficulty': 'medium'},
        {'q': 'A plant is placed in a sealed glass box with no air exchange. It will eventually run out of oxygen. Why is this a problem?', 'options': ['Oxygen is needed for photosynthesis', 'Oxygen is needed for respiration to release energy', 'Plants cannot store CO₂', 'The plant will float away'], 'answer': 'Oxygen is needed for respiration to release energy', 'trap': 'Oxygen is produced by photosynthesis, not required for it', 'difficulty': 'hard'},
    ],

    'Ch4_Human': [
        {'q': 'Why is the left side of the heart more muscular than the right?', 'options': ['It pumps faster', 'It pumps blood farther throughout the whole body', 'It is in a more important position', 'The right side is damaged in most people'], 'answer': 'It pumps blood farther throughout the whole body', 'trap': 'Both pump the same volume, but left side works against higher pressure', 'difficulty': 'hard'},
        {'q': 'Blood vessels are narrowing due to buildup inside them. Which organ will suffer FIRST?', 'options': ['Brain', 'Heart', 'Lungs', 'Kidneys'], 'answer': 'Heart', 'trap': 'The heart is always working and most sensitive to reduced blood flow', 'difficulty': 'hard'},
        {'q': 'Why do athletes have a slower resting heart rate than non-athletes?', 'options': ['Their hearts are weaker', 'Their hearts are more efficient and pump more blood per beat', 'They have more blood', 'Their metabolism is slower'], 'answer': 'Their hearts are more efficient and pump more blood per beat', 'trap': 'A slower rate seems weaker, but it is actually healthier/more efficient', 'difficulty': 'hard'},
        {'q': 'Exhaled air contains less oxygen than inhaled air. Where did the "missing" oxygen go?', 'options': ['Left in the lungs', 'Absorbed into the blood in the lungs', 'Used by the lungs themselves', 'Converted to carbon dioxide'], 'answer': 'Absorbed into the blood in the lungs', 'trap': 'Some oxygen stays in lungs for safety, but most is absorbed into blood', 'difficulty': 'medium'},
        {'q': 'A person holds their breath for 2 minutes. Why do they eventually have to breathe?', 'options': ['Their lungs collapse', 'CO₂ levels rise and trigger the brain\'s breathing center', 'Oxygen levels drop', 'They run out of saliva'], 'answer': 'CO₂ levels rise and trigger the brain\'s breathing center', 'trap': 'Oxygen drop matters less than CO₂ buildup for the breathing reflex', 'difficulty': 'hard'},
        {'q': 'A child exercises and their breathing rate increases. Is this automatic or conscious?', 'options': ['Fully conscious', 'Fully automatic (reflex)', 'Both - conscious effort triggers automatic response', 'Neither'], 'answer': 'Both - conscious effort triggers automatic response', 'trap': 'Some students think it is purely voluntary', 'difficulty': 'medium'},
        {'q': 'Capillaries are one cell thick. Why is this important?', 'options': ['They move faster', 'They allow easy diffusion of oxygen and nutrients', 'They prevent infections', 'They store blood'], 'answer': 'They allow easy diffusion of oxygen and nutrients', 'trap': 'Thinness is not about speed', 'difficulty': 'medium'},
        {'q': 'Blood returning from the lungs contains MORE oxygen than blood returning from the body tissues. Why?', 'options': ['The lungs produce oxygen', 'Oxygen diffuses INTO the blood from air in the lungs', 'Body tissues destroy oxygen', 'Returning blood is actually colder'], 'answer': 'Oxygen diffuses INTO the blood from air in the lungs', 'trap': 'Lungs do not produce oxygen; they receive it from air', 'difficulty': 'hard'},
    ],

    'Ch5_Electrical': [
        {'q': 'A battery has a positive and negative terminal. What does the battery do?', 'options': ['Creates electricity', 'Converts chemical energy to electrical energy', 'Stores electrons', 'Attracts wires'], 'answer': 'Converts chemical energy to electrical energy', 'trap': 'Batteries do not create electricity; they convert energy types', 'difficulty': 'medium'},
        {'q': 'An electrical circuit needs three things to work. What happens if you remove the battery?', 'options': ['Current still flows briefly', 'No current flows (no energy source)', 'The light becomes brighter', 'Resistance decreases'], 'answer': 'No current flows (no energy source)', 'trap': 'Some students think inertia of electrons continues the flow', 'difficulty': 'medium'},
        {'q': 'Why is copper used for wires in circuits?', 'options': ['It is shiny', 'It is a good conductor of electricity', 'It is cheap', 'It does not break'], 'answer': 'It is a good conductor of electricity', 'trap': 'While copper is also relatively cheap, conductivity is the main reason', 'difficulty': 'easy'},
        {'q': 'A light bulb in a circuit grows dimmer when more bulbs are added in series. Why?', 'options': ['Total brightness is shared', 'Resistance increases, reducing current', 'Electrons get tired', 'The battery is weakened'], 'answer': 'Resistance increases, reducing current', 'trap': 'Each bulb adds resistance to the circuit', 'difficulty': 'hard'},
        {'q': 'When a switch is "on," what is physically happening inside the switch?', 'options': ['Electricity is being created', 'A conductor bridge connects the two terminals (circuit is completed)', 'Resistance is removed', 'Voltage increases'], 'answer': 'A conductor bridge connects the two terminals (circuit is completed)', 'trap': 'Off/On refer to broken/closed circuits, not creation of electricity', 'difficulty': 'medium'},
        {'q': 'A series circuit has 4 bulbs and 1 battery. If one bulb breaks, all go dark. Why?', 'options': ['The broken bulb was the brightest', 'The circuit is broken, current cannot flow', 'Other bulbs lose power', 'The battery is drained'], 'answer': 'The circuit is broken, current cannot flow', 'trap': 'In a series circuit, breaking anywhere breaks the whole loop', 'difficulty': 'medium'},
        {'q': 'Why is a parallel circuit safer than a series circuit for house wiring?', 'options': ['Parallel uses less electricity', 'If one branch fails, others still work', 'Parallel uses thinner wires', 'It is actually not safer'], 'answer': 'If one branch fails, others still work', 'trap': 'Parallel circuits are redundant, unlike series circuits', 'difficulty': 'hard'},
        {'q': 'A circuit has a voltage of 6V and resistance of 3Ω. What is the current?', 'options': ['0.5A', '2A', '9A', '18A'], 'answer': '2A', 'trap': 'Using Ohm\'s law: I = V/R = 6/3 = 2A', 'difficulty': 'medium'},
    ],

    'Ch6_Circuits': [
        {'q': 'Adding batteries in series (positive to negative) increases voltage. What if you connect them incorrectly (positive to positive)?', 'options': ['Voltage doubles', 'Voltage is canceled / batteries may be damaged', 'Nothing happens', 'Current increases'], 'answer': 'Voltage is canceled / batteries may be damaged', 'trap': 'Reversing a battery cancels its voltage out', 'difficulty': 'hard'},
        {'q': 'A light bulb dims when you add more bulbs to a series circuit. But if you use MORE batteries, the light brightens. Why?', 'options': ['More batteries overpower the bulbs', 'More batteries increase voltage, counteracting the resistance increase', 'Batteries create new energy', 'Bulbs are confused'], 'answer': 'More batteries increase voltage, counteracting the resistance increase', 'trap': 'More bulbs = more resistance; more batteries = more voltage', 'difficulty': 'hard'},
        {'q': 'A switch can control 2 bulbs. If the switch is not in the main circuit but only controls one bulb, what type of circuit is this?', 'options': ['Series', 'Parallel', 'Series-Parallel (mixed)', 'Not a real circuit'], 'answer': 'Series-Parallel (mixed)', 'trap': 'This describes a hybrid circuit', 'difficulty': 'hard'},
        {'q': 'A circuit symbol shows a battery with one longer line and one shorter line. What do these represent?', 'options': ['Positive and negative terminals', 'Energy levels', 'Wire thickness', 'Direction of current'], 'answer': 'Positive and negative terminals', 'trap': 'The longer line is positive, shorter is negative', 'difficulty': 'easy'},
        {'q': 'A resistor is added to a circuit. The bulb becomes dimmer. What happened?', 'options': ['The resistor absorbed the light', 'The resistor increased resistance, reducing current', 'The resistor created an open circuit', 'The bulb is now older'], 'answer': 'The resistor increased resistance, reducing current', 'trap': 'Resistors oppose the flow of current', 'difficulty': 'medium'},
        {'q': 'In a circuit, current flows from positive to negative. Is this the actual direction electrons move?', 'options': ['Yes', 'No, electrons move from negative to positive', 'Electrons do not move in circuits', 'It depends on the battery'], 'answer': 'No, electrons move from negative to positive', 'trap': 'Conventional current is opposite to electron flow', 'difficulty': 'hard'},
        {'q': 'Ammeters measure current. Where should an ammeter be placed in a circuit?', 'options': ['Across the bulb (parallel)', 'In series with the circuit', 'Outside the circuit', 'On the battery'], 'answer': 'In series with the circuit', 'trap': 'Ammeters have very low resistance and go in series', 'difficulty': 'medium'},
        {'q': 'A circuit board has multiple LEDs. Some light up and some do not. What could explain this?', 'options': ['All LEDs are broken', 'Some LEDs are in series with broken connections', 'The battery is weak', 'LEDs are in parallel and some are wired incorrectly'], 'answer': 'Some LEDs are in series with broken connections', 'trap': 'A break in a series section only affects downstream components', 'difficulty': 'hard'},
    ],
}

def get_brain_drainer_questions(chapter, limit=None, difficulty=None):
    """Fetch brain drainer questions for a chapter"""
    if chapter not in BRAIN_DRAINERS:
        return []

    questions = BRAIN_DRAINERS[chapter]

    # Filter by difficulty if specified
    if difficulty:
        questions = [q for q in questions if q.get('difficulty') == difficulty]

    # Limit number of questions
    if limit:
        questions = questions[:limit]

    return questions

def get_random_brain_drainer(chapter, count=1):
    """Get random brain drainer questions"""
    import random
    questions = get_brain_drainer_questions(chapter)
    if count > len(questions):
        count = len(questions)
    return random.sample(questions, count)

def display_brain_drainer_question(question, show_answer=False):
    """Display a brain drainer question"""
    import streamlit as st

    st.subheader(f"🧠 {question['q']}")

    # Display difficulty indicator
    difficulty_colors = {
        'easy': '🟡',
        'medium': '🟠',
        'hard': '🔴'
    }
    difficulty_text = question.get('difficulty', 'unknown').upper()
    st.caption(f"{difficulty_colors.get(question.get('difficulty'), '❓')} Difficulty: {difficulty_text}")

    # Radio buttons for answer selection
    answer_index = st.radio(
        "Choose your answer:",
        options=range(len(question['options'])),
        format_func=lambda i: question['options'][i],
        key=f"brain_drainer_{id(question)}"
    )

    selected_answer = question['options'][answer_index]
    is_correct = selected_answer == question['answer']

    if st.button("Submit Answer", key=f"submit_{id(question)}"):
        if is_correct:
            st.success(f"✅ Correct! {selected_answer} is the right answer.")
            st.info(f"💡 Trap explanation: {question['trap']}")
        else:
            st.error(f"❌ Incorrect. You answered '{selected_answer}'")
            st.info(f"✅ The correct answer is: {question['answer']}")
            st.warning(f"🎯 The trap: {question['trap']}")

        return is_correct

    return None
