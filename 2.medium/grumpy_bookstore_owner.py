# 

class Solution:

    """
    Runtime 5642 ms Beats 8.25%
    """
    def solution1(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        answer = 0

        for i in range(len(customers) - minutes + 1):
            temp = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    temp += customers[j]
            answer = max(answer, temp)
        
        answer += sum([customers[i] if grumpy[i] == 0 else 0 for i in range(len(customers))])

        return answer

    """
    Runtime 16 ms Beats 74.23%
    """
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        gsum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                gsum += customers[i]
        answer = gsum

        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                gsum -= customers[i - minutes]
            if grumpy[i] == 1:
                gsum += customers[i]

            answer = max(answer, gsum)
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                answer += customers[i]

        return answer