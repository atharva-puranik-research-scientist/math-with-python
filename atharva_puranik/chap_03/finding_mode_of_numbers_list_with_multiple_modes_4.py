# finding mode 
# chapter 03 pg no. 67 -- math with python
# programmer - Atharva Puranik


from collections import Counter

# defining a function
def calculate_mode(scores_list):
    c = Counter(scores_list)
    mode = c.most_common(1)

    return mode[0][0]

if __name__ == '__main__':
    scores_list =  [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores_list)

    print('The mode of the list of numbers is" {0}'.format(mode))
