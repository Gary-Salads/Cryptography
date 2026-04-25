import numpy as np

Leave = False
while Leave != True:
    choice = input("q to exit p to play: ")
    if choice == "q":
        Leave = True
    elif choice == "p":
        ExOne = int(input("What is X1: "))
        ExTwo = int(input("What is X2: "))
        A11 = int(input("What is A11: "))
        A12 = int(input("What is A12: "))
        A21 = int(input("What is A21: "))
        A22 = int(input("What is A22: "))
        A = np.array([[A11, A12], [A21, A22]])
        B = np.array([[ExOne], [ExTwo]])
        EorD = input("e for encryption d for decryption: ")
        if EorD == "e":
            ans = A @ B % 37
            print(ans)
        elif EorD == "d":
            A_inv = np.linalg.inv(A)
            decryption = A_inv @ B % 37
            print(decryption)
    else:
        print("wrong input")
