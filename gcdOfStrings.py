    def gcdOfStrings(str1, str2):
        n1, n2 = len(str1), len(str2)
        n = min(n1, n2)
        for i in range(n,0,-1):
            if n1%i == 0 and n2%i== 0:
                x = str1[:i]
                if x * (n1//i) == str1 and x * (n2//i) == str2:
                    return x
        return ""
