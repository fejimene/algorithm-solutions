from typing import List

given = [10, 15, 3, 6]


class Solution:
    def k_in_list(self, l: List[int], k:int) -> bool:
        hash = {}
        for i in l:
            hash[k - i] = i 
            if i in hash:
                return True
        return False

a = Solution()
print(a.k_in_list(given, 17))
