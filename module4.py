# Ask for input N
N = int(input("Enter a positive integer N: "))

# Read N numbers and store them in a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask for input X
X = int(input("Enter an integer X: "))

# Check if X exists in the list and output the index or -1
if X in numbers:
    print(numbers.index(X) + 1)  # Convert to 1-based index
else:
    print("-1")
