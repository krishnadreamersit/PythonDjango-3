# Task-Automation
    # Create table on SQLitedb
    # Read records from CSV
    # Insert records on SQLitedb-> table

import sqlite3
import csv
import sys


class Database():
    def __init__(self):
        self.DB_NAME ='employees.db'

    def create_table(self):
        sql ="""
        CREATE TABLE tbl_employees(
            EMP_ID INT primary key,
            FIRST_NAME TEXT(50),
            LAST_NAME TEXT(50),
            GENDER TEXT(50),
            E_MAIL TEXT(50),
            DATE_OF_BIRTH TEXT(50),
            DATE_OF_JOINING TEXT(50),
            SSN TEXT(50),
            DEPARTMENT_ID INT
        )
        """
        try:
            conn = sqlite3.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            pass

    def insert_record(self, record):
        sql = """INSERT INTO tbl_employees(EMP_ID, FIRST_NAME, LAST_NAME, GENDER, E_MAIL, DATE_OF_BIRTH, DATE_OF_JOINING, SSN, DEPARTMENT_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            conn = sqlite3.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute(sql, record)
            conn.commit()
            conn.close()
            print("Record insert successfully")
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            pass

class CSV():
    def read_csv(self, filename):
        try:
            csv_file = open(filename, "r")
            reader = csv.reader(csv_file)
            db = Database()
            i=0
            for row in reader:
                if i!=0:
                   # print(row)
                    db.insert_record(row)
                i+=1
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            pass

# Test
obj_csv = CSV()
obj_csv.read_csv("Employee_records.csv")

# db = Database()
# db.create_table()
# db.insert_record()
# https://sqliteonline.com/

