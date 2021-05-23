create table sqlite_master
(
    type     text,
    name     text,
    tbl_name text,
    rootpage int,
    sql      text
);

INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'diler', 'diler', 2, 'CREATE TABLE diler(
                diler_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'sqlite_sequence', 'sqlite_sequence', 3, 'CREATE TABLE sqlite_sequence(name,seq)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'model', 'model', 4, 'CREATE TABLE model(
                model_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                componentry TEXT NOT NULL,
                year_release INTEGER NOT NULL,
                price REAL NOT NULL,
                count INTEGER,
                diler_id INTEGER NOT NULL,
                FOREIGN KEY (diler_id) references diler(diler_id)
            )');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'car', 'car', 5, 'CREATE TABLE car(
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_purchase TEXT NOT NULL,
                model_id INTEGER NOT NULL,
                FOREIGN KEY (model_id) references model(model_id)
            )');