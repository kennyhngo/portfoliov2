PRAGMA foreign_keys = ON;

INSERT INTO skills(language, time, proficiency, meter, description, filelink)
VALUES
    ("C++", "2019-01-01", "Advanced", 95, "Should I add what I coded with the language too?", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/640px-ISO_C%2B%2B_Logo.svg.png"),
    ("Python", "2019-01-01", "Advanced", 95, "Backend of Instagram Clone.", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png"),
    ("R", "2020-08-01", "Elementary", 35, "Data analysis.", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/R_logo.svg/640px-R_logo.svg.png"),
    ("Git", "2019-08-01", "Intermediate", 70, "Control version.", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Git-icon-black.svg/640px-Git-icon-black.svg.png"),
    ("HTML 5", "2021-08-01", "High Intermediate", 80, "Website.", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Devicon-html5-plain.svg/640px-Devicon-html5-plain.svg.png"),
    ("CSS 3", "2021-08-01", "Intermediate", 75, "Website.", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/640px-CSS3_logo.svg.png");


INSERT INTO skills(language, time, proficiency, meter, description, filelink, framework)
VALUES
        ("JavaScript ES6", "2021-09-01", "Intermediate", 70, "Discord bot, Instagram Clone.", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/640px-Unofficial_JavaScript_logo_2.svg.png", "ReactJS"),
        ("SQL", "2022-01-01", "Elementary", 50, "Storing Instagram user data.", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Sqlite-square-icon.svg/640px-Sqlite-square-icon.svg.png", "SQLite3"),
        ("LaTeX", "2019-08-01", "Elementary", 50, "Written homework.", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/LaTeX_logo.png/640px-LaTeX_logo.png", "OverLeaf");