charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"

charge += 35.00

if numChars > 5:
    extraChars = numChars - 5
    charge += extraChars * 4.00

if woodType == "oak":
    charge += 20.00

if color == "gold":
    charge += 15.00

print(f"The charge for this sign is ${charge}.")
