def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=[]
    for i in s:
        if i.isdigit():
            a+=i
    return max(a)

# Read data from file
f=open('data\data08.txt',mode="r")
s=f.read()
print(main(s))