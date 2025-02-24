def read_positive_integer():
    while True:
        try:
            N = int(input("Enter a positive integer: "))
            if N > 0:
                return N
            else:
                print("Please enter a positive integer greater than zero")
        except ValueError:
            print("Invalide input. Please enter a valid positive integer")
N = read_positive_integer()
print(f"You entered: {N}")


        