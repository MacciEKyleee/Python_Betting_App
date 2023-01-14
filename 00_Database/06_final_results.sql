CREATE TABLE "final"
(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "points" INTEGER,
    FOREIGN KEY ("user_id") REFERENCES "users" ("id")
);


INSERT INTO "final"
VALUES (NULL, NULL, NULL);
