import numpy as np  

def pca(X, n_components):  
    # Center data  
    X_centered = X - np.mean(X, axis=0)  
    # Covariance matrix  
    cov = np.cov(X_centered, rowvar=False)  
    # Eigen decomposition  
    eigenvalues, eigenvectors = np.linalg.eig(cov)  
    # Sort and select top components  
    idx = np.argsort(eigenvalues)[::-1]  
    return eigenvectors[:, idx[:n_components]]  

# Example: Reduce 3D data to 2D  
data = np.random.rand(100, 3)  
pca_result = pca(data, 2)  
print("PCA output shape:", pca_result.shape)  