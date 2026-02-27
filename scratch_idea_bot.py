# Scratch Project Idea Bot
# Save this file as: scratch_idea_bot.py

import random

print("🎮 Scratch Project Idea Bot 🎮")
print("------------------------------")

genres = [
    "platformer",
    "RPG",
    "tycoon",
    "adventure",
    "puzzle",
    "clicker",
    "shooter"
]

themes = [
    "space",
    "dragons",
    "robots",
    "school",
    "ocean",
    "magic",
    "future city",
    "jungle"
]

goals = [
    "collect coins",
    "escape enemies",
    "save the world",
    "build a city",
    "solve mysteries",
    "defeat a boss",
    "protect a village"
]


def generate_idea():
    return f"Make a {random.choice(themes)} {random.choice(genres)} game where you {random.choice(goals)}."


while True:
    print("\n💡 Your Scratch Idea:")
    print(generate_idea())

    again = input("\nGenerate another idea? (y/n): ").lower()

    if again != "y":
        print("Good luck making your Scratch project! 🚀")
        break