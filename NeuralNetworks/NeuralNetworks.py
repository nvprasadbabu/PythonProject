# Neural Networks ..........
import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights
        self.W1 = np.random.rand(self.input_size, self.hidden_size)
        self.W2 = np.random.rand(self.hidden_size, self.output_size)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(self.W2.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.a1)
        
        # Update weights
        self.W2 += self.a1.T.dot(output_delta)
        self.W1 += X.T.dot(hidden_delta)
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
# Example usage
if __name__ == "__main__":
    # Sample dataset (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])
    
    # Create and train the neural network
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=5)
    nn.train(X, y, epochs=10000)
    
    # Test the neural network
    output = nn.forward(X)
    print("Predicted output:")
    print(output)
    # Plotting the decision boundary
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap='viridis')
    plt.title('XOR Problem')
    plt.xlabel('Input 1')
    plt.ylabel('Input 2')
    #plt.show()

# example for Loss function
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def cross_entropy_loss(y_true, y_pred):
    epsilon = 1e-12  # To prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1. - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

mean_squared_error_value = mean_squared_error(y, output)
cross_entropy_loss_value = cross_entropy_loss(y, output)
print(f"Mean Squared Error: {mean_squared_error_value}")
print(f"Cross Entropy Loss: {cross_entropy_loss_value}")


