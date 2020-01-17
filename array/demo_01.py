"""
    给定一个{排序}数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在{原地}修改输入数组并在使用 O(1) 额外空间的条件下完成。

    分析
    1. 数组以排序
    2. O(1) 的空间复杂度 -- 变量所分配的空间不随着处理数据量变化

"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old_len = len(nums)  # 原地删除元素后数组长度会发生变化 故在此记录原始长度
        flag = 0  # 记录删除元素的个数
        for i in range(old_len):
            i -= flag
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    del nums[i]
                    flag += 1
                else:
                    pass
            else:
                return old_len - flag

