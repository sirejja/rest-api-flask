from db import cur_api


def get_models_by_diler_name(diler_name):
    statement = """
                SELECT model.model_id, diler.name, model.name, componentry, price, year_release 
                FROM model 
                JOIN diler on model.diler_id = diler.diler_id
                WHERE diler.diler_id = model.diler_id AND diler.name = ?
                """
    cur = cur_api()
    dilers = cur[0].execute(statement, [diler_name]).fetchall()
    return dilers


def get_dilers():
    query = 'SELECT * FROM diler'
    cur = cur_api()
    diler = cur[0].execute(query).fetchall()
    return diler


def insert_diler(diler_name):
    statement = "INSERT INTO diler(name) VALUES (?)"
    cur = cur_api()
    cur[0].execute(statement, [diler_name])
    cur[1].commit()
    return True


def update_diler(id_diler, diler_name):
    statement = "UPDATE diler SET name = ? WHERE diler_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [diler_name, id_diler])
    cur[1].commit()
    return True


def delete_diler(id_diler):
    statement = "DELETE FROM diler WHERE diler_id = ?"
    cur = cur_api()
    cur[0].execute(statement, [id_diler])
    cur[1].commit()
    return True