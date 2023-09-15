def find_pair(nums,target):
    d ={}

    for i ,e in enumerate(nums):
        if target -e in d:
            print('pair found',(nums[d.get(target-e)], nums[i]))
            return

            d[e] = i
    print('pair not found')

if __name__ == '__main__':
     nums = [8,7,2,5,3,1]
     target = 10

     find_pair(nums,target)