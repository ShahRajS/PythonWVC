# Raj Shah     CIST-005B-72148

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node("4", None)
node2 = Node("-7", node1)
node3 = Node("34", node2)
