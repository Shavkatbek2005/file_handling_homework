def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=0
    b=0
    for i in s:
        if i.isdigit():
            a+=1
        if i.isalpha():
            b+=1
    return [a,b]
    
    
# Read data from file
f=open('data\data05.txt',mode="r")
s=f.read()
print(main(s))

