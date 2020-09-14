def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

# Understand
 # test case given

# Plan
# Execute  
    # Set up hash table
    # key: number
    # value: boolean (list contains its negation)
    has_opp = {}

    # Set up result list
    result = []

    # Iterate through the nums
    for num in a:
        # Check if num is positive
        if num > 0:
            # If positive num is not in hash table
            if num not in has_opp:
                # then enter num key with False value
                has_opp[num] = False
            # If num is negative in hash
            if -num in has_opp:
                # change key -num value to True
                has_opp[-num] = True
                # change positive num value to True
                has_opp[num] = True
        else:
        # Otherwise iff negative
            # Check if negative num not in hash table
            if num not in has_opp:
                # then store entry with false
                has_opp[num] = False
            # If positive version is in hash table
            if abs(num) in has_opp:
                # Set its value to true
                has_opp[abs(num)] = True
                has_opp[num] = True

    # Iterate through the entries of num:boolean
    for num, boolean in has_opp.items():
        if boolean is True and num > 0:
            result.append(num)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
