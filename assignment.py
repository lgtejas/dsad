import sys

from base import Node  # Node is a datastructure which is child class of TreeNode
from inputs import read_inputs
from outputs import write_outputs


def solve_ps3(input):
    if not isinstance(input, list):
        raise ValueError('Invalid input , please input a valid array as input')
    elif len(input) <= 1:
        raise ValueError('Invalid input , please input a an array with size > 1')
    min_sum = sum(input)  # n
    stack = []
    pos = 0
    i = 0
    while len(input) > 1:
        i = input.index(min(input))  # n * n
        left = input[i - 1] if i > 0 else float("inf")
        right = input[i + 1] if i < len(input) - 1 else float("inf")
        p = input.pop(i)
        if pos == 0:
            stack.append(p)
        t = min(left, right) * p
        min_sum += t
        stack.append(min(left, right))
        stack.append(t)
        pos = pos + 1
    return min_sum, _build_tree(stack)


def _build_tree(stack):  # n * n
    i = 0
    root_node = None
    current_node = None
    while (len(stack) > 0):
        if i == 0:
            root_node = Node(stack.pop())
            current_node = root_node
        else:
            right = stack.pop()
            left = stack.pop()
            current_node.right = Node(right)
            current_node.left = Node(left)
            current_node = current_node.left
        i = i + 1
    return root_node


if __name__ == "__main__":
    inputs = read_inputs()
    if inputs is None:
        sys.exit(1)
    elif len(inputs) == 0:
        print('No inputs provided , please enter input values in inputPS3.txt')
        sys.exit(1)
    results = []
    result_format ="Minimum sum = {0}, inorder traversal = {1}"
    for index, input in enumerate(inputs):
        print(f'--------------- input [{index + 1}] -----------')
        print(f'Input = {input}')
        min_sum , root = solve_ps3(input)
        print(f'Minimum sum = {min_sum}')
        print(f'--------- inorder traversal ---------')
        print(root.inorder_traversal(root))
        results.append(result_format.format(min_sum,root.inorder_traversal(root)))
    write_outputs(results)
