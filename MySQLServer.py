import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection, creation, and proper cleanup.
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database with IF NOT EXISTS to avoid errors if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Commit the transaction
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close cursor and connection properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

def main():
    """Main function to execute the database creation."""
    create_database()

if __name__ == "__main__":
    main()