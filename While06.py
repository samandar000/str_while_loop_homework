from platform import python_revision


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
    k=len(s)
    s = s.lower()
    # x = 'a,i,e,o,u,A,O,I,E,U'
    while i < len(s):
        if s[i]=='a':
            k-=1
        if s[i]=='i':
            k-=1
        if s[i]=='e':
            k-=1
        if s[i]=='o':
            k-=1
        if s[i]=='u':
            k-=1
        i+=1

    #n=len(s)-k and and s[i]=='i' and s[i]=='e' and s[i]=='o' and s[i]=='u'
            
    return k

