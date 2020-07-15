from datetime import datetime

# Better example of writing testable code

def get_time_of_day(now = datetime.now().time()):
    '''Returns time of day (morning, afternoon, night, evening)'''

    if now.hour >= 0 and now.hour < 6:
        return 'Night'

    if now.hour >= 6 and now.hour < 12:
        return 'Morning'

    if now.hour >= 12 and now.hour < 18:
        return 'Afternoon'
    
    return 'Evening'


if __name__ == '__main__':
    current_time = get_time_of_day()
    print(current_time)


# Input isn't hidden - shows that this function takes in datetime format
