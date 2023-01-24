# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    i = 0
    def serialize(self, root):
        stack = []
        def dfs(root):
            if not root:
                stack.append("*")
                return
            stack.append(str(root.val))
            stack.append(",")
            dfs(root.left)
            dfs(root.right)
        dfs(root)        
        return "".join(stack)

    def deserialize(self, data):
        def dfs(data):
            if self.i == len(data):
                return
            if data[self.i] == "*":
                self.i+=1
                return None
            num = ""
            while data[self.i]!=",":
                num+=data[self.i]
                self.i+=1
            val = int(num)
            self.i+=1
            node = TreeNode(val)
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))