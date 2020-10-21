def find_word(matrix,word,i,j,num,beforeI,beforeJ):
    '''

  Rekursive Funtion
  input:
  matrix voll von Buchstaben,
  word=Wort, den wir suchen,
  i,j-Current position einer Buchstabe des Wortes
  num-reprasentiert welche der Buchstabe der Wort wir suchen
  beforeI,beforeJ-vorige Position, damit wir nicht die selbe Buchstabe zwei mal nehmen

    output:
    boolean = ob wir das Wort gefunden haben oder nicht

   wie funktioniert?
   da wir die Position der current Buchstabe als Parameter haben,
   suchen wir die nachste - mogliche Position: rechts,links,oben,unter

   Wenn num die Lange unseres Wortes enthalt, wissen wir, dass die Matrix unseres Wort enthalt.
   '''
    if num==len(word):
        print (True)
    else:
        if matrix[i-1][j]==word[num] and i-1!=beforeI:
            find_word(matrix,word,i-1,j,num+1,i,j)
        if j+1<len(matrix[i])  and matrix[i][j+1] == word[num] and j+1!=beforeJ :
            find_word(matrix, word, i, j+1, num + 1, i,j)
        if  i+1<len(matrix)  and matrix[i+1][j] == word[num] and i+1!=beforeI:
            find_word(matrix, word, i +1, j, num + 1,i,j)
        if matrix[i][j-1] == word[num] and j-1!=beforeJ:
            find_word(matrix, word, i, j-1, num + 1,i,j)

def main():
    word = "ALARM"
    matrix = [
        ['A', 'B', 'C', 'D'],
        ['L', 'A', 'G', 'H'],
        ['C', 'R', 'M', 'Z']
    ]
    for a in range(0,len(matrix)):
        for b in range(0,len(matrix[a])):
            if matrix[a][b]==word[0]:
                find_word(matrix,word,a,b,1,0,0)



main()


