from good_example import get_time_of_day
from datetime import timedelta

class SmartHomeController:
    last_motion_time = datetime.now()

    def actuate_lights(motion_detected, time=datetime.now):

        if motion_detected:
            last_motion_time = time

        time_of_day = get_time_of_day(time)

        if motion_detected and (time_of_day == 'Evening' or time_of_day == 'Night'):
            backyard_light_switcher.turn_on()

        elif (last_motion_time - time) > timedelta(minutes=1) or time_of_day == 'Morning' or time_of_day == 'Noon':
            backyard_light_switched.turn_off()