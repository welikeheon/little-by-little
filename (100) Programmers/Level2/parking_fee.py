import math

def minute_conversion(enter, out):
    enter_hour, enter_min = map(int, enter.split(':'))
    out_hour, out_min = map(int, out.split(':'))
    
    hour_diff = (out_hour - enter_hour) * 60
    min_diff = out_min - enter_min
    return hour_diff + min_diff

def solution(fees, records):
    answer = []
    total_time = dict()
    enter_time = dict()
    cars = []
    
    # calculate the time difference in minutes
    for r in records:
        time, number, action = r.split()
        diff = 0
        if action == 'IN':  # if went in
            enter_time[number] = time   # record the enter time
        else:   # if went out,
            # diff of current and recorded enter time
            diff = minute_conversion(enter_time[number], time)  
            enter_time.pop(number)  # as the car went out from the parking lot
            total_time[number] = total_time.get(number, 0) + diff
        if number not in total_time:
            cars.append(number)
    
    # remaining cars which did not went out
    for key, val in enter_time.items():
        diff = minute_conversion(enter_time[key], "23:59")
        total_time[key] = total_time.get(key, 0) + diff
    
    # fee calculate
    cars.sort()
    for car in cars:
        amount = int(fees[1])
        base_subtracted = total_time[car] - fees[0]
        if base_subtracted > 0:
            amount += math.ceil(base_subtracted/int(fees[2])) * int(fees[3])
        answer.append(amount)
    
    return answer

    