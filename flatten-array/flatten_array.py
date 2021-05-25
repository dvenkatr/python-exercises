def flatten(iterable):
    check = False
    flat = []
    
    for item in iterable:

        if isinstance(item, list):
            check = True
            for element in item:
                if element is not None:
                    flat.append(element)
        else:
            if item is not None:
                flat.append(item)

    if check == True:
        check = False
        return flatten(flat)
    else:
        return flat