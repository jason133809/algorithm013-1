#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
 
        s = list(range(1, n + 1))
        return list(combinations(s, k))

# @lc code=end

