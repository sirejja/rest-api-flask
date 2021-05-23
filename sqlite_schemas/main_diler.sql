create table diler
(
    diler_id INTEGER
        primary key autoincrement,
    name     TEXT not null
);

INSERT INTO diler (diler_id, name) VALUES (1, 'bmw');
INSERT INTO diler (diler_id, name) VALUES (2, 'mercedes');
INSERT INTO diler (diler_id, name) VALUES (3, 'audi');
INSERT INTO diler (diler_id, name) VALUES (4, 'ferrari');