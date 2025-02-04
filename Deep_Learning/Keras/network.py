import numpy as np
from keras.utils import np_utils
import tensorflow as tf
tf.python.control_flow_ops = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0,0],[0,1],[1,0],[1,1]]).astype('float32')
y = np.array([[0],[1],[1],[0]]).astype('float32')

# Initial Setup for Keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# Building the model
xor = Sequential()

# Add required layers
# xor.add()

xor.add(Dense(6, input_dim=X.shape[1]))

# Add a tanh activation layer
xor.add(Activation('tanh'))

# Output Layer - Add a fully connected output layer
xor.add(Dense(1))

# activation function of o/p layer, a sigmoid activation layer
xor.add(Activation('sigmoid'))


# Specify loss as "binary_crossentropy", optimizer as "adam",
# and add the accuracy metric
xor.compile(loss="binary_crossentropy", optimizer="adam", metrics = ["accuracy"])

# Uncomment this line to print the model architecture
xor.summary()

# Fitting the model
history = xor.fit(X, y, nb_epoch=100, verbose=0)

# Scoring the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))