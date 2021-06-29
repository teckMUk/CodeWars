import sys
import ast
class Solution:
    def twoSum(self, nums, target):
        nums_copy = nums.copy()
        nums.sort()
        start = 0
        end =-1
        while True:
            sum = nums[start]+nums[end]
            if sum>target:
                end-=1
            elif sum<target:
                start+=1
            else:
                end_value = nums[end]
                start_value = nums[start]
                if start_value == end_value:
                    start_index = nums_copy.index(start_value)
                    nums_copy.pop(start_index)
                    end_index = nums_copy.index(end_value) +1
                else:
                    start_index = nums_copy.index(start_value)
                    end_index = nums_copy.index(end_value)
                
                return [start_index,end_index]

def main(args=None):
    if args is None:
        list1 = ast.literal_eval(sys.argv[1])

        print(list1)
        target = int(sys.argv[2])
    sol = Solution()    
    print("Your Index is: ",sol.twoSum(list1,target))   
    

if __name__ == "__main__":
    main()              