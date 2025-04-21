# Input
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Kalkulasi
total_with_tip = bill * (1 + tip_percent / 100)
total_per_person = total_with_tip / people

# Output dengan 2 digit desimal
print(f"Each person should pay: ${total_per_person:.2f}")
