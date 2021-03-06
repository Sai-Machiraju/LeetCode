class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s[0]!="-":
            number=int(s)
            reverse_number = 0
            while number > 0:
                    last_digit = number % 10
                    reverse_number = reverse_number*10 + last_digit
                    number = number // 10
            return reverse_number if -(2**31)-1 < reverse_number < 2**31 else 0        
        else:
            s=s[1:]
            number=int(s)
            reverse_number = 0
            while number > 0:
                last_digit = number % 10
                reverse_number = reverse_number*10 + last_digit
                number = number // 10
            return "-"+str(reverse_number) if -(2**31)-1 < -1*reverse_number < 2**31 else 0 