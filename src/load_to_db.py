import psycopg2
import pandas as pd
from style import custom_border_message

def load_to_db(df: pd.DataFrame):
    """
    Loads cleaned Cafe Sales Data into the PostgreSQL database.
    Creates the table if it doesnt exist.
    """
    conn = None
    cursor = None

    try:
        # Database connection settings:
        conn = psycopg2.connect(
            host="localhost",
            database="cafe_db",
            user="cafe_user",
            password="cafe_pass",
            port=5432
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS sales_data (
            id SERIAL PRIMARY KEY,
            drink VARCHAR(50),
            price NUMERIC(6,2),
            branch VARCHAR(50),
            payment_type VARCHAR(20),
            sales_date DATE
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        custom_border_message("[INFO] Table 'sales_data' ready in PostgreSQL.")



        # Insert cleaned data
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO sales_data (drink, price, branch, payment_type, sales_date)
                VALUES (%s, %s, %s, %s, %s);
                """, (row['Drink'], row['Price_num'], row['Branch'], row['Payment Type'], row['Date']))
        
        conn.commit()
        custom_border_message("[INFO] Data successfully loaded into PostgreSQL!")
    
    except Exception as e:
        custom_border_message(f"[ERROR] Failed to load data into PostgreSQL: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
