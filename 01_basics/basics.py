# # list1=[1,2,3,4,5]

# # print(list1)

# # print(list1[4])

# # list1[1] = 100
# # print(list1)

# # fruits = ["apple", "banana"]
# # fruits.append("orange")
# # print(fruits)
# # fruits.pop(1)
# # print(fruits)

# data = [5, 10, 15, 20]
# print(len(data))

# items = ["pen", "book", "eraser"]
# for item in items:
#     print(item)

# sum = 0
# numbers = [1, 2, 9, 2, 5]
# for number in numbers:
#     sum = sum + number 
# print(sum)

# max = numbers[0]
# for number in numbers:
#     if number >= max :
#         max = number
# print(max)

# count = 0
# for number in numbers:
#     if number == 2 :
#         count = count + 1
# print (count)

# even = 0
# for number in numbers: 
#     if number % 2 == 0:
#         even = even + 1
#         print(number)
# print(even)

# numbers.reverse()
# print(numbers)

# numbers2 = numbers.copy()
# print(numbers2)
# sum = 0
# avg = 0
# length = len(numbers)
# for number in numbers:
#     sum = sum + number
# avg = sum / length 
# print(avg)    


# nums = [1, 2, 2, 3, 4, 4]

# unique =[]

# for num in nums:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# nums = [10, 20, 5, 8, 20]
# largest = nums[0]
# second = nums[0]

# for num in nums:
#     if num > largest :
#         second = largest 
#         largest = num
#     elif num> second and num!= largest:
#         second = num 
# print(second)

# t = (1,2,3)

# print(t[0])
# print(t[-1])

# for num in t:
#     print(num)

# print(t.count(2))

# print(t.index(2))
# a,b,c = t
# print(a+b+c)

# t = (10, 20, 30, 40)

# x=list(t)

# x[1]=1

# t=tuple(x)

# print(t)

# sets ------
# s = { 1,1,2,3,4,4,5}
# print(s)

# s.add(9)
# print(s)

# s.discard(9)
# print(s)

# print (2 in s)

# l = [ 1,1,2,2,3,4,5,6,6,7]

# s = set(l)

# l = list(s)

# print(l)

dict = {
    "student_name": "soham",
    "age" : 23
}

print(dict.get("age"))

dict["age"] = 25

print(dict)

# dict.pop("age")
# print(dict)

print(dict.keys())

print(dict.values())

for key,value in dict.items():
    print(key,value)

word = "banana"

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

l1 = [1,2,2,3,1,1]

freq ={}

for ch in l1:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

