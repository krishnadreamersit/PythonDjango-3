# HW? [create functions to manage record in datbase table]
    # insert record
    # update record
    # select record
    # delete record

import sqlite3
import sys
DB_FILE = "./db.sqlite3"


class MyDatabase():
    def connect_db(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            conn.close()
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def create_table(self):
        # DDL - Data Definition Language
        sql="""
            CREATE TABLE tbl_persons(
                pid INTEGER,
                fullname TEXT(50),
                contactaddress TEXT(50)
            )
        """
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor() # Executor Object - runs the sql statement
            cursor.execute(sql) # Execute
            conn.commit() # Save
            conn.close() # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def insert_record(self, pid, full_name, contact_address):
        sql = """INSERT INTO tbl_persons(pid, fullname, contactaddress) VALUES(?, ?, ?)"""
        values = (pid, full_name, contact_address)
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()  # Executor Object - runs the sql statement
            cursor.execute(sql, values)  # Execute
            conn.commit()  # Save
            conn.close()  # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def select_all(self):
        sql = """SELECT * FROM tbl_persons"""
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()  # Executor Object - runs the sql statement
            cursor.execute(sql)  # Execute
            records = cursor.fetchall()
            for record in records:
                print(record)
            conn.close()  # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def search_record(self, search_term):
        sql = """SELECT * FROM tbl_persons WHERE fullname=? or contactaddress=?"""
        values = (search_term, search_term)
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()  # Executor Object - runs the sql statement
            cursor.execute(sql, values)  # Execute
            records = cursor.fetchall()
            for record in records:
                print(record)
            conn.close()  # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def update_record(self, pid, full_name, contact_address):
        sql = """UPDATE tbl_persons set fullname=?, contactaddress=? where pid=?"""
        values = (full_name, contact_address, pid)
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()  # Executor Object - runs the sql statement
            cursor.execute(sql, values)  # Execute
            conn.commit()  # Save
            conn.close()  # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False

    def delete_record(self, pid):
        sql = """DELETE FROM tbl_persons where pid=?"""
        values = (pid,)
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()  # Executor Object - runs the sql statement
            cursor.execute(sql, values)  # Execute
            conn.commit()  # Save
            conn.close()  # Close
            return True
        except:
            print("Error : ", sys.exc_info()[1])
            return False