def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    res=''
    mes=0
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            if s[i:j+1]==s[j:i-1:-1]:
                if j+1-i>mes:
                    mes=j+1-i
                    res=s[i:j+1]
    if len(res)<=1:
        return ''
    else:
        return res
                
            