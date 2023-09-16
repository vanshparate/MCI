class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        pal = ""
        for i in range(len(str(x)), -1):
            pal = pal + x[i]
        return pal


x = 121
solution = Solution()
print(solution.isPalindrome(x))