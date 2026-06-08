from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None



def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)           
        preorder(root.left, result)        
        preorder(root.right, result)       
    return result


def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result



def bfs(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result



def diameter_of_tree(root):

    max_diameter = [0]

    def height(node):
        if node is None:
            return 0
        left_h  = height(node.left)
        right_h = height(node.right)
        max_diameter[0] = max(max_diameter[0], left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter[0]


# ─────────────────────────────────────────────
# Вспомогательные функции вывода
# ─────────────────────────────────────────────

def print_section(title):
    print(f"\n{'═' * 50}")
    print(f"  {title}")
    print('═' * 50)

def print_tree_result(label, value):
    print(f"  {label:<30} {value}")


# ─────────────────────────────────────────────

def build_tree_1():

    root       = TreeNode(1)
    root.left  = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left  = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def build_tree_2():

    root       = TreeNode(1)
    root.left  = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left   = TreeNode(3)
    root.left.right  = TreeNode(4)
    root.right.left  = TreeNode(4)
    root.right.right = TreeNode(3)
    return root


def build_tree_3():

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    return root


def build_tree_4():

    root       = TreeNode(1)
    root.left  = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    return root


def run_tests(label, root):
    print_section(label)
    print_tree_result("Прямой обход (preorder):", preorder(root))
    print_tree_result("Симметричный (inorder):", inorder(root))
    print_tree_result("Обратный (postorder):", postorder(root))
    print_tree_result("BFS (плоский):", bfs(root))
    print_tree_result("Обход в ширину (по уровням):", "")
    for i, lvl in enumerate(level_order(root)):
        print(f"    Уровень {i}: {lvl}")
    print_tree_result("Диаметр дерева:", diameter_of_tree(root))



run_tests("Дерево 1 — несбалансированное", build_tree_1())
run_tests("Дерево 2 — симметричное", build_tree_2())
run_tests("Дерево 3 — вырожденное (цепочка)", build_tree_3())
run_tests("Дерево 4 — длинное левое плечо", build_tree_4())
print()
