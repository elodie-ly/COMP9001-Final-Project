"""
THE MIDNIGHT SPELLBOOK - Game Data
This file stores all story text, room data, character data, and puzzle data.
"""

SAVE_FILE = "midnight_spellbook_save.json"

STORY_INTRO = """
You are a first-year student at Moonstone Academy, a secret school of
magic hidden behind a mountain of silver fog.

Tonight should have been the Starlight Welcome Feast. Instead, the
academy is trapped at midnight. Candles burn backwards. The portraits
repeat half-finished warnings. The same bell rings again and again.

The forbidden Nocturne Codex has been opened.

Most students blame Cassian Vale, a quiet student seen near the library.
But your friend Mira thinks the truth is too neat. Professor Elowen,
the kind but exhausted time-magic teacher, refuses to say the name
"Seren". A black cat with moon-bright eyes keeps appearing wherever
the clock hands tremble.

To break the loop, you must explore rooms, earn trust, collect evidence,
learn spells, and make a final judgement.

This is not only a game about finding the guilty person.
It is a game about understanding why the magic broke.
"""

ROOMS = {
    "Star Hall": {
        "description": "A grand hall filled with floating candles and nervous students. A cracked hourglass stands in the centre.",
        "connections": ["Moon Library", "Potion Lab", "Whispering Garden"],
        "item": "Moon Wand",
        "clue": "The central hourglass cracked before the first midnight bell.",
        "first_visit": """
The Star Hall looks beautiful, but wrong.
A silver hourglass lies cracked under the ceiling of floating candles.
The sand inside is moving upwards.

Mira touches your sleeve and whispers:
'If time is broken, someone left a scar before midnight. Find the scar.'
"""
    },
    "Moon Library": {
        "description": "Tall shelves twist like a maze. The restricted archive door glows with a blue lock.",
        "connections": ["Star Hall", "Clock Tower"],
        "item": "Torn Page",
        "clue": "A torn page says: The Codex can only be opened by someone with archive permission.",
        "first_visit": """
The Moon Library is colder than the rest of the academy.
A fallen chair lies beside the restricted archive.
On the floor, you find ink marks shaped like tiny clock hands.

A portrait of an old librarian mutters:
'Do not ask who held the book. Ask who was allowed to reach it.'
"""
    },
    "Potion Lab": {
        "description": "Glass bottles glow on dusty tables. A half-made memory potion shimmers in a silver bowl.",
        "connections": ["Star Hall", "Whispering Garden"],
        "item": "Moon Water",
        "clue": "The unfinished potion was designed to recover a lost memory, not to attack anyone.",
        "first_visit": """
The Potion Lab smells of mint, smoke, and rain.
A silver bowl bubbles gently, showing a blurry reflection of a young girl
standing beside Professor Elowen.

The image fades before you can see her face.
"""
    },
    "Whispering Garden": {
        "description": "Moonlit flowers whisper names. A black cat watches from beside a frozen fountain.",
        "connections": ["Star Hall", "Potion Lab", "Clock Tower"],
        "item": "Silver Herb",
        "clue": "The flowers whisper the name Seren whenever the clock tower shakes.",
        "first_visit": """
The garden is frozen in a midnight wind.
Flowers turn their heads towards you as if they can hear your thoughts.

A black cat jumps onto the fountain edge and says, calmly:
'You took long enough.'
"""
    },
    "Clock Tower": {
        "description": "The oldest tower in the academy. Its clock face has thirteen numbers and one missing hand.",
        "connections": ["Moon Library", "Whispering Garden"],
        "item": "Crystal Key",
        "clue": "The missing clock hand is not broken. It is holding a memory inside the tower.",
        "first_visit": """
The Clock Tower hums like a living heart.
Each step upward shows a different version of midnight:
students laughing, students screaming, Professor Elowen crying.

At the top, the missing clock hand floats inside a crack of violet light.
"""
    }
}

CHARACTERS = {
    "Mira": {
        "room": "Star Hall",
        "role": "Your friend. Logical, brave, and good at noticing details.",
        "trust": 1,
        "dialogue": [
            "Everyone is blaming Cassian, but that feels too easy.",
            "Notice how Professor Elowen never says Seren's name?",
            "Evidence first. Rumours later. That is how we survive a mystery.",
            "If I disappear in the next loop, promise me you will still question everything."
        ],
        "secret_threshold": 3,
        "secret": "Mira reveals that Seren was Professor Elowen's younger sister."
    },
    "Cassian": {
        "room": "Moon Library",
        "role": "A quiet student who was seen near the restricted archive.",
        "trust": 0,
        "dialogue": [
            "I know everyone thinks it was me. That does not make it true.",
            "I was in the library because someone sent me an anonymous note.",
            "The archive opened before I touched the door.",
            "Professor Elowen looked at the Codex like it was the only thing keeping her alive."
        ],
        "secret_threshold": 3,
        "secret": "Cassian shows you the anonymous note that lured him to the library."
    },
    "Professor Elowen": {
        "room": "Potion Lab",
        "role": "A time-magic teacher. Gentle, brilliant, and visibly exhausted.",
        "trust": 0,
        "dialogue": [
            "Some doors should remain closed, even when love asks us to open them.",
            "Time is not a river. It is a room full of echoes.",
            "I did not mean for the entire academy to suffer.",
            "Seren was not gone. I heard her inside the clock. I thought I could bring her back."
        ],
        "secret_threshold": 4,
        "secret": "Professor Elowen confesses that Seren's memory is trapped inside the Nocturne Codex."
    },
    "Librarian Orin": {
        "room": "Moon Library",
        "role": "The strict keeper of the restricted archive.",
        "trust": 0,
        "dialogue": [
            "The Codex does not open for curiosity. It opens for grief.",
            "Cassian had no archive permission. Remember that.",
            "Only staff-level magic could open the inner lock.",
            "Elowen requested access to memory magic three nights ago."
        ],
        "secret_threshold": 3,
        "secret": "Librarian Orin confirms Professor Elowen had legal archive access."
    },
    "Shadow Familiar": {
        "room": "Whispering Garden",
        "role": "A talking black cat with moon-bright eyes.",
        "trust": 2,
        "dialogue": [
            "Humans always ask who to punish. Magic asks what to release.",
            "The loop is a knot. Pull the wrong thread and everyone stays trapped.",
            "Seren is not the villain. Elowen is not only the villain either.",
            "Seal the grief, little student. Not the person. Not the book. The grief."
        ],
        "secret_threshold": 3,
        "secret": "The Shadow Familiar tells you the final seal must target grief, not a person."
    }
}

PUZZLES = {
    "Archive Lock": {
        "room": "Moon Library",
        "question": """
The archive lock shows three glowing statements:

1. A liar always leaves fingerprints.
2. Permission opens what force cannot.
3. The youngest student must be guilty.

Which statement matches your evidence?
""",
        "answer": 2,
        "reward_spell": "Lumora",
        "reward_clue": "The archive lock recognises Professor Elowen's magical signature.",
        "solved": False
    },
    "Memory Potion": {
        "room": "Potion Lab",
        "question": """
The memory potion requires a balanced formula.

1. Moon Water + Silver Herb
2. Black Ink + Fire Dust
3. Crystal Sand + Shadow Feather

Which formula completes the potion safely?
""",
        "answer": 1,
        "reward_spell": "Chrono Trace",
        "reward_clue": "The potion reveals a memory of Elowen calling Seren's name at the clock tower.",
        "solved": False
    },
    "Thirteenth Bell": {
        "room": "Clock Tower",
        "question": """
The clock tower asks:

What is the correct spell order to calm the time crack?

1. Sealio -> Lumora -> Chrono Trace
2. Chrono Trace -> Sealio -> Lumora
3. Lumora -> Chrono Trace -> Sealio

Choose the correct sequence.
""",
        "answer": 3,
        "reward_spell": "Sealio",
        "reward_clue": "The clock accepts a gentle seal. The target must be grief, not revenge.",
        "solved": False
    }
}
