The project is aimed at developing an application using Flask that can accept data from application X, save it to a database, and then send a callback response back to application X.

Question: Please illustrate this process by creating a dummy model(s), url and defining an endpoint in Flask.

The project contains two folders, one to house the main backend with models, and the other a simple flask project with static data on its endpoint.

To prepare to test the functionality of the project, clone it into your local machine.
on the root path(Where you can see both project folders), run the command ```python3 -m venv venv``` In order to create a virtual environment.
NB: The project has been implemented on an Ubuntu 22.04LTS OS using Python Flask and Postgres Database.

Activate the virtual environment by running the command ```source venv/bin/activate```.

Run the command ```cd MainBackend``` to navigate to the root of the main project.

Run ```pip install -r '/dep/requirements.txt'``` in order to install all the dependencies required to run the project.

on the env file, you will find 'DATABASE_URL' connection string variable that indicates postgresql as the database engine, database is flask running on port 5432,slave as the username and test101 as the password. Create a database with these credentials or adjust to suite your specific requirement.

The 'FETCH_END' indicates the API to access Application X through.
The env file is used to store variables required for the project.

After that, you can proceed to run the command ```export FLASK_APP=manage.py``` in order to load the configuration of your main project to the system variables. All configurations have been done on this file.

You can then proceed to run the command ```flask db init``` in order to initialize the database that you had set up initially.

Run ```flask db migrate -m "migration message"``` in order to migrate the dummy table defined on the 'app/models.py' file.

Run ```flask db upgrade``` in order to apply database changes to the db schema.

Finally run ```flask run -h 0.0.0.0 --port 8000``` to run the MainBackend project on localhost and port 8000. You can adjust the options as per your preferrence.

Now that everything on the main project is set up, its time to start ApplicationX.

In another terminal window, from the root of the cloned git project, initialize the virtual environment and run the command ```python callback.py```.

ApplicationX is preconfigured to run on localhost at port 5000 in the 'ApplicationX/callback.py'.

Both applications are using the same virtual environment as you noticed from the above information.

Now that the project is running, try to create a HTTP GET request to the URL ```http://0.0.0.0:8000/createtransaction``` from your client(Postman, Browser or any other client).

What happens is that MainBackend when hit with a GET request from the above endpoint, it sends a GET request to ApplicationX's '/post_data' endpoint and gets the encoded data which includes a callback url which the MainBackend will use to return a response upon finishing processing data.
MainBackend gets the data, accesses it and saves it to the database, then extracts the callback url from the data in order to return a response upon saving the data.


At this point the question from the second line has been successfully answered.
