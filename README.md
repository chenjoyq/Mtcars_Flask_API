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

## Running Mtcars Flask API
Please follow the steps below to execute the API:

+ Download the files in this repository

+ In your terminal, navigate to the **docker** folder directory and run `docker-compose up` to create your local server

+ If created successfully, 

+ To send a request to the API, use a `curl` command like the example below:  
`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6.0","disp":"","hp":"","drat":"","wt":"","qsec":"","gear":""}' "http://localhost:5000/predict_mpg"`
  + Note: input includes prediction variables as listed in section "Model Prediction Variables"
  + Output will be returned as a linear model prediction of `mpg` using given inputs
