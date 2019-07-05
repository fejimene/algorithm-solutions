from typing import List

class Solution:
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
            
        n = len(nums)
        output = []
        backtrack()

        return output

class Solution2:
    # DFS
    def xrange(self, x):
        return iter(range(x))
    
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            print("found"+str(path)+"\n")
            # return # backtracking
        for i in self.xrange(len(nums)):
            self.dfs(nums[:], path+[nums[i]], res)
