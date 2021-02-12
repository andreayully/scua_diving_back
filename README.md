# scua_diving_back

Backend for Scuba Diving journal App  
Get and stores the track of scuba dives

* maximum depth
* time below surface
* starting and ending oxygen levels
* location
* date and time
* outside temperature
* water temperature
* a description of what you saw

## To run locally
**pre requirements Python 3.+ and Virtualenv**

1. Create virtual environment and activate environment  
`python3 -m venv myvenv`
`source myvenv/bin/activate`

2. Clone repository   
`git clone https://github.com/andreayully/PokeApi.git`

3. Install requirements   
`pip install -r requirements.txt`

4. Runserver   
` python manage.py runserver`

## Frontend in React
https://github.com/andreayully/scuba_diving_front


### Swagger generator
For documentation  
http://localhost:8000/swagger/  
http://localhost:8000/redoc/

### Postman collection
https://www.getpostman.com/collections/04d9f0ba0b95d827fb64

### Feature
* Django 3.1.5
* Django Rest-Framework 3.12.2
