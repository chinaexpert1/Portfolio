# Define the input string
input_str = "Hello World"

# Define the frequency dictionary
freq_dict = {}
for char in input_str:
    freq_dict[char] = freq_dict.get(char, 0) + 1


# Define a function to build the tree recursively
def build_tree(freq_dict):
    # Check if only one element left
    if len(freq_dict) == 1:
        return next(iter(freq_dict.items()))

    # Find the two characters with the smallest frequencies
    min_freq_1 = min(freq_dict, key=freq_dict.get)
    min_val_1 = freq_dict.pop(min_freq_1)

    min_freq_2 = min(freq_dict, key=freq_dict.get)
    min_val_2 = freq_dict.pop(min_freq_2)

    # Build the subtree with the two minimum frequency characters
    subtree = (min_freq_1, min_freq_2)
    subtree_freq = min_val_1 + min_val_2

    # Add the subtree back into the frequency dictionary
    freq_dict[subtree] = subtree_freq

    # Continue building the tree recursively
    return build_tree(freq_dict)


def huffman_codes(tree, prefix=''):
    if isinstance(tree, str):
        return {tree: prefix}

    left, right = tree
    codes = {}
    codes.update(huffman_codes(left, prefix + '0'))
    codes.update(huffman_codes(right, prefix + '1'))
    return codes


# Build the tree recursively
tree = build_tree(freq_dict.copy())

# Generate the Huffman code for each character
huffman_dict = huffman_codes(tree)

# Encode the input string using the Huffman code
encoded_str = ''.join(huffman_dict[char] for char in input_str)

# Print the encoded string
print(encoded_str)

# Print the full tree
print(tree)
