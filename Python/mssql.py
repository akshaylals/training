# importing pyodbc
import pyodbc

# Create a connection with the connection string
conn = pyodbc.connect('Driver={SQL Server};'
            'Server=DESKTOP-4GIE4U2\SQLEXPRESS01;'
            'Database=employee_db;'
            'Trusted_Connection=yes')

myCursor = conn.cursor()

# using cursor, execute SQL commands
print('EmployeeMaster')
myCursor.execute('SELECT * FROM EmployeeMaster;')
for i in myCursor:
    print(i)

print('-' * 60)
print('EmployeeMaster2')
myCursor.execute('SELECT * FROM EmployeeMaster2;')
for i in myCursor:
    print(i)

print('-' * 60)


# Creating a table
try:
    myCursor.execute('''CREATE TABLE EmployeeMaster3(
        Id INT IDENTITY PRIMARY KEY,
        EmployeeCode VARCHAR(10),
        EmployeeName VARCHAR(25),
        DepartmentCode VARCHAR(10),
        LocationCode VARCHAR(10),
        Salary INT
    );''')
    # commit the changes
    conn.commit()
except Exception as e:
    print('Cannot create table because:')
    print(e)

print('-' * 60)

try:
    myCursor = conn.cursor()
    myCursor.execute('SELECT * FROM EmployeeMaster;')
    # for row in myCursor.fetchall():
    #     print(row)
    employees = [{'id': row[0], 'empcode': row[1], 'empname': row[2]} for row in myCursor]
    print(employees)

except Exception as e:
    print('Cannot read the table:\n', e)


# Insert data 
# try:
#     myCursor = conn.cursor()
#     myCursor.execute("INSERT INTO EmployeeMaster VALUES ('E0008', 'Arjun', 'IT', 'TVM', 8000);")
#     conn.commit()
# except:
#     print('Cannot insert into the table')


# Inserting data
# try:
#     myCursor = conn.cursor()
#     myCursor.execute(
#         'INSERT INTO EmployeeMaster VALUES (?, ?, ?, ?, ?)',
#         ('E0009', 'Arjuna', 'IT', 'TVM', 9000)
#     )
#     conn.commit()
# except:
#     print('Cannot insert into the table')

conn.close()