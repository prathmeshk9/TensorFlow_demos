import tensorflow as tf

a = tf.constant(4,name="input_a")
b = tf.constant(3,name="input_b")
c = tf.add(a,b,name="add_c")
#d = tf.multiply(a,b,name="mul_d")
#e = tf.multiply(c,d,name="mul_e")

sess = tf.Session()
print(sess.run(c))

writer = tf.summary.FileWriter('./demo_graph',sess.graph);
