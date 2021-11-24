
# **carsAPI**
## *This is an API allowing adding cars to a database and rating them.*


# Summary of endpoints:

**POST /cars**

 - Request body should contain car make and model name
 - Based on this data, its existence should be checked here
   [](https://vpic.nhtsa.dot.gov/api/)[https://vpic.nhtsa.dot.gov/api/](https://vpic.nhtsa.dot.gov/api/)
 - If the car doesn't exist - return an error
 - If the car exists - it should be saved in the database

**DELETE /cars/{ id }**

 - Should delete the car wi2th the given id from database

 - If the car doesn't exist in database - return an error

**POST /rate**

 - Add a rate for a car from 1 to 5

**GET /cars**

 - Should fetch a list of all cars already present in application
   database with their current average rate

**GET /popular**

 - Should return top cars already present in the database ranking based
   on a number of rates )

API is available under http://150.230.144.242/api/cars/ (deployed on Oracle Cloud VM)
You can deploy the api locally using docker. Fetch this GIT branch and build image by yourself using 

> docker build -t carapi .

or pull the built image from docker hub: 

> docker pull morthell/carapi:latest

[Public View Docker Hub](https://hub.docker.com/r/morthell/carapi)

