ordinals = {
    1 : 'first',
    2 : 'second',
    3 : 'third',
    4 : 'fourth',
    5 : 'fifth',
    6 : 'sixth',
    7 : 'seventh',
    8 : 'eighth',
    9 : 'ninth',
    10 : 'tenth',
    11 : 'eleventh',
    12 : 'twelfth'
}

lyrics = {
    1 : 'a Partridge in a Pear Tree.',
    2 : 'two Turtle Doves, ',
    3 : 'three French Hens, ',
    4 : 'four Calling Birds, ',
    5 : 'five Gold Rings, ',
    6 : 'six Geese-a-Laying, ',
    7 : 'seven Swans-a-Swimming, ',
    8 : 'eight Maids-a-Milking, ',
    9 : 'nine Ladies Dancing, ',
    10 : 'ten Lords-a-Leaping, ',
    11 : 'eleven Pipers Piping, ',
    12 : 'twelve Drummers Drumming, '
}

def recite(start_verse : int, end_verse : int) -> str:

    if start_verse > end_verse:
        raise ValueError("Start verse cannot be greater than end verse")

    result_list = []
    for i in range(start_verse, end_verse + 1):
        result = f'On the {ordinals[i]} day of Christmas my true love gave to me: '
        for j in reversed(range(1, i + 1)):
            if j == 1 and i != 1:
                result = result + 'and ' + lyrics[j]
            else:
                result = result + lyrics[j]
        result_list.append(result)
            
    return result_list