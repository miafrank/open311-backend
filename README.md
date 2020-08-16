# Open 311 St. Louis City
*WIP* 

Replicating back end service for St. Louis City's Implementation of [Open311 GeoReport v2](https://www.open311.org/). 
The end in mind is a mobile application that allows users to easily report concerns to the city. 
(A comparable app to the end in mind would be [Tulsa311](https://apps.apple.com/us/app/tulsa-311/id1453372535))

## [GeoReport v2](http://wiki.open311.org/GeoReport_v2/#apps--resources)
allows developers to build applications to view and report issues which 
government entities (like cities) are responsible for addressing. Traditionally, 
“calls for service” or “service requests” have been handled by custom web forms or 
call centers (311 phone number or other short-codes). The API allows both government 
and third parties to create new applications and technologies to integrate directly with 
the same official contact centers in any government (only non emergency issues). 


## Setup
### Project setup
1. Create virtual env and install dependencies (from `Pipfile`)
    1. `$ pipenv install`
    
1. Set environment variables in `~/.bash_profile` or `~/.zshrc`: 
    1. `export AWS_ACCESS_KEY_ID=`
    2. `export AWS_SECRET_ACCESS_KEY=`
    3. `export STL_API_KEY=`
        1. To request an API Key to Open 311 STL, fill out 
        [this](https://www.stlouis-mo.gov/government/departments/information-technology/web-development/city-api/sign-up.cfm) app.

### Create tables and insert STL data into DynamoDB
`$ python setup_env.py`

### Run tests
`$ pytest tests/test_db_utils.py --disable-pytest-warnings`