from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you are awfully silent...'
    elif 'dice' in lowered:
        return randint(1, 6)
    elif 'coin' in lowered:
        return choice(['heads','tails'])
    elif 'hello' in lowered:
        return choice(['hello!','hola','hey','...'])