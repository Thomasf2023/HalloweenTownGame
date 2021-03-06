# Halloween Town Text Adventure Game
# By: Thomas Fiske
# IT - 140 SNHU
# Date: 10/17/2021

# Dictionary
streets = {
        'Halloween Street': {'South': 'Elm Street', 'North': 'Morgue Ally', 'East': 'Boulevard of the Living Dead', 'West':  'Turn Back Drive'},
        'Elm Street': {'North': 'Halloween Street', 'East': "Crystal Lake Street", 'Item': 'Nightmare fuel'},
        'Turn Back Drive': {'East': 'Halloween Street', 'Item': 'Candy'},
        'Morgue Ally': {'South': 'Halloween Street', 'East': 'Vampire Avenue', 'Item': 'Pumpkin'},
        'Vampire Avenue':{'West': 'Morgue Ally', 'Item': 'Vampire Fangs'},
        'Boulevard of the Living Dead':{'West': 'Halloween Street', 'North': 'Werewolf Way', 'Item': 'Brains'},
        'Werewolf Way': {'South': 'Boulevard of the Living Dead', 'Item': 'Lycan Fang'},
        'Camp Crystal Lake Street': {'West': 'Elm Street'}
        } # Street dictionary(Monster room: renamed from original storyboard to not give away monster location)

# Variables
location = 'Halloween Street'
move = ''
inventory_list = []
item_list = ['Candy', 'Brains', 'Nightmare Fuel', 'Vampire Fangs', 'Lycan Fang', 'Pumpkin']
item = ''
items_left = 6

# Functions
def show_instructions(): # Function to show instructions
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print()
    print()
    print('Halloween Text Adventure Game')
    print()
    print()# White space to make instructions more readable
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print()
    print('Instructions:')
    print()
    print('Travel the streets of Halloween Town and collect 6 halloween items to win the game!')
    print('But! If you run into the Halloween Monster, it will EAT YOU!')
    print()
    print('Move Commands: North, East, West, South.', 'Example: North')
    print('Add Item to Inventory : Get "item name".', 'Example: Get Item')
    print("If you get scared, type 'Exit' to end the game.", 'Example: Exit')
    print()
    print('Every new move will tell you what moves you have, and where they will take you.')
    print('It will also tell you if you can get an item on the street you are on.')
    print('You cannot collect an item more than once.')
    print()
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print()
    print('Good Luck!!')
    print()
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    # |||| lines used to separate instructions from gameplay menu

def current_street(): # Function used to tell player their current street every turn
    print()
    print('You are on', location)


def player_progress(): # Function that will be used in the loop to show player progress every move
    print('Inventory:', ',' .join(inventory_list))
    print()
    print('Items Left:', items_left)
    return

def invalid_move(): # Error message for when player inserts invalid move
    print()
    print('||||||||||||||||||||||||||||||||')
    print('Error: Please enter a valid move')
    print('||||||||||||||||||||||||||||||||')
    print()

def item_again(): #Error message when player tries to take an item twice
    print()
    print('||||||||||||||||||||||||||||')
    print("Nice try! You can't do that!")
    print('||||||||||||||||||||||||||||')
    print()

def monster():
    print()
    print("You have Ventured onto Camp Crystal Lake Street.")
    print('The Monster Eats You!!')
    print("Maybe next time you'll stay home!")
    print('Thank you for playing!')
    print('Happy Halloween!')
    print()


## Game start
show_instructions()

while len(inventory_list) != 6: # Gameplay loop. Will loop until player has an inventory of 6 items, Exits or Loses

    # start of game gameplay menu, everything before the If statement will run every turn.
    current_street()
    print()

    available_moves = str(streets[location])
    available_moves = available_moves.replace('{', '')
    available_moves = available_moves.replace('}', '')
    available_moves = available_moves.replace("'", '')
    available_moves = available_moves.replace("Item", 'Get Item')
    print('Available moves: ', available_moves)
    print()

    player_progress()
    print()
    move = input('Make your move').strip().lower()
    # Everything below this comment starts after first move
    print()
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    # |||| lines used to separate every turn's gameplay menu
    print('New Turn')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print()
    print('Last turn, You entered:', move)


    if move == 'south' and location == 'Halloween Street':  # if statement will run if location is halloween street and move is available
        location = 'Elm Street'
        continue
    elif move == 'exit':  # Easy way for player to end the game
        break
    elif move == 'north' and location == 'Halloween Street':
        location = 'Morgue Ally' # Will move player location to 'Morgue Ally' and Begin their turn again
        continue
    elif move == 'east' and location == 'Halloween Street':
        location = 'Boulevard of the Living Dead'
        continue
    elif move == 'west' and location == 'Halloween Street':
        location = 'Turn Back Drive'
        continue
    elif move not in available_moves and location == 'Halloween Street':
        invalid_move()
        continue
    elif move == 'east' and location == 'Turn Back Drive':
        location = 'Halloween Street'
        continue
    elif move == 'get candy' and location == 'Turn Back Drive':
            if 'Candy' in inventory_list: # This If statement will stop players from collecting two of the same item
                item_again() # call to the function that prints error message
                continue
            else:
                item_add1 = 'Candy'
                inventory_list.append(item_add1) # Adding item to inventory list
                streets['Turn Back Drive'] = {'East': 'Halloween Street'}
                items_left -=1 # takes one away from item_left for player progress function
                print()
                print('You got the item: Candy')
            continue
    elif move not in available_moves and location == 'Turn Back Drive':
        invalid_move()
        continue
    elif move == 'north' and location == 'Elm Street':
        location = 'Halloween Street'
        continue
    elif move == 'get nightmare fuel' and location == 'Elm Street':
        if 'Nightmare Fuel' in inventory_list:
            item_again()
            continue
        else:
            item_add2 = 'Nightmare Fuel'
            inventory_list.append(item_add2)
            streets['Elm Street'] = {'North': 'Halloween Street', 'East': "Camp Crystal Lake"}
            items_left -= 1
            print()
            print('You got the item: Nightmare Fuel')
            continue
    elif move == 'east' and location == 'Elm Street':
        location = 'Camp Crystal Lake Street' # Monster's Street, Player loses the game
        monster() # call to the monster function that prints end of game text
        break
    elif move not in available_moves and location == 'Elm Street':
        invalid_move()
        continue
    elif move == 'south' and location == 'Morgue Ally':
        location = 'Halloween Street'
        continue
    elif move == 'east' and location == 'Morgue Ally':
        location = 'Vampire Avenue'
        continue
    elif move == 'get pumpkin' and location == 'Morgue Ally':
        if 'Pumpkin' in inventory_list:
            item_again()
            continue
        else:
            item_add3 = 'Pumpkin'
            inventory_list.append(item_add3)
            streets['Morgue Ally'] = {'South': 'Halloween Street', 'East': 'Vampire Avenue'}
            items_left -= 1
            print()
            print('You got the item: Pumpkin')
            continue
    elif move not in available_moves and location == 'Morgue Ally':
        invalid_move()
        continue
    elif move == 'west' and location == 'Vampire Avenue':
        location = 'Morgue Ally'
        continue
    elif move == 'get vampire fangs' and location == 'Vampire Avenue':
        if 'Vampire Fangs' in inventory_list:
            item_again()
            continue
        else:
            item_add4 = 'Vampire Fangs'
            inventory_list.append(item_add4)
            streets['Vampire Avenue'] = {'West': 'Morgue Ally'}
            items_left -= 1
            print()
            print('You got the item: Vampire Fangs')
            continue
    elif move not in available_moves and location == 'Vampire Avenue':
        invalid_move()
    elif move == 'west' and location == 'Boulevard of the Living Dead':
        location = 'Halloween Street'
        continue
    elif move == 'north' and location == 'Boulevard of the Living Dead':
        location = 'Werewolf Way'
        continue
    elif move == 'get brains' and location == 'Boulevard of the Living Dead':
        if 'Brains' in inventory_list:
            item_again()
            continue
        else:
            item_add5 = 'Brains'
            inventory_list.append(item_add5)
            streets['Boulevard of the Living Dead'] = {'West': 'Halloween Street', 'North': 'Werewolf Way'}
            items_left -= 1
            print()
            print('You got the item: Brains')
            continue
    elif move not in available_moves and location == 'Boulevard of the Living Dead':
        invalid_move()
        continue
    elif move == 'south' and location == 'Werewolf Way':
        location = 'Boulevard of the Living Dead'
        continue
    elif move == 'get lycan fang' and location == 'Werewolf Way':
        if 'Lycan Fang' in inventory_list:
            item_again()
            continue
        else:
            item_add6 = 'Lycan Fang'
            inventory_list.append(item_add6)
            streets['Werewolf Way'] = {'South': 'Boulevard of the Living Dead'}
            items_left -= 1
            print()
            print('You got the item: Lycan Fang')
            continue
    elif move not in available_moves and location == 'Boulevard of the Living Dead':
        invalid_move()
        continue
    elif move == exit : # using exit variable to break string in move = 'exit'
        break
    else:
        invalid_move()

while len(inventory_list) != 6 and location != 'Camp Crystal Lake Street':
    print('You got scared and ran home!')
    print('Thanks for playing!')
    print('Happy Halloween!')
    break # loop for when gameplay loop is broken and game is not won but not exited

while len(inventory_list) == 6: # loop for when gameplay loop is broken and game is won but not exited
     print('Congratulations!! You have won the game!')
     print('Thank you for playing!')
     print('Happy Halloween!')
     break

## Game over





