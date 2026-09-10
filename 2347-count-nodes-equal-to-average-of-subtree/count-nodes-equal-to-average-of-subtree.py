class Solution:
    def averageOfSubtree(self, root):
        
        def dfs(node):
            if node is None:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(node.left)
            right_sum, right_count, right_ans = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            ans = left_ans + right_ans

            if node.val == total_sum // total_count:
                ans += 1

            return total_sum, total_count, ans

        return dfs(root)[2]