# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:

    """
    Runtime 446 ms Beats 69.75%
    """
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        answer = 0
        arr_sum = sum(arr[:k])
        if arr_sum / k >= threshold:
            answer += 1
        
        for i in range(k, len(arr)):
            arr_sum = arr_sum - arr[i - k] + arr[i]
            
            if arr_sum / k >= threshold:
                answer += 1

        return answer