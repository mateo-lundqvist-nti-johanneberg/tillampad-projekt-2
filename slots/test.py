
import random

jackpot = "7 7 7 "
halfPot = ["<3 <3 <3 ", "BAR BAR BAR ", "BELL BELL BELL ", ">-8 >-8 >-8 ", "-O -O -O ", "D D D "]
money = 1000

slots = ["7 ", "<3 ", "BAR ", "BELL ", ">-8 ", "-O ", "D "]

slot1 = random.choice(slots)
slot2 = random.choice(slots)
slot3 = random.choice(slots)

final = slot1 + slot2 + slot3

print(final)

if final.split(" ")[0] == final.split(" ")[1] or final.split(" ")[1] == final.split(" ")[2]:
    print("halfpot")

if final == slots[0] + slots[0] + slots[0]:
    print("jackpot")



