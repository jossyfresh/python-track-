def swap_case(s):
    i = 0
    new = ""
    while i<len(s):
        if s[i].isupper():
            new = new+s[i].lower()
        else :
            new= new + s[i].upper()
        i+=1
    return new 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
