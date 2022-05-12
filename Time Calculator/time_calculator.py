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

    # dictionary to check the days that is passed in and to accordingly change the day to pass out.
    # added appropriate range list to be used in loop.
    # a current day index to store the index of day that is passed in.
    # convert the passed in day argument to lowercase to keep consistency.
    days_in_a_week = {1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday', 7:'sunday'}
    days_in_a_week_index = range(1,8)
    current_day_index = 0
    day = day.lower()
    new_day = ''

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
    
    # calculates the number of days passed using the denomination counter.
    # its divide by 2 because in a day, there's 2 denomination in a day.
    no_of_days_passed = denomination_change_counter/2

    # converts the no of days passed into whole integer.
    no_of_days_passed_whole_number = int(no_of_days_passed)
    # obtains the remaining decimal value to determine the rounding off.
    no_of_days_passed_decimals = no_of_days_passed - no_of_days_passed_whole_number

    # if the remaining decimal value calculated above is 0.5 or more, the no_of_days_passed_whole_number is increased by 1.
    if no_of_days_passed_decimals >= 0.5:
        no_of_days_passed_whole_number += 1

    # convert start hour and minute to string.
    start_time_hour = str(start_time_hour)
    start_time_minutes = str(start_time_minutes)

    # check the length of minutes. If it's not 2, then add a leading 0
    if len(start_time_minutes) != 2:
        start_time_minutes = "0" + start_time_minutes


    if day:
        # loop through the index of the days and uses it as key value for dictionary
        # compares day argument with dictionary. if found, sets the index to current_day_index.
        for day_index in days_in_a_week_index:
            if days_in_a_week[day_index] == day:
                current_day_index = day_index
                break

        # loop through the no of days passed range. add 1 to the current_day_index
        # if the current_day_index reaches 8, it sets to 1 [meaning set back to monday index]
        for days_passed in range(no_of_days_passed_whole_number):
            current_day_index += 1
            if current_day_index == 8:
                current_day_index = 1

        # sets the new day based on the current day index
        new_day = days_in_a_week[current_day_index]





    return new_time