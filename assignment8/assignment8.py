"""
Assignment of Get Started TO TensorFLOW
https://www.tensorflow.org/get_started/get_started
"""

import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)

print(node1,node2)

sess = tf.Session()
print(sess.run([node1,node2]))

node3 = tf.add(node1,node2)
print(sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

print(sess.run(adder_node,{a:3,b:4.5}))  # single values

print(sess.run(adder_node,{a:[1,3],b:[2,4]}))  # two dimentional array

add_triple = adder_node * 3
print(sess.run(add_triple,{a:3,b:4.5}))     # adder_node multiply by 3

w = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
x = tf.placeholder(tf.float32)
linear_model = w * x + b

"""
Constants are initialized when you call tf.constant, and their value can never change.
 By contrast, variables are not initialized when you call tf.Variable. 
 To initialize all the variables in a TensorFlow program, you must explicitly call 
 a special operation as follows:
"""

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model,{x:[1,2,3,4]}))

"""
We've created a model, but we don't know how good it is yet. To evaluate the model on training data, 
we need a y placeholder to provide the desired values, and we need to write a loss function. 

A loss function measures how far apart the current model is from the provided data. We'll use a standard 
loss model for linear regression, which sums the squares of the deltas between the current model and the 
provided data. linear_model - y creates a vector where each element is the corresponding example's error delta. 
We call tf.square to square that error. Then, we sum all the squared errors to create a single scalar that 
abstracts the error of all examples using tf.reduce_sum:
"""

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

"""
We could improve this manually by reassigning the values of W and b to the perfect values of -1 and 1. 
A variable is initialized to the value provided to tf.Variable but can be changed using operations 
like tf.assign. For example, W=-1 and b=1 are the optimal parameters for our model. We can change W and b 
accordingly:
"""

fixw = tf.assign(w,[-1.])
fixb = tf.assign(b,[1.])

sess.run([fixw,fixb])
print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

"""
A complete discussion of machine learning is out of the scope of this tutorial. However, TensorFlow 
provides optimizers that slowly change each variable in order to minimize the loss function. 
The simplest optimizer is gradient descent. It modifies each variable according to the magnitude 
of the derivative of loss with respect to that variable. In general, computing symbolic derivatives 
manually is tedious and error-prone. Consequently, TensorFlow can automatically produce derivatives 
given only a description of the model using the function tf.gradients. For simplicity, optimizers 
typically do this for you. For example,
"""

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)

for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
print(sess.run([w,b]))