def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i < len(s):
        if  int(s[i])%2==1:
            k=k+int(s[i])
        i +=1
    return k
