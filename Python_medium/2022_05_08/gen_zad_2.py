from datetime import datetime, timedelta


def date_start_end(start_date, end_date):
    moment_date = datetime(*start_date)
    while moment_date <= datetime(*end_date):
        yield moment_date.strftime('%Y %B %d')
        moment_date += timedelta(days=1)


date1983 = date_start_end([1983, 1, 1],[1983, 12, 31])

for date in date1983:
    print(date)