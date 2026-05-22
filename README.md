Project Title: The Midnight Spellbook - Four File Story Edition
Game Description:
The Midnight Spellbook is a text-based magical mystery game.
The player explores Moonstone Academy, collects evidence, earns character trust, solves puzzles, learns spells, and makes a final judgement. The story includes a time loop, a false suspect, emotional motivation, and multiple endings.
Main File:Run main.py
This project only uses Python built-in libraries: copy, random, json, os.
![Project Cover](assests/Project%20Cover.png)

The Midnight Spellbook Game Flowchart
START
  │
  ▼
Show story background
Moonstone Academy Trapped in a midnight time loop
  │
  ▼
Player enters name
  │
  ▼
Go to the main menu
  │
  ├── 1. Explore current room
  │       │
  │       ├── Display the description of the current room
  │       ├── Obtain an item
  │       └── Get a clue
  │
  ├── 2. Move to another room
  │       │
  │       ├── Show available rooms
  │       └── Update current_room
  │
  ├── 3. Talk to a character
  │       │
  │       ├── Select a character in the current room
  │       ├── Display character dialogue
  │       ├── The player chooses how to respond
  │       │       ├── 1. Empathy → Trust score increased
  │       │       ├── 2. Accuse → Decrease in trust score
  │       │       └── 3. Ask evidence → Trust score increased
  │       └── Unlock hidden clues when your trust level is high enough
  │
  ├── 4. Solve a puzzle
  │       │
  │       ├── Check whether you are in a room with a puzzle
  │       ├── The player enters the answer
  │       ├── The answer is correct
  │       │       ├── Learn a new spell
  │       │       └── Uncover key clues
  │       └── The answer is incorrect
  │               └── Please try again
  │
  ├── 5. View inventory, spells, and clues
  │       │
  │       ├── Show items you have obtained
  │       ├── Show spells you have learnt
  │       ├── Show collected clues
  │       └── Display character trust score
  │
  ├── 6. View story guide / next step
  │       │
  │       └── Based on the current progress, suggest the next objective
  │
  ├── 7. Restart midnight loop
  │       │
  │       ├── loop_count + 1
  │       ├── Keep the clues and items you have obtained
  │       └── Back to Star Hall
  │
  ├── 8. Save game
  │       │
  │       └── Using JSON to save game progress
  │
  ├── 9. Load game
  │       │
  │       └── Reading game progress from JSON
  │
  ├── 10. Final accusation
  │       │
  │       ├── Check whether there is sufficient evidence
  │       ├── The player answers the final deduction question
  │       │       ├── Who opened the Codex?
  │       │       ├── Why was it opened?
  │       │       └── What should be sealed?
  │       └── Reach different endings based on your answers and clues
  │
  └── 11. Quit
          └── Exit the game


Core Plot Flowchart
Player login Moonstone Academy
        │
        ▼
Discovery College Trapped in a Midnight Loop
        │
        ▼
Everyone suspects Cassian Vale
        │
        ▼
The player begins the investigation
        │
        ├── Star Hall
        │       ├── obtain Moon Wand
        │       └── Discovery hourglass Abnormal cracks
        │
        ├── Moon Library
        │       ├── obtain Torn Page
        │       ├── Unlock Archive Lock
        │       └── Society Lumora
        │
        ├── Potion Lab
        │       ├── obtain Moon Water
        │       ├── Unlock Potion Puzzle
        │       └── Society Chrono Trace
        │
        ├── Whispering Garden
        │       ├── obtain Silver Herb
        │       ├── Talk to the Shadow Familiar
        │       └── Upon learning that Seren’s memories were trapped
        │
        └── Clock Tower
                ├── obtain Crystal Key
                ├── Unlock Final Judgement Puzzle
                └── Learn Sealio
        │
        ▼
Players are gradually realising:
Cassian isn't the villain
        │
        ▼
It was Professor Elowen who actually unlocked the Nocturne Codex
        │
        ▼
The reason wasn't malice, but to save my sister, Seren
        │
        ▼
Final conclusion:
It is not a person who has been sealed away,
but Professor Elowen's grief.
        │
        ▼
Go to the ending



Room Exploration Diagram

                 Star Hall
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
  Moon Library   Potion Lab   Whispering Garden
        │            │            │
        └──────┬─────┴─────┬──────┘
               ▼           ▼
            Clock Tower ← Final Area


List of rooms, items, puzzles and spells
| Room              | Item        | Character               | Puzzle          | Reward       |
| ----------------- | ----------- | ----------------------- | --------------- | ------------ |
| Star Hall         | Moon Wand   | Mira                    | None            | Initial clues|
| Moon Library      | Torn Page   | Cassian, Librarian Orin | Archive Lock    | Lumora       |
| Potion Lab        | Moon Water  | Professor Elowen        | Potion Puzzle   | Chrono Trace |
| Whispering Garden | Silver Herb | Shadow Familiar         | None            | Seren clues  |
| Clock Tower       | Crystal Key | None / Memory Echo      | Final Judgement | Sealio       |


Character Relationship Diagram
                   Seren
                     │
              younger sister
                     │
                     ▼
           Professor Elowen
                     │
      opened the Nocturne Codex
                     │
       because she wanted to save Seren
                     │
                     ▼
             Time Loop begins

Mira ───────── helps player think logically
Cassian ────── is blamed by others but is innocent
Orin ───────── guards the library records
Shadow Cat ─── gives mysterious emotional truth
Player ─────── collects evidence and makes final judgement


Ending Decision Flowchart
Final Accusation
        │
        ▼
Players answer 3 questions
        │
        ├── All correct + Sufficient evidence + High trust score
        │       └── Secret Ending
        │
        ├── All correct + Sufficient evidence
        │       └── Good Ending
        │
        ├── Partially correct
        │       └── Partial Ending
        │
        └── Most errors
                └── Bad Ending



The correct answer
1. Who opened the Nocturne Codex?
   → Professor Elowen

2. Why was it opened?
   → To save Seren's trapped memory

3. What should be sealed?
   → The grief binding Seren to the Codex