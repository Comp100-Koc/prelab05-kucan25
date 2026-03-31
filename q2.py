def helper(n):
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            return True
    return False



def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while helper(s):
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s=s[:i]+s[i+2:]
                print(s)
                break
    return s
                
print(remove_adjacent_duplicates("abbacadd"))