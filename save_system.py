"""
THE MIDNIGHT SPELLBOOK - Save System
This file saves and loads progress using JSON File I/O.
"""

import json
import os

from game_data import SAVE_FILE
from models import Player


def save_game(player, characters, puzzles):
    """Save the current game state to a JSON file."""
    data = {
        "player": {
            "name": player.name,
            "current_room": player.current_room,
            "inventory": player.inventory,
            "spells": player.spells,
            "clues": player.clues,
            "loop_count": player.loop_count,
            "visited_rooms": player.visited_rooms,
            "story_flags": player.story_flags
        },
        "characters": characters,
        "puzzles": puzzles
    }

    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("Game saved successfully.")
    except OSError:
        print("Could not save the game file.")


def load_game():
    """Load a game from JSON. Returns player, characters, puzzles, or None values."""
    if not os.path.exists(SAVE_FILE):
        print("No saved game found.")
        return None, None, None

    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)

        p_data = data["player"]
        player = Player(p_data["name"])
        player.current_room = p_data["current_room"]
        player.inventory = p_data["inventory"]
        player.spells = p_data["spells"]
        player.clues = p_data["clues"]
        player.loop_count = p_data["loop_count"]
        player.visited_rooms = p_data.get("visited_rooms", [])
        player.story_flags = p_data.get("story_flags", {
            "met_mira": False,
            "saw_clock_memory": False,
            "secret_ready": False
        })

        characters = data["characters"]
        puzzles = data["puzzles"]
        print("Game loaded successfully.")
        return player, characters, puzzles

    except (OSError, KeyError, json.JSONDecodeError):
        print("Save file is damaged or unreadable.")
        return None, None, None
