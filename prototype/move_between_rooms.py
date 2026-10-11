# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'south': 'Bedroom'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
        'Cellar': {'west': 'Bedroom'}
}

# Set starting room of player.
current_room = 'Great Hall'

#Keep playing until the player chooses to exit.
while current_room != 'exit':
    print(f"\nYou are in the {current_room}.")

    # Prompt user to input their command
    command = input(
    "what would you like to do? (go north, go south, go east, go west, exit):"
    ).strip().lower().split()

    # Exit the game when requested.
    if command == ['exit']:
        current_room = 'exit'

    # Handle movement commands.
    elif len(command) == 2 and command[0] == 'go':
        direction = command[1]

        # Check whether the direction connects to another room.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.")

    # Handle invalid commands.
    else:
        print("Invalid command. Use 'go north', 'go south'," "'go east', 'go west', or 'exit'.")

print("Thanks for playing!")
