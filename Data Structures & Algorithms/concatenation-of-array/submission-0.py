class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        new_length = 2 * length
        new_nums = [0] * new_length
        for i in range(length):
            new_nums[i] = nums[i]
            new_nums[i + length] = nums[i]
        return new_nums
        