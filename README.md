**How to run
Be sure to have both Python and Node.js installed. Make sure python is <br>
in yout path variable (windows)
on Windows open the command prompt at this directory. type:<br>

`venv\script\activate`

on linux/mac open the terminal at this directory. type: <br>
`source venv/bin/activate`

You have now activated the virtual environment. All packages are installed here, not in your
whole machine, so please type:<br>
`pip install -r requirements.txt` <br>
We will now run the backend on this cmd/terminal and then the front-end on another terminal. <br>
During deployment the apps work seperately but communicate through tunneling via REST-api.<br>

type:<br>
`cd campmon`

then<br>
`python manage.py runserver`

of course you have to have python installed.<br>

This is done. <br>

Now for the front end. Open another cmd/terminal and navigate to the `frontend` directory type

`npm start`

You have to have Node.js installed on your computer for npm to run. If there are errors other packages can be installed with
`pip install `

Thats it, you are ready. frontend works at `localhost:3000` and backend at `localhost:8000`

**Technologies used

*backend
The Django Rest framework was used for brevity of the backend. It is a python framework that allows us to built an effective <br>
backend within hours, complete with a database and basic CRUD operations via REST API, the API endpoint is `localhost:8000/api/subscribers`.<br>
The ViewSet CRUD operations had to be overwritten with new ones to handle calling the campaign API. Everytime a user performs a CRUD operation <br>
on the list the backend updates its own Database and also the campaign API database. (For brevity it then syncs the Campaign API data with the DB data).

*frontend
The react framework was used fot the front-end, a really powerfull JavaScript framework, along with bottstrap and reactstrap for UI tools. The frontend<br>
is a seperate entity from the backend and it makes requests to the backend API endpoint.