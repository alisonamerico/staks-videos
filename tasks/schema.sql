create table if not exists tasks (
    id integer primary key autoincrement,
    name char(100) not null,
    theme char(100) not null,
    closed bool not null
);

insert or ignore into tasks (id, name, theme, closed) values (0, 'Start learning Pyramid', 'Music', 0);
insert or ignore into tasks (id, name, theme, closed) values (1, 'Do quick tutorial', 'Game', 0);
insert or ignore into tasks (id, name, theme, closed) values (2, 'Have some beer!', 'Sport', 0);