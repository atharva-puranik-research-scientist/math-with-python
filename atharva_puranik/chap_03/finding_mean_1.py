# finding mean 
# chapter 03 pg no. 62 -- math with python
# programmer - Atharva Puranik

# defining a function
def calculate_mean(numbers):
    s = sum(donations_list)
    N = len(donations_list)

    # Mean formula
    mean = s/N

    return mean

if __name__ == '__main__':
    donations_list = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations_list)
    N = len(donations_list)

    print("Mean donation over the last {0} days is {1}".format(N, mean))
