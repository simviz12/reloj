"""
Implementación de Lista Circular Doblemente Enlazada.
Utilizada para gestionar los modos del reloj de manera bidireccional y circular.
"""

class Node:
    """Nodo de la lista con referencias al anterior y al siguiente."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    """
    Estructura de datos para navegación circular bidireccional.
    Ideal para selectores de modo (Reloj -> Alarma -> Crono -> Timer -> Reloj).
    """
    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def append(self, data):
        """Agrega un nuevo elemento a la lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    def next(self):
        """Avanza al siguiente nodo y lo retorna."""
        if self.current:
            self.current = self.current.next
            return self.current.data
        return None

    def prev(self):
        """Retrocede al nodo anterior y lo retorna."""
        if self.current:
            self.current = self.current.prev
            return self.current.data
        return None

    def get_current(self):
        """Retorna el dato del nodo actual."""
        if self.current:
            return self.current.data
        return None
