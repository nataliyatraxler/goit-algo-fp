import networkx as nx
import matplotlib.pyplot as plt
import uuid
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def array_to_heap(array):
    nodes = [Node(val) for val in array]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def update_colors(node_list, cmap_name='viridis'):
    cmap = plt.get_cmap(cmap_name)
    norm = mcolors.Normalize(vmin=0, vmax=len(node_list) - 1)
    for idx, node in enumerate(node_list):
        rgba_color = cmap(norm(idx))
        hex_color = mcolors.to_hex(rgba_color)
        node.color = hex_color

def bfs(root):
    queue = [root]
    bfs_order = []
    while queue:
        node = queue.pop(0)
        if node:
            bfs_order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return bfs_order

def dfs(root):
    stack = [root]
    dfs_order = []
    while stack:
        node = stack.pop()
        if node:
            dfs_order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return dfs_order

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_data['color'] for node_id, node_data in tree.nodes(data=True)]
    labels = {node_id: node_data['label'] for node_id, node_data in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання
heap_array = [0, 4, 1, 5, 10, 3]
tree_root = array_to_heap(heap_array)

# Обхід у ширину
bfs_order = bfs(tree_root)
update_colors(bfs_order)
print("Обхід у ширину:")
draw_tree(tree_root)

# Обхід у глибину
dfs_order = dfs(tree_root)
update_colors(dfs_order)
print("Обхід у глибину:")
draw_tree(tree_root)
