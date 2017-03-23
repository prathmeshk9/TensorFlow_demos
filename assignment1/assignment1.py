# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:46:46 2017
Hello World Program in TensorFlow with addition Computation
@author: admin
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
#sess.run(a+b)
print('addition -> ',sess.run(a+b));
