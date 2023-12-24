#Runtime 35ms: Beats 99.16% of users with Python3
"""
Time complexity:
O(n)

Space complexity:
O(n)
"""
import math
class Solution:
    def minOperations2(self, s: str) -> int:
        op1=0
        first_one=0
        first_zero=0
        d1=s.count("10")
        d2=s.count("01")
        if d1*2 ==len(s) or d2*2==len(s):
            return 0
        len_even=bool(~(len(s)%2))
        for index in range(len(s)):
            if index%2==0:
                if s[index]=="0":
                    first_zero+=1
                else: 
                    first_one+=1
            else:
                if s[index]=="1":
                    first_zero+=1
                else: 
                    first_one+=1
        if first_zero<first_one:
            op1=len(s)-first_one
        else:
            op1=len(s)-first_zero
        return op1

    def minOperations1(self, s: str) -> int:
        
        new_sone=("10"*(math.ceil(len(s)/2)))[:len(s)]
        new_szer=("01"*(math.ceil(len(s)/2)))[:len(s)]
        #print(new_sone,new_szer)
        mask = (1 << len(s)) - 1
        decimal_num1 = int(s, 2)
        decimal_num2 = int(new_sone, 2)
        #decimal_num3 = int(new_szer, 2)
        result_xnor_one = bin(~(decimal_num1 ^ decimal_num2) & ((1 << len(s)) - 1)).count("1")
        result_xnor_zero = bin(~(decimal_num1 ^ ~decimal_num2) & ((1 << len(s)) - 1)).count("1")
        print(result_xnor_one,result_xnor_zero)
        return min(len(s)- result_xnor_one, len(s)- result_xnor_zero)



s=Solution()
deneme="110"
x  
        

        