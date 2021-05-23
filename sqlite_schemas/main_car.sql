create table car
(
    car_id        INTEGER
        primary key autoincrement,
    date_purchase TEXT    not null,
    model_id      INTEGER not null
        references model
);

INSERT INTO car (car_id, date_purchase, model_id) VALUES (1, '12.10.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (2, '22.10.2020', 10);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (3, '12.07.2020', 10);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (4, '12.05.2020', 15);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (5, '12.10.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (6, '12.02.2020', 15);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (7, '12.10.2020', 15);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (8, '12.03.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (9, '04.10.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (10, '07.04.2020', 18);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (11, '12.10.2020', 18);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (12, '08.10.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (13, '12.09.2020', 13);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (14, '15.04.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (15, '12.10.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (16, '12.10.2020', 14);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (17, '17.12.2020', 1);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (18, '11.10.2020', 15);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (19, '12.10.2020', 15);
INSERT INTO car (car_id, date_purchase, model_id) VALUES (20, '18.10.2020', 16);