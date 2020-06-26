# Road Assess:
## a machine vision tool for roadway assessment.
check the web application by clicking [here!](http://sohiai.com:8501/) it may take a minute to load.

![RoadAssess Web App](https://drive.google.com/file/d/1EAtp-DT-3zR0wa9yrkyRDztpoJFDFsX8/view?usp=sharing)
Format: ![Alt Text](url)


## Problem Statement
Roads are an essential part of the transportation system. 
Recently, roadways index in the US rated as D. Pavement condition is one of the critical indicators of regional prosperity and public well-being. If the department of transportation has a tool to evaluate the pavement they can expedite the process of pavement assessment and budget allocation to fix them.
Older roads tend to deteriorate faster due to environmental conditions such as high traffic,and climate fluctuation.
Assessment of these roads are often expensive and some cities have tight budget to assess the entire of the region.

The yearly budget used in this evaluation is between $200,000 and $230,000. The system has been extended for a period of 10 years and includes between 2 to 4 roadways per year that can be repaved[1]. The statistics shows that the age of these roads are 19 years old and 20% of them have inadequate conditions.

The goal of this project is to develop a web app tool to grade roads using machine vision for the users at the department of transportation.


## Model Pipeline
It all starts from an image of pavement, which is accessing images from static google street view API. The machine vision model is then used to extract features such as the number of distress, area of the crack, severity of cracks, type of the distresses such as alligator, potholes, longitudinal, or joint cracks. On the other hand, there are databases available to provide additional features such as the length of the roads, the roads' width, and the last time the road was resurfaced.With all roadway data combined, A regression model can estimate the pavement condition index for every street and ultimately generate a heatmap with repairing construction recommendation. 


## Machine Vision
I have manually labeled 3 street on google street view image by an online software called "make sense' and used them for tranining Mobilnet using transfer learning technique.  I trained the model with 200,000 epochs and achived the speed of 31 frames per second.On the right-hand side, these images are examples of crack detection models where on top, the cracks are detected, and on the lower one, there is no crack, and the model is correctly ignoring it.


The IoU (Intersect over Union)is used for the detection evaluation. Given the area of the bounding box of prediction vs the expectation, the mutual section is the intesect, and the total area is the union. If the Intersect area over the union area is bigger than the threshold is True Positive, otherwise would be False Positive. Predictions are classified into True Positive where the crack is detected, False Positve where intact road mistakenly detected as crack, and False Negative where the crack is not detected.

## Roadway Condition Estimation
Final PCI estimation is carried out through a regression model.The roadways of Irvington Village is used in this for the case study.The logistic regression model reached 81.80 percent accuracy and outperformed other models.The heatmap is generated using the model's output, which ran over 360-degree images of along with their geo-location. and pavement scores.

## Web App
The heat map hosted on the AWS cloud service. The heatmap app provides a tool for people in the department of transportation to visualize the road conditions and prioritize the pavement. The road construction level is routine maintenance, rehabilitation, and reconstruction.The web app lets the user hop over the streets and get information about the street. This application can be used as an alternative for the traditional pavement assessment, which was costly and time-consuming.

## Challenges
The challenges of this project was to find a solution with the use of google street view and come up with a fast and reliable machine vision solution to evaluate them.

Currently there are multiple research papers and old fasion assessemnt papers but none is provoding a user friendly web app to provide the quality of the roads on a street.

In this project the speed of processing is improved to over 30 frame per second, The scale is expanded to the region and zip code, the design is improved to a friendly user web app, and is extensible for future improvement on every section.

## Source
[1] https://www.irvingtonny.gov/DocumentCenter/View/8036/Public-Works-Roadway-Pavement-Report?bidId=

