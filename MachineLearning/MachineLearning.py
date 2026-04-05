# Machine Learning
# This file contains the code for the machine learning algorithms used in the project.
# This code defines a simple machine learning class that uses linear regression to fit a model to the data. The class has methods for training the model, making predictions, and evaluating the model's performance. The example usage demonstrates how to use the class with sample data.
# Note: In a real-world application, you would typically use more complex models and handle data preprocessing, feature engineering, and model selection.
# Additionally, you would likely want to split your data into training and testing sets to evaluate the model's performance on unseen data.
# The code is designed to be modular and can be easily extended to include other machine learning algorithms or additional functionality as needed.
# The machine learning algorithms can be further enhanced by incorporating techniques such as cross-validation, hyperparameter tuning, and regularization to improve model performance and prevent overfitting.
# Overall, this code serves as a basic framework for implementing machine learning algorithms in a project and can be expanded upon to meet specific requirements and use cases.
# The code is written in Python and utilizes the scikit-learn library for the linear regression model. It is important to ensure that the necessary libraries are installed and properly imported to avoid any issues when running the code.
# The machine learning class can be easily integrated into a larger project, allowing for seamless incorporation of machine learning capabilities into various applications and systems.
# The code is intended for educational purposes and can be used as a starting point for learning about machine learning concepts and techniques. It is recommended to further explore the scikit-learn library and other machine learning frameworks to gain a deeper understanding of the field and its applications.
# The machine learning algorithms can be applied to a wide range of problems, including regression, classification, clustering, and more. By leveraging the power of machine learning, you can uncover insights from data, make predictions, and automate decision-making processes in various domains such as finance, healthcare, marketing, and beyond.



import numpy as np
from sklearn.linear_model import LinearRegression

class MachineLearning:
    def __init__(self):
        self.model = LinearRegression()
    def train(self, X, y):
        self.model.fit(X, y)
    def predict(self, X):
        return self.model.predict(X)
    def evaluate(self, X, y):
        return self.model.score(X, y)
# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])
    
    # Create an instance of the MachineLearning class
    ml = MachineLearning()
    
    # Train the model
    ml.train(X, y)
    
    # Predict using the model
    predictions = ml.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = ml.evaluate(X, y)
    print("Model Score:", score)

print("\n====================== K-Fold Cross Validation ===================================\n")
# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
# https://en.wikipedia.org/wiki/Confusion_matrix


from sklearn.model_selection import KFold

# Example of K-Fold Cross Validation
# K-Fold Cross Validation is a technique used to evaluate the performance of a machine learning model by splitting the data into K subsets (folds) 
# and training the model on K-1 folds while testing it on the remaining fold. This process is repeated K times, with each fold serving as the test 
# set once. The average performance across all folds is then calculated to provide an estimate of the model's generalization ability.

# In this example, we will use K-Fold Cross Validation to evaluate the performance of our linear regression model on the sample data. 
# We will split the data into 2 folds and train the model on one fold while testing it on the other fold, and then repeat this process for the second fold.

# Note: In a real-world application, you would typically use more folds (e.g., 5 or 10) to get a more reliable estimate of the model's performance. 
# Additionally, you may want to use techniques such as stratified K-Fold for classification problems to ensure that each fold has a representative distribution of the target variable.

# The KFold class from scikit-learn provides a convenient way to perform K-Fold Cross Validation. You can specify the number of folds using the n_splits parameter, 
# and the split method will generate the indices for the training and test sets for each fold.
# By using K-Fold Cross Validation, you can better assess the performance of your machine learning model and make informed decisions about model selection and hyperparameter tuning based on the results obtained from the cross-validation process.
# The code below demonstrates how to implement K-Fold Cross Validation using the KFold class from scikit-learn, and how to train and evaluate the model on each fold of the data.

if __name__ == "__main__":
    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])
    
    # Create an instance of the MachineLearning class
    ml = MachineLearning()
    
    # K-Fold Cross Validation
    kf = KFold(n_splits=2)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        print("Train Index:", train_index, "Test Index:", test_index)
        print("X_train:", X_train, "y_train:", y_train)
        print("X_test:", X_test, "y_test:", y_test)

        # Train the model on the training set
        ml.train(X_train, y_train)
        
        # Evaluate the model on the test set
        score = ml.evaluate(X_test, y_test)
        print("Fold Score:", score)

print("\n====================== Logistic Regression ===================================\n")
# Logistic Regression is a statistical method used for binary classification problems. It models the relationship between a dependent variable (target) 
# and one or more independent variables (features) by estimating probabilities using a logistic function.
# The logistic function, also known as the sigmoid function, maps any real-valued number into the (0, 1) interval, which can be interpreted as probabilities. 
# The logistic regression model estimates the parameters of the logistic function to best fit the data and make predictions about the probability of a certain class or outcome.

# In this example, we will use logistic regression to classify a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, 
# and we will use the LogisticRegression class from scikit-learn to train and evaluate the model.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. 
# Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance.

# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# https://en.wikipedia.org/wiki/Softmax_function

from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the LogisticRegression class
    model = LogisticRegression() # Create an instance of the LogisticRegression class from scikit-learn to perform logistic regression on the dataset. This model will be used to fit the data and make predictions based on the input features and target variable.
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)

print("\n========== # Example for plotting the decision boundary of the logistic regression model ============================\n")
# example for plotting the decision boundary of the logistic regression model
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the LogisticRegression class
    model = LogisticRegression()
    
    # Train the model
    model.fit(X, y)
    
    # Plotting the decision boundary
    plt.scatter(X, y, color='blue', label='Data Points')
    
    # Create a range of values for plotting the decision boundary
    x_values = np.linspace(0, 6, 100).reshape(-1, 1)
    y_values = model.predict_proba(x_values)[:, 1]  # Get the probability of class 1
    plt.figure("Logistic Regression Decision Boundary", figsize=(8, 6))
    plt.plot(x_values, y_values, color='red', label='Decision Boundary')
    plt.xlabel('Feature')
    plt.ylabel('Probability of Class 1')
    plt.title('Logistic Regression Decision Boundary')
    plt.legend()
    #plt.show()

print("\n========== # Example for Naive Bayes classifier ============================\n")
# Naive Bayes is a probabilistic machine learning algorithm based on Bayes' theorem, which assumes that the features are independent given the class label.
# It is commonly used for classification tasks, especially in text classification and spam filtering. The Naive Bayes classifier calculates the posterior probability of each class given the input features and predicts the class with the highest probability.
# In this example, we will use the GaussianNB class from scikit-learn to perform Naive Bayes classification on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance.
# https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html

from sklearn.naive_bayes import GaussianNB
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the GaussianNB class
    model = GaussianNB() # Create an instance of the GaussianNB class from scikit-learn to perform Naive Bayes classification on the dataset. This model will be used to fit the data and make predictions based on the input features and target variable.
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)



print("\n========== # Example for Support Vector Machine (SVM) classifier ============================\n")
# Support Vector Machine (SVM) is a powerful supervised learning algorithm used for classification and regression tasks. It works by finding the hyperplane that best separates the classes in the feature space. SVM can handle both linear and non-linear classification problems by using different kernel functions to transform the data into a higher-dimensional space where it becomes linearly separable.
# In this example, we will use the SVC class from scikit-learn to perform SVM classification on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance.
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
from sklearn.svm import SVC
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the SVC class
    model = SVC(kernel='linear') # Create an instance of the SVC class from scikit-learn to perform Support Vector Machine classification on the dataset. The kernel parameter is set to 'linear' to specify that we want to use a linear kernel for the SVM model.
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)

print("\n========== # Example for Decision Tree classifier ============================\n")
# Decision Tree is a popular supervised learning algorithm used for classification and regression tasks. It works by recursively splitting the data into subsets based on the feature that provides the best separation of the classes. The resulting tree structure can be used to make predictions by traversing the tree from the root to a leaf node, where the predicted class is determined by the majority class in that leaf node.
# In this example, we will use the DecisionTreeClassifier class from scikit-learn to perform decision tree classification on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance.
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html


from sklearn.tree import DecisionTreeClassifier
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the DecisionTreeClassifier class
    model = DecisionTreeClassifier() # Create an instance of the DecisionTreeClassifier class from scikit-learn to perform decision tree classification on the dataset. This model will be used to fit the data and make predictions based on the input features and target variable.
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)

print("\n========== # Example for Random Forest classifier ============================\n")
# Random Forest is an ensemble learning method that combines multiple decision trees to improve the performance and robustness of the model. It works by creating a collection of decision trees, where each tree is trained on a random subset of the data and features. The final prediction is made by aggregating the predictions from all the individual trees, typically using majority voting for classification tasks or averaging for regression tasks.
# In this example, we will use the RandomForestClassifier class from scikit-learn to perform random forest classification on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance.
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    # Sample data for binary classification with more features
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    y = np.array([0, 0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the RandomForestClassifier class
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y, predictions)
    print("Accuracy Score:", accuracy)

    # Feature importance
    print("Feature Importance:", model.feature_importances_)

print("\n========== # Example for K-Nearest Neighbors (KNN) classifier ============================\n")
# K-Nearest Neighbors (KNN) is a simple and intuitive supervised learning algorithm used for classification and regression tasks. It works by finding the K nearest neighbors to a given data point in the feature space and making predictions based on the majority class (for classification) or the average value (for regression) of those neighbors. The distance metric used to determine the nearest neighbors can be Euclidean distance, Manhattan distance, or other distance measures depending on the problem at hand.
# In this example, we will use the KNeighborsClassifier class from scikit-learn to perform KNN classification on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance. The choice of K (the number of neighbors) can also significantly impact the performance of the KNN algorithm, and it is often determined through experimentation or cross-validation.
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier
if __name__ == "__main__":
    # Sample data for binary classification with more features
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    y = np.array([0, 0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the KNeighborsClassifier class
    model = KNeighborsClassifier(n_neighbors=5)
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y, predictions)
    print("Accuracy Score:", accuracy)

print("\n========== # Example for Grid search CV ============================\n")
# Grid search CV (Cross Validation) is a technique used to find the best hyperparameters for a machine learning model by exhaustively searching through a specified grid of hyperparameter values. It involves training and evaluating the model for each combination of hyperparameters using cross-validation, and selecting the combination that yields the best performance based on a chosen evaluation metric.
# In this example, we will use the GridSearchCV class from scikit-learn to perform grid search cross-validation on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data. We will specify a grid of hyperparameters for a logistic regression model and use grid search to find the best combination of hyperparameters that maximizes the model's performance.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance. The choice of hyperparameters can significantly impact the performance of the model, and grid search CV provides a systematic way to find the optimal hyperparameters for your specific problem.
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the LogisticRegression class
    model = LogisticRegression()
    
    # Define a grid of hyperparameters to search
    param_grid = {
        'C': [0.1, 1, 10],  # Regularization strength
        'solver': ['liblinear', 'lbfgs']  # Optimization algorithm
    }
    
    # Create an instance of the GridSearchCV class
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=2) # Create an instance of the GridSearchCV class from scikit
    
    # Perform grid search cross-validation
    grid_search.fit(X, y)
    
    # Print the best hyperparameters and the best score
    print("Best Hyperparameters:", grid_search.best_params_)
    print("Best Score:", grid_search.best_score_)

print("\n========== # Example for K-Means ============================\n")
# K-Means is an unsupervised learning algorithm used for clustering tasks. It works by partitioning the data into K clusters based on the similarity of the data points. The algorithm iteratively assigns each data point to the nearest cluster center and then updates the cluster centers based on the mean of the assigned data points. This process continues until convergence, where the cluster assignments no longer change or a specified number of iterations is reached.
# In this example, we will use the KMeans class from scikit-learn to perform K-Means clustering on a simple dataset. We will create a dataset with two features and use K-Means to cluster the data into two clusters. We will then visualize the clusters using a scatter plot.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the clustering results using metrics such as silhouette score or Davies-Bouldin index to get a more comprehensive understanding of the quality of the clusters. The choice of K (the number of clusters) can also significantly impact the performance of the K-Means algorithm, and it is often determined through experimentation or methods such as the elbow method.
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans
if __name__ == "__main__":
    # Sample data for clustering
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    
    # Create an instance of the KMeans class
    kmeans = KMeans(n_clusters=3, random_state=42)
    
    # Fit the model to the data
    kmeans.fit(X)
    
    # Get the cluster centers and labels
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    print("Cluster Centers:\n", cluster_centers)
    print("Labels:", labels)
    plt.figure("K-Means Clustering", figsize=(8, 6))
    # Visualize the clusters
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('K-Means Clustering')
    plt.legend()
    #plt.show()

print("\n========== # Example for Principal Component Analysis (PCA) ============================\n")
# Principal Component Analysis (PCA) is a dimensionality reduction technique used to reduce the number of features in a dataset while retaining as much variance as possible. It works by identifying the principal components, which are linear combinations of the original features that capture the maximum variance in the data. PCA can be used for visualization, noise reduction, and feature extraction.
# In this example, we will use the PCA class from scikit-learn to perform PCA on a simple dataset. We will create a dataset with two features and use PCA to reduce it to one principal component. We will then visualize the original data and the transformed data in the new feature space.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the explained variance ratio to understand how much variance is retained in the reduced feature space. PCA can be sensitive to the scale of the features, so it is often recommended to standardize the data before applying PCA.
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
from sklearn.decomposition import PCA
if __name__ == "__main__":
    # Sample data for PCA
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    
    # Create an instance of the PCA class
    pca = PCA(n_components=1)
    
    # Fit and transform the data
    X_pca = pca.fit_transform(X)
    
    print("Original Data:\n", X)
    print("Transformed Data (PCA):\n", X_pca)
    
    # Visualize the original data and the transformed data
    plt.figure("Principal Component Analysis (PCA)", figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c='blue')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Original Data')
    
    plt.subplot(1, 2, 2)
    plt.scatter(X_pca[:, 0], np.zeros_like(X_pca[:, 0]), c='red')
    plt.xlabel('Principal Component 1')
    plt.title('Transformed Data (PCA)')
    
    plt.tight_layout()
    #plt.show()

print("\n========== # Example for Linear Discriminant Analysis (LDA) ============================\n")
# Linear Discriminant Analysis (LDA) is a supervised learning algorithm used for classification tasks. It works by finding a linear combination of features that best separates the classes in the feature space. LDA assumes that the data for each class is normally distributed and that the classes have equal covariance matrices. The algorithm projects the data onto a lower-dimensional space while maximizing the separation between the classes.
# In this example, we will use the LinearDiscriminantAnalysis class from scikit-learn to perform LDA on a simple dataset. We will create a dataset with two features and use LDA to reduce it to one linear discriminant. We will then visualize the original data and the transformed data in the new feature space.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the explained variance ratio to understand how much variance is retained in the reduced feature space. LDA can be sensitive to the assumptions of normality and equal covariance, so it is important to check these assumptions before applying LDA.
# https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
if __name__ == "__main__":
    # Sample data for LDA
    
    X = np.array([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])
    y = np.array([0, 0, 0, 1, 1, 1])

    lda = LinearDiscriminantAnalysis(n_components=1, solver='eigen', shrinkage='auto')
    X_lda = lda.fit_transform(X, y)

    print("X_lda:\n", X_lda)

    X_lda_1d = X_lda.ravel()

    plt.figure("Linear Discriminant Analysis (LDA)", figsize=(12, 6))

    # Original data
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Original Data")

    # LDA transformed data
    plt.subplot(1, 2, 2)
    plt.scatter(X_lda_1d, np.zeros_like(X_lda_1d), c=y, cmap='viridis')
    plt.xlabel("Linear Discriminant 1")
    plt.title("Transformed Data (LDA)")

    plt.tight_layout()
    #plt.show()

print("\n====================== Example for Kernel Principal Component Analysis (Kernel PCA) ===================================\n")
# Kernel Principal Component Analysis (Kernel PCA) is a non-linear dimensionality reduction technique that extends the traditional PCA by using kernel functions to project the data into a higher-dimensional feature space. This allows Kernel PCA to capture non-linear relationships in the data that may not be captured by linear PCA. The choice of kernel function (e.g., linear, polynomial, radial basis function) can significantly impact the performance of Kernel PCA, and it is often determined through experimentation or cross-validation.
# In this example, we will use the KernelPCA class from scikit-learn to perform Kernel PCA on a simple dataset. We will create a dataset with two features and use Kernel PCA to reduce it to one principal component. We will then visualize the original data and the transformed data in the new feature space.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the explained variance ratio to understand how much variance is retained in the reduced feature space. Kernel PCA can be sensitive to the choice of kernel and its parameters, so it is important to experiment with different kernels and parameter settings to find the best fit for your specific problem.
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html
from sklearn.decomposition import KernelPCA
if __name__ == "__main__":
    # Sample data for Kernel PCA
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    
    # Create an instance of the KernelPCA class
    kernel_pca = KernelPCA(n_components=1, kernel='rbf', gamma=15)
    
    # Fit and transform the data
    X_kpca = kernel_pca.fit_transform(X)
    
    print("Original Data:\n", X)
    print("Transformed Data (Kernel PCA):\n", X_kpca)
    
    # Visualize the original data and the transformed data
    plt.figure("Kernel Principal Component Analysis (Kernel PCA)", figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c='blue')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Original Data')
    
    plt.subplot(1, 2, 2)
    plt.scatter(X_kpca[:, 0], np.zeros_like(X_kpca[:, 0]), c='red')
    plt.xlabel('Principal Component 1')
    plt.title('Transformed Data (Kernel PCA)')
    
    plt.tight_layout()
    #plt.show()

print("\n====================== Example for Bootstrap Aggregating (Bagging) ===================================\n")
# Bootstrap Aggregating, also known as Bagging, is an ensemble learning technique that combines the predictions of multiple base models to improve the overall performance and reduce overfitting. The idea is to create multiple subsets of the training data by sampling with replacement (bootstrap samples) and then train a base model on each subset. The final prediction is made by aggregating the predictions from all the base models, typically using majority voting for classification tasks or averaging for regression tasks.
# In this example, we will use the BaggingClassifier class from scikit-learn to perform bagging on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data. We will specify a base estimator (e.g., DecisionTreeClassifier) and use bagging to create an ensemble of models that can improve the performance compared to a single base model.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance. The choice of base estimator and the number of estimators (n_estimators) can significantly impact the performance of the bagging ensemble, and it is often determined through experimentation or cross-validation.
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the BaggingClassifier class with a DecisionTreeClassifier as the base estimator
    model = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42)
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y, predictions)
    print("Accuracy Score:", accuracy)

print("\n====================== Example for AdaBoost (Adaptive Boosting) ===================================\n")
# AdaBoost, short for Adaptive Boosting, is an ensemble learning technique that combines multiple weak learners to create a strong learner. The algorithm works by iteratively training weak learners on the training data, where each subsequent learner focuses more on the samples that were misclassified by the previous learners. The final prediction is made by combining the predictions of all the weak learners, typically using a weighted majority vote for classification tasks or a weighted average for regression tasks.
# In this example, we will use the AdaBoostClassifier class from scikit-learn to perform AdaBoost on a simple dataset. We will create a binary classification problem where the target variable is 0 or 1, and we will train and evaluate the model using the sample data. We will specify a base estimator (e.g., DecisionTreeClassifier) and use AdaBoost to create an ensemble of weak learners that can improve the performance compared to a single base model.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as accuracy, precision, recall, and F1-score to get a more comprehensive understanding of its performance. The choice of base estimator and the number of estimators (n_estimators) can significantly impact the performance of the AdaBoost ensemble, and it is often determined through experimentation or cross-validation.
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html
from sklearn.ensemble import AdaBoostClassifier
if __name__ == "__main__":
    # Sample data for binary classification
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 1, 1, 1])  # Binary target variable
    
    # Create an instance of the AdaBoostClassifier class with a DecisionTreeClassifier as the base estimator
    model = AdaBoostClassifier(estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42)
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score:", score)
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y, predictions)
    print("Accuracy Score:", accuracy)

print("\n====================== Example for Linear Regression ===================================\n")
# Linear Regression is a supervised learning algorithm used for regression tasks. It models the relationship between a dependent variable (target) and one or more independent variables (features) by fitting a linear equation to the observed data. The goal of linear regression is to find the best-fitting line that minimizes the sum of squared differences between the observed values and the predicted values.
# In this example, we will use the LinearRegression class from scikit-learn to perform linear regression on a simple dataset. We will create a dataset with one feature and a continuous target variable, and we will train and evaluate the model using the sample data. We will also visualize the original data and the fitted line to understand the relationship between the feature and the target variable.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as mean squared error (MSE), mean absolute error (MAE), or R-squared to get a more comprehensive understanding of its performance. Linear regression assumes a linear relationship between the features and the target variable, so it may not perform well if the underlying relationship is non-linear.
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
from sklearn.linear_model import LinearRegression
if __name__ == "__main__":
    # Sample data for linear regression
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])  # Continuous target variable
    
    # Create an instance of the LinearRegression class
    model = LinearRegression()
    
    # Train the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X, y)
    print("Model Score (R-squared):", score)
    
    # Visualize the original data and the fitted line
    plt.figure("Linear Regression", figsize=(8, 6))
    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X, predictions, color='red', label='Fitted Line')
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('Linear Regression')
    plt.legend()
    #plt.show()

print("============== Example for Regularization with Lasso, Ridge and ElasticNet =============================\n")
# Regularization is a technique used to prevent overfitting in machine learning models by adding a penalty term to the loss function. Lasso (L1 regularization), Ridge (L2 regularization), and ElasticNet (a combination of L1 and L2 regularization) are common regularization methods used in linear regression. Lasso can shrink some coefficients to zero, effectively performing feature selection, while Ridge shrinks coefficients towards zero but does not set any coefficients exactly to zero. ElasticNet combines the properties of both Lasso and Ridge, allowing for both feature selection and coefficient shrinkage.
# In this example, we will use the Lasso, Ridge, and ElasticNet classes from scikit-learn to perform regularization on a simple dataset. We will create a dataset with one feature and a continuous target variable, and we will train and evaluate the models using the sample data. We will also visualize the original data and the fitted lines for each regularization method to understand the impact of regularization on the model's performance.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the models using metrics such as mean squared error (MSE), mean absolute error (MAE), or R-squared to get a more comprehensive understanding of their performance. The choice of regularization method and the regularization strength (alpha) can significantly impact the performance of the model, and it is often determined through experimentation or cross-validation.
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
from sklearn.linear_model import Lasso, Ridge, ElasticNet
if __name__ == "__main__":
    # Sample data for regularization
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])  # Continuous target variable
    
    # Create instances of the Lasso, Ridge, and ElasticNet classes
    lasso = Lasso(alpha=0.1)
    ridge = Ridge(alpha=0.1)
    elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
    
    # Train the models
    lasso.fit(X, y)
    ridge.fit(X, y)
    elastic_net.fit(X, y)
    
    # Predict using the models
    lasso_predictions = lasso.predict(X)
    ridge_predictions = ridge.predict(X)
    elastic_net_predictions = elastic_net.predict(X)
    
    print("Lasso Predictions:", lasso_predictions)
    print("Ridge Predictions:", ridge_predictions)
    print("ElasticNet Predictions:", elastic_net_predictions)
    
    # Evaluate the models
    lasso_score = lasso.score(X, y)
    ridge_score = ridge.score(X, y)
    elastic_net_score = elastic_net.score(X, y)
    
    print("Lasso Model Score (R-squared):", lasso_score)
    print("Ridge Model Score (R-squared):", ridge_score)
    print("ElasticNet Model Score (R-squared):", elastic_net_score)

    # Visualize the original data and the fitted lines for each regularization method
    plt.figure("Regularization with Lasso, Ridge, and ElasticNet", figsize=(12, 6))
    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X, lasso_predictions, color='red', label='Lasso Fit')
    plt.plot(X, ridge_predictions, color='green', label='Ridge Fit')
    plt.plot(X, elastic_net_predictions, color='orange', label='ElasticNet Fit')
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('Regularization with Lasso, Ridge, and ElasticNet')
    plt.legend()
    #plt.show()

print("\n====================== Example for Polynomial Regression ===================================\n")
# Polynomial Regression is a type of regression analysis that models the relationship between the independent variable(s) and the dependent variable as an nth degree polynomial. It is used when the relationship between the variables is non-linear. By adding polynomial features to the dataset, we can fit a non-linear curve to the data, which can capture more complex relationships than linear regression.
# In this example, we will use the PolynomialFeatures class from scikit-learn to create polynomial features from a simple dataset. We will then use the LinearRegression class to fit a polynomial regression model to the data. We will visualize the original data and the fitted curve to understand the relationship between the feature and the target variable.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as mean squared error (MSE), mean absolute error (MAE), or R-squared to get a more comprehensive understanding of its performance. The choice of polynomial degree can significantly impact the performance of the model, and it is often determined through experimentation or cross-validation.
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
from sklearn.preprocessing import PolynomialFeatures
if __name__ == "__main__":
    # Sample data for polynomial regression
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])  # Continuous target variable
    
    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    
    # Create an instance of the LinearRegression class
    model = LinearRegression()
    
    # Train the model on the polynomial features
    model.fit(X_poly, y)
    
    # Predict using the model
    predictions = model.predict(X_poly)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X_poly, y)
    print("Model Score (R-squared):", score)
    
    # Visualize the original data and the fitted curve
    plt.figure("Polynomial Regression", figsize=(8, 6))
    plt.scatter(X, y, color='blue', label='Data Points')
    
    # Generate a range of values for plotting the polynomial curve
    X_range = np.linspace(1, 5, 100).reshape(-1, 1)
    X_range_poly = poly.transform(X_range)
    curve_predictions = model.predict(X_range_poly)
    
    plt.plot(X_range, curve_predictions, color='red', label='Fitted Curve')
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('Polynomial Regression')
    plt.legend()
    #plt.show()

print("\n====================== Example for RANSAC Regression ===================================\n")
# RANSAC (Random Sample Consensus) Regression is a robust regression algorithm that is used to fit a model to data that may contain outliers. It works by iteratively selecting random subsets of the data, fitting a model to those subsets, and then determining how many data points from the entire dataset fit the model within a certain tolerance. The model with the highest number of inliers (data points that fit the model) is selected as the final model.
# In this example, we will use the RANSACRegressor class from scikit-learn to perform RANSAC regression on a simple dataset. We will create a dataset with one feature and a continuous target variable, and we will introduce some outliers to demonstrate the robustness of RANSAC. We will train and evaluate the model using the sample data, and we will visualize the original data, the fitted line, and the inliers identified by RANSAC.
# Note: In a real-world application, you would typically use more complex datasets and may need to perform data preprocessing, feature engineering, and model selection to achieve better performance. Additionally, you may want to evaluate the model using metrics such as mean squared error (MSE), mean absolute error (MAE), or R-squared to get a more comprehensive understanding of its performance. RANSAC can be sensitive to the choice of parameters such as the maximum number of iterations and the residual threshold, so it is important to experiment with these parameters to find the best fit for your specific problem.
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html
from sklearn.linear_model import RANSACRegressor
if __name__ == "__main__":
    # Sample data for RANSAC regression
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])  # Continuous target variable
    
    # Introduce some outliers
    X_outliers = np.array([[6], [7]])
    y_outliers = np.array([20, 25])
    
    X_combined = np.vstack((X, X_outliers))
    y_combined = np.hstack((y, y_outliers))
    
    # Create an instance of the RANSACRegressor class
    model = RANSACRegressor(random_state=42)
    
    # Train the model
    model.fit(X_combined, y_combined)
    
    # Predict using the model
    predictions = model.predict(X_combined)
    print("Predictions:", predictions)
    
    # Evaluate the model
    score = model.score(X_combined, y_combined)
    print("Model Score (R-squared):", score)
    
    # Visualize the original data, the fitted line, and the inliers identified by RANSAC
    plt.figure("RANSAC Regression", figsize=(8, 6))
    plt.scatter(X_combined, y_combined, color='blue', label='Data Points')
    
    # Generate a range of values for plotting the fitted line
    X_range = np.linspace(1, 7, 100).reshape(-1, 1)
    line_predictions = model.predict(X_range)
    
    plt.plot(X_range, line_predictions, color='red', label='Fitted Line')
    
    # Identify inliers and outliers
    inlier_mask = model.inlier_mask_
    outlier_mask = ~inlier_mask
    
    plt.scatter(X_combined[inlier_mask], y_combined[inlier_mask], color='green', label='Inliers')
    plt.scatter(X_combined[outlier_mask], y_combined[outlier_mask], color='orange', label='Outliers')
    
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('RANSAC Regression')
    plt.legend()
    plt.show()