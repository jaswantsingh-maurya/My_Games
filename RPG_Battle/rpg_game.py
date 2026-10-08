import random 

#player and monster hp
player_hp=100
monster_hp=100

is_defending = False

print("===============================================================")
print("|----- ⚔⚔ Welcome to Player😎 vs Monster👹 RPG Game ⚔⚔ -----|")
print("===============================================================")

#_Game Loop
while monster_hp>0 and player_hp>0:
    print(f"Health ❤ of Player = {player_hp} || Health ❤ of Monster = {monster_hp }")
    user=input("Choose Attack,Defend or Heal : ").lower()
        # Player Attacks Defend and Heal
    if user=="attack":
        attack=random.randint(10,20)
        monster_hp-=attack
        print(f"You dealt {attack} damage! ")
    
    elif user=="defend":
        is_defending=True
        print(f"You are defending! Next attack is half ")
    
    elif user=="heal":
        heal = 15
        player_hp=min(100,player_hp + heal)
        print(f"You Healed {heal} HP! ")
    
    else:
        print("Invalid Choice")
        continue
        # Monster attacks if alive
    if monster_hp > 0 :
        monster = random.randint(10,20)
        if is_defending:
            monster = monster//2
            is_defending=False
        
        player_hp-=monster
        print(f"Monster dealt {monster} damage! \n")
# Game Ends
if player_hp>0:
    print("You Killed Monster!\n You Won")
else:
    print("You Died\n Monster Won")
