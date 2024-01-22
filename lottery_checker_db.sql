create table draw_balls
(
    lottery_id TEXT,
    draw_id    TEXT,
    ball_type  TEXT,
    ball_id    integer
);

create table draw_breakdown
(
    lottery_id       TEXT,
    draw_id          TEXT,
    breakdown_column TEXT,
    breakdown_values TEXT,
    breakdown_id     TEXT
);

create table lottery_meta
(
    lottery_name              TEXT,
    lottery_slug              TEXT,
    active                    TEXT,
    lottery_start_year        INTEGER,
    lottery_archive_columns   TEXT,
    lottery_end_year          integer,
    lottery_balls_draw        TEXT,
    lottery_id                TEXT,
    lottery_breakdown_columns TEXT,
    lottery_class             TEXT
);

create table lottery_results
(
    lottery_id  TEXT,
    draw_id     TEXT,
    draw_date   TEXT,
    draw_column TEXT,
    draw_values TEXT
);