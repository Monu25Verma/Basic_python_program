#min to hours
# 1 hr = 60 min
# i min  = 60 sec

def min_to_hours(hr, min):
    hours = (hr * 60)
    minute = (min / 60)
    print(hr, "hours is =", hours, "min")
    print(min, "minute is =", format(minute, '.1f'), "hrs")


min_to_hours(5, 200)

