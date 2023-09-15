def find_pair(nums,target):

  for i in range(len(nums)-1):
      for j in range(i +1,len(nums)):
          if nums[i] + nums[j] == target:
              print('pair found',(nums[i],nums[j]))
              return
  print('pair not found')

if __name__ == '__main__':

    nums = [8,7,2,5,3,1]
    target = 10
    find_pair(nums,target)
