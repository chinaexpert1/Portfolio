# Open the "FreqTable.txt" file in read mode
with open('FreqTable.txt', 'r') as f:
    # Read the contents of the file
    table = f.read()
print('Frequency Table from file:')
print(table)
print('\n')

def parse_table(table):
    table_lines = table.split('\n')
    table_dict = {}

    for line in table_lines:
        if line != '':
            symbol, value = line.split(' - ')
            table_dict[symbol] = value

    return table_dict

table = parse_table(table)
my_dict = table
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
table = sorted_dict

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        if isinstance(freq, str) and freq.isdigit():
            freq = int(freq)
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = None

    def __str__(self):
        return f"{self.symbol}: {self.freq} ({self.code})"


    def __str__(self):
        return f"{self.symbol}: {self.freq} ({self.code})"


def __str__(self):
    return f"{self.symbol}: {self.freq} ({self.code})"



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

    # Return the sorted array
    return array



def build_huffman_tree(table):
    print('Huffman Tree Report:')
    frequencies = table
    print('Dictionary of frequencies:')
    print(frequencies)
    print('\n')
    nodes = [Node(freq, symbol) for symbol, freq in frequencies.items()]
    print('Collection of nodes without codes yet:')
    for i in nodes:
        print(i)
    print('\n')
    nodes = insertion_sort(nodes)
    print('Nodes sorted according to frequency, alphabetically breaking ties:')
    print(nodes)
    for i in nodes:
        print(i)
    print('\n')
    internalnodes =[]

    # Assemble nodes into leaves of internal nodes
    while len(nodes) > 0:

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        nodes.remove(right)
        nodes.remove(left)
        internalnodes.append(newNode)

        # Return the root node of the final tree, nodes populated in left and right children

    print('internal nodes: ')
    for i in internalnodes:
        print(i)
    print('\n')
    print('leaves:')
    for i in internalnodes:
        print('   ', i.right)
        print('   ', i.left)

    # assemble internal nodes into the whole tree
    internalnodes = insertion_sort(internalnodes)
    print('internal nodes after sorting:')
    print('internal nodes: ')
    for i in internalnodes:
        print(i)
    print('\n')
    while len(internalnodes) > 1:

        # pick 2 smallest nodes
        right = internalnodes[0]
        left = internalnodes[1]

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        internalnodes.remove(right)
        internalnodes.remove(left)
        internalnodes.append(newNode)

    print(internalnodes)
    return internalnodes[0]


def huffman_encoding(node, code=''):
    if node is None:
        return
    if node.left is None and node.right is None:
        node.code = code
    huffman_encoding(node.left, code + '0')
    huffman_encoding(node.right, code + '1')



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
    print('\n')
    print('Decoding Report:')
    print('\n')
    root = build_huffman_tree(table)
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


def print_tree(root):
    if not root:
        return

    # Get the height of the tree
    height = get_height(root)

    # Calculate the number of nodes in the last level
    last_level = [root]
    for i in range(height - 1):
        level = []
        for node in last_level:
            if node:
                level.append(node.left)
                level.append(node.right)
            else:
                level.append(None)
                level.append(None)
        last_level = level

    # Calculate the maximum width of any node value
    max_width = len(str(max([node.freq for node in last_level if node])))

    # Print the tree
    for i in range(height):
        level = get_level(root, i)
        spacing = ' ' * (2 ** (height - i) * max_width - max_width)
        print(spacing.join(str(x.freq) if x else ' ' * max_width for x in level))
    print('\n')
    for i in range(height):
        level = get_level(root, i)
        spacing = ' ' * (2 ** (height - i) * max_width - max_width)
        print(spacing.join(str(x.symbol) if x else ' ' * max_width for x in level))

def get_height(node):
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def get_level(node, level):
    if not node:
        return []
    if level == 0:
        return [node]
    left = get_level(node.left, level - 1)
    right = get_level(node.right, level - 1)
    return left + right


data = "HELLOWORLD"
tree = build_huffman_tree(table)
encoded_data = huffman_encode(data, tree)
encoding_table = print_encoding(tree)
print(encoding_table)
print('\n')
print("Original Data:", data)
print("Encoded Data:", encoded_data)
print("Decoded Data:", huffman_decode(encoded_data, encoding_table))
