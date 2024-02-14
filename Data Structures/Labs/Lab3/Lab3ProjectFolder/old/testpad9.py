class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

def min_frequency_nodes(freq_dict):
    min_1, min_2 = None, None
    freq_1, freq_2 = float('inf'), float('inf')

    for key, value in freq_dict.items():
        if value < freq_1:
            min_2, freq_2 = min_1, freq_1
            min_1, freq_1 = key, value
        elif value < freq_2:
            min_2, freq_2 = key, value

    return min_1, freq_1, min_2, freq_2

def build_huffman_tree(freq_dict):
    while len(freq_dict) > 1:
        min_1, freq_1, min_2, freq_2 = min_frequency_nodes(freq_dict)

        left_node = Node(freq_1, min_1) if isinstance(min_1, str) else min_1
        right_node = Node(freq_2, min_2) if isinstance(min_2, str) else min_2
        merged_node = Node(freq_1 + freq_2, (left_node.symbol) + (right_node.symbol), left_node, right_node)

        freq_dict[merged_node] = merged_node.freq

        del freq_dict[min_1]
        del freq_dict[min_2]

    return next(iter(freq_dict.keys()))

# Define the input string
input_str = "Hello World"

# Define the frequency dictionary
freq_dict = {}
for char in input_str:
    freq_dict[char] = freq_dict.get(char, 0) + 1

# Building the binary tree using Huffman encoding
root = build_huffman_tree(freq_dict.copy())

# Function to print the tree in a preorder traversal
def preorder_traversal(node):
    if node is None:
        return []

    if node.symbol is not None:
        return [(node.symbol, node.freq)]

    left = preorder_traversal(node.left)
    right = preorder_traversal(node.right)

    return [(node.symbol, node.freq)] + left + right

# Print the tree using preorder traversal
tree = preorder_traversal(root)
print(tree)
