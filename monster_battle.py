#seb ydia         sirr why no globalll :[
def display_intro():
    print('''=================================
 MONSTER BATTLE ARENA
=================================
''')

def show_weapons():
    print('''Choose your weapon:
[1] Iron Sword - 30 Attack
[2] Magic Staff - 45 Attack
[3] Golden Axe - 60 Attack''')

def choose_weapon(choice):
    if choice == 1:
        attack = 30
    elif choice == 2:
        attack = 45
    else:
        attack = 60
    return attack

def show_monsters():
    print("""Choose your opponent:
[1] Green Slime - 20 Damage
[2] Forest Goblin - 40 Damage
[3] Fire Dragon - 70 Damage""")

def monster_attack(monster):
    if monster == 1:
        damage = 20
    elif monster == 2:
        damage = 40
    else:
        damage = 60
    return damage

def calculate_health(health, damage):
    remaining = health - damage
    return remaining

def battle_result(attack, health,damage, ):
    print("The monster attacks!")
    print(f"You recieved {damage} damage!")
    print("You attacked using your weapon!")
    print(f"Attack Power: {attack}")
    print(f"Remaining Health: {health}")
    if health >= 0 and attack >= 50:
        result = "VICTORY!"
    else:
        result = "DEFEAT!"
    return result
def points(points,attack,choice):
    if attack >= 50 and choice == 1:
        points +=20
    elif attack >= 50 and choice == 2:
        points +=40
    elif attack >= 50 and choice == 3:
        points +=70
    else:
        points = 0
    return points

def get_rank(points):
    if points >= 70:
        rank = "Legendary Warrior"
    elif points >= 40:
        rank = "Elite Fighter"
    elif points >= 20:
        rank = "Brave Beginner"
    else:
        rank = "Rookie Warrior"
    return rank
def display_report(player, health, points, rank, result):
    print(f'''-------- BATTLE REPORT --------
Player: {player} 
Remaining Health: {health} HP
Battle Points: {points}
Warrior Rank: {rank}
Battle Result: {result}
-------------------------------''')

#-----------------------------------------------------


display_intro()

player = input("Enter player name:")

show_weapons()
choice = int(input("Enter weapon choice: "))
attack = choose_weapon(choice)

show_monsters()
monster = int(input("Enter monster choice:"))

damage = monster_attack(monster)
health = calculate_health(100, damage)

result = battle_result(attack, health, damage)

points = points(0,attack, choice)

rank = get_rank(points)
display_report(player, health, points, rank, result)