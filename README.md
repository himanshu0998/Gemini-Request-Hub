Gemini-Request-hub

This is a backend project build on top of freely available Google Gemini APIs which provides prompt, chat and image processsing APIs to its end users which can be further used to integrate with any frontend application as per the requirements. 

Clone this repository using:

git clone https://github.com/himanshu0998/Gemini-Request-Hub.git

Repository Structure:

Gemini-Request-Hub/\
│\
├── app/\
│   ├── __init__.py\
│   ├── models/\
│   │   ├── User.py\
│   │   ├── TextInteractions.py\
│   │   └── ImageInteractions.py\
│   │\
│   └── routes/\
│       ├── auth.py\
│       ├── image_processing.py\
│       └── text_processing.py\
│\
├── logs/\
│   ├── app.log\
│\
│── api_client.py\
│── config.py\
│── database.py\
│── logger_config.py\
│── run.py\
├── requirements.txt\
└── README.md\

Requirements

The basic requirements include:

1. Python 3.10
2. MySQL setup on the local machine

Apart from this The requirements.txt file consists of all the necessary dependencies required to run this project. These dependencies can be installed by executing the below command:

pip install -r requirements.txt

Setting Up the Database

The project utilizes SQLAlchemy to establish an ORM (Object-Relational Mapping) based database, which abstracts the MySQL database into Python objects. This approach allows to interact with the database using Pythonic operations rather than writing raw SQL queries. Models for each tables is present in the 'app/models/' folder.

User.py - corresponds to the structure of 'users' table in the database.
TextInteractions.py - corresponds to the structure of 'usertextinteractions' table in the database.
ImageInteractions.py - corresponds to the structure of 'userimageinteractions' table in the database.

Inorder to setup the database update the 'config.py' file in the roor directory with the below details:

1. MYSQL_USER - username of the MySQL database (typically its root)
2. MYSQL_PASSWORD - password of the MySQL database
3. MYSQL_DB - name of the database
4. MYSQL_HOST - hostname (this would be 'localhost') when running on the local machine.

Note: The database and the tables would be created when the application is run for the first time with the help of SQLAlchemy utils. The user does not need to explicitly create a database and the tables in it to run the application. 

Setting up the Gemini API client

API key would be needed inorder to setup the Google gemini client. The api key can be obtained from https://ai.google.dev/ .
This key should be written as a value of 'API_KEY' variable in 'config.py' file.

Running the flask Server

In order to run this server/application run the below command from the root directory of the project

flask run

OR

python -m flask run

API Documentation

The API Documentation folder in the root directory of the project holds the details about all the API end points, the expected parameters,
the URLs and what does the end point do.

This documentation is a HTML page generated from postman and should be opened in a browser (preferably Google Chrome)

Logging

The 'logs' folder with 'app.log' file will hold all the logs of the project. The logging is configured and initialized in the 'app/__init__.py' using the 'logger_config.py'

Unit Testing


