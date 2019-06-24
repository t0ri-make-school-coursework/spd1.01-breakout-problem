"""
Tori's Challenge:
Find the middle item in a singly linked list, 
or two middle items if it contains an even number of nodes.
"""

# Whiteboard Implementation
iterator = 0
length = self.size - 1
mid = length // 2

while node is not None:
    if iterator == mid:
        if length % 2 == 1:
            return node.data
        next_node = node.next
        return (node.data, next_node.data)
    
    iterator += 1
    node = node.next
