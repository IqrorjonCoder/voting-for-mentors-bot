import sqlite3

# connection = sqlite3.connect("./mentors.db")
# connection.execute("""
# CREATE TABLE mentors(mentors_name CHAR(30), result CHAR(20), becauseof CHAR(70))
# """)


def to_sql(mentors_name, result, becauseof):
    connection = sqlite3.connect("C:/Users/Student/PycharmProjects/astrummentors/voting-mentors/mentors.db")
    connection.execute(f"""
    INSERT INTO mentors(mentors_name, result, becauseof)
    VALUES ("{mentors_name}", "{result}", "{becauseof}");
    """)
    connection.commit()
    connection.close()

