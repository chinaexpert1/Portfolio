class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def calculate_probabilities(data):
    symbols = {}
    for element in data:
        symbols[element] = symbols.get(element, 0) + 1
    return symbols

def build_huffman_tree(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        left.code = '0'
        right.code = '1'

        merged_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.append(merged_node)

    return nodes[0]

def calculate_codes(node, val=''):
    codes = {}
    new_val = val + node.code

    if node.left:
        codes.update(calculate_codes(node.left, new_val))
    if node.right:
        codes.update(calculate_codes(node.right, new_val))

    if not node.left and not node.right:
        codes[node.symbol] = new_val

    return codes

# Define the input string
input_str = "Hello World"

# Calculate the probabilities
probabilities = calculate_probabilities(input_str)

# Create nodes for each symbol
nodes = [Node(freq, symbol) for symbol, freq in probabilities.items()]

#covert nodes to a list of tuples of the symbol and the freq and print the list here


# Build the Huffman tree
root = build_huffman_tree(nodes)

# Calculate the Huffman codes
huffman_codes = calculate_codes(root)
print("Huffman codes:", huffman_codes)

# Encode the input string
encoded_str = ''.join([huffman_codes[char] for char in input_str])
print("Encoded string:", encoded_str)
