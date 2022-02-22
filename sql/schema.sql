PRAGMA foreign_keys = ON;

CREATE TABLE skills
(
    language VARCHAR(40) PRIMARY KEY,
    time DATETIME NOT NULL,
    proficiency VARCHAR(40) NOT NULL,
    meter INTEGER NOT NULL,
    description TEXT NOT NULL,
    filelink TEXT NOT NULL,
    framework TEXT DEFAULT NULL
);