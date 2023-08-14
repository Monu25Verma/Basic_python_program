def convert_days(days):
    years = (days // 365)
    weeks = (days % 365) // 7
    days = (days % 365) % 7
    return f"{years}years {weeks}weeks and {days}days"


print(convert_days(500))