day = int(input("Enter today's day (sunday is 0..,saturday is 6): "))
future_day = int(input("Enter the number of days elapsed since today: "))
new_day = ""
number = day + future_day

if day == 0:
    day = "Sunday"
if number % 7 == 0:
    new_day = "Sunday"
if day == 1:
    day = "Monday"

if number % 7 == 1:
    new_day = "Monday"
if day == 2:
    day = "Tuesday"
if number % 7 == 2:
    new_day = "Tuesday"
if day == 3:
    day = "Wednesday"
if number % 7 == 3:
    new_day = "Wednesday"
if day == 4:
    day = "Thursday"
if number % 7 == 4:
    new_day = "Thursday"
if day == 5:
    day = "Friday"
if number % 7 == 5:
    new_day = "Friday"
if day == 6:
    day = "Saturday"
if number % 7 == 6:
    new_day = "Saturday"

print("Today is", day, "and the future day is", new_day)
