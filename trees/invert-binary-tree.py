def invert_tree(root):
     if not root.left and not root.right:
          return
     
     temp = root.left
     root.left = root.right
     root.right = temp
     return