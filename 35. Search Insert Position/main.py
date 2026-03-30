"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #da pra percorrer tudo ou usar o modo binary three pq ta ordenado papai
        #[1,2,3,4,5]
        inicio = 0
        final = len(nums)-1
        meio = (len(nums)) // 2

        while(inicio <= final):
            
            if(nums[meio]<target): #direita
                inicio = meio + 1
                meio = (inicio + final)//2
            elif(nums[meio]>target): #esquerda
                final = meio - 1
                meio = (inicio + final)//2
            else:
                return meio #achei
        
        return meio+1