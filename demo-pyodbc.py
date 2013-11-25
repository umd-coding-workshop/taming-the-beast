import pyodbc

# Demonstrate use of pyodbc to connect to EAD MS Access database

# Setup connection parameters
db_file = r'''C:\Users\User\Documents\taming-the-beast\ead_be_2013-10-06.accdb'''
user = 'admin'
password = ''
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (db_file, user, password)

# Connect to the database
conn = pyodbc.connect(odbc_conn_str)

# Iterate over the list of tables
cursor = conn.cursor()
for row in cursor.tables():

    # Skip the MS Access system tables
    if not row.table_name.startswith('MSys'):

        # Get number of rows in the table
        countCursor = conn.cursor()
        count = countCursor.execute("select count(*) from %s" % (row.table_name)).fetchone()[0]
        countCursor.close()
    
        print("table: %s, rowcount=%d" %(row.table_name, count))

cursor.close()

