def singleNumber(nums):
        length = len(nums)
        if length ==1:
            return nums[0]
        for i in range(length):
            count =0
            for j in range(0, length):
                print("i = " , i , " j = " , j , " count= " , count , " length = " , length)
                if nums[i]==nums[j]:
                    count+=1
                if count >1:
                    break
            if count<=1:
                return nums[i]
        return nums[-1]

nums = [2,2,1]
print(singleNumber(nums))