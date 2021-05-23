import db
from db import cur_api


def get_cars_by_model_id(id_model):
    statement = """
                SELECT  diler.name as diler_name, model.name as model_name, componentry, price, year_release, date_purchase, car_id
                FROM car
                JOIN model on car.model_id = model.model_id
                JOIN diler on model.diler_id = diler.diler_id
                WHERE diler.diler_id = model.diler_id AND car.model_id = ?
                """
    cur = cur_api()
    cars = cur[0].execute(statement, [id_model]).fetchall()
    return cars


def get_cars():
    query = "SELECT * FROM car"
    cur = cur_api()
    cars = cur[0].execute(query).fetchall()
    return cars


def insert_car(id_model, date_purchase):
    statement = "INSERT INTO car(model_id, date_purchase) VALUES (?, ?)"
    cur = cur_api()
    cur[0].execute(statement, [id_model, date_purchase])
    cur[1].commit()
    return True


def update_car(id_model, id_car, date_purchase):
    statement = "UPDATE car SET model_id = ?, date_purchase = ? WHERE car_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [id_model, date_purchase, id_car])
    cur[1].commit()
    return True


def delete_car_by_id(id_car):
    statement = "DELETE FROM car WHERE car_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [id_car])
    cur[1].commit()
    return True