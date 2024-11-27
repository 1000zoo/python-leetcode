# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

class Solution:

    """
    Runtime 23 ms Beats 69.73%
    """
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        answer = []
        table = {}
        
        for i in range(k):
            num = nums[i]
            if not num in table:
                table[num] = 0
            table[num] += 1

        for i in range(len(nums) - k + 1):
            sortedList = sorted(list(table.keys()), key=lambda x: (-table[x], -x))
            temp = 0
            for j in range(min(x, len(sortedList))):
                temp += table[sortedList[j]] * sortedList[j]

            answer.append(temp)

            if i == len(nums) - k:
                continue

            table[nums[i]] = table[nums[i]] - 1
            if table[nums[i]] == 0:
                del(table[nums[i]])
            if not nums[i + k] in table:
                table[nums[i + k]] = 0
            table[nums[i + k]] += 1

        return answer