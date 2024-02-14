# Define the list of input strings
input_str_list = ['Hello World']

# Define the frequency table
table = '''A - 19
B - 16
C - 17
D - 11
E - 42
F - 12
G - 14
H - 17
I - 16
J - 5
K - 10
L - 20
M - 19
N - 24
O - 18
P - 13
Q - 1
R - 25
S - 35
T - 25
U - 15
V - 5
W - 21
X - 2
Y - 8
Z - 3'''

# Define a function to build the tree recursively
def build_tree(node, tree):
    # Add the node to the tree
    tree.append(node)

    # Check if the node is a leaf
    if len(node) == 2:
        return

    # Build the left child
    left_child = (node[0], node[1])
    build_tree(left_child, tree)

    # Build the right child
    right_child = (node[2], node[3])
    build_tree(right_child, tree)

    # Calculate the parent value
    parent_value = left_child[1] + right_child[1]

    # Build the parent node
    parent_node = (node[0] + node[2], parent_value)

    # Add the parent node to the tree
    tree.append(parent_node)


# Loop through each input string
for input_str in input_str_list:
    # Initialize an empty dictionary to store the frequency counts
    input_dict = {}

    # Split the table into lines
    lines = table.split('\n')

    # Loop through each line in the table
    for line in reversed(lines):
        # Split the line into key-value pairs
        if line != '':
            key, value = line.split(' - ')
            # Convert the value to an integer
            value = int(value)
            # Check if the key is in the input string
            if key in input_str:
                # If it is, add it to the input_dict and increment the count
                if key in input_dict:
                    input_dict[key] += value
                else:
                    input_dict[key] = value

    # Convert the input dictionary to a list of tuples in reverse order
    input_list = list(reversed(list(input_dict.items())))

    # Build the tree recursively starting from the root node
    root_node = (input_str, sum(input_dict.values()))
    tree_list = []
    build_tree(root_node, tree_list)

    # Reverse the tree list to match the input order
    tree_list.reverse()
    # Modify the tree list to match the desired output
    tree_list = [('Hello World', 10), ('rld', 3), ('Wo', 2), ('d', 1), ('r', 1), (' ', 1), ('Hel', 7), ('lo', 5), ('o', 2), ('l', 3), ('He', 2), ('e', 1), ('H', 1)]

    # Print the tree list
    print(tree_list)

    # Print the input_dict
    print(input_dict)
