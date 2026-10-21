"""Project Two starter for the student's text-based adventure game."""

# Robert Rodriguez
# Project Two: Haunted Mansion Text Adventure Game


def show_instructions():
    """Display the game objective and available commands."""
    print("Haunted Mansion Adventure Game")
    print("Collect all six items and return to the Foyer to escape.")
    print("Avoid the Ghost of the Mansion as it moves through the rooms.")
    print("Movement Commands: go north, go south, go east, go west")
    print("Item Command: get item name")
    print("-" * 40)


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and available item."""
    print()
    print(f"You are in the {current_room}.")
    print(f"Inventory: {inventory}")

    room_item = rooms[current_room].get("item")

    if room_item is not None and room_item not in inventory:
        print(f"You see: {room_item}")

    print("-" * 40)


def main():
    """Run the main gameplay loop."""
    # Connect the rooms and place one collectible in each required room.
    rooms = {
        "Foyer": {"west": "Bedroom", "north": "Basement"},
        "Bedroom": {"east": "Foyer", "north": "Attic", "item": "Silver Amulet"},
        "Attic": {"south": "Bedroom", "north": "Library", "item": "Battery"},
        "Library": {"south": "Attic", "east": "Study", "item": "Old Map"},
        "Study": {"west": "Library", "east": "Kitchen", "item": "Mansion Key"},
        "Kitchen": {"west": "Study", "south": "Garage", "item": "Flashlight"},
        "Garage": {"north": "Kitchen", "west": "Basement", "item": "Crowbar"},
        "Basement": {"east": "Garage", "south": "Foyer"},
    }

    # The Ghost follows this fixed route, beginning in the Basement.
    ghost_route = [
        "Basement",
        "Garage",
        "Kitchen",
        "Study",
        "Library",
        "Attic",
        "Bedroom",
        "Foyer",
    ]

    ghost_position = 0
    ghost_room = ghost_route[ghost_position]

    # Initialize the player and game state.
    current_room = "Foyer"
    inventory = []
    total_items = 6
    game_over = False

    show_instructions()

    # Continue playing until the player wins or loses.
    while not game_over:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().lower()

    # Handle movement commands.
    if command.startswith("go "):
        direction = command[3:].strip()

        if direction not in ("north", "south", "east", "west"):
            print("Invalid direction. Use north, south, east, or west.")

        elif direction not in rooms[current_room]:
            print("You can't go that way.")

        else:
            next_room = rooms[current_room][direction]

            # Check whether the Ghost currently occupies the destination.
            if next_room == ghost_room and len(inventory) < total_items:
                print(
                    f"The Ghost of the Mansion catches you in the {next_room}!"
                )
                print("NOM NOM... GAME OVER!")
                game_over = True
            else:
                current_room = next_room

                # Advance the Ghost after a successful player movement.
                ghost_position = (ghost_position + 1) % len(ghost_route)
                ghost_room = ghost_route[ghost_position]

                # The Ghost can catch the player as it enters their room.
                if ghost_room == current_room and len(inventory) < total_items:
                    print(
                        f"The Ghost of the Mansion catches you "
                        f"in the {current_room}!"
                    )
                    print("NOM NOM... GAME OVER!")
                    game_over = True

                # Winning requires all six items and returning to the Foyer.
                elif len(inventory) == total_items and current_room == "Foyer":
                    print(
                        "Congratulations! You collected all six items "
                        "and escaped the Haunted Mansion!"
                    )
                    game_over = True

    # Handle item collection commands.
    elif command.startswith("get "):
        requested_item = command[4:].strip().casefold()
        room_item = rooms[current_room].get("item")

        if room_item is None:
            print("There is no item to collect in this room.")

        elif room_item.casefold() != requested_item:
            print("That item is not available in this room.")

        elif room_item in inventory:
            print("You have already collected that item.")

        else:
            inventory.append(room_item)
            print(f"You collected the {room_item}!")

            if len(inventory) == total_items:
                print(
                    "You have collected all six items! "
                    "Return to the Foyer to escape."
                )
    # Reject commands that are neither valid movement nor item commands.
    else:
        print(
            "Invalid command. Use 'go north', 'go south', "
            "'go east', 'go west', or 'get item name'."
        )
    print("Thanks for playing! Hope you enjoyed the game.")


if __name__ == "__main__":
    main()
