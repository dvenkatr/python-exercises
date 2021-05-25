def transform(legacy_data):
    data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = score
    return data

