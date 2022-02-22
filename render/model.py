import json
import os
import pathlib
import arrow # type: ignore
import sqlite3


def sql_db():
    db_path = pathlib.Path(os.getcwd())
    db_path = pathlib.Path(db_path/'sql'/'portfolio.sqlite3')
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    skills = cur.execute(
        "SELECT * "
        "FROM skills "
        "ORDER BY meter DESC"
    )
    skills = cur.fetchall()
    con.close()
    return skills


def create_json():
    skills_db = sql_db()
    skills = []
    for skill_db in skills_db:
        skill = {}
        skill['language'] = skill_db[0]
        skill['time'] = get_time(skill_db[1])
        skill['proficiency'] = skill_db[2]
        skill['meter'] = skill_db[3]
        skill['description'] = skill_db[4]
        skill['filelink'] = skill_db[5]
        if skill_db[6]:
            skill['framework'] = skill_db[6]
        skills.append(skill)
    context = {"skills": skills}
    data = {"template": "index.html", "context": context}
    data = json.dumps(data)

    # write to json file
    path = pathlib.Path(os.getcwd())
    path = str(path/'render/context.json')
    with open(path, 'w+', encoding='utf-8') as outfile:
        outfile.write(data)


def get_time(db_time):
    now = arrow.now().format("YYYY-MM-DD")
    arr_now = now.split('-')
    arr_time = db_time.split('-')
    time_diff = []
    for time_now, time_time in zip(arr_now, arr_time):
        time_now = int(time_now)
        time_time = int(time_time)
        diff = abs(time_now - time_time)
        time_diff.append(round(diff))
    # dont care about day
    # check year
    if time_diff[0] != 0:
        if time_diff[0] == 1:
            return f'{time_diff[0]} year'
        return f'{time_diff[0]} years'
    # year is 0
    else:
        if time_diff[1] == 1:
            return f'{time_diff[1]} month'
        return f'{time_diff[1]} months'