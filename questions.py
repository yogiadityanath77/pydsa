# reverse array 
arr = [1,2,2,3,1,4]

left = 0 
right = len(arr) - 1

while left < right :
    arr[left],arr[right] = arr[right],arr[left]

    left +=1 
    right -= 1

print("Reversed :" ,arr)

#Palindrome check

arr1 = [1,2,3,2,1,4]
right = len(arr1) -1 
left = 0
palindrome = True
while left < right :
    if arr1[left] != arr1[right]:
        palindrome = False
        break
    left +=1
    right -= 1 
    
        
print(" is palindrome : " , palindrome)

# push zeroes to the left 
arr2= [1,0,2,0,3]

j=0

for i in range(len(arr2)):
    if arr2[i] != 0:
        arr2[i],arr2[j] = arr2[j],arr[i]
        j+=1

print( "after pushed zeroes :" , arr2)    
        
#remove duplicates in a sorted array 

arr3 =[1,1,2,2,3,3,3,4,4]

j=0

for i in range(len(arr3)):
    if arr3[i]!=arr3[j]:
        j+=1
        arr3[j] = arr3[i]

print(" array without duplicates : " , arr3[:j+1])

# freq count using dict 

arr4 = [1,1,2,2,3,3,3,4,4]

freq = {}

for num in range(len(arr4)):
    if arr4[num] in freq:
        freq[arr4[num]] += 1
    else :
        freq[arr4[num]] = 1

print("frequency : " , freq)      

#first repeating element

arr6 = [1,2,3,2,5]

freq2 = {}

for num in range(len(arr6)):
    if arr6[num] in freq2:
        freq2[arr6[num]] += 1
    else :
        freq2[arr6[num]] = 1

first_repeating = None

for num in range(len(arr6)):
    if freq2[arr6[num]] > 1:
        first_repeating = arr6[num]
        break

print("first repeating element : " , first_repeating)

# first non repeating element 

arr5 = [1,1,2,2,3,3,3,4]
freq1 = {}

for num in range(len(arr5)):
    if arr5[num] in freq1:
        freq1[arr5[num]] += 1
    else :
        freq1[arr5[num]] = 1

first_non_repeating = None

for num in range(len(arr5)):
    if freq1[arr5[num]] == 1:
        first_non_repeating = arr5[num]
        break

print("first non repeating element : " , first_non_repeating)

# pair sum 

arr7 = [2,7,11,15]
target = 18

seen = set()

for num in arr7:
    complement = target - num
    if complement in seen:
        print("pair found : " , (complement,num))
        break
    seen.add(num)

# pair sum with two pointers

left = 0
right = len(arr7) -1
found = False

while left < right :
    current_sum = arr7[left] + arr7[right]
    if current_sum == target:
        print("pair found : " , (arr7[left],arr7[right]))
        found = True
        break

    elif current_sum < target:
        left += 1

    elif current_sum > target:
        right -= 1

if not found:
    print("No pair found")

#merge sorted arrays 

arr8 = [1,3,5]
arr9 = [2,4,6]
i = 0 
j = 0
merged = []

while i < len(arr8) and j < len(arr8):

    if arr8[i] < arr9[j]:
        merged.append(arr8[i])
        i += 1

    else:
        merged.append(arr9[j])
        j+=1

while i<len(arr8):
    merged.append(arr8[i])
    i +=1

while j< len(arr9):
    merged.append(arr9[j])
    j += 1

print(" merged array :" , merged)

# count distinct elements

l1 = [1,2,2,3,1,4]

distinct = set(l1)

count = len(distinct)

print(count)


# majority element ( more than n/2 times)

l2 = [2,2,1,2,3,2,2]
n = int(len(l2)/2)

freq3 = {}

for i in range(len(l2)):
    if l2[i] in freq3:
        freq3[l2[i]] += 1
    else :
        freq3[l2[i]] = 1

for key in l2:
    if freq3[key] > n:
        print(key)
        break

