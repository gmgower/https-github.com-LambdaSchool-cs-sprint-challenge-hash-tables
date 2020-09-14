def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

# Understand
    # Test case given

# Plan 
   # Create hash-tables for weights & their indexes
   # Iterate through the weights
    # Check is weight value is not in the hash-table
    # if not then store the indexes in the hash-tables
   # Otherwise check if the weight equals itself minus the limit
    # Then return the current index & stored index

    # Calculate the complement
    #complement = limit - weights[i]

    # If the complement exits & is not equal to itself
    # Return the indexes of the weights, sorted in reverse order

    # Return None if there is no pair that adds up to the limit
    
# Execute
    hash_indexes = {} # {4:0, 6:1, 10:2, 15:3}

    for i in range(length):
        if weights[i] not in hash_indexes:
            hash_indexes[weights[i]] = i
        else:
            if limit - weights[i] == weights[i]:
                return (i, hash_indexes[weights[i]])

        complement = limit - weights[i] # 17, 15, 11, 6

        if complement in hash_indexes and complement != weights[i]:
            return sorted((hash_indexes[complement], hash_indexes[weights[i]]), reverse=True) #[3,1]

    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))