class Solution:
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])     # xi
            ans.append(nums[i+n])   # yi
        return ans
