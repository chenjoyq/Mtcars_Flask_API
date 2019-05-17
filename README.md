## Mtcars Flask API

#### DESCRIPTION
Construction of local flask API with Docker container functionality. Using `mtcars.csv` dataset and returning predictive linear model using Python in a Docker container  
<br/>

#### MODEL PREDICTION VARIABLES
Outcome Variable: `mpg`  
Predictors (Continuous): `cyl` `disp` `hp` `drat` `wt` `qsec` `gear`

<br/>

***

<br/> 

## Instructions: Running API
Please follow the steps below to execute the API:

+ Download the files in this repository

+ In your terminal, navigate to the **docker** folder directory and run `docker-compose up` to create your local server

+ If created successfully, you should see 9 lines with `flask_1 | ....` outputs but will *not* be receiving a prompt back

+ Open up a new terminal and navigate to the same **docker** directory

+ To check the status of the server run:
`curl https://localserver:5000/`  
The response should say: Server is up!

+ To send a request to the API, use a `curl` command like the example below:  
`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6.0","disp":"200","hp":"175","drat":"3.5","wt":"3.1","qsec":"16","gear":"4"}' "http://localhost:5000/predict_mpg"`  

> The response should look like: `{mpg prediction: 18.6039}`

<br/>

**NOTES**: 
- Input includes prediction variables as listed above and values can be altered
- Output will be returned as a linear model prediction of `mpg` using given inputs

<br/> 

## Shutdown API
To stop your server, type `ctrl-C`. Check if any docker containers are running with `docker container ls` and shutdown using `docker container kill <container-name>`

