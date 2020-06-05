# DRF-TODO
Sample project to get my self familiar with Django rest framework
___

## Setup steps
* Python: 3.6
* Create python virtual environment
* activate the virtual env
* install requirements using requirements.txt file from the repo

___
## End Points
* ```http://localhost:8000/api/tasks/``` - Task create and list end point
* ```http://localhost:8000/api/tasks/id``` - retrieve, update and delete endpoint
* ```http://localhost:8000/api/auth/signup/``` - Signup new user
* ```http://localhost:8000/api/auth/login/``` - Log in new user and obtain auth_token
* ```http://localhost:8000/api/auth/logout/``` - Log out user 
___
## Issues Identified:
* ~~Create is not working because ```save()``` method in models file is creating some issue. I tried to differentiate ```insert``` and ```update``` by putting an if condition. If id is none then it is insert else it is an update. But that does not seem to work. I beleive there is a better way to do it and I am not handeling it the correct way.~~ - Resolved
___
## TODO:
* ~~Resolve post task end point issue.~~ - Resolved 
* ~~Create test script~~
* ~~Include authentication~~
* Make changes in test script after authentication
* Summary end point to give user summary about how many tasks are done, how many tasks are pending and avg time to complete a task.
 
___
## Test:
* For this project, I am using pytest and requests module. requirements file has all the required dependancies.
* Use command ```pytest tests\tasks_test.py``` from project root in order to run the tests
* Use ```-s``` flag in tests in case print statements are required for debigging

