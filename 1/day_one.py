def main():
    print(get_highest_cal_elf(3))

def get_highest_cal_elf(amount):
    with open('day_one_input.txt') as f:
        lines = f.readlines()

    totalCalorieSums = [0] * amount
    currentCalorieSum = 0
    min, min_index = get_min(totalCalorieSums)

    for line in lines:
        if len(line.strip()) == 0:
            if currentCalorieSum > min:
                totalCalorieSums[min_index] = currentCalorieSum
                min, min_index = get_min(totalCalorieSums)
            currentCalorieSum = 0
        else:
            currentCalorieSum += int(line)
    
    return get_sum(totalCalorieSums)


def get_min(array):
    min = array[0]
    index = 0

    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
            index = i
    
    return min, index

def get_sum(array):
    sum = 0
    for line in array:
        sum += line
    return sum

if __name__=="__main__":
    main()