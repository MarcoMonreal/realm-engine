realm_name = "Eldenmoor"
population = 4200
danger_level = 7.5
is_at_war = False

print(f"Welcome to {realm_name}!")
print(f"Population: {population}, Danger Level: {danger_level}")

hero_name = input("Enter your hero's name: ")
print(f"Hail, {hero_name}! The realm of {realm_name} awaits.")

gold = 100
potion_cost = 25
potions_bought = 3

remaining_gold = gold - (potion_cost * potions_bought)
print(f"You bought {potions_bought} potions. Gold remaining: {remaining_gold}")

if remaining_gold > 50:
    print("You have plenty of gold.")
elif remaining_gold > 0:
    print("Funds are running low - spend wisely.")
else:
    print("You are broke! Seek a quest.")

party = ["Aldric the Knight", "Seraphine the Mage", "Torvin the Rogue"]
print(f"\nYour party has {len(party)} members:")

for member in party:
    print(f" - {member}")

#Add a new member to the party
party.append("Lyra the Healer")
print(f"\n{party[-1]} has joined the party!")

hero_stats = {
    "name": hero_name,
    "health": 100,
    "attack": 15,
    "defense": 8,
    "gold": remaining_gold
}

print(f"\n--- Hero Stats ---")
for stat, value in hero_stats.items():
    print(f" {stat}: {value}")