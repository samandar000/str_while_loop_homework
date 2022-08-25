def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    k=0
    s = s.lower()
    
    while i < len(s):
        if s[i]!='a' or s[i]!='u' or s[i]!='i' or s[i]!='o' or s[i]!='e':
            k+=1
        i+=1

    return k


