from datetime import datetime

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    time_format = "%H:%M"
    
    car_total_times = {}
    car_in_times = {}
    
    for record in records:
        time, car_num, in_out = record.split(" ")

        if in_out == "IN":
            car_in_times[car_num] = datetime.strptime(time, time_format)
        
        else:
            if car_num not in car_total_times:
                car_total_times[car_num] = (datetime.strptime(time, time_format) - car_in_times[car_num])
            else:
                car_total_times[car_num] += (datetime.strptime(time, time_format) - car_in_times[car_num])
            
            del car_in_times[car_num]
    
    for car_num, time in car_in_times.items():
        if car_num not in car_total_times:
            car_total_times[car_num] = (datetime.strptime("23:59", time_format) - time)
        else:
            car_total_times[car_num] += (datetime.strptime("23:59", time_format) - time)

    car_fees = []
    
    for car_num, total_time in car_total_times.items():
        total_minute = total_time.seconds // 60
        
        if total_minute <= base_time:
            car_fees.append([car_num, base_fee])
        
        else:            
            additional_time = (total_minute - base_time) // unit_time
            if (total_minute - base_time) % unit_time != 0:
                additional_time += 1
            
            total_fee = base_fee + additional_time * unit_fee

            car_fees.append([car_num, total_fee])
    
    car_fees.sort(key=lambda x: x[0])
    answer = [x[1] for x in car_fees]   

    return answer