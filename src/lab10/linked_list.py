from __future__ import annotations

from typing import Any, Iterator, Optional


class Node:

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value: Any = value
        self.next: Optional[Node] = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next

        assert prev is not None
        new_node = Node(value, next=prev.next)
        prev.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            assert self.head is not None
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next

        assert prev is not None and prev.next is not None
        to_delete = prev.next
        prev.next = to_delete.next
        if to_delete is self.tail:
            self.tail = prev
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = ", ".join(repr(v) for v in self)
        return f"SinglyLinkedList([{values}])"