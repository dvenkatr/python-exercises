from enum import Enum

class Response(Enum):
    say_nothing = 'Fine. Be that way!'
    yell_and_ask = 'Calm down, I know what I\'m doing!'
    yell = 'Whoa, chill out!'
    ask = 'Sure.'
    default = 'Whatever.'

def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return Response.say_nothing.value

    if hey_bob.upper().isupper() and hey_bob.upper() == hey_bob and hey_bob[-1] == '?':
        return Response.yell_and_ask.value

    if hey_bob[-1] == '?':
        return Response.ask.value

    if hey_bob.upper().isupper() and hey_bob.upper() == hey_bob:
        return Response.yell.value

    return Response.default.value



