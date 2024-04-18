def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    a=[]
    for i in s:
        if i.isalpha():

            a+=i
    return a
    
# Read data from file
f=open('data\data04.txt',mode="r")
s=f.read()
print(main(s))