#! /usr/bin/env python3

"""
Modul zawiera klase do nauki sieci kerasem
"""

import tensorflow as tf

class Learning:

    def __init__(self, input_size: int, output_size: int):
        # Wzorowalem sie na https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
        # UWAGA - dla kazdych danych nalezy zmienic strukture sieci!!!
        self.__model = tf.keras.Sequential([
            tf.keras.layers.Dense(8,  input_dim=input_size, activation='relu'),# input ~= 22 - bierzemy nastepna warstwe troszke wieksza
            #tf.keras.layers.Dense(8, activation='relu'),# warstwa powinan byc wieksza niz output
            tf.keras.layers.Dense(output_size)# output =4 w testach
        ])
        self.__model.summary()
        self.__model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def learn(self, features, classes, epochs, batch_size):
        #np.asarray(classes).astype('float32').reshape((-1, 1))
        self.__model.fit(features, classes, epochs=epochs, batch_size=batch_size)

    def attach_generator(self, generator):
        self.__model

