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

You can explore DB diagram in **main.png**  

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
  
So CRUD is on board.  

HTTP file contains all available queries-schemas. I used PyCharm HTTP Tool during development.

There are no exception processing. And it's really bad. There are no classes, only functions. 
So it's exactly not pythonic way. I focused on "what to code" instead of "how", and it was a mistake. 


Of course, I'll come back and write v0.2 soon.