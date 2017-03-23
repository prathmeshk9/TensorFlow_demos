import tensorflow as tf
g = tf.Graph()
with g.as_default():
	c = tf.constant(30)
assert c.graph is g
indefalutgraph = tf.add(1,2,name="indefalutgraph")
with g.as_default():
	ingraphg = tf.multiply(2,3,name="ingraphg")
alsoindefgraph = tf.subtract(5,1,name="alsoindef")
sess = tf.Session()
writer = tf.summary.FileWriter('./my_graph',sess.graph);