import regex as re

def znajdz_slowo():
    text = input('')
    slowa = input('').split()
    output = []
    for slowo in slowa:
        pattern = slowo
        if re.search(pattern, text, re.IGNORECASE):
            output.append('TAK')
        else:
            output.append('NIE')

    print(*output)


znajdz_slowo()