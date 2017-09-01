#import Keras libs and packages

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Init CNN
classifier = Sequential()

# Add layers
# Steps : Convolution - Max Pooling - Flattening - Full Connection

# Convolution
# For better result use 64 ( for input shape 128 | 256 ) *** Better Use the GPU ***
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))

# Max Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Flattening
classifier.add(Flatten())

# Full Connection
classifier.add(Dense(128,activation='relu'))
classifier.add(Dense(1,activation='sigmoid'))

# Compiling the CNN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Image Augmentation from https://keras.io/preprocessing/image/

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
# (target_size 64 in the -Convolution- )
train_generator = train_datagen.flow_from_directory('dataset/training_set',target_size=(64, 64),batch_size=32,class_mode='binary')
validation_generator = test_datagen.flow_from_directory('dataset/test_set', target_size=(64, 64),batch_size=32,class_mode='binary')

classifier.fit_generator(train_generator,steps_per_epoch=8000,epochs=25,validation_data=validation_generator,validation_steps=2000)
