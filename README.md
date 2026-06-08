# Обход бинарного дерева


## Описание задачи

Реализовать методы обхода произвольного бинарного дерева и вычислить некоторые его свойства.

**Выполненные пункты:**

`preorder` — прямой обход (DFS)
`inorder` — симметричный обход (DFS)
`postorder` — обратный обход (DFS)
`bfs` / `level_order` — обход в ширину по уровням (BFS)
**Задание 9** — диаметр дерева

---


### DFS-обходы

#### Прямой обход — `preorder`

```python
def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)           # 1. узел
        preorder(root.left, result)         # 2. левое поддерево
        preorder(root.right, result)        # 3. правое поддерево
    return result
```

#### Симметричный обход — `inorder`

```python
def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)          # 1. левое поддерево
        result.append(root.value)           # 2. узел
        inorder(root.right, result)         # 3. правое поддерево
    return result
```

> Для дерева поиска (BST) `inorder` возвращает значения в отсортированном порядке.

#### Обратный обход — `postorder`

```python
def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)        # 1. левое поддерево
        postorder(root.right, result)       # 2. правое поддерево
        result.append(root.value)           # 3. узел
    return result
```

---

### BFS-обход

#### Плоский список — `bfs`

```python
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
```

#### По уровням — `level_order`

Расширение `bfs`: перед каждой итерацией фиксируем размер очереди — это число узлов текущего уровня. Возвращает список списков.

```python
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
```

---

### Диаметр дерева (задание 9)

**Диаметр** — длина (в рёбрах) самого длинного пути между любыми двумя узлами. Путь не обязан проходить через корень.

**Ключевое наблюдение:** диаметр через узел `v` равен сумме высот его левого и правого поддеревьев:

```
diameter(v) = height(v.left) + height(v.right)
```

Алгоритм рекурсивно вычисляет высоту каждого узла и попутно обновляет максимум:

```python
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
```

> `max_diameter` обёрнут в список, чтобы вложенная функция `height` могла изменять его значение.

---

## Тестовые деревья

### Дерево 1 — несбалансированное

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

### Дерево 2 — симметричное

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

### Дерево 3 — вырожденное (цепочка)

```
    1
     \
      2
       \
        3
         \
          4
```

### Дерево 4 — длинное левое плечо

```
          1
         / \
        2   3
       /
      4
     /
    5
```

Ожидаемый диаметр: путь `5 → 4 → 2 → 1 → 3` = **4 ребра**.

---

## Результаты

### Дерево 1

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 4, 5, 3, 6]` |
| `inorder` | `[4, 2, 5, 1, 3, 6]` |
| `postorder` | `[4, 5, 2, 6, 3, 1]` |
| `bfs` | `[1, 2, 3, 4, 5, 6]` |
| `level_order` | `[[1], [2, 3], [4, 5, 6]]` |
| `diameter` | `4` |

### Дерево 2

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 3, 4, 2, 4, 3]` |
| `inorder` | `[3, 2, 4, 1, 4, 2, 3]` |
| `postorder` | `[3, 4, 2, 4, 3, 2, 1]` |
| `bfs` | `[1, 2, 2, 3, 4, 4, 3]` |
| `level_order` | `[[1], [2, 2], [3, 4, 4, 3]]` |
| `diameter` | `4` |

### Дерево 3

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 3, 4]` |
| `inorder` | `[1, 2, 3, 4]` |
| `postorder` | `[4, 3, 2, 1]` |
| `bfs` | `[1, 2, 3, 4]` |
| `level_order` | `[[1], [2], [3], [4]]` |
| `diameter` | `3` |

> У вырожденного дерева `preorder` и `inorder` совпадают — каждый узел имеет только правого потомка, поэтому левое поддерево всегда пусто.

### Дерево 4

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 4, 5, 3]` |
| `inorder` | `[5, 4, 2, 1, 3]` |
| `postorder` | `[5, 4, 2, 3, 1]` |
| `bfs` | `[1, 2, 3, 4, 5]` |
| `level_order` | `[[1], [2, 3], [4], [5]]` |
| `diameter` | `4` |
