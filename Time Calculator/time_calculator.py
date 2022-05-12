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





    return new_time