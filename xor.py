from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
import time
import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
z = np.array([[0, 0], ])

print(x)
model = Sequential()
model.add(Dense(3, input_dim=2, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

sgd = SGD(lr=0.1)
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer=sgd)
start = time.time()
model.fit(x, y, batch_size=1, nb_epoch=300)
end = time.time()
delta = end - start
print(model.predict_proba(x))

score = model.evaluate(x, y,  verbose=0)
print('accuracy:', score[1])
print('score:', score[0])
predict = model.predict(z)
print(predict)
print('time = ', delta)
