# Q1: Reverse a string without using built-in reverse methods.

# s = 'mayank'

# rs = s[::-1]
# print(rs)

# Q2: Count vowels in a string (case-insensitive).
# vowels = 'aeiouAEIOU'
# s = 'mayank'
# count = 0

# result = sum(1 for i in s if i in vowels)
# print(result)
# or
# for i in s:
#     if i in vowels:
#         count+= 1
# print(count)

# Q3: Check if string is palindrome (ignore spaces/case).
# flag = True
# s = 'mayam'

# for i in range(1,len(s)//2):
#     if s[i] != s[len(s)-1-i]:
#         flag = False
#         print('not pallandrome')
#         break
#     else:
#         print('pallandrome') 

# Q4: Find longest word in string.
# s = "The quick brown fox jumps"
# words = s.split()
# longest = max(words, key=len)
# print(longest)  # "jumps"

# Q5: Replace all occurrences of substring (manual implementation).

# Q6: Generate all possible abbreviations (e.g., "word" → ["w", "wo", "wor", "word"]).
# s = "word"
# abbrevs = [s[:i] for i in range(1, len(s)+1)]
# print(abbrevs)  # ['w', 'wo', 'wor', 'word']

# Q7: Check if two strings are anagrams.
# anagrams means each words should have same letters 
# def is_anagrams(l1,l2):
#     return sorted(l1.lower()) == sorted(l2.lower())

# print(is_anagrams('listen','siltent'))

# Q8: Find first non-repeating character.

# s = 'mayank'
# n = len(s)

# for i in range(n):
#     found = False
#     for j in range(n):
#         if i != j and s[i] == s[j]:
#             found = True
#             break
#     if not found:
#         print(s[i])
#         break

# Q9: Remove duplicates while preserving order.
# unique_list = []
# my_list = ['m','a','y','a','n','k']

# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
merge_ls = [sorted(list1) + sorted(list2)]

print(merge_ls)