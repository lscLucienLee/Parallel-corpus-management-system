import pandas as pd
import mysql.connector


class CSVToMySQL:
    def __init__(self, db_config, csv_file_path, table_name):
        self.db_config = db_config
        self.csv_file_path = csv_file_path
        self.table_name = table_name

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                print("Connected to MySQL")
                return connection
        except Exception as e:
            print("Error connecting to MySQL:", e)
            return None

    def close_db_connection(self, connection):
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")

    def create_table(self, connection, column_names):
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} "
        create_table_query += f"({', '.join([f'{col_name} TEXT' for col_name in column_names])})"
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()

    def import_csv_to_mysql(self,data=None):
        connection = self.connect_to_db()
        if connection:
            if data is None:
                df = pd.read_csv(self.csv_file_path)
            else:
                df = pd.DataFrame(data)
            column_names = df.columns.tolist()
            self.create_table(connection, column_names)

            cursor = connection.cursor()
            for _, row in df.iterrows():
                insert_query = f"INSERT INTO {self.table_name} ({', '.join(column_names)}) VALUES "
                insert_query += f"({', '.join(['%s' for _ in range(len(column_names))])})"
                cursor.execute(insert_query, tuple(row))
            connection.commit()
            cursor.close()

            self.close_db_connection(connection)
            print("CSV data imported to MySQL successfully")

