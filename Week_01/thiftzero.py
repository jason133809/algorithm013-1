class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0 #替换下标从0开始
        for i in range(len(nums)):
            if nums[i]!=0:  #遍历数组 如果第一次碰到不为0的值，交换位置 
                nums[j],nums[i]=nums[i],nums[j]
                print(nums[j],nums[i])
                j=j+1 #替换下标加1 便于存储第二次交换的值
        return nums