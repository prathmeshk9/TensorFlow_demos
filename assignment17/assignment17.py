# SVD example in TensorFlow
import numpy as np
import matplotlib.pyplot as plt
la = np.linalg
words = ["I","Like","enjoy","deep","learning","NLP","flying","."]

X = np.array([[0,2,1,0,0,0,0,0],
			  [2,0,0,1,0,1,0,0],
			  [1,0,0,0,0,0,1,0],
			  [0,1,0,0,1,0,0,0],
			  [0,0,0,1,0,0,0,1],
			  [0,1,0,0,0,0,0,1],
			  [0,0,1,0,0,0,0,1],
			  [0,0,0,0,1,1,1,0]])
			  
U, s, Vh = la.svd(X,full_matrices=False)

for i in range(len(words)):
	plt.text(U[i,0],U[i,1],words[i])

plt.show()