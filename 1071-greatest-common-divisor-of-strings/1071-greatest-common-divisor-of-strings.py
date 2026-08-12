class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      a=len(str1)
      b=len(str2)
      while b!=0:
        rem=a%b
        a=b
        b=rem
      gcd_component=str2[:a]
      if gcd_component*(len(str1)//a)!=str1:
        return ""
      if gcd_component*(len(str2)//a)!=str2:
        return ""
      return gcd_component