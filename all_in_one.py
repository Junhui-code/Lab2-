def display_main_menu():
    print("display main menu")

def get_user_input():
    temp = input("Enter some temperature values: ")
    temp = temp.split()
    temp = [float(x) for x in temp]
    return temp

def calc_average(temperatures):
    sum = 0
    for temp in temperatures:
        sum += temp   
    average = sum / len(temperatures)
    return average
    
def find_min_max(temperature):
    min = temperature[0]
    max = temperature[0]
    for temp in temperature:
        if temp < min:
            min = temp
        if temp > max:
            max = temp
    return min, max

def sort_temperature(tempera):
    tempera.sort()
    return tempera

def cal_median_temperature(tempe):
    a = len(tempe)
    median = 0
    if a % 2 == 0:
        median = (tempe[int(a//2)] + tempe[int((a//2)-1)]) / 2
    else:
        median = tempe[int(a/2)]
    return median

temperaturess = get_user_input()

average = calc_average(temperaturess)

min, max = find_min_max(temperaturess)

sorted_temperatures = sort_temperature(temperaturess)

median = cal_median_temperature(sorted_temperatures)


print("\nMinimum temperature:", min)
print("\nMaximum temperature:", max)
print("\nMedian temperature:", median)
print("\nAverage temperature:", average)


