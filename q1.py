print("Quiz 1")
def triangles(size):
    for i in range(1, size +1):
        for j in range(i):
            print("T", end="")
        print()

    for i in range(1,size):
        for j in range(size-i):
            print("T", end="")
        print()

size=int(input("Dame el ancho de tu piramide"))
h=triangles(size)
print(h)
