def add_time(start, duration, day=''):

    # split the start time and duration into separate variables for easier calculation.
    # split start time and denomination
    start_time, start_denomination = start.split()
    # further split start time into hours and minutes
    start_time_hour, start_time_minutes = start_time.split(':')
    # split duration into hour and minutes
    duration_hour, duration_minutes = duration.split(':')

    # converted all the hours and minutes into integer for calculation
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)
    start_time_hour = int(start_time_hour)
    start_time_minutes = int(start_time_minutes)

    # added time_denomination for comparison later.
    # added counter that check how many times the hours go past 12 [both AM and PM]
    # set initial day_changed = False. This is used to check if the time shifts from PM to AM
    # no_of_days keeps count of how many times it turns from PM to AM
    time_denomination = ['AM', 'PM']
    denomination_change_counter = 0
    day_changed = False
    no_of_days_passed = 0

    # variable that is to be returned
    new_time = ''

    # loop through the duration hour. Add 1 to start hour. If reaches 12, check if its the last value, if yes keep as 12
    # else, change hour to 0 and start again.
    # denomination counter +1 everything it reaches to 12.
    for hour in range(duration_hour):
        start_time_hour += 1

        if start_time_hour == 12:
            if hour == (duration_hour - 1):
                start_time_hour = 12
            else:
                start_time_hour = 0

            denomination_change_counter += 1

    # loop through duration minutes. add 1 to minutes. when minutes reach 60, sets it back to 0 and adds 1 to hour.
    # if the hour addition goes to 12, add 1 denomination counter.
    for minutes in range(duration_minutes):
        start_time_minutes += 1

        if start_time_minutes == 60:
            start_time_minutes = 0
            start_time_hour += 1

            if start_time_hour == 12:
                denomination_change_counter += 1

    # used to changed AM to PM or vice versa. when changes occur, sets day_changed to True.
    # if the counter % 2 is 0, then no change. this means it switched from AM -> PM -> AM.
    # else, change it. if AM -> PM. if PM -> AM.
    if denomination_change_counter >= 1:
        if denomination_change_counter % 2 == 0:
            day_changed = True
        else:
            if start_denomination == time_denomination[0]:
                start_denomination = time_denomination[1]
            else:
                start_denomination = time_denomination[0]
                day_changed = True





    return new_time