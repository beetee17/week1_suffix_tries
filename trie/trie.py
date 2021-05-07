#Uses python3
import sys
from collections import defaultdict
# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    """The trie has a single root node with in degree 0, denoted root. Each edge of Trie(Patterns) is labeled with a letter of the alphabet. Edges leading out of a given node have distinct labels. Every string in patterns is spelled out by concatenating the letters along some path from the rootdownward. Every path from the root to a leaf, or node with outdegree 0, spells a string from Patterns"""
    
    # initialise root node in tree
    tree = {0 : {}}

    for pattern in patterns:

        curr_node_id = 0
        curr_node = tree[curr_node_id]

        for i in range(len(pattern)):

            curr_symbol = pattern[i]

            # there is an outgoing edge from curr_node with label curr_symbol
            if curr_symbol in curr_node:
                
                # go to this node and search next symbol
                curr_node_id = curr_node[curr_symbol]
                curr_node = tree[curr_node_id]

            else:
                
                # add a new node to the trie
                new_node_id = len(tree)
                
                tree.update({new_node_id : {}})

                # add a new edge from the current node to this new node with the label of curr_symbol
                curr_node.update({curr_symbol : new_node_id})

                # go to the new node and search next symbol
                curr_node_id = new_node_id
                curr_node = tree[curr_node_id]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
