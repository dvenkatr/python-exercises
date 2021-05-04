'''
Refactored solution
'''


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


    def __repr__(self):
        return str(self.node_id) + " " + str(self.children)


def BuildTree(records):

    records.sort(key=lambda x : (x.parent_id, x.record_id))

    if records == []:
        return None

    if records[0].parent_id != records[0].record_id and records[0].record_id != 0:
        raise ValueError("Invalid tree")

    if records[-1].record_id != len(records) - 1:
        raise ValueError("Tree must be continuous")

    for r in records:
        if r.record_id == r.parent_id and r.record_id != 0:
            raise ValueError("Cyclic tree")

    # Create list of nodes
    tree = []
    for r in records:
        n = Node(r.record_id)
        tree.append(n)

    def find_child(tree, record):
        for child in tree:
            if child.node_id == record.record_id:
                return child

    # Populate children
    for node in tree:
        for record in records:
            if node.node_id == record.parent_id and record.record_id != 0:
                node.children.append(find_child(tree, record))

    return tree[0]


'''
Working solution provided that was to be refactored
'''

# def BuildTree2(records):
#     root = None
#     records.sort(key=lambda x: x.record_id)
#     ordered_id = [i.record_id for i in records]
#     if records:
#         if ordered_id[-1] != len(ordered_id) - 1:
#             raise ValueError('Tree must be continuous')
#         if ordered_id[0] != 0:
#             raise ValueError('Tree must start with id 0')
#     trees = []
#     parent = {}
#     for i in range(len(ordered_id)):
#         for j in records:
#             if ordered_id[i] == j.record_id:
#                 if j.record_id == 0:
#                     if j.parent_id != 0:
#                         raise ValueError('Root node cannot have a parent')
#                 if j.record_id < j.parent_id:
#                     raise ValueError('Parent id must be lower than child id')
#                 if j.record_id == j.parent_id:
#                     if j.record_id != 0:
#                         raise ValueError('Tree is a cycle')
#                 trees.append(Node(ordered_id[i]))
#     for i in range(len(ordered_id)):
#         for j in trees:
#             if i == j.node_id:
#                 parent = j
#         for j in records:
#             if j.parent_id == i:
#                 for k in trees:
#                     if k.node_id == 0:
#                         continue
#                     if j.record_id == k.node_id:
#                         child = k
#                         parent.children.append(child)
#     if len(trees) > 0:
#         root = trees[0]
#     return root