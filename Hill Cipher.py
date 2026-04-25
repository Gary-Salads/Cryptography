import numpy as np

Leave = False
while Leave != True:
    choice = input("q to exit p to play")
    if choice == "q":
        Leave = True
    elif choice == "p":
        ExOne = int(input("What is X1:"))
        ExTwo = int(input("What is X2:"))
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[ExOne], [ExTwo]])
        EorD = input("e for encryption d for decryption")
        if EorD == "e":
            ans = A @ B % 37
            print(ans)
        elif EorD == "d":
            A_inv = np.linalg.inv(A)
            decryption = A_inv @ B % 37
            print(decryption)
    else:
        print("wrong input")
