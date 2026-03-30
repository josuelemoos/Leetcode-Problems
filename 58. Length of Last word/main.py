"""
58. Length of Last word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #basicamente contar espacos ate encontrar o ultimo, e retornar o que ha apos esse ultimo espaco
        s = s.strip()

        cont = 0
        resultado = 0
        posicao_do_last = 0
        posicao_do_last_letra = 0

        if " " not in s:
                resultado = len(s)
                return resultado

        for character in s:

            if character != " ":
                posicao_do_last_letra = cont  #marca onde ta a ultima letra
                resultado = cont - posicao_do_last + 1

            if character == " ": #  and posicao_do_last < posicao_do_last_letra:
                posicao_do_last = cont + 1
            
            
            cont += 1 #vai marcar todas as letras e espacos

            
        #aaa
        return resultado

            

        
