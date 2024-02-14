from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def build_freq_dict(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    return freq_dict


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda node: (len(node.char), node.char))

    def pop(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)


def build_huffman_tree(freq_dict):
    queue = PriorityQueue()
    for char, freq in sorted(freq_dict.items()):
        queue.insert(Node(char, freq))

    while len(queue) > 1:
        left = queue.pop()
        right = queue.pop()
        parent = Node(left.char + right.char, left.freq + right.freq)
        parent.left = left
        parent.right = right
        queue.insert(parent)

    return queue.pop()


def preorder_traversal(node, prefix="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}

    if node is not None:
        if len(node.char) == 1:
            huffman_codes[node.char] = prefix
        preorder_traversal(node.left, prefix + "0", huffman_codes)
        preorder_traversal(node.right, prefix + "1", huffman_codes)

    return huffman_codes


def huffman_encode(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)


text = "Hello World"
freq_dict = build_freq_dict(text)
huffman_tree = build_huffman_tree(freq_dict)
huffman_codes = preorder_traversal(huffman_tree)
encoded_text = huffman_encode(text, huffman_codes)

print("Huffman Codes:", huffman_codes)
print("Encoded Text:", encoded_text)
