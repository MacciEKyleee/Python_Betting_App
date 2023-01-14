import sqlite3

def execute_script(cursor, script_file):
    with open(script_file, encoding='utf-8') as f:
        query = f.read()
    cursor.executescript(query)


if __name__ == '__main__':
    conn = sqlite3.connect('World_Cup_2022')
    cursor = conn.cursor()

    execute_script(cursor, '00_drop_tables.sql')
    execute_script(cursor, '01_users_hashed_init.sql')
    execute_script(cursor, '02_groups_init.sql')
    execute_script(cursor, '03_matches_init.sql')
    execute_script(cursor, '04_teams_init.sql')
    execute_script(cursor, '05_results.sql')
    execute_script(cursor, '06_final_results.sql')

    conn.commit()

    conn.close()
