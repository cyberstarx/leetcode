class Solution:
 def isPalindrome(w, x=121):

    if x < 0:
        return False
    
    # Convert the integer to a string
    str_x = str(x)
    
    if str_x == str_x[::-1]:
        return True
