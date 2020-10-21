def swapVocals(sir, i, j):
    '''
    input: ein Vektor,
    i,j-Positionen der Vokalen die getauscht werden mussen

    output: Vektor mit getauschten zwei Vokalen
    '''
    lst = list(sir)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def findVocals(sir, i, j):
    '''
    input:Vektor, zwei Index
    output: Vektor, mit allen getauschten Vokalen

    wie funtioniert?
    ein Index beginnt vom Anfang, der andere vom Ende
    Wenn beide Index eine Vokale gefunden haben, werden diese getauscht
    '''

    while i < j:
        if sir[i] == "a" or sir[i] == "e" or sir[i] == "i" or sir[i] == "o" or sir[i] == "u":
            break
        else:
            i += 1

    while i < j:
        if sir[j] == "a" or sir[j] == "e" or sir[j] == "i" or sir[j] == "o" or sir[j] == "u":
            break
        else:
            j -= 1

    sir = swapVocals(sir, i, j)
    if i >= j:
        print(sir)
    else:
        findVocals(sir, i + 1, j - 1)


def main():
    s = "Terminator"
    i = 0
    j = len(s) - 1
    findVocals(s, i, j)


main()
