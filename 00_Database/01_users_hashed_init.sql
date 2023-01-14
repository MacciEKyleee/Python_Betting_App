DROP TABLE IF EXISTS "users";

CREATE TABLE "users"
(
    "id"       INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL,
    "is_admin" NUMERIC    NOT NULL
);

-- 'Administrator' ma hasło 'admin'
-- 'testowy' ma hasło 'testowy'
-- 'Mateusz' ma hasłó 'Mateusz123'
-- 'Bartosz' ma hasło 'Bartosz123'
INSERT INTO "users"
VALUES
        (NULL, 'Administrator','pbkdf2:sha256:260000$rZydEJoz2kt6Vc2r$cd05fb853d5dcb0999308ca3aa9e674c8528fc58e6a883b967c9b3c46565b95a', 1),
        (NULL, 'testowy', 'pbkdf2:sha256:150000$pZTQ81tw$0b4c87aaa463676d91c6c99690634288b1fae8a4f8a34df865ae72f504a50e0a',0),
        (NULL, 'Mateusz', 'pbkdf2:sha256:260000$t4k6sR4ntNExJPMy$6181bd502d122ac25151d283d95a0cea58d36056024c013913095bcac5cf8f6f',0),
        (NULL, 'Bartosz', 'pbkdf2:sha256:260000$lNOWZ7ihDyoPnKCC$0caac4cdf87ee0946bed4298803d1204ef2e5b75f4b3be025765eef9067b8c44',0);