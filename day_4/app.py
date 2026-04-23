# List vs Tuple (Mutation Logic)

# What will happen?

# a = (1, 2, [3, 4])
# a[2].append(5)
# print(a)

# answer is Tuple is immutable, but mutable objects inside it can change. thus a is now (1,2,[3,4,5])

# Set Deduplication
# What will happen?

# nums = [1, 2, 2, 3, 4, 4, 5]
# print(list(set(nums)))

# answer is set will remove all the dublicates but order is not defined thus nums is [1,2,3,4,5]

# Dictionary Key Constraint
# Which will fail?

# d = {
#     (1,2): "valid",
#     [3,4]: "invalid"
# }

# thus conclusion is lists are unshapable 
# What will happen?

# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

# answer is lists have same reference not copy thus b will also change when we change a 

# a = [[1,2], [3,4]]
# b = a.copy()
# b[0][0] = 100
# print(a) 

# this peice of code create the shallow copy to store the copy and do not change the actual data thus prevents refrencing of list 

# a = {1,2,3}
# b = {3,4,5}
# print(a & b)

# this is an example of intersection means whenever their are same elements in both set only those elements will be visible thus answer here is {3}

# d = {"a":1}
# print(d.get("b"))
# print(d["b"])

# key notable difference is get method will through no error while d['b'] method do , result of the code is none /n KeyError

# a, b = (10, 20)
# print(a+b) 

# this code is help to unpack the touples and use therir values
# another way is 
# a , b *others = (1,2,4,5,56)
# when we want only first two values from the touple 

# s = {1,1,1,2,3}
# print(len(s))

# set first remove the dublicates then count the no. of element or you should say set helps to count the distinct values in set 

# result = [x**2 for x in range(5) if x%2==0]
# print(result)

# sets , dictonary , touple , and lists we can use loops to for comprehensive  logic

# Find Duplicate Using Set Logic

# nums = [1,2,3,4,3,4,5,6]
# seen = set()
# dublicates = set()

# for num in nums:
#     if num in seen:
#         dublicates.add(num)
#     else:
#         seen.add(num)

# print(dublicates)

# Frequency Counter (Dict Logic)
# nums = [1,2,3,4,3,4,5,6]
# det = {}

# for num in nums:
#     det[num] = det.get(num, 0) + 1
    
# print(det)

# Reverse Dictionary
# d = {'a':5 ,'b':20}

# r = {j:i for i , j in d.items()}
    
# print(r)

# Unique Elements Only
# nums = [1,2,2,3,4,4]
# result = [x for x in nums if nums.count(x) == 1]

# Flatten Nested List
# lst = [[1,2],[3,4],[5,6]] # output

# flat = [item for sublist in lst for item in sublist]

# print(lst)

# Merge Two Dictionaries
d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}

result = {}

for k in set(d1)|set(d2):
    result[k] = d1.get(k,0) + d2.get(k, 0)    

print(result)