#MODULE 13 OF 30 Days of python programming
#Exercises - Module 13 Python Datetime Exercises

from datetime import datetime
now =datetime.now()
print(now)

now = datetime.now()
format_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(format_now)

time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y")

print(time_object)

now = datetime.now()
new_year = datetime(year=now.year + 1, month=1, day=1)
time_difference = new_year - now
print(f"Time difference until New Year: {time_difference}")

epoch_start = datetime(1970, 1, 1)
now = datetime.now()
time_difference = now - epoch_start
print(f"Time difference between 1 January 1970 and now: {time_difference}")