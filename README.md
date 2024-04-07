<h1>Gemini-Request-hub</h1>

This is a backend system is build on top of freely available Google Gemini APIs and provides API end points for prompt, chat and image processing AI-powered features to its end users which can be further used to integrate with any frontend application as per the requirements.

This system also provides a basic user authentication and authorization to secure the API end points using Flask-JWT.

<h2>Repository Structure:</h2>

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

<h2>Step 1: Installing Requirements</h2>

The basic requirements to run this project include:

+ ```Python 3.10``` - refer https://www.python.org/downloads/ for installation.
+ ```MySQL setup on the local machine``` - refer https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ for installation.

These should be installed in the local machine for installing any further dependencies.

Apart from this, the ```requirements.txt``` file consists of all the necessary dependencies required to run this project. These dependencies can be installed by executing the below command:

```pip install -r requirements.txt```

<h2>Step 2: Clone this repository</h2>

```git clone https://github.com/himanshu0998/Gemini-Request-Hub.git```

<h2>Step 3: Navigate to the Project directory</h2>

```cd Gemini-Request-hub```

<h2>Step 4: Setting Up the Database</h2>

The project utilizes <b>SQLAlchemy</b> to establish an <u>ORM (Object-Relational Mapping)</u> based database, which abstracts the MySQL database into Python objects. This approach allows to interact with the database using Pythonic operations rather than writing raw SQL queries. Model for each tables is present in the ```app/models/``` folder.

```User.py``` - corresponds to the structure of ```users``` table in the database.\
```TextInteractions.py``` - corresponds to the structure of ```usertextinteractions``` table in the database.\
```ImageInteractions.py``` - corresponds to the structure of ```userimageinteractions``` table in the database.\
```BlockListedToken.py``` - corresponds to the structure of ```userimageinteractions``` table in the database.\

Inorder to setup the database update the ```config.py``` file in the roor directory with the below details:
+ ```MYSQL_USER``` - username of the MySQL database (typically its root)
+ ```MYSQL_PASSWORD``` - password of the MySQL database
+ ```MYSQL_DB``` - name of the database
+ ```MYSQL_HOST``` - hostname (this would be ```localhost```) when running on the local machine.

Note: The database and the tables would be created when the application is run for the first time with the help of ```SQLAlchemy utils```. <i>The user does not need to explicitly create a database and the tables in it to run the application.</i> 

<h2>Step 5: Setting up the Gemini API client</h2>

API key would be needed inorder to setup the Google gemini client. The api key can be obtained from https://ai.google.dev/ .
This key should be written as a value of ```API_KEY``` variable in ```config.py``` file.

<h2>Step 6: Running the Flask Server</h2>

To run this server/application run the below command from the root directory of the project

```flask run```

OR

```python -m flask run```

<h2>Documentation</h2>

+ The ```API Documentation/``` folder in the root directory of the project holds the details about all the API end points, the expected parameters, the URLs and what does the end point do.
    + This documentation is a HTML page generated from postman and should be opened in a browser (preferably Google Chrome).
    + The ```css/``` and ```js/``` folders cater to this HTML page.
    + The ```Gemini-Request-Hub.postman_collection.json``` file is generated from Postman to document all the APIs.

+ Each python file in the project has a description about what is the code in the file, its functionality and usage at the top of the file. I have also added ```doc strings in each method (or function)``` throught the project to provide a comprehensive understanding of it.

+ Sample code on how to make the API calls in python can be found in unit testing scripts in ```Unit and Integration Tests\``` folder. You can refer the same to write a custom script based on your business logic.

<h2>Unit Testing</h2>

The ```Unit and Integration Tests\``` folder consists of different python based test scripts. Each Python file tests different cases for each API end point in this project.

Inorder to run the any of the script follow the below steps:

+ In one terminal run the server as mentioned in ```Step 7```

+ In the second terminal - 

    + ```cd '.\Unit and Integration Tests\'```

    + ```python <file_name>.py```

The output consists of different cases and the response obtained for each of them. This gives a detailed about all the edge cases, exceptions and scenarios.

<h2>Logging</h2>

The ```logs``` folder with ```app.log``` file will hold all the logs of the project. The logging is configured and initialized in the ```app/__init__.py``` using the ```logger_config.py```
