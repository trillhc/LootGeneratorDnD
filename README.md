first thing! checkout development branch and then create your own branch off of it.
submit PR of your new branch to development, you can even open it if not ready to be merged yet just to show the difference differences on github. 
Start issues with WIP: in name in this case

structure:
in /api
views are endpoints that will be called by the api ie. api.dndloot.info/person
models are database tables, giving name and listing columns

database will be managed separately and connected to on local server for now.
app will be launched with docker-compose.yml file to heroku if possible, otherwise locally.


reference material:

https://roll20.net/ 

https://donjon.bin.sh 

https://donjon.bin.sh/d20/treasure/ 

https://www.d20srd.org/indexes/treasure.htm

boilerplate:

https://github.com/tko22/flask-boilerplate