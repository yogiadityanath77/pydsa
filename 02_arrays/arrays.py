# arr = [4,1,2,5,8,4,5,3]
# sum =0
# largest = arr[0]
# largest1 = arr[0]
# smallest = arr[0]
# count = 0
# count1 = 0
# #print(arr)

# for i in range(len(arr)):
#     print(arr[i])

# for i in range(len(arr)):
#     sum = sum + arr[i]

# print(sum)

# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]

# print (largest)

# for i in range(len(arr)):
#     if arr[i] < smallest:
#         smallest = arr[i]

# print(smallest)

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         count += 1

# print(count)

# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         count1 += 1

# print(count1)

# target = 7
# ch = 0 
# for i in range(len(arr)):
#     if arr[i] == target:
#         ch = 1
# if ch == 1 :
#     print("found")
# else :
#     print("not found")    

# second_largest= arr[0]
# largest1 = arr[0]

# for i in range(len(arr)):
#     if arr[i] > largest1:
#         second_largest = largest1
#         largest1 = arr[i]

#     elif arr[i]>second_largest and arr[i] != largest1:
#         second_largest = arr[i]

# print( second_largest)        

# arr = [4,1,2,5,5,4,5,3]

# # largest = float('-inf')
# # second_largest = float('-inf')

# # for num in arr:

# #     if num > largest:
# #         second_largest = largest
# #         largest = num

# #     elif num > second_largest and num != largest:
# #         second_largest = num

# # print(second_largest)

# arr1 = [1,2,3,4,1]
# sorted_array = True

# for i in range(len(arr1)-1):
#     if arr1[i]  > arr1[i+1]:
#         sorted_array = False
#         break

# print(sorted_array)

# #reverse array 

# arr2=[]

# for i in range(len(arr)-1,-1,-1):
#     arr2.append(arr[i])

# print(arr2)

# left=0
# right = len(arr)-1

# while left<right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left+=1
#     right -= 1

# print(arr)

#left rotate

# arr = [1,2,3,4]

# first = arr[0] 

# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]

# arr[len(arr)-1] = first 

# print(arr)
# count =0
# arr = [1,0,2,0,3]
# arr1 = []
# for i in range(len(arr)):
#     if arr[i] == 0:
#         count += 1

# for i in range(len(arr)):
#     if arr[i] != 0 :
#         arr1.append(arr[i])

# for i in range(count):
#     arr1.append(0)

# print(arr1)    


# list = [1,2,3,4,5]
# reversed_list = []

# left = 0
# right = len(list)-1

# while left < right:
#     list[left] ,list [right] = list[right], list[left]
#     left += 1
#     right -= 1

# print(list)

# st = "madam"

# left = 0
# right = len(st)-1
# palindrome = True
# while left < right :
#     if st[left] != st[right]:
#         palindrome = False

#     left += 1
#     right -= 1

# print(palindrome)

# arr = [1,0,2,0,3]

# j = 0

# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[i],arr[j] = arr[j],arr[i]
#         j += 1

# print(arr)

# remove duplicates in sorted array 

# arr = [1,1,2,2,3,4,4]
# j = 0
# for i in range(len(arr)):
#     if arr[i] != arr[j]:
#         j += 1
#         arr[j] = arr[i]

# print(arr[:j+1])

# freq = {}

# for i in range(len(arr)):
#     if arr[i] in freq:
#         freq[arr[i]] += 1
#     else :
#         freq[arr[i]] = 1

# print(freq)


# arr =[1,2,3,2,5,1]

# freq={}

# for i in range( len(arr)):
#     if arr[i] in freq:
#         freq[arr[i]] += 1
        
#     else:
#         freq[arr[i]] = 1

# for i in range(len(arr)):
#     if freq[arr[i]] > 1:
#         print(arr[i])
#         break        

# # print(freq)

# arr = [1,2,3,2,5]

# seen = set()

# for num in arr:

#     if num in seen:
#         print(num)
#         break

#     seen.add(num)

arr = [1,2,2,3,1,4]
freq={}
for num in arr:
    if num in freq:
        freq[num] += 1
    else :
        freq[num] = 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break

    







        







