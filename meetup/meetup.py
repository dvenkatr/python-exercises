import datetime
import calendar

def meetup(year, month, week, day_of_week):
    
    ordinals = {
        '1st' : 0,
        '2nd' : 1,
        '3rd' : 2,
        '4th' : 3,
        '5th' : 4,
    }

    day_name = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 
        'Sunday'
            ]

    delta = 1
    nth = 0

    if week == 'teenth':
        start_day = 13
    elif week == 'last':
        start_day = calendar.monthrange(year, month)[1]
        delta = -1
    else:
        start_day = 1
        nth = ordinals[week]

    while(True):
        try:
            date_guess = str(start_day) + " " + str(month) + " " + str(year)
            day_guess = datetime.datetime.strptime(date_guess, '%d %m %Y').weekday()
            if day_name[day_guess] == day_of_week:
                return datetime.date(year, month, start_day + 7 * nth)
            start_day +=delta
        except Exception:
            raise MeetupDayException()


class MeetupDayException(Exception):
    
    def __init__(message):
        super().__init__("No such date exists")