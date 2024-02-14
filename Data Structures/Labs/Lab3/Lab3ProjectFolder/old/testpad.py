# Define the input string
input_str = "Hello World"

# Define the frequency dictionary
freq_dict = {}
for char in input_str:
    freq_dict[char] = freq_dict.get(char, 0) + 1


def merge_nodes(a, b):
    return (a, b)


def min_frequency_nodes(freq_dict):
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1])
    min_1, freq_1 = sorted_items[0]
    min_2, freq_2 = sorted_items[1]

    return min_1, freq_1, min_2, freq_2


def build_tree(freq_dict):
    while len(freq_dict) > 1:
        min_1, freq_1, min_2, freq_2 = min_frequency_nodes(freq_dict)
        merged_node = merge_nodes(min_1, min_2)
        freq_dict[merged_node] = freq_1 + freq_2

        del freq_dict[min_1]
        del freq_dict[min_2]

    return next(iter(freq_dict.keys()))


def huffman_codes(tree, prefix=''):
    if isinstance(tree, str):
        return {tree: prefix}

    left, right = tree
    codes = {}
    codes.update(huffman_codes(left, prefix + '0'))
    codes.update(huffman_codes(right, prefix + '1'))
    return codes

finaldict = freq_dict.copy()
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

print(finaldict)