# 0416_이진트리의 구현 _ 탐색
# 이진트리는 노드값, 왼쪽 노드,오른쪽 노드 총 3가지로 구성.
# https://geonlee.tistory.com/72 를 참조하였다.
# https://geonlee.tistory.com/78?category=318965 또한 참조하였다.

class Node(object):
    # 1단계. 각 노드의 초기화.
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# 이진 탐색 트리의 구현

class BinarySearchTree(object):
    # 최초의 시작 노드는 없다
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None  # 왜 is not None 을 했는가?

    def _insert_value(self, node, data):
        # 노드가 없을 경우 노드를 생성한다.
        if node is None:
            node = Node(data)
        # 노드가 있을 경우 작으면 왼쪽, 크면 오른쪽에 삽입
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left,data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 원하는 값의 존재 유뮤를 확인하고자 한다.
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:  # 왼쪽으로 비비고
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # 삭제
    # 자식이 없다면 그냥 없애면 무관.
    # 자식이 하나일 경우, 자식을 끌고온다.
    # 자식이 둘이면, 없앤 위치에서 나뉜 두개의 서브트리 중
    # 우측 트리의 가장 작은 값을 끌고 와야 대소 순서가 맞는다.

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right :  # 양 측의 자식 존재
                parent, child = node, node.right  # 부모, 자식 지정
                while child.left is not None:  # 왼쪽이 있으면 더 가야해서
                    parent, child = child, child.left  # leftmost까지 감
                child.left = node.left  # 71줄에서, 왼쪽은 그대로 둘거고
                if parent != node: # 오른쪽을 나머지 반쪽으로 끌고올거라서.
                    parent.left = child.right
                    child.right = node.right
                node = child  # 그렇게 노드를 새로지정

            elif node.left or node.right:  # 한 측만 자식 존재
                node = node.left or node.right # 그거 데려옴

            else:
                node = Node
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    # 트리의 순회
    # 1. 깊이 우선 순회 : 전위, 중위 후휘
    # Depth First Traversal

    # 전위 순회 : Root > 좌측 > 우측 순서로 순회

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    # 정위 순회 : 좌측 > Root > 우측 순서로 순회

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)
    # 이 경우, 정렬된 데이터를 얻는다.

    # 후위 순회 : 좌측 > 우측 > Root 순서로 순회

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)


    # 2. 너비 우선 탐색
    # root부터 level단위별 탐색

    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)

array = [30, 21, 13, 29, 46, 38, 57, 10, 99, 68, 27]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)

bst.pre_order_traversal() # 30 21 13 10 29 27 46 38 57 99 68
bst.in_order_traversal() # 10 13 21 27 29 30 38 46 57 68 99
bst.post_order_traversal() # 10 13 27 29 21 38 68 99 57 46 30
bst.level_order_traversal() # 30 21 46 13 29 38 57 10 27 99 68