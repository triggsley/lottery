import sqlite3

class LotteryResultsCRUD:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create the 'lottery_results' table if it doesn't exist
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS lottery_results (
            draw_id TEXT PRIMARY KEY,
            lottery_id TEXT,
            draw_date TEXT,
            draw_column TEXT,
            draw_values TEXT            
        )
        '''
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def check_and_insert(self, melted_df):

        # Check if the draw_id already exists in the table
        tmp_draw_id = melted_df['draw_id'][0]
        check_sql = 'SELECT COUNT(*) FROM lottery_results WHERE draw_id = ?'
        self.cursor.execute(check_sql, (tmp_draw_id,))
        result = self.cursor.fetchone()

        if result[0] == 0:

            for _, row in melted_df.iterrows():
                draw_id = row['draw_id']
                lottery_id = row['lottery_id']
                draw_date = row['draw_date_str']
                draw_column = row['draw_column']
                draw_values = row['draw_values']

                insert_sql = 'INSERT INTO lottery_results (lottery_id, draw_id, draw_date, draw_column, draw_values) VALUES (?, ?, ?, ?, ?)'
                #print(insert_sql)
                self.cursor.execute(insert_sql, (lottery_id, draw_id, draw_date, draw_column, draw_values))
                self.conn.commit()
                print(f"Draw ID '{draw_id}' added to the table.")

        else:
            print(f"Draw ID '{tmp_draw_id}' already exists in the table.")

    def close_connection(self):
        self.conn.close()


# Example usage:
if __name__ == '__main__':
    db_file = 'your_database.db'  # Replace with your SQLite database file
    crud = LotteryResultsCRUD(db_file)

    # Example data to insert
    draw_id = 'lo|2022-12-31'
    draw_date = 'Saturday 31st December 2022'
    draw_column = '2\n3\n27\n29\n39\n44\n6'
    draw_values = '£7,789,557'
    lottery_id = 'lo'

    # Check and insert the data
    crud.check_and_insert(draw_id, draw_date, draw_column, draw_values, lottery_id)

    # Close the connection when done
    crud.close_connection()
