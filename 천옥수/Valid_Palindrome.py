class Solution:
    def isPalindrome(self, s: str) -> bool:

        # make all the letters into lists
        # alpha_list = list(s)
        
        # remove all the non-alphanumeric characters
        alpha_list = [e for e in s if e.isalpha() or e.isnumeric()]
        alpha_list = list(map(lambda x: x.lower(), alpha_list))
        print(alpha_list)


        # convert all uppercase letters into lowercase letters 

        # check if it is palindrome
        # 5 개 -> 2개까지만 검증
        # 0, -1
        # 1, -2, 
        # 2, -3 
        # 0, 1, 2, 3, 4
        
        for i in range(len(alpha_list)//2):
            if alpha_list[i] != alpha_list[-(i+1)]:
                return False
        
        return True