import numpy as np

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a positive integer.")

def get_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a real number.")

def main():
    # Step 1: Read N (Number of Points)
    N = get_positive_integer("Enter the number of data points (N): ")
    
    # Step 2: Read k (Number of Neighbors)
    k = get_positive_integer("Enter the number of neighbors (k): ")
    
    # Step 3: Collect N (x, y) Points
    data = np.zeros((N, 2))  # Initialize an array for N points (x, y)
    
    for i in range(N):
        x = get_real_number(f"Enter x for point {i+1}: ")
        y = get_real_number(f"Enter y for point {i+1}: ")
        data[i] = [x, y]
    
    # Step 4: Read the query X
    X_query = get_real_number("Enter the query X: ")
    
    # Step 5: Perform k-NN Regression
    if k > N:
        print("Error: k cannot be greater than N.")
        return
    
    x_values = data[:, 0]  # Extract x values
    y_values = data[:, 1]  # Extract y values
    
    # Compute absolute differences between stored x values and query X
    distances = np.abs(x_values - X_query)
    
    # Get indices of k smallest distances
    nearest_indices = np.argsort(distances)[:k]
    
    # Extract corresponding y values
    nearest_y_values = y_values[nearest_indices]
    
    # Compute the mean as the predicted Y
    predicted_Y = np.mean(nearest_y_values)
    
    # Step 6: Output the Result
    print(f"Predicted Y value using k-NN Regression: {predicted_Y}")

if __name__ == "__main__":
    main()
