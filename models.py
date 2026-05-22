"""
THE MIDNIGHT SPELLBOOK - Models
This file contains the main classes used by the game.
"""


def line():
    print("=" * 68)


def small_line():
    print("-" * 68)


class Player:
    """Stores the player's current progress, inventory, spells, and clues."""

    def __init__(self, name):
        self.name = name
        self.current_room = "Star Hall"
        self.inventory = []
        self.spells = []
        self.clues = []
        self.loop_count = 1
        self.visited_rooms = []
        self.story_flags = {
            "met_mira": False,
            "saw_clock_memory": False,
            "secret_ready": False
        }

    def add_item(self, item):
        if item and item not in self.inventory:
            self.inventory.append(item)
            print(f"You collected: {item}")
        elif item:
            print(f"You already have: {item}")

    def add_spell(self, spell):
        if spell and spell not in self.spells:
            self.spells.append(spell)
            print(f"New spell learned: {spell}")

    def add_clue(self, clue):
        if clue and clue not in self.clues:
            self.clues.append(clue)
            print(f"New clue added: {clue}")

    def show_status(self):
        line()
        print(f"Student: {self.name}")
        print(f"Loop: {self.loop_count}")
        print(f"Current Room: {self.current_room}")
        small_line()

        print("Inventory:")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("- Empty")

        print("\nSpells:")
        if self.spells:
            for spell in self.spells:
                print(f"- {spell}")
        else:
            print("- No spells learned yet")

        print("\nClues:")
        if self.clues:
            for i, clue in enumerate(self.clues, 1):
                print(f"{i}. {clue}")
        else:
            print("- No clues collected yet")
        line()


class GameJournal:
    """Tracks story progress and provides next-step hints."""

    def __init__(self):
        self.chapter = 1
        self.objectives = [
            "Explore Star Hall and take the Moon Wand.",
            "Visit Potion Lab and solve the Memory Potion puzzle.",
            "Visit Moon Library and solve the Archive Lock puzzle.",
            "Visit Whispering Garden and speak with the Shadow Familiar.",
            "Reach Clock Tower and solve the Thirteenth Bell puzzle.",
            "Use the final accusation when you understand the truth."
        ]

    def show_objectives(self, player, puzzles, characters):
        line()
        print("CURRENT STORY GUIDE")
        small_line()

        if "Moon Wand" not in player.inventory:
            print("Next step: Explore Star Hall to collect your Moon Wand.")
        elif not puzzles["Memory Potion"]["solved"]:
            print("Next step: Go to Potion Lab, explore it, then solve the Memory Potion puzzle.")
        elif not puzzles["Archive Lock"]["solved"]:
            print("Next step: Go to Moon Library, explore it, then solve the Archive Lock puzzle.")
        elif "Silver Herb" not in player.inventory:
            print("Next step: Go to Whispering Garden and explore it.")
        elif not puzzles["Thirteenth Bell"]["solved"]:
            print("Next step: Go to Clock Tower, explore it, then solve the Thirteenth Bell puzzle.")
        else:
            print("Next step: Use Final accusation from the main menu.")

        print("\nRecommended for better ending:")
        print("- Talk to characters and choose empathy or evidence.")
        print("- Avoid accusing people too early.")
        print("- Try to unlock secret clues from Mira, Cassian, Elowen, Orin, and the Shadow Familiar.")
        small_line()

        print("Trust levels:")
        for name, data in characters.items():
            print(f"- {name}: {data['trust']}")
        line()
