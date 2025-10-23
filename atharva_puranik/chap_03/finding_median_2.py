# Program for calculating medians in Python with Spyder 
# chapter 03 pg no. 64 -- math with python
# programmer - Atharva Puranik

# defining a function
def calculate_median(numbers):
    N = len(donations_list)
    numbers.sort()

    # find the median 
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        # if N is odd
        m2 = (N/2)+1
        # convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
        
    return median

if __name__ == '__main__':
    donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_median(donations_list)
    N = len(donations_list)

    print("Median donation over the last {0} days is {1}".format(N, mean))
