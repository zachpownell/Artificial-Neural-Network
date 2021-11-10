import random
import string

class Node:

    def __init__(self):

        self.children = []

        # Set a random name. This is just to OUTPUT out. Use whatever name you want.
        self.node_name = ''.join(random.choice(string.ascii_letters) for i in range(3))
        self.children_connection_weights = []

    def make_children(self, current_layer, nodes_per_layer_map):

        # Recursion end condition
        if current_layer == len(nodes_per_layer_map):
            return

        # Create the children FOR this node
        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())

        # First born :D
        first_born = self.children[0]

        # Connect our first child
        first_born.make_children(current_layer + 1, nodes_per_layer_map)

        # Copy the connections from first child to each child
        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]

    def adjust_child_weights(self):

        # Recursion end condition
        if len(self.children) == 0:
            return

        self.children_connection_weights = []

        # Yup... at this stage... just set random

        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0, 1))

            # Recurse
            self.children[i].adjust_child_weights()

    def print_children(self, layer):

        # Just used to indent per level
        indent = '    ' * layer

        # Recursion end case
        if len(self.children) == 0:
            print(f"{indent}{self.node_name}")
            return

        print(f"{indent}{self.node_name} is connected to ")

        for i in range(len(self.children)):
            self.children[i].print_children(layer+1)

            # output the weight IF we have it
            if i < len(self.children_connection_weights):
                print(f"{indent} with weight {self.children_connection_weights[i]}")

# Create a master node that we can use to connect to all the layers


input_nodes = []
master_node = Node()

# Make our first node
my_first_node = Node()

# Make all the children FOR the first node

my_first_node.make_children(1, ['1234'])

master_node.children.append(my_first_node)

# Duplicate the first node FOR all INPUT nodes

for i in range(1, len(['1234'])):

    new_node = Node()

    # Copy the children to the new node
    new_node.children = my_first_node.children[:]
    master_node.children.append(new_node)

# OUTPUT out to see IF we are all connected
master_node.print_children(0)
print("!! Set Weights !!")

# init the weights
master_node.adjust_child_weights()

# OUTPUT out with weights
master_node.print_children(0)
