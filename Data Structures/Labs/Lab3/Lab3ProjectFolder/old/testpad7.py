# Define the input string
input_str = "Hello World"

# Define the frequency dictionary
freq_dict = {}
for char in input_str:
    freq_dict[char] = freq_dict.get(char, 0) + 1

print(freq_dict)

class TreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.value}, {self.freq})"

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
        merged_node = TreeNode(None, freq_1 + freq_2)
        merged_node.left = min_1 if isinstance(min_1, TreeNode) else TreeNode(min_1, freq_1)
        merged_node.right = min_2 if isinstance(min_2, TreeNode) else TreeNode(min_2, freq_2)
        freq_dict[merged_node] = merged_node.freq

        del freq_dict[min_1]
        del freq_dict[min_2]

    return next(iter(freq_dict.values()))

# Building the binary tree using Huffman encoding
root = build_huffman_tree(freq_dict.copy())

print(root)

# Function to print the tree in a preorder traversal
def preorder_traversal(node):
    if node is None or isinstance(node, int):
        return []

    return [node] + preorder_traversal(node.left) + preorder_traversal(node.right)

# Print the tree using preorder traversal
tree = preorder_traversal(root)
print(tree)
