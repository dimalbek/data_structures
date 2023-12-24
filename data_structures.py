from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        self.array = [None] * capacity
        self.capacity = capacity

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """
        if 0 <= index < self.capacity:
            self.array[index] = value
        else:
            raise IndexError

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError


class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = []

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
        else:
            raise IndexError

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        if 0 <= index < len(self.array):
            del self.array[index]
        else:
            raise IndexError

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError


class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        node_to_add = Node(value)
        if self.head is None:
            self.head = node_to_add
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node_to_add

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        node_to_add = Node(value)
        if position == 0:
            self.head = node_to_add
            return
        last_node = self.head
        for it in range(position - 1):
            last_node = last_node.next
        node_to_add.next = last_node.next
        last_node.next = node_to_add

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        node_to_remove = self.head
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        while node_to_remove.next is not None:
            if node_to_remove.next.value == value:
                node_to_remove.next = node_to_remove.next.next
                return
            node_to_remove = node_to_remove.next

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        node_to_find = self.head
        if self.head is None:
            return None
        if self.head.value == value:
            return self.head
        while node_to_find is not None:
            node_to_find = node_to_find.next
            if node_to_find.value == value:
                return node_to_find
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        last_node = self.head
        counter = 0
        while last_node is not None:
            last_node = last_node.next
            counter += 1
        return counter

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        node_to_print = self.head
        while node_to_print is not None:
            print(node_to_print, end=" ")
            node_to_print = node_to_print.next

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        return tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        node_to_add = DoubleNode(value)
        if self.head is None:
            self.head = node_to_add
            self.tail = node_to_add
            return
        self.tail.next = node_to_add
        node_to_add.prev = self.tail
        self.tail = node_to_add

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        node_to_add = DoubleNode(value)
        if position == 0:
            if self.head is not None:
                node_to_add.next = self.head
                self.head.prev = node_to_add
            else:
                self.tail = node_to_add
            self.head = node_to_add
        else:
            current = self.head
            for it in range(position - 1):
                if current is None:
                    raise IndexError
                current = current.next
            node_to_add.next = current.next
            node_to_add.prev = current
            if current.next is not None:
                current.next.prev = node_to_add
            else:
                self.tail = node_to_add
            current.next = node_to_add

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        node_to_remove = self.head
        if node_to_remove is None:
            return

        if node_to_remove.value == value:
            self.head = node_to_remove.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        while node_to_remove.next:
            if node_to_remove.next.value == value:
                next_node = node_to_remove.next.next
                node_to_remove.next = next_node
                if next_node:
                    next_node.prev = node_to_remove
                else:
                    self.tail = node_to_remove
                return
            node_to_remove = node_to_remove.next

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        node_to_find = self.head
        if self.head is None:
            return None
        if self.head.value == value:
            return self.head
        while node_to_find is not None:
            node_to_find = node_to_find.next
            if node_to_find.value == value:
                return node_to_find
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        last_node = self.head
        counter = 0
        while last_node is not None:
            last_node = last_node.next
            counter += 1
        return counter

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        node_to_print = self.head
        while node_to_print is not None:
            print(node_to_print, end=" ")
            node_to_print = node_to_print.next

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        current = self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        return self.tail


class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            raise IndexError
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0


class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """
        node_to_add = TreeNode(value)
        if self.root is None:
            self.root = node_to_add
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node_to_add
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = node_to_add
                    return
                current = current.right
            else:
                return

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """
        parent = None
        current = self.root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        # 0 or 1 child
        if current.left is None or current.right is None:
            new_child = current.left if current.left else current.right
            if parent is None:  # root
                self.root = new_child
            elif parent.left == current:
                parent.left = new_child
            else:
                parent.right = new_child

        else:  # 2 children
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.value = successor.value

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """
        if self.root is None:
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    return
                current = current.right
            else:
                return current

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """

        def _inorder(node):
            if node is None:
                return []
            return _inorder(node.left) + [node.value] + _inorder(node.right)

        return _inorder(self.root)

    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return self._size(node.left) + self._size(node.right) + 1

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        return self.root is None

    def height(self) -> int:
        """
        Returns the height of the tree.
        """
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left = self._height(node.left)
        right = self._height(node.right)
        return max(left, right) + 1

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """

        def _preorder(node):
            if node is None:
                return []
            return [node.value] + _preorder(node.left) + _preorder(node.right)

        return _preorder(self.root)

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """

        def _postorder(node):
            if node is None:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.value]

        return _postorder(self.root)

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """
        if not self.root:
            return []
        queue, result = [self.root], []
        while queue:
            node = queue.pop(0)  # Note: pop(0) is less efficient than deque.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """
        current = self.root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
        current = self.root
        while current is not None and current.right is not None:
            current = current.right
        return current

    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """

        def _is_valid(node, min_val, max_val):
            if node is None:
                return True
            if (min_val is not None and node.value <= min_val) or (
                max_val is not None and node.value >= max_val
            ):
                return False
            return _is_valid(node.left, min_val, node.value) and _is_valid(
                node.right, node.value, max_val
            )

        return _is_valid(self.root, None, None)
