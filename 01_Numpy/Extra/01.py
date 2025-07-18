import numpy as np

def date_array0(start, end):
    return np.arange(start,end ,dtype="datetime64[D]")

def date_array1(start, end):

    total_days_of_month = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    
    end = end.split('-')
    end_date = int(end[-1]) + 1

    if total_days_of_month[end[-2]] < end_date:
        end_date = end_date - total_days_of_month[end[-2]]

        end[-2] = f"0{int(end[-2]) + 1}" if int(end[-2])  < 9 else int(end[-2])

    end[-1] = f"0{end_date}" if end_date < 10 else end_date
    print(end)
    end= '-'.join(end)
    print(end)
    # print(type(end))
    return np.arange(start,end ,dtype="datetime64[D]")

def date_array2(start, end):
    # Add one day to end date to make it inclusive
    end_plus_one = np.datetime64(end) + np.timedelta64(1, 'D')
    print(end_plus_one)
    print(np.datetime64(end) , np.timedelta64(4, 'D'))
    print(np.datetime64(end) , np.timedelta64(4, 'D'))
    print(np.datetime64(end) , np.timedelta64(4, 'M'))
    # print(np.datetime64(end) + np.datetime64(4, 'Y'))      #ERROR
    # Generate the range
    return np.arange(np.datetime64(start), end_plus_one, dtype='datetime64[D]')

print(date_array0(start='2025-01-01',end ='2025-02-04'))
print(date_array1(start='2025-01-01',end ='2025-02-04'))
print(date_array2(start='2025-12-01', end='2025-12-31'))