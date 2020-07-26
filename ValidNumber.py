def isNumber(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False

if __name__ == "__main__":
    print(isNumber(""))
    print(isNumber("0"))
    print(isNumber(" 0.1 "))
    print(isNumber("abc"))
    print(isNumber("1 a"))
    print(isNumber("2e10"))
    print(isNumber(" -90e3 "))
    print(isNumber(" 1e "))
    print(isNumber("e3"))
    print(isNumber(" 6e-1"))
    print(isNumber(" 99e2.5 "))
    print(isNumber("53.5e93"))
    print(isNumber(" --6  "))
    print(isNumber("-+3"))
    print(isNumber("95a54e53"))
