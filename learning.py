#! /usr/bin/env python3

"""
Modul zawiera klase do nauki sieci kerasem
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models, optimizers
import matplotlib.pyplot as plt

from data_parsers.image_learning_data import ImageLearningData
from data_parsers.learning_data import LearningData


class Learning:

    def __init__(self, input_size: int, output_size: int):
        # Wzorowalem sie na https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
        # UWAGA - dla kazdych danych nalezy zmienic strukture sieci!!!
        self.__model = tf.keras.Sequential([
            tf.keras.layers.Dense(2*input_size,  input_dim=input_size, activation='relu'),# input ~= 22 - bierzemy nastepna warstwe troszke wieksza
            tf.keras.layers.Dense(3*output_size, activation='relu'),# warstwa powinan byc wieksza niz output
            tf.keras.layers.Dense(output_size, activation="sigmoid")# output =4 w testach
        ])
        self.__model.summary()
        opt = optimizers.Adam(learning_rate=5e-5)
        self.__model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

    def learn(self, data: LearningData, epochs: int, batch_size: int):
        features, classes = data.get_training_data()
        test_features, test_classes = data.get_testing_data()
        return self.__model.fit(features, classes, epochs=epochs, batch_size=batch_size,
                         validation_data=(test_features, test_classes))

    def plot_history(self, history):
        fig, ax = plt.subplots()
        ax.plot(history.history['accuracy'], label='accuracy')
        ax.plot(history.history['val_accuracy'], label='val_accuracy')
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Accuracy')
        ax.set_ylim([0.2, 1])
        ax.legend(loc='lower right')
        plt.show()

class ImageLearning:

    def __init__(self, input_size: int, output_size: int):
        # Wzorowalem sie na https://www.tensorflow.org/tutorials/images/cnn?hl=en
        # UWAGA - dla kazdych danych nalezy zmienic strukture sieci!!!
        self.__model = models.Sequential()
        self.__model.add(layers.Conv2D(input_size, (1, 1), activation='relu', input_shape=(input_size, input_size, 1)))
        self.__model.add(layers.MaxPooling2D((2, 2)))
        self.__model.add(layers.Conv2D(2*input_size, (1, 1), activation='relu'))
        self.__model.add(layers.MaxPooling2D((2, 2)))
        self.__model.add(layers.Conv2D(2*input_size, (1, 1), activation='relu'))
        self.__model.add(layers.MaxPooling2D((2, 2)))
        self.__model.add(layers.Flatten())
        self.__model.add(layers.Dense(output_size, activation="sigmoid"))
        self.__model.summary()

        opt = optimizers.Adam(learning_rate=1e-5)
        self.__model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

    def learn(self, data: ImageLearningData, epochs: int, batch_size: int):
        features, classes = data.get_training_data()
        test_features, test_classes = data.get_testing_data()
        return self.__model.fit(features, classes, epochs=epochs, batch_size=batch_size,
                         validation_data=(test_features, test_classes))

    def plot_history(self, history):
        fig, ax = plt.subplots()
        ax.plot(history.history['accuracy'], label='accuracy')
        ax.plot(history.history['val_accuracy'], label='val_accuracy')
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Accuracy')
        ax.set_ylim([0.2, 1])
        ax.legend(loc='lower right')
        plt.show()
