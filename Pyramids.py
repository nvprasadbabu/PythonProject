
print("\n========== Full pyramid ==========\n")
def full_pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")

        for k in range(1, 2*i):
            #print("*", end="")
            #print(i, end="")
            print(k, end="")
        print()

full_pyramid(5)

print("\n========== Pyramid Patterns with Alphabets ==========\n")
def pyramid_alphabets(n):
    alph = 65
    for i in range(0, n):
        print(" " * (n-i), end=" ")
        for j in range(0, i+1):
            print(chr(alph), end=" ")
            alph += 1
        alph = 65
        print()

pyramid_alphabets(10)

print("\n========== Inverted Full pyramid ==========\n")
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end="")

        for k in range(1, 2*i):
            #print("*", end="")
            #print(i, end="")
            print(k, end="")
        print()

inverted_pyramid(5)

print("\n========== Inverted Pyramid Patterns with Alphabets ==========\n")
def inverted_pyramid_alphabets(n):
    alph = 65
    for i in range(n, 0, -1):
        print(" " * (n-i), end=" ")
        for j in range(0, i):
            print(chr(alph), end=" ")
            alph += 1
        alph = 65
        print()

inverted_pyramid_alphabets(10)


