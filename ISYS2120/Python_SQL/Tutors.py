import psycopg2

# TODO: replace the content of this cell with your Python + psycopg2 solution
def create_tutor_table(sql, args=None):
    conn = connect()
    with conn.cursor() as cur:
        try:
            curs.execute(sql, "CREATE TABLE Salary (rate_code VARCHAR(8) PRIMARY KEY, Rate FLOAT, Description VARCHAR(80))")
            curs.execute(sql, "CREATE TABLE Tutor (sid INT PRIMARY KEY, rate_code VARCHAR(8) REFERENCING Salary(rate_code))")
            curs.execute(sql, "CREATE TABLE UoS (sid INT REFERENCING Tutor(sid) NOT NULL, uos VARCHAR(8) PRIMARY KEY)")
        except Exception as e:
            print("Query Failed with error {}".format(e))
            conn.rollback()
        finally:
            conn.close()
