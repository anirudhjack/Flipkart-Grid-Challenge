## Flipkart-Grid-Challenge
#Object localisation Challenge->
The Problem Statement was to draw a bounding bounding box around the objects present in the image.
x1,x2,y1,y2 are the bounding lines which bound the object in the image(480x640).
The accuracy Metric is Intersection by union.

![Flipkart](https://user-images.githubusercontent.com/48343220/54883570-bc1e4880-4e8c-11e9-97ca-420f2ddd5f4c.jpg)



# Approach for the Problem Statement.
The Flipkart.ipynb is written in google colab.
To draw the bounding box two Inception Modules are used :-
One model for drawing x1 and x2.
Other model for drawing y1 and y2.
Then trained images using this modules and saved results in a csv file.

# Data
Data is provided in the Data folder
The Folder has only 100 images for training.
