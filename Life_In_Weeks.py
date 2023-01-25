age = input("What is your current age? ")

timeLeft = 90 - int(age)
months = timeLeft * 12
weeks = timeLeft * 52
days = timeLeft * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
