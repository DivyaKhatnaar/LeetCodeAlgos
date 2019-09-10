# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
class Solution:
    def plusOne(self, list1):
        num = list1[0]
        for x in range(1,len(list1)):
        num = num*10 + list1[x]
        num = num+1
        list2 = [int(d) for d in str(num)]
        return list2