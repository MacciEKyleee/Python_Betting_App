CREATE TABLE "matches"
(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "group_id" INTEGER,
    "date" TEXT NOT NULL,
    "team_host" TEXT NOT NULL,
    "team_guest" TEXT NOT NULL,
    "home_score" INTEGER,
    "guest_score" INTEGER,
    FOREIGN KEY ("group_id") REFERENCES "groups" ("id")
);
--
--INSERT INTO "matches"
--VALUES (1, 1, "2022-11-22 11:00:00.000", 1, 23, NULL, NULL, NULL, NULL),
--       (2, 1, "2022-11-22 17:00:00.000", 17, 20, NULL, NULL, NULL, NULL),
--       (3, 1, "2022-11-26 14:00:00.000", 20, 23, NULL, NULL, NULL, NULL),
--       (4, 1, "2022-11-26 20:00:00.000", 1, 17, NULL, NULL, NULL, NULL),
--       (5, 1, "2022-11-30 20:00:00.000", 20, 1, NULL, NULL, NULL, NULL),
--       (6, 1, "2022-11-30 20:00:00.000", 23, 17, NULL, NULL, NULL, NULL);

INSERT INTO "matches"
VALUES (1, 1, "2022-11-22 11:00:00.000", "Argentina", "Saudi_Arabia", NULL, NULL),
       (2, 1, "2022-11-22 17:00:00.000", "Mexico", "Poland", NULL, NULL),
       (3, 1, "2022-11-26 14:00:00.000", "Poland", "Saudi_Arabia", NULL, NULL),
       (4, 1, "2022-11-26 20:00:00.000", "Argentina", "Mexico", NULL, NULL),
       (5, 1, "2022-11-30 20:00:00.000", "Poland", "Argentina", NULL, NULL),
       (6, 1, "2022-11-30 20:00:00.000", "Saudi_Arabia", "Mexico", NULL, NULL);