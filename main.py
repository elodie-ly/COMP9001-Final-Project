"""
THE MIDNIGHT SPELLBOOK - Four File Edition
Run this file: python3 main.py

A pure Python interactive magical mystery game.

Advanced concepts demonstrated:
1. Object-Oriented Programming
2. File I/O with JSON
3. Exception handling
4. Dictionaries, lists, and nested data structures
5. Modular program structure across four Python files
"""

import copy
import random

from game_data import STORY_INTRO, ROOMS, CHARACTERS, PUZZLES
from models import Player, GameJournal, line, small_line
from save_system import save_game, load_game


# ============================================================
# Utility Functions
# ============================================================

def slow_print(text):
    """Prints story text in readable paragraphs without external libraries."""
    print()
    for paragraph in text.strip().split("\n"):
        print(paragraph.strip())


def get_number(prompt, minimum, maximum):
    """Safely gets a number from the player."""
    while True:
        try:
            choice = int(input(prompt))
            if minimum <= choice <= maximum:
                return choice
            print(f"Please enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid number.")


class MidnightSpellbookGame:
    """Controls the main game loop, story actions, puzzles, and endings."""

    def __init__(self):
        self.player = None
        self.rooms = copy.deepcopy(ROOMS)
        self.characters = copy.deepcopy(CHARACTERS)
        self.puzzles = copy.deepcopy(PUZZLES)
        self.journal = GameJournal()

    # --------------------------------------------------------
    # Start / Load / Save
    # --------------------------------------------------------

    def start(self):
        line()
        print("THE MIDNIGHT SPELLBOOK".center(68))
        print("Four File Story Edition".center(68))
        line()
        slow_print(STORY_INTRO)
        line()
        print("1. Start new game")
        print("2. Load saved game")
        choice = get_number("Choose an option: ", 1, 2)

        if choice == 1:
            name = input("Enter your student name: ").strip()
            if not name:
                name = "New Student"
            self.player = Player(name)
            print(f"\nWelcome, {name}. Your first loop begins.")
            self.story_scene("opening")
        else:
            self.load_game_action()
            if self.player is None:
                print("No save file found. Starting a new game.")
                name = input("Enter your student name: ").strip() or "New Student"
                self.player = Player(name)

        self.main_loop()

    def save_game_action(self):
        save_game(self.player, self.characters, self.puzzles)

    def load_game_action(self):
        player, characters, puzzles = load_game()
        if player is not None:
            self.player = player
            self.characters = characters
            self.puzzles = puzzles

    # --------------------------------------------------------
    # Main Menu
    # --------------------------------------------------------

    def main_loop(self):
        while True:
            line()
            print(f"Loop {self.player.loop_count} | Current Room: {self.player.current_room}")
            line()
            print("1. Explore current room")
            print("2. Move to another room")
            print("3. Talk to a character")
            print("4. Solve a puzzle")
            print("5. View inventory, spells, and clues")
            print("6. View story guide / next step")
            print("7. Restart midnight loop")
            print("8. Save game")
            print("9. Load game")
            print("10. Final accusation")
            print("11. Quit")

            choice = get_number("Choose an option: ", 1, 11)

            if choice == 1:
                self.explore_room()
            elif choice == 2:
                self.move_room()
            elif choice == 3:
                self.talk_to_character()
            elif choice == 4:
                self.solve_puzzle()
            elif choice == 5:
                self.player.show_status()
            elif choice == 6:
                self.journal.show_objectives(self.player, self.puzzles, self.characters)
            elif choice == 7:
                self.restart_loop()
            elif choice == 8:
                self.save_game_action()
            elif choice == 9:
                self.load_game_action()
            elif choice == 10:
                self.final_accusation()
            elif choice == 11:
                print("Thanks for playing The Midnight Spellbook.")
                break

    # --------------------------------------------------------
    # Story Scenes
    # --------------------------------------------------------

    def story_scene(self, scene):
        scenes = {
            "opening": """
A bell rings once.

For a second, the entire academy becomes silent.
Then every candle flame bends backwards, pointing towards the Clock Tower.

Mira pulls you away from the crowd.

Mira: 'Do not panic. Panic is how mysteries win.'
Mira: 'Start with the hourglass. Then follow the evidence.'
""",
            "loop_restart": """
The thirteenth bell rings.

The world folds like a page in a book.
You wake again in Star Hall. The same candle drips upward.
The same students gasp.

But your memory remains.

This loop is not a prison anymore.
It is a second chance.
""",
            "library_memory": """
When you touch the Torn Page, the letters rearrange themselves.

'The Codex answers grief.
The Codex imitates mercy.
The Codex always asks for a price.'
""",
            "tower_memory": """
The tower shows you a memory:

Professor Elowen stands before a younger girl made of silver light.
Elowen: 'Seren, I found a way.'
Seren: 'Sister, please. Do not trade the school for my echo.'

Then the memory shatters.
"""
        }

        if scene in scenes:
            slow_print(scenes[scene])

    # --------------------------------------------------------
    # Game Actions
    # --------------------------------------------------------

    def explore_room(self):
        room_name = self.player.current_room
        room = self.rooms[room_name]

        line()
        print(room_name)
        small_line()
        print(room["description"])

        if room_name not in self.player.visited_rooms:
            slow_print(room["first_visit"])
            self.player.visited_rooms.append(room_name)

        self.player.add_item(room["item"])
        self.player.add_clue(room["clue"])

        if room_name == "Moon Library":
            self.story_scene("library_memory")
        if room_name == "Clock Tower" and not self.player.story_flags["saw_clock_memory"]:
            self.story_scene("tower_memory")
            self.player.story_flags["saw_clock_memory"] = True

    def move_room(self):
        current = self.player.current_room
        connections = self.rooms[current]["connections"]

        print("\nWhere would you like to go?")
        for i, room in enumerate(connections, 1):
            print(f"{i}. {room}")

        choice = get_number("Choose an option: ", 1, len(connections))
        self.player.current_room = connections[choice - 1]

        print(f"\nYou move to {self.player.current_room}.")

        events = [
            "A portrait watches you leave, then quickly pretends to sleep.",
            "Somewhere far away, a clock ticks thirteen times.",
            "A paper crane made of old homework flies past your shoulder.",
            "The floor briefly reflects a version of you from another loop."
        ]
        print(random.choice(events))

    def talk_to_character(self):
        available = [
            name for name, data in self.characters.items()
            if data["room"] == self.player.current_room
        ]

        if not available:
            print("There is no one to talk to here.")
            return

        print("\nCharacters here:")
        for i, name in enumerate(available, 1):
            print(f"{i}. {name}")

        choice = get_number("Choose an option: ", 1, len(available))
        name = available[choice - 1]
        character = self.characters[name]

        line()
        print(name)
        print(character["role"])
        small_line()

        dialogue = random.choice(character["dialogue"])
        print(f"{name}: {dialogue}")

        print("\nHow do you respond?")
        print("1. Listen carefully and show empathy")
        print("2. Accuse them directly")
        print("3. Ask for evidence")
        response = get_number("Choose an option: ", 1, 3)

        if response == 1:
            character["trust"] += 1
            print(f"{name}'s trust increased.")
            self.character_followup(name, "empathy")
        elif response == 2:
            character["trust"] -= 1
            print(f"{name} becomes defensive. Trust decreased.")
            self.character_followup(name, "accuse")
        else:
            character["trust"] += 1
            print(f"{name} respects your careful thinking. Trust increased.")
            self.character_followup(name, "evidence")

        if character["trust"] >= character["secret_threshold"]:
            secret = character["secret"]
            if secret not in self.player.clues:
                print(f"\nSecret revealed by {name}: {secret}")
                self.player.add_clue(secret)

    def character_followup(self, name, response_type):
        followups = {
            "Mira": {
                "empathy": "Mira smiles slightly. 'Good. A detective with a heart is still a detective.'",
                "accuse": "Mira frowns. 'If you accuse everyone, nobody will tell you the truth.'",
                "evidence": "Mira nods. 'Exactly. Evidence is the only thing the loop cannot fake forever.'"
            },
            "Cassian": {
                "empathy": "Cassian looks surprised. 'You are the first person tonight who asked how I felt.'",
                "accuse": "Cassian steps back. 'Then you are no different from the others.'",
                "evidence": "Cassian lowers his voice. 'Fine. Then look for who had permission, not who looked suspicious.'"
            },
            "Professor Elowen": {
                "empathy": "Elowen's eyes soften. 'Kindness is dangerous in a place like this. But thank you.'",
                "accuse": "Elowen's expression closes. 'You are too young to understand impossible choices.'",
                "evidence": "Elowen whispers. 'Evidence may tell you what I did. It may not tell you why.'"
            },
            "Librarian Orin": {
                "empathy": "Orin adjusts his glasses. 'Unexpectedly polite. Continue.'",
                "accuse": "Orin sniffs. 'Poor method. Loud accusation, little proof.'",
                "evidence": "Orin smiles thinly. 'Good. The archive respects documented thinking.'"
            },
            "Shadow Familiar": {
                "empathy": "The cat purrs. 'At last, a human who does not try to win by shouting.'",
                "accuse": "The cat yawns. 'Boring. Even villains deserve accurate paperwork.'",
                "evidence": "The cat flicks its tail. 'Evidence is useful. Wisdom is knowing where to point it.'"
            }
        }

        print(followups[name][response_type])

    def solve_puzzle(self):
        available = [
            name for name, data in self.puzzles.items()
            if data["room"] == self.player.current_room and not data["solved"]
        ]

        if not available:
            print("There is no unsolved puzzle here.")
            return

        puzzle_name = available[0]
        puzzle = self.puzzles[puzzle_name]

        line()
        print(f"Puzzle: {puzzle_name}")
        small_line()
        print(puzzle["question"])

        choice = get_number("Choose an option: ", 1, 3)

        if choice == puzzle["answer"]:
            print("Correct. The magic accepts your answer.")
            puzzle["solved"] = True
            self.player.add_spell(puzzle["reward_spell"])
            self.player.add_clue(puzzle["reward_clue"])
        else:
            print("Incorrect. The room trembles, but the loop gives you another chance.")
            self.player.loop_count += 1
            print(f"Loop count increased to {self.player.loop_count}.")

    def restart_loop(self):
        self.player.loop_count += 1
        self.player.current_room = "Star Hall"
        print("\nYou let the midnight bell take you back to the beginning.")
        self.story_scene("loop_restart")

    # --------------------------------------------------------
    # Ending
    # --------------------------------------------------------

    def final_accusation(self):
        line()
        print("FINAL ACCUSATION")
        line()

        required_spells = ["Lumora", "Chrono Trace", "Sealio"]
        missing = [spell for spell in required_spells if spell not in self.player.spells]

        if missing:
            print("You are not ready yet.")
            print("Missing spells:")
            for spell in missing:
                print(f"- {spell}")
            print("\nUse the story guide if you are lost.")
            return

        if len(self.player.clues) < 7:
            print("You do not have enough evidence yet.")
            print("Collect more clues by exploring rooms and talking to characters.")
            return

        slow_print("""
You climb to the top of the Clock Tower.

The Nocturne Codex floats open in the air.
Professor Elowen stands beside it, crying silently.
Cassian is trapped behind a ring of blue fire.
Mira looks at you and says:

'Do not just choose who to blame.
Choose what truth can actually save us.'
""")

        print("Question 1: Who opened the Nocturne Codex?")
        print("1. Cassian Vale")
        print("2. Professor Elowen")
        print("3. Librarian Orin")
        q1 = get_number("Choose an option: ", 1, 3)

        print("\nQuestion 2: Why was it opened?")
        print("1. To gain power over the academy")
        print("2. To save Seren's trapped memory")
        print("3. To frame Cassian")
        q2 = get_number("Choose an option: ", 1, 3)

        print("\nQuestion 3: What should be sealed?")
        print("1. Cassian")
        print("2. The grief binding Seren to the Codex")
        print("3. The whole library")
        q3 = get_number("Choose an option: ", 1, 3)

        score = 0
        if q1 == 2:
            score += 1
        if q2 == 2:
            score += 1
        if q3 == 2:
            score += 1

        high_trust_count = sum(1 for c in self.characters.values() if c["trust"] >= c["secret_threshold"])

        if score == 3 and high_trust_count >= 4:
            self.secret_ending()
        elif score == 3:
            self.good_ending()
        elif score == 2:
            self.partial_ending()
        else:
            self.bad_ending()

    def secret_ending(self):
        line()
        print("SECRET ENDING: THE FOURTEENTH CHIME")
        line()
        slow_print("""
You raise the Moon Wand.

Lumora reveals the truth.
Chrono Trace shows the pain behind it.
Sealio does not strike Professor Elowen. It does not destroy the Codex.

Instead, it seals the grief that chained Seren's memory to the book.

The clock rings thirteen times.
Then, impossibly, once more.

A fourteenth chime.

Seren's silver figure appears, peaceful at last.
'Sister,' she says, 'you have to live forward now.'

Professor Elowen falls to her knees, not defeated, but released.
Cassian is freed. Mira laughs and cries at the same time.
The Shadow Familiar blinks slowly.

'Acceptable work, little detective.'

Morning arrives at Moonstone Academy.
For the first time, the candles burn in the right direction.
""")
        self.end_game()

    def good_ending(self):
        line()
        print("GOOD ENDING: MORNING RETURNS")
        line()
        slow_print("""
You identify the truth and cast Sealio correctly.

The time crack closes.
Professor Elowen admits what she did and asks the academy for forgiveness.
Cassian is cleared of blame.

Seren's memory fades gently into the clock tower light.

The academy is saved, though some questions remain.
Still, morning returns.
""")
        self.end_game()

    def partial_ending(self):
        line()
        print("PARTIAL ENDING: THE LOOP WEAKENS")
        line()
        slow_print("""
You understand part of the truth, but not all of it.

The loop weakens, and most students escape the midnight prison.
However, the Clock Tower still rings strangely on rainy nights.

Somewhere inside the Nocturne Codex, one page continues to glow.
""")
        self.end_game()

    def bad_ending(self):
        line()
        print("BAD ENDING: MIDNIGHT REPEATS")
        line()
        slow_print("""
You choose punishment before understanding.

The Codex rejects your judgement.
The tower bell rings again.
The candles burn backwards.

You wake in Star Hall.

Midnight has not forgiven you.
""")
        self.player.loop_count += 1
        self.player.current_room = "Star Hall"

    def end_game(self):
        print("\nThank you for playing The Midnight Spellbook.")
        print("You can replay to discover different trust paths and endings.")
        raise SystemExit


if __name__ == "__main__":
    game = MidnightSpellbookGame()
    game.start()
