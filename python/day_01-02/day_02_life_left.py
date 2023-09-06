age = input("What is your current age? ")

age=int(age)
day= (90*365) - age*365
week = (90*52) - age*52
month = (90*12) - age*12
print(f"You have {day} days, {week} weeks, and {month} months left.")