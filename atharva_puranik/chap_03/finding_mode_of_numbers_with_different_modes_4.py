# finding mode of numbers list with multiple modes
# chapter 03 pg no. 68 -- math with python
# programmer - Atharva Puranik


from collections import Counter

# defining a function to calculate mode(s)
def calculate_mode(scores_list):
    
    # count how many times each number appears in the list
    c = Counter(scores_list)
    scores_list_freq = c.most_common() # retrives all numbers with their frequencies
    # find the maximum frequency (the highest count) 
    max_count = scores_list_freq[0][1]

    modes = []
    # check which numbers have the same count as the maximum
    for num in scores_list_freq:
        if num[1] == max_count:
            modes.append(num[0]) # add those number to the list of modes

    return modes

if __name__ == '__main__':
    scores_list =  [5, 5, 5, 4, 4, 4, 9, 1, 3]
    modes = calculate_mode(scores_list)

    print('The mode(s) of the list of numbers are: ')
    # iterate over the returned list and print each mode
    for mode in modes:
        print(mode)
