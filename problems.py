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