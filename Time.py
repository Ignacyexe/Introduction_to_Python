import time

print(time.ctime(0))  # converts a time expressed in seconds since epoch to a readable string

# epoch - when your computer thinks time began (reference point)

print(time.time())   # return current seconds since epoch
print(time.ctime(time.time()))
print()
print(time.gmtime())   # UTC time

time_object = time.localtime()   # local time
print(time_object)

local_time = time.strftime("%d %B %Y %H:%M:%S", time_object)
print(local_time)

print()

# year, month, day, hours, minutes, seconds, day of the week, day of the year, dst
time_tuple = (2020, 4, 20, 12, 0, 0, 0, 0, 0)
time_str = time.asctime(time_tuple)
print(time_str)

time_tuple = (2020, 4, 20, 12, 0, 0, 0, 0, 0)
time_str = time.mktime(time_tuple)
print(time_str)
