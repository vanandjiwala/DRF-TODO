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
```http://localhost:8000/api/tasks/``` - Task create and list end point
```http://localhost:8000/api/tasks/id``` - retrieve, update and delete endpoint
___
## Issue:
* Create is not working because ```save()``` method in models file is creating some issue. I tried to differentiate ```insert``` and ```update``` by putting an if condition. If id is none then it is insert else it is an update. But that does not seem to work. I beleive there is a better way to do it and I am not handeling it the correct way. 
___
## TODO:
* ~~Resolve post task end point issue.~~ - Resolved 
* Summary end point to give user summary about how many tasks are done, how many tasks are pending and avg time to complete a task. 

