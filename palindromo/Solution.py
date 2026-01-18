class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lista = [int(digit) for digit in str(x)]
        print(lista)

        for i in range(len(lista)):
            print(i)
            if lista[i] == lista[((len(lista)-1)-i)]:
                print("ok " + str(i) + " ta igual a " + str(((len(lista))-1)-i))
            else:
                print("opss " + str(i) + " ta diferente de " + str(((len(lista))-1)-i))
                print("nao é palindromo")
                return False
        print("é palindromo")
        return True
        
s = Solution()
s.isPalindrome(110110)