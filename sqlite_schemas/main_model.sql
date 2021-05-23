create table model
(
    model_id     INTEGER
        primary key autoincrement,
    name         TEXT    not null,
    componentry  TEXT    not null,
    year_release INTEGER not null,
    price        REAL    not null,
    count        INTEGER,
    diler_id     INTEGER not null
        references diler
);

INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (1, '812 superfast', 'extra', 2017, 3000000, 8, 4);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (2, 'Monza SP1', 'mid', 2020, 3000000, 6, 4);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (3, 'Roma', 'low', 2015, 3500000, 7, 4);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (4, 'portofino', 'extra', 2016, 2000000, 5, 4);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (5, 'a1', 'mid', 2010, 1000000, 30, 3);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (6, 'a2', 'mid', 2016, 4000000, 6, 3);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (7, 'a3', 'low', 2017, 6000000, 17, 3);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (8, 'a4', 'extra', 2018, 3000000, 7, 3);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (9, 'a5', 'extra', 2020, 5000000, 2, 3);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (10, 'x2', 'extra', 2011, 3000000, 5, 1);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (11, 'x3', 'extra', 2010, 2000000, 8, 1);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (12, 'x4', 'extra', 2013, 4000000, 5, 1);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (13, 'x5', 'extra', 2019, 7000000, 4, 1);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (14, 'x7', 'extra', 2077, 10000000, 1, 1);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (15, 'w210', 'mid', 2020, 1000000, 5, 2);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (16, 'w211', 'low', 204, 1230000, 15, 2);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (17, 'w212', 'extra', 2011, 2000000, 3, 2);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (18, 'x164', 'extra', 2012, 1002000, 2, 2);
INSERT INTO model (model_id, name, componentry, year_release, price, count, diler_id) VALUES (19, 'w163', 'extra', 2014, 12800000, 14, 2);