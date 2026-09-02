dice = [
    """
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘
""",

    """
┌─────────┐
│ ●       │
│         │
│       ● │
└─────────┘
""",

    """
┌─────────┐
│ ●       │
│    ●    │
│       ● │
└─────────┘
""",

    """
┌─────────┐
│ ●     ● │
│         │
│ ●     ● │
└─────────┘
""",

    """
┌─────────┐
│ ●     ● │
│    ●    │
│ ●     ● │
└─────────┘
""",

    """
┌─────────┐
│ ●     ● │
│ ●     ● │
│ ●     ● │
└─────────┘
"""
] 
import random
total = 0
num_dice = int(input("How many dice do you want to roll? "))
for i in range(num_dice):
    roll = random.choice(dice)
    print(roll)
    total += dice.index(roll) + 1

print(f"Total: {total}")  