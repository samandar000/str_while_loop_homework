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
        if s[i]!='a' and s[i]!='u' and s[i]!='i' and s[i]!='o' and s[i]!='e':
            k+=1
        i+=1

    return k


