class Solution:
    def romanToInt(self, s: str) -> int:
        #recebe a uma string, adiciona o valor relacionado a cada character, soma tudo no final
        s = s.upper()
        s = s + "_"
        soma = 0
        x = 0
        while x < len(s):
            if s[x] == "_":
                return soma

            if s[x] == "I" and s[x+1] == "V":
                soma = soma + 4
                x = x+2
                continue
            elif s[x] == "I" and s[x+1] == "X":
                soma = soma + 9
                x = x+2
                continue
            elif s[x] == "X" and s[x+1] == "L":
                soma = soma + 40
                x = x+2
                continue
            elif s[x] == "X" and s[x+1] == "C":
                soma = soma + 90
                x = x+2
                continue
            elif s[x] == "C" and s[x+1] == "D":
                soma = soma + 400
                x = x+2
                continue
            elif s[x] == "C" and s[x+1] == "M":
                soma = soma + 900
                x = x+2
                continue
            elif s[x] == "I":
                soma = soma + 1
            elif s[x] == "V":
                soma = soma + 5
            elif s[x] == "X":
                soma = soma + 10
            elif s[x] == "L":
                soma = soma + 50
            elif s[x] == "C":
                soma = soma + 100
            elif s[x] == "D":
                soma = soma + 500
            elif s[x] == "M":
                soma = soma + 1000
            elif s[x] == "_":
                soma = soma + 0
            else:
                print("Character invalido")
            x = x+1

        return soma
