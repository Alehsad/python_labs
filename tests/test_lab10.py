from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def main() -> None:
    print("=== Stack ===")
    stack = Stack()
    print("Пустой?", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("После push 1,2,3:", stack)
    print("peek():", stack.peek())
    print("pop():", stack.pop())
    print("После pop:", stack)
    print("Длина стека:", len(stack))

    print("\n=== Queue ===")
    queue = Queue()
    print("Пустая?", queue.is_empty())
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    print("После enqueue a,b,c:", queue)
    print("peek():", queue.peek())
    print("dequeue():", queue.dequeue())
    print("После dequeue:", queue)
    print("Длина очереди:", len(queue))

    print("\n=== SinglyLinkedList ===")
    lst = SinglyLinkedList()
    print("Пустой список:", lst, "len =", len(lst))

    lst.append(10)
    lst.append(20)
    lst.prepend(5)
    print("После append(10), append(20), prepend(5):", lst, "len =", len(lst))

    lst.insert(1, 15)
    print("После insert(1, 15):", lst, "len =", len(lst))

    lst.remove_at(2)
    print("После remove_at(2):", lst, "len =", len(lst))

    print("Итерирование по списку:", list(lst))


if __name__ == "__main__":
    main()
