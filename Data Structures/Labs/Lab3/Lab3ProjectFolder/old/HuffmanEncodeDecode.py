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


def insertion_sort(array):
    # Loop through array starting from second element
    for i in range(1, len(array)):
        # Store current element and initialize index variable
        key_item = array[i]
        j = i - 1

        # Compare current element with elements to its left
        while j >= 0 and array[j].freq > key_item.freq:
            # Shift elements to the right to make room
            array[j + 1] = array[j]
            j -= 1

        # Insert current element in correct position
        array[j + 1] = key_item

    li = []
    s = array
    l = len(s)
    for i in range(l):
        li.append(s[i])

    for i in range(l):
        for j in range(i + 1, l):
            if li[j].freq == li[i].freq and li[i].symbol > li[j].symbol:
                li[i], li[j] = li[j], li[i]

    j = ""
    for i in range(l):
        j += li[i].symbol

    # Return the sorted array
    return li


def build_huffman_tree(data):
    print('Huffman Tree Report:')
    frequencies = calculate_frequency(data)
    print('Dictionary of frequencies:')
    print(frequencies)
    print('\n')
    nodes = [Node(freq, symbol) for symbol, freq in frequencies.items()]
    print('Collection of nodes:')
    for i in nodes:
        print(i)
    print('\n')
    nodes = insertion_sort(nodes)
    print('Nodes sorted according to frequency, alphabetically breaking ties:')
    for i in nodes:
        print(i)
    print('\n')

    while len(nodes) > 1:
        left = nodes[0]
        right = nodes[1]

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)
        nodes = sorted(nodes, key=lambda x: (x.freq, ord(x.symbol[0])))

    return nodes[0]


def huffman_encoding(node, code=''):
    if node is None:
        return
    if node.left is None and node.right is None:
        node.code = code
    huffman_encoding(node.left, code + '0')
    huffman_encoding(node.right, code + '1')


def build_tree_from_table(table):
    if not table:
        return None

    root = Node(0, '')
    for symbol, code in table.items():
        current_node = root
        for bit in code:
            if bit == '0':
                if current_node.left is None:
                    current_node.left = Node(0, '')
                current_node = current_node.left
            elif bit == '1':
                if current_node.right is None:
                    current_node.right = Node(0, '')
                current_node = current_node.right
        current_node.symbol = symbol
    return root


def huffman_encode(data, tree):
    huffman_encoding(tree)
    print("Huffman Tree used for encoding:")
    print_tree(tree)
    print('\n')
    encoding = {}

    def fill_encoding(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            encoding[node.symbol] = node.code
        fill_encoding(node.left)
        fill_encoding(node.right)

    fill_encoding(tree)

    encoded_data = ''.join([encoding[symbol] for symbol in data])
    return encoded_data



    encoded_data = ''.join([encoding[symbol] for symbol in data])
    return encoded_data


def huffman_decode(encoded_data, table):
    root = build_tree_from_table(table)
    huffman_encoding(root)
    print("Huffman Tree used for decoding:")
    print_tree(root)

    decoded_data = ''
    current_node = root

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.symbol
            current_node = root

    return decoded_data


def print_encoding(tree):
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
    return encoding

def print_tree(node, indent=''):
    if node is None:
        return
    print_tree(node.right, indent + '   ')
    print(indent, node)
    print_tree(node.left, indent + '   ')



data = "helloworld"
tree = build_huffman_tree(data)
encoded_data = huffman_encode(data, tree)
encoding_table = print_encoding(tree)
print("Original Data:", data)
print("Encoded Data:", encoded_data)
print("Decoded Data:", huffman_decode(encoded_data, encoding_table))
