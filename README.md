
get service_account.json
https://docs.gspread.org/en/latest/oauth2.html

first thing! make sure you are on development branch (made it default) and then create your own branch off of it.
submit PR of your new branch to development, you can even open it if not ready to be merged yet just to show the difference differences on github. 
Start issues with WIP: in name in this case

structure:
in /api
start in __init__
views are endpoints that will be called by the api ie. api.dndloot.info/person
models are database tables, giving name and listing columns

ignore:
.idea
.circleci

database:
database will be managed separately and connected to on local server for now. (not done yet)
app will be launched with docker-compose.yml file to heroku if possible, otherwise locally.
review and ask questions about anything docker in this as it is a perfect way to learn how docker works

virtual enviroment setup in windows:

#make sure you are in this projects main folder in a cmd terminal and enter call commands
#if this doesnt work try pip3 install virtualenv and that you have python 3.7+ setup on pc
pip install virtualenv
#this creates a folder with a virtual python enviroment in it, you may need to set your ide to use it
virtualenv venv
#this activates the venv in your current terminal so you can do things in it
.\venv\Scripts\activate.bat
#installs everything this project needs, and nothing it doesnt
pip install -r requirements.txt
pip install -r requirements-dev.txt
#create file called creds.ini in the root project dir containing this text:
[pg_creds]
pg_url = postgresql://postgres:*****@192.168.1.25:5432/dnd
#replace stars with supplied password

Run debug server to test endpoints:
!!!
.\venv\Scripts\activate.bat
python manage.py runserver
!!!
http://127.0.0.1:5000
or
http://0.0.0.0:5000

ex:
http://127.0.0.1:5000/persons

reference material:

https://roll20.net/ 

https://donjon.bin.sh 

https://donjon.bin.sh/d20/treasure/ 

https://www.d20srd.org/d20/treasure/

boilerplate:

https://github.com/tko22/flask-boilerplate

