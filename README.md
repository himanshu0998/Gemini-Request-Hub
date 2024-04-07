## Gemini-Request-hub

This is a backend system is build on top of freely available Google Gemini APIs and provides API end points for prompt, chat and image processing AI-powered features to its end users which can be further used to integrate with any frontend application as per the requirements.

This system also provides a basic user authentication and authorization to secure the API end points using Flask-JWT.

# Table of Contents
- [Repository Structure](#repository-structure)
- [Installing Requirements](#step-1-installing-requirements)
- [Cloning Respository](#step-2-clone-this-repository)
- [Navigate to root folder](#step-3-navigate-to-the-project-directory)
- [Database Setup](#step-4-setting-up-the-database)
- [Gemini Client Setup](#step-5-setting-up-the-gemini-api-client)
- [Running the project](#step-6-running-the-flask-server)
- [Documentation](#documentation)
- [Unit and Integration Tests](#unit-testing)
- [Application Logging Details](#logging)
- [Database Description](#database-description)

## Repository Structure

Gemini-Request-Hub/\
│\
├── app/\
│   ├──\_\_init\_\_.py\
│   ├── models/\
│             &nbsp;&nbsp;&nbsp;&nbsp;├── User.py\
│             &nbsp;&nbsp;&nbsp;&nbsp;├── TextInteractions.py\
│             &nbsp;&nbsp;&nbsp;&nbsp;├── ImageInteractions.py\
│             &nbsp;&nbsp;&nbsp;&nbsp;└── BlockListed.py\
│\
│── routes/\
│          ├── auth.py\
│          ├── image_processing.py\
│          └── text_processing.py\
│\
├── logs/\
│   └──app.log\
│\
│── api_client.py\
│── config.py\
│── database.py\
│── logger_config.py\
│── run.py\
├── requirements.txt\
└── README.md

Here, the ```app/routes``` folder contains the code for all the various end points.

+ ```auth.py``` contains the definition for ```/auth/signup```, ```/auth/signin```, ```/auth/logout``` end points.
+ ```text_processing.py``` contains the definition for ```/text/prompt```, ```/text/chat``` end points.
+ ```image_processing.py``` contains the definition for ```/text/prompt```, ```/text/chat``` end points.

The other files are explained below in the document wherever required. 

## Step 1: Installing Requirements

The basic requirements to run this project include:

+ ```Python 3.10``` - refer https://www.python.org/downloads/ for installation.
+ ```MySQL setup on the local machine``` - refer https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ for installation.

These should be installed in the local machine for installing any further dependencies.

Apart from this, the ```requirements.txt``` file consists of all the necessary dependencies required to run this project. These dependencies can be installed by executing the below command:

```pip install -r requirements.txt```

## Step 2: Clone this repository

```git clone https://github.com/himanshu0998/Gemini-Request-Hub.git```

## Step 3: Navigate to the Project directory

```cd Gemini-Request-hub```

## Step 4: Setting Up the Database

The project utilizes <b>SQLAlchemy</b> to establish an <u>ORM (Object-Relational Mapping)</u> based database, which abstracts the MySQL database into Python objects. This approach allows to interact with the database using Pythonic operations rather than writing raw SQL queries.

Details of the tables in the database and their corresponding models can viewed [here](#database-description).

Inorder to setup the database update the ```config.py``` file in the roor directory with the below details:
+ ```MYSQL_USER``` - username of the MySQL database (typically its root)
+ ```MYSQL_PASSWORD``` - password of the MySQL database
+ ```MYSQL_DB``` - name of the database
+ ```MYSQL_HOST``` - hostname (this would be ```localhost```) when running on the local machine.

Note: The database and the tables would be created when the application is run for the first time with the help of ```SQLAlchemy utils```. <i>The user does not need to explicitly create a database and the tables in it to run the application.</i> 

## Step 5: Setting up the Gemini API client

API key would be needed inorder to setup the Google gemini client. The api key can be obtained from https://ai.google.dev/ .
This key should be written as a value of ```API_KEY``` variable in ```config.py``` file.

## Step 6: Running the Flask Server

To run this server/application run the below command from the root directory of the project

```flask run```

OR

```python -m flask run```

## Documentation

+ The ```API Documentation/``` folder in the root directory of the project holds the details about all the API end points, the expected parameters, the URLs and what does the end point do.
    + This documentation is a HTML page generated from postman and should be opened in a browser (preferably Google Chrome).
    + The ```css/``` and ```js/``` folders cater to this HTML page.
    + The ```Gemini-Request-Hub.postman_collection.json``` file is generated from Postman to document all the APIs.

+ Each python file in the project has a description about what is the code in the file, its functionality and usage at the top of the file. I have also added ```doc strings in each method (or function)``` throught the project to provide a comprehensive understanding of it.

+ Sample code on how to make the API calls in python can be found in unit testing scripts in ```Unit and Integration Tests\``` folder. You can refer the same to write a custom script based on your business logic.

## Unit Testing

The ```Unit and Integration Tests\``` folder consists of different python based test scripts. Each Python file tests different cases for each API end point in this project.

Inorder to run the any of the script follow the below steps:

+ In one terminal run the server as mentioned in ```Step 7```

+ In the second terminal - 

    + ```cd '.\Unit and Integration Tests\'```

    + ```python <file_name>.py```

The output consists of different cases and the response obtained for each of them. This gives a detailed about all the edge cases, exceptions and scenarios.

## Logging

The ```logs``` folder with ```app.log``` file will hold all the logs of the project. The logging is configured and initialized in the ```app/__init__.py``` using the ```logger_config.py```

## Database Description

Model for each tables is present in the ```app/models/``` folder.

+ ```User.py``` - corresponds to the structure of ```users``` table in the database.
    + Columns:
        + ```username```: A String column that stores the username. It is the primary key, unique, and not nullable.
        + ```emailid``` : A String column that stores the email address. It is unique and not nullable.
        + ```password```: A String column that stores the password. It is not nullable and can store up to 200 characters.
+ ```TextInteractions.py``` - corresponds to the structure of ```usertextinteractions``` table in the database.
    + Columns:
        + ```username```: A String column storing the username of the user who initiated the interaction. It is part of the primary key.
        + ```input_type```: A String column indicating the type of input (e.g., 'chat', 'prompt'), limited to 10 characters.
        + ```input_content```: A Text column containing the text input provided by the user.
        + ```input_timestamp```: A DateTime column recording the time when the input was received. It is part of the primary key.
        + ```output_content```: A Text column containing the text response generated by the system or service.
        + ```output_timestamp```: A DateTime column recording the time when the output was generated.
        + ```status```: A String column indicating the status of the interaction (e.g., 'Processed', 'No Response'), limited to 10 characters.
+ ```ImageInteractions.py``` - corresponds to the structure of ```userimageinteractions``` table in the database.
    + Columns:
        + ```username``` : Stores the username of the user involved in the interaction as a String, part of the primary key, ensuring that interactions are user-specific.
        + ```input_type``` : A String column indicating the nature of the interaction input (e.g., 'image'), limited to 10 characters.
        + ```input_prompt``` : A Text column for any text prompt accompanying the image input, nullable to allow interactions without textual prompts.
        + ```input_image``` : A LargeBinary column that holds the image data, with a maximum length sufficient for storing large images.
        + ```input_timestamp``` : A DateTime column recording the exact time the input was received, part of the primary key to differentiate interactions.
        + ```output_content``` : A Text column containing textual response or content generated in response to the user's input.
        + ```output_timestamp``` : A DateTime column noting the time when the response or output content was generated.
        + ```status``` : A String column reflecting the status of the interaction (e.g., 'Processed', 'Failed'), limited to 10 characters, to quickly assess the outcome.

+ ```BlockListedToken.py``` - corresponds to the structure of ```userimageinteractions``` table in the database.
    + Columns:
        + ```id```: A unique identifier for each blocklisted token record. It is the primary key and is auto-incremented.
        + ```jti```: The JWT ID claim that provides a unique identifier for the token. The 'jti' field is set to be unique and non-nullable.
        + ```expires_at```: The expiration timestamp of the token. This is used to identify when the token is no longer valid, even without checking its signature. The field is non-nullable.