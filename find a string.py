def count_substring(string, sub_string):
    x = 0 
    y=len(sub_string) 
    for i in range(len(string)): 
        if string [i:y]==sub_string:
            x= x + 1 
            y=y+1 
        else: 
            y=y+1
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
