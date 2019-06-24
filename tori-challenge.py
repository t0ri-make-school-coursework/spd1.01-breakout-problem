"""
Tori's Challenge:
Find the middle item in a singly linked list, 
or two middle items if it contains an even number of nodes.
"""

from linkedlist import LinkedList

def get_middle(ll):
    iterator = 0
    length = ll.size - 1
    node = ll.head # added this line
    
    while node is not None:
        if iterator == length // 2:
            if length % 2 == 0: # '== 1' to '== 0'
                return node.data
            next_node = node.next
            return (node.data, next_node.data)
        
        iterator += 1
        node = node.next

def main():
    linked_list_odd = LinkedList()
    for item in ['A', 'B', 'C']:
        linked_list_odd.append(item)
    print('Odd List: {}, returns one: {}'.format(linked_list_odd, get_middle(linked_list_odd)))

    linked_list_even = LinkedList()
    for item in ['A', 'B', 'C', 'D']:
        linked_list_even.append(item)
    print('Even List: {}, returns two: {}'.format(linked_list_even, get_middle(linked_list_even)))

if __name__ == "__main__":
    main()