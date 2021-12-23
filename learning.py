#! /usr/bin/env python

"""
Modul zawiera klase do nauki sieci kerasem
"""
import keras
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import optimizers

from data_parsers.classify_data import ClassifyData
from data_parsers.learning_data import LearningData


class Learning:

    def __init__(self, input_size: int, output_size: int):
        # Wzorowalem sie na https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
        # UWAGA - dla kazdych danych nalezy zmienic strukture sieci!!!
        self.__model = tf.keras.Sequential([
            #tf.keras.layers.Dense(output_size,  input_dim=input_size, activation='sigmoid'),# input ~= 22 - bierzemy nastepna warstwe troszke wieksza
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

    def save_model(self, path: str):
        if self.__model is not None:
            self.__model.save(path)

class LearningClassify:
    def __init__(self, model_path: str):
        self.__model = keras.models.load_model(model_path)

    def classify(self, data: ClassifyData):
        data = data.get_classify_data()
        classes = self.__model.predict(data)
        for c in classes:
            print(c)
        return classes