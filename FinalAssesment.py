import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        apple = sqlite3.connect('finalAssesment.db')
        return apple
    except Error:
        print(Error)


def sql_table(apple):
    cursorObj = apple.cursor()

    cursorObj.execute("CREATE TABLE employee(employee_id n(5), name char(30), city char(35), commission decimal(7.2));")

    cursorObj.executescript("""
    INSERT INTO employee VALUES(1001,'purushottam kumar', 'tokyo',0.23);
    INSERT INTO employee VALUES(1002,'matt demon', 'berlin',0.43);
    INSERT INTO employee VALUES(1003,'pallavi kumar', 'chennai',0.13);
    INSERT INTO employee VALUES(1004,'sunny kumar', 'singapore',0.19);
    """)

    apple.commit()

    cursorObj.execute("SELECT * FROM employee")
    rows = cursorObj.fetchall()
    print("Employee details")
    for row in rows:
        print(row)

    ### for accesing only certain records

    # cursorObj.execute("SELECT name,city FROM employee WHERE employee_id >1001 and employee_id < 1005 ")
    # rows = cursorObj.fetchall()
    # print("Employee details")
    # for row in rows:
    #     print(row)

# for updating certain records
#
    # sql_update = """ UPDATE employee set name = "jktech" WHERE employee_id = 1004 """
    # cursorObj.execute(sql_update)
    # apple.commit()
    #
    # cursorObj.execute("SELECT * FROM employee")
    # rows = cursorObj.fetchall()
    # print("\n")
    # print("Table after update operation is performed!\n")
    #
    # for row in rows:
    #     print(row)

## DELETE OPERATION

    # cursorObj.execute("SELECT * FROM employee")
    # rows = cursorObj.fetchall()
    # print("\n")
    # print("Original Table\n")
    # for p in rows:
    #     print(p)
    #
    #
    # delete_id = 1002
    # cursorObj.execute("""
    # DELETE FROM employee WHERE employee_id = ?
    # """,(delete_id, ))
    # apple.commit()
    #
    # cursorObj.execute("SELECT * FROM employee")
    # rows = cursorObj.fetchall()
    # print("\n")
    # print("Table after deletion operation is performed\n")
    # for row in rows:
    #     print(row)



sqllite_apple = sql_connection()
sql_table(sqllite_apple)
if(sqllite_apple):
    sqllite_apple.close()
    print("\n exit here")