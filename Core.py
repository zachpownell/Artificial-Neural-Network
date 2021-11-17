import random
import string

NODE_COUNT_PER_LAYER = [4, 3, 2]

# We will use these random human names for our children.
RANDOM_NAMES = ["Zach", "Paul", "Everett", "Christina", "Ryan", "Jenna", "Kayla", "Hannah", "Ivy", "Shane", "Sammi",
                "Chris", "Tyler", "Steve", "Nikki", "Taylor", "Pedro", "Luis", "Vincent", "Mark", "Connor", "Bob"]

class Node:

    # Constructor function for Node.
    def __init__(self):

        # Assigning Node's children to an empty list.
        self.children = []

        # Random name generator used to set node names.
        self.node_name = ''.join(RANDOM_NAMES[random.randrange(len(RANDOM_NAMES))])

        # Assign children connection weights to an empty list.
        self.children_connection_weights = []


    # make_children function to create children for the Node.
    def make_children(self, current_layer, nodes_per_layer_map):

        # Check to see if current_layer parameter is equal to the length of nodes_per_layer_map. If so, end recursion.
        if current_layer == len(nodes_per_layer_map):
            return

        # Otherwise, lets first create the children for this node.
        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())

        # Assigning first born to children at index 0.
        first_born = self.children[0]

        #
        first_born.make_children(current_layer + 1, nodes_per_layer_map)

        # Copy the connections from first child to each child
        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]


    # adjust_child_weights function to assign weights to children.
    def adjust_child_weights(self):

        # Check to see if the length of children is 0. If so, end condition
        if len(self.children) == 0:
            return

        # Assign children_connect_weights to an empty list.
        self.children_connection_weights = []

        # We'll assign all the children's weights to random numbers between 0-1000.
        for i in range(len(self.children)):
            self.children_connection_weights.append(random.randint(0, 1000))

            # Recurse.
            self.children[i].adjust_child_weights()


    # print_children function to print out our family to the console.
    def print_children(self, layer):

        # Use this to indent and make the output look pretty.
        indent = '    ' * layer

        # Recursion end case
        if len(self.children) == 0:
            print(f"{indent}{self.node_name}")
            return

        print(f"{indent}{self.node_name} is connected to ")

        for i in range(len(self.children)):
            self.children[i].print_children(layer+1)

            # Output the weight if we have it.
            if i < len(self.children_connection_weights):
                print(f"{indent} with weight {self.children_connection_weights[i]}")


# input_nodes = []

# Create a master node that we can use to connect to all the layers
master_node = Node()

# Create our first node.
my_first_node = Node()

# Make all the children for the first node.
my_first_node.make_children(1, NODE_COUNT_PER_LAYER)

master_node.children.append(my_first_node)

# Duplicate the first node for all input nodes.
for i in range(0, len(NODE_COUNT_PER_LAYER)):

    new_node = Node()

    # Copy the children to the new node.
    new_node.children = my_first_node.children[:]
    master_node.children.append(new_node)

# Lets output to see if we are all connected.
master_node.print_children(0)
print("!! Set Weights !!")

# Cool, we are all connected. Lets initialize weights.
master_node.adjust_child_weights()

# Output out with weights.
master_node.print_children(0)
