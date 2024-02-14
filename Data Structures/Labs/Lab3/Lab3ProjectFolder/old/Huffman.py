class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = None

    def __str__(self):
        return f"{self.symbol}: {self.freq} ({self.code})"


def calculate_frequency(data):
    frequency = {}
    for symbol in data:
        if symbol not in frequency:
            frequency[symbol] = 0
        frequency[symbol] += 1
    return frequency


def print_tree(node):
    if node is None:
        return
    print(str(node))
    print_tree(node.left)
    print_tree(node.right)


def build_huffman_tree(data):
    frequencies = calculate_frequency(data)
    nodes = [Node(freq, symbol) for symbol, freq in frequencies.items()]
    nodes = sorted(nodes, key=lambda x: (x.freq, x.symbol))

    while len(nodes) > 1:
        left = nodes[0]
        right = nodes[1]

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)
        nodes = sorted(nodes, key=lambda x: (x.freq, x.symbol))

    return nodes[0]


def huffman_encoding(node, code=''):
    if node is None:
        return

    if node.left is None and node.right is None:
        node.code = code

    huffman_encoding(node.left, code + '0')
    huffman_encoding(node.right, code + '1')


def print_encoding(data, tree):
    encoding = {}
    huffman_encoding(tree)

    def fill_encoding(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            encoding[node.symbol] = node.code
        fill_encoding(node.left)
        fill_encoding(node.right)

    fill_encoding(tree)

    encoded_data = ''
    for symbol in data:
        if symbol != ' ':
            encoded_data += encoding[symbol]

    print(f"\nString to encode: {data}")
    print('\nEncoding of string ignoring spaces:')
    print(encoded_data)


data = "Hello World"
tree = build_huffman_tree(data)
print("Huffman tree printed with preorder traversal:")
print_tree(tree)
print_encoding(data, tree)
