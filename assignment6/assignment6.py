import tensorflow as tf

# create the tensor
nt = [4,3]

a = tf.constant(nt,name="constant_a")
b = tf.reduce_sum(a,name="sum_b")
c = tf.reduce_prod(a,name="mul_c")

sess = tf.Session()
print(sess.run(c))

writer = tf.summary.FileWriter('./my_graph',sess.graph)

