class TreeNode:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ''

char_codes = dict()

def compute_char_codes(node, value=''):
    new_value = value + str(node.code)

    if node.left:
        compute_char_codes(node.left, new_value)
    if node.right:
        compute_char_codes(node.right, new_value)

    if not node.left and not node.right:
        char_codes[node.char] = new_value

    return char_codes

def compute_probabilities(data):
    char_freq = dict()
    for element in data:
        if char_freq.get(element) == None:
            char_freq[element] = 1
        else:
            char_freq[element] += 1
    return char_freq

def encode_output(data, codes):
    encoded_output = []
    for c in data:
        encoded_output.append(codes[c])

    encoded_str = ''.join([str(item) for item in encoded_output])
    return encoded_str

def compression_gain(data, codes):
    before_compression = len(data) * 8
    after_compression = 0
    symbols = codes.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(codes[symbol])
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):", after_compression)

def huffman_encoding(data):
    char_freq = compute_probabilities(data)
    chars = char_freq.keys()

    tree_nodes = []

    for char in chars:
        tree_nodes.append(TreeNode(char_freq.get(char), char))

    while len(tree_nodes) > 1:
        tree_nodes = sorted(tree_nodes, key=lambda x: x.freq)

        right_node = tree_nodes[0]
        left_node = tree_nodes[1]

        left_node.code = 0
        right_node.code = 1

        merged_node = TreeNode(left_node.freq + right_node.freq, left_node.char + right_node.char, left_node, right_node)

        tree_nodes.remove(left_node)
        tree_nodes.remove(right_node)
        tree_nodes.append(merged_node)

    huffman_codes = compute_char_codes(tree_nodes[0])
    print("Characters with codes:", huffman_codes)
    compression_gain(data, huffman_codes)
    encoded_str = encode_output(data, huffman_codes)
    return encoded_str, tree_nodes[0]

def huffman_decoding(encoded_data, huffman_tree):
    tree_root = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.char == None and huffman_tree.right.char == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.char)
            huffman_tree = tree_root

    decoded_str = ''.join([str(item) for item in decoded_output])
    return decoded_str
