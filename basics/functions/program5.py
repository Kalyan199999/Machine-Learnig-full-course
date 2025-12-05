import statistics

def mean_median_mode(numbers):

    mean = statistics.mean(numbers)

    median = statistics.median(numbers)

    mode = statistics.mode(numbers)

    return mean, median, mode

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

mean, median, mode = mean_median_mode(numbers)

print(f"Mean: {round(mean,2)}\nMedian:{median}\nMode: {mode}")

cor  = statistics.correlation( [1,2,3,4] , [1,4,9,16])
print(cor)

corr = statistics.correlation( [1,2,3,4] , [16,9,4,1])
print(corr)

corr = statistics.correlation( [1,2,3,4] , [5,1,20,10])
print(corr)