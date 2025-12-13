#Radney Johnson
#12/13/2025
#Final Project
# adventure_game_map.py

# Text-based adventure game with emojis, map, and dynamic character stats

import random
import time

# ==============================
# Functions
# ==============================

def intro():
    """Introduce the game and instructions with emojis."""
    print("🗡️ Welcome to the Dungeon Adventure! 🏰")
    print("Your goal: Collect 3 treasures 💎 and escape safely 🚪.")
    print("Move 'left' or 'right' and see what happens! 💥👹")
    print("-" * 50)
    time.sleep(2)

def create_map(length=10):
    """Create a simple 1D map represented by a list of spaces."""
    dungeon_map = ["⬜"] * length
    return dungeon_map

def display_map(dungeon_map, player_pos):
    """Display the map showing the player's current position."""
    map_copy = dungeon_map.copy()
    map_copy[player_pos] = "🧍"  # Player emoji
    print(" ".join(map_copy))
    time.sleep(1)

def player_move(player_pos, map_length):
    """Ask the player to choose a direction and update position."""
    choice = input("➡️ Move left or right? ").lower()
    while choice not in ["left", "right"]:
        choice = input("❌ Invalid choice. Choose 'left' or 'right': ").lower()
    if choice == "left":
        player_pos = max(0, player_pos - 1)
    else:
        player_pos = min(map_length - 1, player_pos + 1)
    return player_pos

def encounter_enemy(player):
    """Randomly determines if player encounters an enemy and handles combat."""
    print("👹 You might encounter an enemy...")
    time.sleep(1)
    if random.randint(0, 1) == 1:
        damage = random.randint(5, 20)
        player["health"] -= damage
        print(f"💥 You were attacked! Lost {damage} health.")
    else:
        print("✅ No enemies here. You're safe!")
    time.sleep(1)

def find_treasure(player):
    """Randomly gives the player a treasure and updates inventory."""
    print("🔍 Searching the area...")
    time.sleep(1)
    treasures = ["gold", "potion", "gem"]
    found = random.choice(treasures)
    player["inventory"][found] = player["inventory"].get(found, 0) + 1
    print(f"🎉 You found a {found}!")

def use_item(player):
    """Allows player to use a potion if available."""
    if player["inventory"].get("potion", 0) > 0:
        choice = input("🧪 Use a potion to restore 20 health? (yes/no): ").lower()
        if choice == "yes":
            player["health"] += 20
            player["inventory"]["potion"] -= 1
            print("✨ Potion used! Health restored by 20.")

def check_game_over(player, player_pos, map_length):
    """Check if the player has won or lost."""
    if player["health"] <= 0:
        print("💀 You lost all your health. Game over!")
        return True
    if sum(player["inventory"].get(t, 0) for t in ["gold", "gem"]) >= 3 and player_pos == map_length - 1:
        print("🏆 Congratulations! You collected treasures and escaped! 🚪")
        return True
    return False

# ==============================
# Main Game Loop
# ==============================

def main():
    """Main function to run the game."""
    # Main character dictionary
    player = {
        "health": 100,
        "inventory": {}
    }

    dungeon_length = 10
    player_pos = 0  # Start at leftmost position
    dungeon_map = create_map(dungeon_length)

    intro()

    game_over = False
    while not game_over:
        display_map(dungeon_map, player_pos)
        player_pos = player_move(player_pos, dungeon_length)

        # Randomly encounter enemy or treasure
        if random.randint(0, 1) == 0:
            encounter_enemy(player)
        else:
            find_treasure(player)

        use_item(player)

        # Display updated player stats
        print(f"❤️ Health: {player['health']}")
        print(f"🎒 Inventory: {player['inventory']}")
        print("-" * 40)
        time.sleep(1)

        game_over = check_game_over(player, player_pos, dungeon_length)

    print("🎮 Thanks for playing Dungeon Adventure!")

# ==============================
# Program Entry Point
# ==============================

if __name__ == "__main__":
    main()
