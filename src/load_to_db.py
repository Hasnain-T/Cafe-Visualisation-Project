import psycopg2
import pandas as pd
from style import custom_border_message

def load_to_db(df: pd.DataFrame):
    """
    Loads cleaned Cafe Sales Data into the PostgreSQL database.
    Creates the table if it doesnt exist.
    Uses 'Sale_GUID' as a unique key to avoid duplicates.
    Inserts cleaned data using 'Price_num' for numeric stroage.
    Also saves a clean display version (without 'Price_num') for CSV.
    Returns True if the load is successful, False otherwise.
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
        custom_border_message("[Info] Connected to PostgreSQL successfully.")
        
        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS sales_data (
            id SERIAL PRIMARY KEY,
            sale_guid VARCHAR(10) UNIQUE,
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

        # Insert cleaned data into PostgreSQL
        print(f"Inserting into columns: {tuple(df.columns)}")

        insert_query = """
        INSERT INTO sales_data (sale_guid, drink, price, branch, payment_type, sales_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (sale_guid) DO NOTHING;
        """
        inserted_count = 0

        for _, row in df.iterrows():
            try:
                cursor.execute(insert_query, (
                    row['Sale_GUID'],
                    row['Drink'],
                    row['Price_num'],
                    row['Branch'],
                    row['Payment Type'],
                    row['Date']
                    ))
                inserted_count += 1

            except Exception as row_error:
                # Log row-level error but continue with other rows
                custom_border_message(f"[WARN] Failed to insert row: {row.to_dict()} | Error: {row_error}")
        
        conn.commit()
        custom_border_message(f"[INFO] Successfully inserted {inserted_count} new rows into PostgreSQL!")
        
        # Save cleaned, readable version (without Price_num) for CSV
        cleaned_display_df = df.drop(columns=['Price_num'], errors='ignore')
        cleaned_display_df.to_csv("../data/cleaned_data.csv", index=False)
        custom_border_message("[INFO] Saved readable cleaned data to 'cleaned_data.csv'")
        # Print readable DataFrame to Terminal
        custom_border_message(cleaned_display_df.to_string(index=False))

        return True
    
    except Exception as e:
        custom_border_message(f"[ERROR] Failed to load data into PostgreSQL: {e}")
        return False
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Access via localhost:8080