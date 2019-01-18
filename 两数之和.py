# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 时间复杂度O(n^2)
# nums = [3,6,3]
# target = 6
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

def getstrindex(str):
    maxnum = 0
    num = 0
    str_ = ''
    for i in str:
        if i not in str_:
            num += 1
            str_ += i
        else:
            if num > maxnum:
                maxnum = num
            index = str_.index(i)
            str_ = str_[(index+1):] + i
            num = len(str_)
    if num > maxnum:
        maxnum = num
    return maxnum

getstrindex('abcabcbb')
