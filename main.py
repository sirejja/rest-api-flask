from flask import Flask, jsonify, request

import car_controller
import diler_controller
import model_controller


app = Flask(__name__)

"""
Diler table managing
"""

@app.route("/diler/all", methods=["GET"])
def get_diler_all():
    diler = diler_controller.get_dilers()
    return jsonify(diler)


@app.route("/diler", methods=["GET"])
def get_models_by_dilers_name():
    query_parameters = request.args
    name = query_parameters.get('name')
    diler = diler_controller.get_models_by_diler_name(name)
    return jsonify(diler)


@app.route("/diler", methods=["POST"])
def ins_diler():
    content = request.get_json()
    name = content["name"]
    diler_controller.insert_diler(name)
    return "Done"


@app.route("/diler", methods=["PUT"])
def upd_diler():
    content = request.get_json()
    id = content["id"]
    name = content["name"]
    diler_controller.update_diler(id, name)
    return "Done"


@app.route("/diler", methods=["DELETE"])
def del_diler():
    content = request.get_json()
    id = content["id"]
    diler_controller.delete_diler(id)
    return "Done"


"""
Model table managing
"""
@app.route("/diler/model/all", methods=["GET"])
def get_models_all():
    model = model_controller.get_models()
    return jsonify(model)


@app.route("/diler/model", methods=["GET"])
def get_models():
    query_parameters = request.args
    model_id = query_parameters.get('id')
    model = model_controller.get_models_by_id(model_id)
    return jsonify(model)


@app.route("/diler/model", methods=["POST"])
def ins_model():
    content = request.get_json()
    model_name = content["model_name"]
    price = content["price"]
    componentry = content["componentry"]
    year_release = content["year_release"]
    count = content["count"]
    id_diler = content["id_diler"]
    result = model_controller.insert_model(model_name, price, componentry, year_release, count, id_diler)
    return jsonify(result)


@app.route("/diler/model", methods=["PUT"])
def upd_model():
    content = request.get_json()
    model_name = content["model_name"]
    price = content["price"]
    componentry = content["componentry"]
    year_release = content["year_release"]
    count = content["count"]
    id_diler = content["id_diler"]
    id_model = content["id_model"]
    result = model_controller.update_model(model_name, price, componentry, year_release, count, id_diler, id_model)
    return jsonify(result)


@app.route("/diler/model/", methods=["DELETE"])
def del_model():
    content = request.get_json()
    id_model = content["id"]
    result = model_controller.delete_model_by_id(id_model)
    return jsonify(result)


"""
Car table managing
"""
@app.route("/diler/model/car/all", methods=["GET"])
def get_cars_all():
    cars = car_controller.get_cars()
    return jsonify(cars)


@app.route("/diler/model/car", methods=["GET"])
def get_cars():
    query_parameters = request.args
    id_model = query_parameters.get('id_model')
    car = car_controller.get_cars_by_model_id(id_model)
    return jsonify(car)


@app.route("/diler/model/car", methods=["POST"])
def ins_car():
    content = request.get_json()
    id_model = content['id_model']
    date_purchase = content['date_purchase']
    result = car_controller.insert_car(id_model, date_purchase)
    return jsonify(result)


@app.route("/diler/model/car", methods=["PUT"])
def upd_car():
    content = request.get_json()
    id_model = content['id_model']
    id_car = content['id_car']
    date_purchase = content['date_purchase']
    result = car_controller.update_car(id_model, id_car, date_purchase)
    return jsonify(result)


@app.route("/diler/model/car", methods=["DELETE"])
def del_car():
    content = request.get_json()
    id_car = content['id']
    result = car_controller.delete_car_by_id(id_car)
    return jsonify(result)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=False)
