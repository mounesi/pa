# Road Assess:
## a machine vision tool for roadway assessment.
Check the web application by clicking [here!](http://sohiai.com:8501/) it may take a minute to load. Slides are available [here!](https://drive.google.com/file/d/1kkndJiWxvidbQfpAiQ053NZJzN-4_53u/view)

![Web App](/images/webapp.png)

## Problem Statement
Roads are an essential part of the transportation system. 
Recently, roadways index in the US rated as D. Pavement condition is one of the critical indicators of regional prosperity and public well-being. If the department of transportation has a tool to evaluate the pavement, they can expedite the process of pavement assessment and budget allocation to fix them.
Older roads tend to deteriorate faster due to environmental conditions such as high traffic and climate fluctuation.
Assessment of these roads is often expensive, and some cities have tight budgets to assess the region's entirety.

The yearly budget used in this evaluation is between $200,000 and $230,000. The system has been extended for ten years and includes between 2 to 4 roadways per year that can be repaved[1]. The statistics show that the age of these roads is 19 years old, and 20% of them have inadequate conditions.

This project aims to develop a web app tool to grade roads using machine vision for the users at the department of transportation.
![crack image](/images/crack.png)

## Model Pipeline
It all starts from an image of pavement, which is accessing images from static google street view API. The machine vision model is then used to extract features such as the number of distress, area of the crack, severity of cracks, type of the distresses such as alligator, potholes, longitudinal, or joint cracks. On the other hand, there are databases available to provide additional features such as the roads' length, the roads' width, and the last time the road was resurfaced. With all roadway data combined, A regression model can estimate the pavement condition index for every street and ultimately generate a heatmap with repairing construction recommendation. 
![model pipeline](/images/model_pipeline.png)


## Machine Vision
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/OxOXjhtULTk/0.jpg)](http://www.youtube.com/watch?v=OxOXjhtULTk)

[![Alt text](https://youtu.be/OxOXjhtULTk/0.jpg)](https://youtu.be/OxOXjhtULTk)

I have manually labeled 3 street on google street view image by an online software called "make sense' and used them for training Mobilnet using the transfer learning technique.  The model was trained with 200,000 epochs and achieved a speed of 31 frames per second. On the right-hand side, these images are examples of crack detection models where the cracks are detected on top, and on the lower one, there is no crack, and the model is not predicting any crack.

![True Positive](/images/TP.png)
![True Negative](/images/TN.png)

The IoU (Intersect over Union) is used for the detection evaluation. Given the area of the bounding box of prediction vs. the expectation, the mutual section is the intersect, and the total area is the union. If the Intersect area over the union area is larger than the threshold is True Positive, otherwise would be False Positive. Predictions are classified into True Positive where the crack is detected, False Positive where intact road mistakenly detected as crack, and False Negative where the crack is not detected.

![IoU](/images/iou2.png)
source: [2] 

## Roadway Condition Estimation
Final PCI estimation is carried out through a regression model. The roadways of Irvington Village is used in this for the case study. The logistic regression model reached 81.80 percent accuracy and outperformed other models. The heatmap is generated using the model's output, which ran over 360-degree images along with their geo-location, and pavement scores.

![model pipeline](/images/reg_bench.png)

## Web App
The heat map hosted on the AWS cloud service. The heatmap app provides a tool for people in the transportation department to visualize the road conditions and prioritize the pavement. The road construction level is routine maintenance, rehabilitation, and reconstruction. The web app lets the user hop over the streets and get information about the street. This application can be used as an alternative for the traditional pavement assessment, which was costly and time-consuming.

![Irvington roadway data](/images/Irv_data.png)


# Features
For feature importance analysis, random forest regression is applied to the dataset. Comparing the two features from the database and machine vision shows that the variable importance on the model has the same effect on the overall model. The gaussian distribution on those parameters also shows the machine vision system can be used as an alternative for pavement estimation.

![features](/images/features.png)

![Variable importance](/images/Var_importance.png)
## Challenges
The challenges of this project were finding a solution using google street view and coming up with a fast and reliable machine vision solution to evaluate them.

Currently, there are multiple research papers and old fashion assessment papers, but none is providing a user-friendly web app to demonstrate the quality of the roads on the street.

In this project, the speed of processing is improved to over 30 frames per second; The scale is expanded to the region and zip code, the design is improved to a friendly user web app, and is extensible for future improvement on every section.
![data acquisition](/images/3d_data.png)

![machine vision vs manucipility](/images/mv_manu.png)

![prediction vs label](/images/pred_label.png)



## Source
[1] https://www.irvingtonny.gov/DocumentCenter/View/8036/Public-Works-Roadway-Pavement-Report?bidId=

[2] https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
