playerName = input("Enter player name: ")
strength = input("Enter strength (0-100): ")
endurance = input("Enter endurance (0-100): ")
charisma = input("Enter charisma (0-100): ")

maxCarryWeight = float(strength) * 2.3
hitPoints = 100 + int(endurance)
convinceSomeone = 0.5 + ((float(charisma)/200.0))
print("Player name: ", playerName)
print("Maximum weight: ", "%.2f" % maxCarryWeight)
print("Hit points: ", int(hitPoints))
print("Convincing probability: " + "%.0f" % float(convinceSomeone*100) + "%")
