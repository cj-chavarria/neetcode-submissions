class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1

        while True:
            if nums[i] + nums[j] == target:
                break
            
            elif j == len(nums)-1:
                i += 1
                j = i+1

            else:
                j += 1
        
        return [i, j]
        


        

        