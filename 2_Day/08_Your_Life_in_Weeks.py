age = input("what is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12

massage = f"You have {days_remaining} days, {weeks_remaining} weeks, {month_remaining} month"
print(massage)