"""
Javier's Challenge:
Given a list of n numbers, determine if it contains any duplicate numbers.
"""

def check_duplicates(numbers):
    numbers_dict = dict()
    for number in numbers:
        if number in numbers_dict:
            return True
        numbers_dict[number] = 1
    return False


def main():
    test_cases = list()
    test_cases.append((True, [3, 11, 5, 9, 7, 5])) # normal true
    test_cases.append((False, [9, 2, 7, 15, 11, 4])) # normal false
    test_cases.append((False, [4, 6, 13, -4, 8, 1 ])) # pos/neg duplicates
    test_cases.append((True, [str, '', 2, '2', -0, float('inf'), '2'])) # edge cases etc

    for expected, test_case in test_cases:
        print('Test Case: ({}, {}) -- Result: {}'.format(test_case, expected, check_duplicates(test_case)))


if __name__ == "__main__":
    main()