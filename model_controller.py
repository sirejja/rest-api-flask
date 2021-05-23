from db import cur_api


def get_models_by_id(id_model):
    statement = """SELECT model.name as model_name, componentry, year_release, price, count, diler.name as diler_name
                    FROM model, diler 
                    WHERE model_id = ? and model.diler_id = diler.diler_id"""
    cur = cur_api()
    model = cur[0].execute(statement, [id_model]).fetchall()
    return model


def get_models():
    query = "SELECT * FROM model"
    cur = cur_api()
    model = cur[0].execute(query).fetchall()
    return model


def insert_model(model_name, price, componentry, year_release, count, id_diler):
    statement = "INSERT INTO model(name, price, componentry, year_release, count, diler_id) VALUES (?, ?, ?, ?, ?, ?)"
    cur = cur_api()
    cur[0].execute(statement, [model_name, price, componentry, year_release, count, id_diler])
    cur[1].commit()
    return True


def update_model(model_name, price, componentry, year_release, count, id_diler, id_model):
    statement = "UPDATE model SET name = ?, price = ?, componentry = ?, year_release = ?, count = ?, diler_id = ? WHERE model_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [model_name, price, componentry, year_release, count, id_diler, id_model])
    cur[1].commit()
    return True


def delete_model_by_id(id_model):
    statement = "DELETE FROM model WHERE model_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [id_model])
    cur[1].commit()
    return True