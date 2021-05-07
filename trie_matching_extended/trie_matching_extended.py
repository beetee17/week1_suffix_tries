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

	# initialise root node in trie
	trie = {0 : {}}

	for pattern in patterns:

		curr_node_id = 0
		curr_node = trie[curr_node_id]

		for i in range(len(pattern)):

			curr_symbol = pattern[i]

			# there is an outgoing edge from curr_node with label curr_symbol
			if curr_symbol in curr_node:
				
				if i == len(pattern) - 1:

					curr_node[curr_symbol][1] = True

				# go to this node and search next symbol
				curr_node_id = curr_node[curr_symbol][0]
				curr_node = trie[curr_node_id]

			else:
	
				# add a new node to the trie
				new_node_id = len(trie)
	
				trie.update({new_node_id : {}})

				# add a new edge from the current node to this new node with the label of curr_symbol
				curr_node.update({curr_symbol : [new_node_id, None]})

				if i == len(pattern) - 1:

					# the current symbol is the end of the pattern, flag that this node should be seen as a root					
					curr_node[curr_symbol][1] = True

				else:

					curr_node[curr_symbol][1] = False

					# go to the new node and search next symbol
					curr_node_id = new_node_id
					curr_node = trie[curr_node_id]

	return trie

def prefix_trie_matching(text, trie):

	"""The goal in this problem is to extend the algorithm from the previous problem such that it will be able to handle cases when one of the patterns is a prefix of another pattern. In this case, some patterns are spelled in a trie by traversing a path from the root to an internal vertex, but not to a leaf"""

	i = 0
	v = 0

	while True:

		if not trie[v]:

			return text[0:v]


		if i < len(text):

			if text[i] in trie[v]:

				if trie[v][text[i]][1]:
					# the current node was flagged as a root (a patten match was found)
					return text[0:v]

				v = trie[v][text[i]][0]
				i += 1

				if i == len(text) and not trie[v]:
					return text[0:v]

			else:
				return 'no match'

		else:
			return 'no match'


def solve(text, trie):

    i = 0
    matches = []

    while text:
        # print(text)
        match = prefix_trie_matching(text, trie)

        if match != 'no match':
            matches.append((i, i + len(match)-1))

        i += 1
        text = text[1:]
    
    return matches

        

if __name__ == '__main__':
	data = sys.stdin.read().split()

	text = data[0]

	patterns = data[2:]

	trie = build_trie(patterns)

	matches = solve(text, trie)

	print(' '.join([str(match[0]) for match in matches]))
    
