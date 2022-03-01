class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # will use the hashmap method
        # iterate through the array and find each elements complement in the hash map
        
        hash_map = {nums[0]: 0}
        
        for i in range(1, len(nums)):
            
            req_sum = target - nums[i]
            
            if req_sum in hash_map:
                return [hash_map[req_sum], i]
            
            else:
                hash_map[nums[i]] = i
                