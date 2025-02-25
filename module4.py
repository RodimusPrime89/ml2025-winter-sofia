User_Input = input() 
N = int(input("Enter a Number ?"))
numbers = list(map(int, input("Enter the Numbers: "))).split()
X = int(input("Enter X: "))

print(numbers.index(X) + 1 if X in numbers else -1)