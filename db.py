import sqlite3

from flask import Blueprint, request, redirect, session

from auth import login_required
from db_utils import get_connection, get_all_typed_results
from datetime import datetime


database_bp = Blueprint('database_endpoints', __name__)


@database_bp.route('/add_item', methods=['POST'])
@login_required
def add_item():
    home_score = request.form.get('type_host')
    guest_score = request.form.get('type_guest')
    matches_id = request.form.get('match_id')
    user_id = session.get('user_id')
    entry_time = str(datetime.now())

    conn = get_connection()
    c = conn.cursor()

    query_1 = c.execute('SELECT COUNT(*) FROM results WHERE "matches_id" = ? AND "user_id"= ?', (matches_id, user_id))
    user_data = query_1.fetchall()[0][0]

    query_time = c.execute('SELECT "date" FROM matches WHERE "id" = ?', (matches_id, ))
    match_time = query_time.fetchall()[0][0]

    if match_time > entry_time:
        if int(user_data) != 0:
            return "You have already submitted your tip for the result", 400
        else:
            query_2 = 'INSERT INTO "results" ("matches_id", "user_id", "host_goals", "guest_goals", "data") VALUES (?, ?, ?, ?, ?)'
            params = (matches_id, user_id, home_score, guest_score, entry_time)

            try:
                c.execute(query_2, params)
            except sqlite3.OperationalError:
                return "Bad Request", 400
            conn.commit()
    else:
        return "Time for result typing is expired", 400

    return redirect('/')


@database_bp.route('/delete_item', methods=['POST'])
@login_required
def delete_item():
    user_id = session.get('user_id')
    item_id = request.form['matches_id']

    conn = get_connection()
    c = conn.cursor()

    query = 'DELETE FROM "results" WHERE ("matches_id" = ? AND "user_id" = ?)'
    params = (item_id, user_id)

    c.execute(query, params)
    conn.commit()

    return redirect('/')


@database_bp.route('/result_item', methods=['POST'])
@login_required
def result_item():
    home_score = request.form.get('type_host')
    guest_score = request.form.get('type_guest')
    matches_id = request.form.get('match_id')

    conn = get_connection()
    c = conn.cursor()

    query_home = c.execute('SELECT "home_score" FROM matches WHERE "id" = (?)', (matches_id,))
    home_team_score = query_home.fetchall()[0][0]

    query_guest = c.execute('SELECT "guest_score" FROM matches WHERE "id" = (?)', (matches_id,))
    guest_team_score = query_guest.fetchall()[0][0]

    if (home_team_score is None) & (guest_team_score is None):
        query_2 = 'UPDATE "matches" SET "home_score" = (?), "guest_score"= (?) WHERE "id" = (?)'
        params = (home_score, guest_score, matches_id)

        try:
            c.execute(query_2, params)
        except sqlite3.OperationalError:
            return "Bad Request", 400
        conn.commit()

    else:
        return "You have already submitted your tip for the result", 400

    return redirect('/')


@database_bp.route('/delete_result_item', methods=['POST'])
@login_required
def delete_result_item():
    user_id = session.get('user_id')
    item_id = request.form['matches_id']

    conn = get_connection()
    c = conn.cursor()

    query = 'DELETE FROM "matches" WHERE ("id" = ? AND "user_id" = ?)'
    params = (item_id, user_id)

    c.execute(query, params)
    conn.commit()

    return redirect('/')

def calculate_score(user_id):
    user_id = session.get('user_id')


@database_bp.route('/score', methods=['POST'])
@login_required
def score():
    user_id = session.get('user_id')
    matches = get_all_typed_results(user_id)

    list_of_typing = []

    for element in matches:
        list_of_typing.append(element['matches_id'])
    conn = get_connection()
    c = conn.cursor()

    query_points = c.execute('SELECT "points" FROM results WHERE "user_id" = (?) AND "points" is NULL', (user_id,))

    z = query_points.fetchall()

    if len(z) == 0:
        return "You have already submitted your tip for the result", 400

    is_any_points = z[0][0]

    if is_any_points is None:
        for matches_id in list_of_typing:

            conn = get_connection()
            c = conn.cursor()

            user_data_1 = c.execute('SELECT host_goals FROM results WHERE ("matches_id" = ? AND "user_id"= ?)', (matches_id, user_id))
            query_1 = user_data_1.fetchall()[0][0]

            user_data_2 = c.execute('SELECT guest_goals FROM results WHERE ("matches_id" = ? AND "user_id"= ?)', (matches_id, user_id))
            query_2 = user_data_2.fetchall()[0][0]

            user_data_3 = c.execute('SELECT home_score FROM matches WHERE "id" = ? ', (matches_id, ))
            query_3 = user_data_3.fetchall()[0][0]

            user_data_4 = c.execute('SELECT guest_score FROM matches WHERE "id" = ?', (matches_id, ))
            query_4 = user_data_4.fetchall()[0][0]

            if (query_1 == query_3) & (query_2 == query_4):
                points = 3
            elif (query_1 == query_2) & (query_3 == query_4):
                points = 1
            elif (query_1 > query_2) & (query_3 > query_4):
                points = 1
            elif (query_1 < query_2) & (query_3 < query_4):
                points = 1
            else:
                points = 0

            final_query = 'UPDATE "results" SET "points" = (?) WHERE ("user_id" = (?) AND "matches_id" = (?) )'
            params = (points, user_id, matches_id)

            try:
                c.execute(final_query, params)
            except sqlite3.OperationalError:
                return "Bad Request", 400

            conn.commit()

            conn = get_connection()
            c = conn.cursor()

            user_points = c.execute('SELECT SUM("points") FROM results WHERE "user_id" = ?', (user_id,))
            query_points = str(user_points.fetchall())

            all_points = 'UPDATE "final" SET "points" = (?) WHERE "user_id" = (?)'
            params_point = (query_points, user_id)

            try:
                c.execute(all_points, params_point)
            except sqlite3.OperationalError:
                return "Bad Request", 400

            conn.commit()
    else:
        return "You have already submitted your tip for the result", 400

    return redirect('/')
