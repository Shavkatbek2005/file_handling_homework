def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in s:
        if i.isdigit():

            a+=i
    return a
    
# Read data from file
f=open('data\data03.txt',mode="r")
s=f.read()
print(main(s))
