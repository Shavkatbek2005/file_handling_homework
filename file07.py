def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    d=0
    for i in s:
        if i.isalpha():
            d+=1

    return d
    
# Read data from file
f=open('data\data07.txt',mode="r")
s=f.read()
print(main(s))