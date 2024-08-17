[REQUIREMENTS]
-  Latest Python 3.9+
-  Docker Desktop

[DOWNLOAD]
-  Download the files from the google drive link and save it on the machine to the directory of choice.

[USING-DOCKER]
-  Install and run Docker Desktop
-  Build the docker image using the command : docker build -t topnews-fastapi .
-  Run the docker container : docker run -d -p 8000:8000 topnews-fastapi
-  You can access the API at : http://localhost:8000/top-news?count=10

[FAQ]
-  If the application does not run then restart Docker Desktop.
-  Run "pip install -r requirements" if given unspecified errors.

[ASSUMPTIONS]
-  Assuming the returning information is in JSON file format.
-  Top stories may contain jobs as mentioned in the documentation for Hacker-News.