def findsum(lst,sum):
    for i in lst:
        if sum-lst[i] in lst:
            return True
    return False

def main():
    l = [1, 2, 3, 4, 5]
    a = int(input("Insert sum:"))
    print(findsum(l,a))

main()


