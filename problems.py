# 1. Two Sum
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++){
            if (nums[i] + nums[j] === target){
                const numbers = [i,j];
                return numbers;
            }
        }
    }
};
# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
# 13. Roman to Integer
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
                # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total
# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, currentPrefix = 0, ''
        while True:
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return currentPrefix
            currentPrefix += strs[0][i]
            i += 1
#20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
#21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)
        prev = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
                #print(l1)
            else:
                prev.next = l2
                l2 = l2.next
                #print(l2)
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
        # print(prehead)

        return prehead.next
# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        if len(nums) == 0:
            return 0
        temp = nums[0]
        while i < len(nums):
            if nums[i]==temp:
                del nums[i]
            else:
                temp = nums[i]
                i+=1
        print(nums)
#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while count is not -1:
            try:
                nums.remove(val)
                count += 1
            except:
                break
#28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        l = 0
        if k == 0:
            return 0
        while l <= (len(haystack)-k):
            if haystack[l:l+k] == needle:
                return l
            l+=1
        return -1
#35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_subarray = -math.inf
        # for i in range(len(nums)):
        #     current_sub = 0
        #     for j in range(i, len(nums)):
        #         current_sub += nums[j]
        #         max_subarray = max(max_subarray,current_sub)
        # return max_subarray
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray+num)
            max_subarray = max(current_subarray, max_subarray)
        return max_subarray

#58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        some_list = s.strip()
        some_list = some_list.split(" ")
        return len(some_list[-1])

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1]+=1
        for i in range(len(digits)-1,0,-1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits
#67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tot = 0
        c = ""
        for i in range(len(a)-1,-1,-1):
            tot += int(a[i])*pow(2,len(a)-i-1)
        for i in range(len(b)-1,-1,-1):
            tot += int(b[i])*pow(2,len(b)-i-1)

        if tot == 0:
            return str(tot)
        
        if tot < pow(2,max(len(a),len(b))):
            i = max(len(a),len(b))-1
        else:
            i = max(len(a),len(b))
            
        for j in range(i,-1,-1):
            print(tot)
            if pow(2,j)<=tot:
                tot -= pow(2,j)
                c+= "1"
            elif pow(2,j) > tot or tot == 0:
                c+= "0"

        return c
#69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        temp = 0
        i = 0
        while i!=-1:
            if x >= i*i:
                temp = i
                i+=1
            elif x < i*i and x >= (i-1)*(i-1):
                return temp