import mysql.connector

import csv


def fetch_table_data(table_name):
    # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    cnx = mysql.connector.connect(
        host='localhost',
        database='du_an_ban_dat',
        user='root',
        password='Password12@'
    )

    cursor = cnx.cursor()
    cursor.execute('select * from ' + table_name + ' where categoty LIKE "%Nhà riêng%" and provines LIKE "%Hà Nội%" and created_at between "10/11/2023" and "19/11/2023" limit 100'  )

        
    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    # Closing connection
    cnx.close()

    return header, rows


def export(table_name):
    header, rows = fetch_table_data(table_name)

    # Create csv file
    f = open(table_name + '.csv', 'w',newline='', encoding='utf-8')
    
    
    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)


# Tables to be exported
export('infor_news')
#export('TABLE_2')