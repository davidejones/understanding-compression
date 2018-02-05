from collections import Counter


class Node(object):
    def __init__(self, value=None, probability=None):
        self.left = None
        self.right = None
        self.value = value
        self.probability = probability

    def get(self):
        return self.value

    def __repr__(self):
        return '<Node {}, {}>'.format(self.value, self.probability)


def build_tree(probabilities):
    q = []
    # create a leaf node for each symbol add to queue
    for char, count in probabilities.items():
        q.append(Node(char, count))
    q.sort(key=lambda t: t.probability)
    # while there is more than one node in the queue
    while len(q) > 2:
        # remove the 2 nodes of highest priority / lowest probability from the queue
        item_1, item_2 = q[0:2]
        q = q[2:]
        # create a new internal node with these 2 nodes as children and add to the queue
        internal_node = Node(None, item_1.probability + item_2.probability)
        internal_node.left = item_1
        internal_node.right = item_2
        # add the new node to the queue
        q.append(internal_node)
        # resort the "priority" queue
        q.sort(key=lambda t: t.probability)
    # the remaining node is the root node and the tree is complete
    root = Node()
    root.left = q[0]
    root.right = q[1]
    q = [root]
    return q


def walk_tree(node, prefix="", code={}):
    if node.value is None:
        walk_tree(node.left, prefix + "0", code)
    else:
        code[node.value] = prefix + "0"
    if node.value is None:
        walk_tree(node.right, prefix + "1", code)
    else:
        code[node.value] = prefix + "1"
    return code


def encode(data):
    output = ''
    # Calculate probability for all symbols
    probabilities = Counter(data)
    # Assign codewords to symbols based upon their probability, more frequent symbols are assigned smaller codewords
    tree = build_tree(probabilities)
    # assign each symbol a code
    root = tree.pop()
    code_words = walk_tree(root)
    # Walk through the data set when you encode a symbol output tits codeword to the compressed bit stream
    for c in data:
        output += code_words[c]
    return output


def decode():
    pass
