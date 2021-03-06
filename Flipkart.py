# -*- coding: utf-8 -*-
"""Grid (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0BxUnr1HHotMNS1p2WVQ2TjI2bTc0SlRZS3ctc185NUtZNEp3

Load the csv files into Google drive
"""

from google.colab import drive
drive.mount('/content/gdrive',force_remount=True)

"""importing all the essential directories"""

import keras
from keras.models import Model, Sequential, model_from_json
from keras.optimizers import SGD
from keras.layers import Dense, Dropout, Flatten, Input
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, concatenate,Activation
from keras import regularizers
import numpy as np
import glob
import cv2
import numpy as np
import csv 
import os
from numpy import genfromtxt

"""Inception module"""

def inception():
    inputs = Input(shape=(480, 640, 3))
    input_img = Conv2D(2, (7,7), strides = (2,2), activation='relu')(inputs)
    input_img = Conv2D(3, (5,5), activation='relu')(input_img)
    
    tower_4 = MaxPooling2D((3,3), strides=(2,2), padding='same')(input_img)
    
    tower_5 = Conv2D(6, (6,6), strides=(2,2), padding='same', activation='relu')(input_img)
    
    input_img = concatenate([tower_4, tower_5], axis = 3)
    
    tower_1 = AveragePooling2D((3,3), strides=(1,1), padding='same')(input_img)
    tower_1 = Conv2D(3, (1,1), padding='same', activation='relu')(tower_1)
    
    tower_2 = Conv2D(3, (1,1), padding='same', activation='relu')(input_img)
    tower_2 = Conv2D(3, (3,3), padding='same', activation='relu')(tower_2)
    
    tower_3 = Conv2D(3, (1,1), padding='same', activation='relu')(input_img)
    tower_3 = Conv2D(3, (5,1), padding='same', activation='relu')(tower_3)
    tower_3 = Conv2D(3, (1,5), padding='same', activation='relu')(tower_3)
    
    outputs = concatenate([tower_1, tower_2, tower_3], axis = 3)
    
    dense = MaxPooling2D((3, 3), strides=(2,2))(outputs)
    dense = Flatten(name='flatten')(dense)
    dense = Dense(128, activation='relu', name='dense_1')(dense)
    dense = Dropout(0.5)(dense)
    dense = Dense(2, name='dense_2')(dense)
    
    prediction = Activation('sigmoid', name='sigmoid')(dense)
    
    model = Model(input=inputs, output=prediction)
    
    return model

"""compiling the created inception model"""

model1=inception()
model1.compile(loss="mean_squared_error",optimizer="adam",metrics=['accuracy'])

model2=inception()
model2.compile(loss="mean_squared_error",optimizer="adam",metrics=['accuracy'])

"""training the images and saving the both the models weights and saving the results in a csv file(result.csv)"""

# Set the path to folder containing training images and train.csv
os.chdir('/content/gdrive/My Drive/images')
ans=0
X_train1=list()
Y_train1=list()

X_Val1=list()
Y_Val1=list()

mpg_data = np.genfromtxt('training_set.csv',delimiter=',',dtype=str)

for i in range(1,len(mpg_data),240):
      img = cv2.imread(mpg_data[i][0])
      if img is not None:
        X_Val1.append(img)
        Y_Val1.append(list(map(int, mpg_data[i][1:3])))
X_Val1=np.array(X_Val1)
X_Val1=X_Val1/255
Y_Val1=np.array(Y_Val1).astype(float)
Y_Val1[:,0:2]=Y_Val1[:,0:2]/640.0

for i in range(1,len(mpg_data)):

    if i%100 ==0:
      print(i)
      X_train1=np.array(X_train1)
      X_train1=X_train1/255
      Y_train1=np.array(Y_train1).astype(float)
      Y_train1[:,0:2]=Y_train1[:,0:2]/640.0
      # Fit the model
      model1.fit(X_train1, Y_train1,validation_data=(X_Val1,Y_Val1), epochs=1, batch_size=20)
      X_train1=list()
      Y_train1=list()

    if i!=0:
      img = cv2.imread(mpg_data[i][0])
      if img is not None:
        X_train1.append(img)
        Y_train1.append(list(map(int, mpg_data[i][1:3])))
    if i%1000 == 0:
      model_json = model1.to_json()
      with open("model_.json", "w") as json_file:
          json_file.write(model_json)
      # serialize weights to HDF5
      model1.save_weights("model_a12.h5")
      print("Saved model to disk")

X_train2=list()
Y_train2=list()

X_Val2=list()
Y_Val2=list()

mpg_data = np.genfromtxt('training_set.csv',delimiter=',',dtype=str)

for i in range(1,len(mpg_data),240):
      img = cv2.imread(mpg_data[i][0])
      if img is not None:
        X_Val2.append(img)
        Y_Val2.append(list(map(int, mpg_data[i][3:5])))
X_Val2=np.array(X_Val2)
X_Val2=X_Val2/255
Y_Val2=np.array(Y_Val2).astype(float)
Y_Val2[:,2:4]=Y_Val2[:,2:4]/480.0

for i in range(1,len(mpg_data)):

    if i%100 ==0:
      print(i)
      X_train2=np.array(X_train2)
      X_train2=X_train/255
      Y_train2=np.array(Y_train2).astype(float)
      Y_train2[:,2:4]=Y_train2[:,2:4]/480.0
      # Fit the model
      model2.fit(X_train2, Y_train2,validation_data=(X_Val2,Y_Val2), epochs=1, batch_size=20)
      X_train=list()
      Y_train2=list()

    if i!=0:
      img = cv2.imread(mpg_data[i][0])
      if img is not None:
        X_train2.append(img)
        Y_train2.append(list(map(int, mpg_data[i][3:5])))
    if i%1000 == 0:
      model_json = model2.to_json()
      with open("model_.json", "w") as json_file:
          json_file.write(model_json)
      # serialize weights to HDF5
      model2.save_weights("model_a13.h5")
      print("Saved model to disk")

"""Loading the saved inception modules for testing"""

os.chdir('/content/gdrive/My Drive/images')
loaded_model=inception()
# load weights into new model
loaded_model.load_weights("model_a12.h5")
loaded_model.compile(loss="mean_squared_error",optimizer="adam",metrics=['accuracy'])

model2=inception()
# load weights into new model
model2.load_weights("model_a13.h5")
model2.compile(loss="mean_squared_error",optimizer="adam",metrics=['accuracy'])

X_test=list()
img_test = list()
out = open('result.csv', "w")
out.write("image_name,x1,x2,y1,y2\n")
mpg_data = np.genfromtxt('test.csv',delimiter=',',dtype=str)

for i in range(1,len(mpg_data)):
        if i%100 ==0 and i!=0:
          print(i)
          X_test=np.array(X_test)
          X_test=X_test/255
          # Fit the model
          Y_test1 = loaded_model.predict(X_test)
          Y_test2 = model2.predict(X_test)
          rows =['']*len(Y_test1)
          for j in range(len(Y_test1)):
            rows[j]='%s,%s,%s,%s,%s\n' % (img_test[j],int(Y_test1[j][0]*640),int(Y_test1[j][1]*640),int(Y_test2[j][0]*480),int(Y_test2[j][1]*480))
            print(rows[j])
          out.writelines(rows)
          img_test = list()
          X_test = list()
        if i!=0:
          img = cv2.imread(mpg_data[i][0])
          if img is not None:
            X_test.append(img)
            img_test.append(mpg_data[i][0])

X_test=np.array(X_test)
X_test=X_test/255
# Fit the model
Y_test1 = loaded_model.predict(X_test)
Y_test2 = model2.predict(X_test)
rows =['']*len(Y_test1)
for j in range(len(Y_test1)):
  rows[j]='%s,%s,%s,%s,%s\n' % (img_test[j],int(Y_test1[j][0]*640),int(Y_test1[j][1]*640),int(Y_test2[j][0]*480),int(Y_test2[j][1]*480))
  print(rows[j])
out.writelines(rows)
img_test = list()
X_test = list()
out.close()

"""Downloading the result.csv file from drive"""

os.chdir('/content/gdrive/My Drive/images')
from google.colab import files
downloaded = files.download('result.csv')
