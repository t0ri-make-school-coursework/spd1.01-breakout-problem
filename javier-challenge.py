"""
Javier's Challenge:
Given a list of n numbers, determine if it contains any duplicate numbers.
"""

# Whiteboard Implementation
dict = dict()
for elements in n:
    if dict[element] == element:
        return True
    else:
        dict[element] = element
return False
