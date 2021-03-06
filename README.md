# FinSTC Software LLC test task.
# RESTful_API_Flask for car dealership 
I decided to try my hand in Flask. So let's get it started.

Libraries and frameworks: sqlite3, Flask.

IDE: PyCharm  
DB: diler.db (sqlite3)  

SQL schemas, insert files included.

There are three tables:
* diler(means dealer), 
* model, 
* car.

You can explore DB diagram in **main.png** below

![Image alt](https://github.com/sirejja/RESTful_API_Flask/blob/6c309a9ed6b6b85ec0d054e71821aec7f75c70f1/main.png)

There are 6 **endpoints**: 
* **/diler**
  *  get all dealer's models by dealer's name, 
  *  insert dealer's name, 
  *  update dealer's name by id, 
  *  delete dealer by id
* **/diler/all**
  *  get all dealers
* **/diler/model**
  *  get all models by model's id, 
  *  insert model,
  *  update model by id, 
  *  delete model by id
* **/diler/model/all**
  *  get all models
* **/diler/model/car,** 
  *  get all cars by model's id, 
  *  insert car, update car by id, 
  *  delete car by id,
* **/diler/model/car/all**
  *  get all cars
  
So **CRUD** is on board.  

**rest-api.http** file contains all available queries-schemas. I used PyCharm HTTP Tool during development.

There are no exception and error processing. And it's really bad. So you can get an error 500 on a working method, just because there is no such value in database. To make testing easier, I recommend to use methods GET at first, then POST, PUT, DELETE(sorry..).  
There are no classes, only functions.
So it's exactly not pythonic way. I focused on "what to code" instead of "how", and it was a mistake. 


