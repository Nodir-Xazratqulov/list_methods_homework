def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    
    i=0
    k=[]
    while i<len(fruits):
        if fruits[i]=='apple':
            k.append(i)
        i+=1
    s=fruits.count("apple")
    k.insert(0,s)
    return k
print(main(["apple", "apple", "apple", "apple", "apple", 'apple']))

