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

CRUD stands for Create, Read, Update and Delete, which are the four basic operations that are used to help in the interaction with the resources in the system. These operations are fundamental for managing data, and they used in the REST APIs for web services. These operations are considered to be HTTP methods by the correspondence to these operations. The first HTTP method is "GET", which is used to retrieve data, this is progressed by fetching the representation of the source from a specific URL in particularly (URI). However, this won't cause any changes to the server, it will only read the data. For example assuming that we need to retrieve the user's profile, then the following command would be GET/users/userID, which will return the user ID "userID". The next method is the "POST" HTTP method, which is used to innovate a new data or resources on the server. This is progressed by automatically assigning a unique URI to the most recent innovate resource and retrieves it. This method could be used in order to innovate new records in the database, or creating a new user profile. For example, POST/USERS which the return would be the URI of users/userID. The third method is the "PUT" method, which is used to update an existing resource to create a new resource at a specific URI (assuming that the server allows it). For example, PUT/users/userID which will modify the user with the "userID" with the new data being requested in the request. Lastly, is the "DELETE" HTTP method, which is used to remove an existing resource from the server at a specific URI. For example, DELETE/users/userID, this command would remove "userID" from the database. 

## Simplified terms: 
GET is for reading (retrieving) data,
POST is for creating new data,
PUT is for updating existing data,
DELETE is for removing data


## Method Responses
Based on the above HTTP methods we receive different types of responses to check whether the resposes went successsfully or not. These responses are considered to be HTTP status codes which conveys whether the operation of the request is preformed or not, and based on these responses different actions are taken.

## 200 OK:
This command determines that the request went successfuly.
## 201 Created:
The resource was successfully created. 
## 204 No Content:
The request was successful, but there is no content to return.
##  400 Bad Request: 
The request was malformed or missing required data.
## 404 Not Found: 
The resource was not found.
## 405 Method Not Allowed:
The HTTP method used is not supported for the requested resource.
## 500 Internal Server Error:
A general server error occurred (something went wrong on the server side).
## 401 Unauthorized: 
The request requires authentication.
## 403 Forbidden: 
The server understands the request but refuses to authorize it.




## External API User

An API (Application Programming Interface) is a set of rules and tools that allow different software applications to communicate with each other. It acts like a contract between the provider (who offers the data or service) and the consumer (who uses the data or service). The API defines what information the consumer needs to send (the request) and what kind of response the provider will give back.


## Cloud Architecture

![Screenshot 2024-11-28 at 22 37 24](https://github.com/user-attachments/assets/6cd9e58a-c665-4186-99d9-99de415926df)
