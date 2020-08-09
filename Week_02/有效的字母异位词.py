# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s==None or t==None or s=="" or t=="":
            return False
        if len(s)!=len(t):
            return False
        else:
            s_dict={}
            t_dict={}
            for i in range(len(s)):
                if s_dict.get(s[i])==None:
                    s_dict[s[i]]=1
                else:
                    s_dict[s[i]]=s_dict.get(s[i])+1
                if t_dict.get(t[i])==None:
                    t_dict[t[i]]=1
                else:
                    t_dict[t[i]]=t_dict.get(t[i])+1
        for key in s_dict.keys():
            if s_dict.get(key)!=t_dict.get(key):
                return False
        return True