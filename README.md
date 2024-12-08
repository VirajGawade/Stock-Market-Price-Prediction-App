# Stock-Market-Price-Prediction-App

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [System Overview](#system-overview)
  - [Terms used for Stock-Market-Price-Prediction-App](#terms-used-for-Stock-Market-Price-Prediction-App)
- [System Architecture](#system-architecture)
- [Application Overview](#application-overview)
- [Application Architecture](#application-architecture)
  - [Flask App](#flask-app)
  - [RESTful API](#restful-api)
  - [CRUD Operations](#crud-operations)
  - [External APIs Used](#external-apis-used)
- [Cloud Infrastructure](#cloud-infrastructure)
  - [Google Cloud](#google-cloud)
  - [Kubernetes](#kubernetes)
  - [Docker](#docker)

## About

This application leverages machine learning algorithms to predict stock market prices, providing users with data-driven insights into potential market trends. By analysing historical price data and market indicators, the app aims to assist traders and investors in making informed decisions based on predicted price movements. We will be utilising **Google's Finance API** in order to fetch real-time and historical stock data - giving us confidence that we have up-to-date and accurate information to do our analysis/predictions.

## System Architecture

![Screenshot 2024-11-19 at 11 18 35](https://github.com/user-attachments/assets/f8960847-e587-4efc-91b0-4c27fac68059)


## Application Architecture

## Flask App
Flask is the efficient way to be used as Python web framework that is innovated to produce a web development in an easier and more smoother way. It is very popular method that most of the developers use to simplify their flexibility in order to come up with an easier way to produce a website developed in Python. This is progressed through the advantages that Flask has when it collaborates with Python, such as it contributes to minimal setup, it only require a single Python file to start with, and then the development could be progressed after this step. It is also a reliable initial point to be used for beginners as well as this who are looking to develop small to medium level of applications without considering a step learning curve. 

One of the biggest strength that flask has is the adaptability, unlike other frameworks, as it does not enforce a specific project structure or force developers to adhere to strict regulations. This provides a better way to cause freedom to organise the appication in whatever way meets the developer's requirments. As well as this, Flask also helps in the integration with Jinja, that is considered to be a powerful templating engine, which allows dynamic generation of HTML content. In comparison with static HTML which only display a fixed content. This leads to the prevention of building moderns, and data-driven applications where content is constantly changing based on the backend requirements. 

Through the consideration to the above, developers can easily insert Python as syntax into HTML files, such as variables, loops, and conditionals, which would make it simple to generate dynamic web pages based on the data, or the change of any external factors. This is a strong key that makes Flask very rapid for web application development. 

## RESTFUL-API
A REST API (Representational State Transfer Application Programming Interface), which is an architectural style that is used to create a networked applications for the purpose of collaboration. This is progressed by allowing different software components to communicate with each other over the web standard protocol HTTP (HyperText Transfer Protocol) methods such as GET, POST, PUT, DELETE, etc. 

In 2000, the computer scientist Roy Fielding has completed his doctoral dissertation titled "Architectural Styles and the Design of Network-based Software Architectures", which after this completion the term "REST" began. In this dissertation the article outlined some guidance which are used to increase the level of concentration on the design of web services. The first point is "statelessness" which means that in order for a server to respond to the client's request, the request must contain all the needed information the server needs to process the request, and the server does not store any information of previous requests asked by clients. The second point is the "Client-Server Architecture", this contains the segregation between the UI (User Interface) and the server, each of the ends has a specific task, as the UI manages the user experience and the server manages the data and the business logic behind the UI (Backend). 

Subsequently, the "uniform Interface" which is the collaboration between the UI with the API without needing to understand the underlying infrastructure. This is progressed by the utilisation of uniform set of regulations to help in the resources accessibility. The next term is the "cacheability", at each request being progressed at each time the process to deal with this request takes long to output the needed result, therefore at this process the server maintains the request by caching it and if this request been requested again by the user then it will be faster to procced than the first attempt. The last point is the "Layered System", which is the segregation of the layers considering each layer is responsible for a certain task, without the need for the client to know if there is interaction with other layers such as the database layer.


## CRUD Operations 


## External API User


## Cloud Architecture

![Screenshot 2024-11-28 at 22 37 24](https://github.com/user-attachments/assets/6cd9e58a-c665-4186-99d9-99de415926df)
