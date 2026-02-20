class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        window = {}
        longest = 0
        l, r = 0, 0
        
        while r < len(s):
              c = s[r]
              if c in window:
                while c in window:
                  window.pop(s[l])
                  l += 1
              else:
                window[c] = None
                if r-l+1 > longest: longest = r-l+1
                r += 1
                  
        # if s == "": return 0
        # current_substring = {}
        # longest_substring = 1
        # j, i = 0, 1
        
        # while j < len(s)-1 and i < len(s):
        #       c = s[i]
        #       if c not in current_substring:
        #           current_substring[c] = 0
        #           if len(current_substring) > longest_substring:
        #             longest_substring = len(current_substring)
        #           i += 1
        #       else:
        #           j += 1
        #           current_substring.clear()
        #           current_substring[s[j]] = 0
                  
        # if s == "": return 0
        # current_substring = s[0]
        # longest_substring = 1
        # j = 0
        
        # for i, c in enumerate(s[1:],1):
        #       if c not in current_substring:
        #           current_substring += c
        #           if len(current_substring) > longest_substring:
        #             longest_substring = len(current_substring)
        #       else:
        #           j += 1
        #           current_substring = s[j]
        return longest
      
  
sol = Solution()
#x = sol.lengthOfLongestSubstring("zxyzxyz")
x = sol.lengthOfLongestSubstring(s="pwwkew")
#x = sol.lengthOfLongestSubstring(s="dvdf")


print(x)