command_list = [
    'jump',
    'close your eyes',
    'double blink',
    'wink'
]

def commands(number : int) -> list:

    # Convert number to binary and strip '0b'
    binary = bin(number)[2:]
    # Pad the number so length = 5
    binary = binary.zfill(5)

    handshake = []

    for i in range(1, 5):
        if binary[i] == '1':
            handshake.append(command_list[i - 1])
    if binary[0] == '1':
        return handshake
    return list(reversed(handshake))
    