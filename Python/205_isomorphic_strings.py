class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        output_s = []
        output_t = []
        i, j = 1,1
        for char in s:
            if char not in dict_s:
                dict_s[char] = i
                i += 1
            output_s.append(dict_s[char])
        
        for char in t:
            if char not in dict_t:
                dict_t[char] = j
                j += 1
            output_t.append(dict_t[char])
        
        return output_s == output_t

# Top Solution

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         mapping = {}
#         for i in range(len(s)):
#             if s[i] in mapping:
#                 if mapping[s[i]]!=t[i]:
#                     return False
#             else:
#                 if t[i] in mapping.values():
#                     return False
#                 else:
#                     mapping[s[i]] = t[i]
        
#         return True
