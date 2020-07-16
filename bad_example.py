from datetime import datetime

# Bad example of writing testable code

def get_time_of_day():
    '''Returns time of day (morning, afternoon, night, evening)'''

    now = datetime.now().time()

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


# Why is this bad?
# datetime.now().time() is a hidden input that is impossible to test
# calls to this function will produce different results
# Tied to concrete data source - not reusable for other sources
# violates Single Responsibility Principle - it consumes and processes
# lies about the information - should know where the sources is coming from (hidden inputs)
# Hard to predict and maintain - depends on a mutable global state 