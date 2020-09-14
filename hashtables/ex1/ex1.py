def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

# Understand
    # Test case given

# Plan     
# Execute
    # Create hash-tables for weights & their indexes
    hash_indexes = {} # {4:0, 6:1, 10:2, 15:3}

    # Iterate through the weights
    for i in range(length):
        # Check is weight value is not in the hash-table
        if weights[i] not in hash_indexes:
            # if not then store the indexes in the hash-tables
            hash_indexes[weights[i]] = i
        else:
            # Otherwise check if the weight equals itself minus the limit
            if limit - weights[i] == weights[i]:
                # Then return the current index & stored index
                return (i, hash_indexes[weights[i]])

        # Calculate the complement
        complement = limit - weights[i] # 17, 15, 11, 6

        # If the complement exits & is not equal to itself
        if complement in hash_indexes and complement != weights[i]:
            # Return the indexes of the weights, sorted in reverse order
            return sorted((hash_indexes[complement], hash_indexes[weights[i]]), reverse=True) #[3,1]

    # Return None if there is no pair that adds up to the limit
    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))