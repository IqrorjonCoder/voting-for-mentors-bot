import sqlite3
import gspread

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


def to_googlesheets(mentors_name, result, becauseof):
    # https://docs.google.com/spreadsheets/d/1ethT44IClSK8v1qTnJXB5Qdmad2L2QvVtSMODxhI_Eo/edit#gid=2010795925
    gc = gspread.service_account(filename="voiting-for-mentors-43f7032bd3cf.json")
    sh = gc.open("mentors data")
    worksheet = sh.worksheet(title="mentors")
    worksheet.append_row([mentors_name, result, becauseof])

