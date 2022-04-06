from datetime import datetime

def is_weekday():
    date_today = datetime.today()
    # 0 - Monday, 6 - Sunday
    day_of_week = date_today.weekday()
    if day_of_week <=4:
        return True
    return False

print(is_weekday())