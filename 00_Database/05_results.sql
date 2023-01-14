CREATE TABLE "results"
(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "matches_id" INTEGER,
    "user_id" INTEGER,
    "host_goals" INTEGER,
    "guest_goals" INTEGER,
    "points" INTEGER,
    "data" TEXT,
    FOREIGN KEY ("matches_id") REFERENCES "matches" ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users" ("id")
);


INSERT INTO "results"
VALUES (1, NULL, NULL, NULL, NULL, NULL, NULL);