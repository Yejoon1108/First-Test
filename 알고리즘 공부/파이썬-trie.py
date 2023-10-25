class Node:
    def __init__(self,data):
        self.left=None
        self.right = None
        self.data = data
#          10
#        /    \
#       34      89
#     /    \
#    45    50

root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


#Post-order traversal의 경우 왼쪽 노드와 오른쪽
#노드에서 재귀를 수행 한 다음 동일한 노드를 세 번째로 방문하면 해당 노드를 인쇄합니다.
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

#순서 내 순회(inorder)
#두번 거치면 print를 하는 방식
#일단 차례대로 쭉 내려가서, 재귀를 한다.
#left가 없기때문에 위로 올라오는 형식
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
#선주문 선회(preorder)
#순서대로 왼쪽으로 쭉 내려갔다가, 반대로 재귀를함
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)



postorder(root)

from anytree import Node, RenderTree

root = Node(10)

level_1_child_1 = Node(34, parent=root)
level_1_child_2 = Node(89, parent=root)
level_2_child_1 = Node(45, parent=level_1_child_1)
level_2_child_2 = Node(50, parent=level_1_child_2)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))



