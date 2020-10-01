import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

sess = tf.Session()

YEHS = tf.constant('YEHS')
print(sess.run(YEHS).decode())

# Add your name and print it :)
JHSEO = tf.constant('Jun Ho Seo')
print(sess.run(JHSEO).decode())