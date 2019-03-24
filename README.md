# Flipkart-Grid-Challenge
Object localisation Challenge->
The Problem Statement was to draw a bounding bounding box around the objects present in the image.
x1,x2,y1,y2 are the bounding lines which bound the object in the image(480x640).

![alt text](https://github.com/anirudhjack/Flipkart-Grid-Challenge/Flipkart.jpeg)


# Approach for the Problem Statement.
The Flipkart.ipynb is written in google colab.
Due to memory issues only 100 images are trained at a time.


Now to draw the bounding box two Inception Modules are used :-
One for drawing x1 and x2.
Other for drawing y1 and y2.
Then trained images using this modules and saved results in a csv file.

# Data
Data is provided in the Data folder
The Folder has only 100 images for training.
