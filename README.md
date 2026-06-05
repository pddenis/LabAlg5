# Обход бинарного дерева

## Описание задачи

Реализовать различные методы обхода произвольного бинарного дерева (не обязательно дерева поиска) и вычислить некоторые его свойства.

**Выполненные пункты:**

-  `preorder` — прямой обход
-  `inorder` — симметричный обход
-  `postorder` — обратный обход
-  `level_order` — обход в ширину (BFS) по уровням
-  **Задание 9** — диаметр дерева

---


## Реализация

### Класс TreeNode

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
```

Стандартный узел бинарного дерева с полями значения и ссылками на левого и правого потомков.

---

### Обязательная часть

#### Прямой обход — `preorder`

Порядок посещения: **корень → левое поддерево → правое поддерево**.

```python
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

#### Симметричный обход — `inorder`

Порядок посещения: **левое поддерево → корень → правое поддерево**.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

> Для дерева поиска (BST) `inorder` возвращает значения в отсортированном порядке.

#### Обратный обход — `postorder`

Порядок посещения: **левое поддерево → правое поддерево → корень**.

```python
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

#### Обход в ширину — `level_order`

Использует очередь (`deque`). Возвращает **список уровней**, где каждый уровень — отдельный список.

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
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

---

### Вариативная часть — задание 9

#### Диаметр дерева — `diameter_of_tree`

**Диаметр** — длина (в рёбрах) самого длинного пути между двумя узлами дерева. Путь не обязан проходить через корень.

**Ключевое наблюдение:** диаметр через произвольный узел `v` равен сумме высот его левого и правого поддеревьев:

```
diameter(v) = height(v.left) + height(v.right)
```

Алгоритм рекурсивно вычисляет высоту каждого узла, попутно обновляя глобальный максимум:

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

> `max_diameter` обёрнут в список, чтобы вложенная функция `height` могла изменять его значение (аналог `nonlocal`).

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
| `level_order` | `[[1], [2, 3], [4, 5, 6]]` |
| `diameter` | `4` |

### Дерево 2

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 3, 4, 2, 4, 3]` |
| `inorder` | `[3, 2, 4, 1, 4, 2, 3]` |
| `postorder` | `[3, 4, 2, 4, 3, 2, 1]` |
| `level_order` | `[[1], [2, 2], [3, 4, 4, 3]]` |
| `diameter` | `4` |

### Дерево 3

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 3, 4]` |
| `inorder` | `[1, 2, 3, 4]` |
| `postorder` | `[4, 3, 2, 1]` |
| `level_order` | `[[1], [2], [3], [4]]` |
| `diameter` | `3` |

> У вырожденного дерева `preorder` и `inorder` совпадают — это ожидаемо, так как у каждого узла есть только правый потомок.

### Дерево 4

| Метод | Результат |
|---|---|
| `preorder` | `[1, 2, 4, 5, 3]` |
| `inorder` | `[5, 4, 2, 1, 3]` |
| `postorder` | `[5, 4, 2, 3, 1]` |
| `level_order` | `[[1], [2, 3], [4], [5]]` |
| `diameter` | `4` |

---

## Анализ сложности

| Функция | Время | Память |
|---|---|---|
| `preorder` | O(n) | O(h) |
| `inorder` | O(n) | O(h) |
| `postorder` | O(n) | O(h) |
| `level_order` | O(n) | O(w) |
| `diameter_of_tree` | O(n) | O(h) |

- **n** — количество узлов дерева
- **h** — высота дерева (O(log n) для сбалансированного, O(n) для вырожденного)
- **w** — максимальная ширина дерева (максимальное число узлов на одном уровне)

Все функции обходят каждый узел ровно один раз, поэтому временная сложность линейна во всех случаях.
