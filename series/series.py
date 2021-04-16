def slices(series:str, length:int) -> list:
    
    if length > len(series):
        raise ValueError("The series must be at least as long as length")

    if length <= 0:
        raise ValueError("Length cannot be zero or negative")

    # result = []
    # for i in range(len(series) - length + 1):
    #     print(series[i : i+length])
    #     result.append(series[i : i+length])
    # return result

    return [series[i : i + length] for i in range(len(series) - length + 1)]