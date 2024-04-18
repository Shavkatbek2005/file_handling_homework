def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=''
    for i in s:
        l+=i
    a=l.split("\n")
    k=[]
    for u in a:
        k.append(len(u))
        return k
# Read data from file
f=open('data\data05.txt',mode="r")
s=f.read()
print(main(s))