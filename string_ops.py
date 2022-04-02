# def solve(a,b):
#     asterix_a = a.find('*')
#     a,b = a.lower(),b.lower()
#     try:
#         if isinstance(a,str) and isinstance(b,str) and asterix_a != -1:
#             if asterix_a == len(a) -1 and a[:asterix_a] == b[:asterix_a]:
#                  return True
#             elif a[:asterix_a] == b[:asterix_a] and a[:asterix_a] == b[:asterix_a] and a[:asterix_a] != b and a[-1] == b[-1]:
#                 return True
#         if a == b:
#             return True
#         else:
#             return False
#     except:
#         print('Your Enter is not correct, Please try again')
        


# def is_palindrome(s):
#     if s.lower() == s[::-1].lower():
#         return True
#     else:
#         return False



# def find_nth_occurrence(substring, string, occurrence=1):
#     occurrences = []
#     current_index = None
    
#     while current_index != -1:
#         current_index = string.find(substring, current_index)
#         if current_index != -1:
#             occurrences.append(current_index)
#             current_index += 1

#     if len(occurrences) >= occurrence:
#         return occurrences[occurrence - 1]
#     else:
#         return -1

import sys
print(sys.prefix)