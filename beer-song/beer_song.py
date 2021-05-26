def recite(start, take=1):

    lyrics = []
    i = start

    while(take != 0):
        take -= 1

        if i == 0:
            i = 99
            line1 = f'No more bottles of beer on the wall, no more bottles of beer.'
            line2 = f'Go to the store and buy some more, {i} bottles of beer on the wall.'
        
        elif i == 1:
            line1 = f'1 bottle of beer on the wall, 1 bottle of beer.'
            line2 = f'Take it down and pass it around, no more bottles of beer on the wall.'
                
        elif i == 2:
            line1 = f'2 bottles of beer on the wall, 2 bottles of beer.'
            line2 = f'Take one down and pass it around, 1 bottle of beer on the wall.'
        
        else:
            line1 = f'{i} bottles of beer on the wall, {i} bottles of beer.'
            line2 = f'Take one down and pass it around, {i - 1} bottles of beer on the wall.'

        lyrics.append(line1)
        lyrics.append(line2)
        lyrics.append('')
        
        i -= 1

    lyrics.pop()
    return lyrics