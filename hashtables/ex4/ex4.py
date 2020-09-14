def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

# Understand
 # test case given

# Plan
    # Set up hash table
    # key: number
    # value: boolean (list contains its negation)
    
    # Set up result list

    # Iterate through the nums
     # Check if num is positive
      # If positive num is not in hash table
       # then enter num key with False value
      # If num is negative in hash
        # change key -num value to True
         # change positive num value to True
     # Otherwise iff negative
      # Check if negative num not in hash table
        # then store entry with false
      # If positive version is in hash table
        # Set its value to true

    # Iterate through the entries of num:boolean

# Execute  
    has_opp = {}

    result = []

    for num in a:
        if num > 0:
            if num not in has_opp:
                has_opp[num] = False
            if -num in has_opp:
                has_opp[-num] = True
                has_opp[num] = True
        else:
            if num not in has_opp:
                has_opp[num] = False
            if abs(num) in has_opp:
                has_opp[abs(num)] = True
                has_opp[num] = True

    for num, boolean in has_opp.items():
        if boolean is True and num > 0:
            result.append(num)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
