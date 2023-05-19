import mysql.connector
import csv

class IDBtoCSVConverter:
    def __init__(self, host, port, user, password, database, table):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def convert(self, output_file):
        # Connect to MySQL server
        conn = mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        cursor = conn.cursor()

        # Get column names
        cursor.execute("DESCRIBE {}".format(self.table))
        columns = [row[0] for row in cursor.fetchall()]

        # Query table data
        cursor.execute("SELECT * FROM {}".format(self.table))
        rows = cursor.fetchall()

        # Write data to CSV file
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            for row in rows:
                writer.writerow(row)

        # Close database connection
        cursor.close()
        conn.close()
