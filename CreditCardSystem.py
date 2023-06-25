import mysql.connector

def display_transactions_by_zip(zip_code, month, year):
    # Establish a connection to the MySQL database
    # connection = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="password",
    #     database="creditcard_capstone"
    # )

    conn = mysql.connector.connect(user='root', database='creditcard_capstone',
                               password='password',
                               host="localhost",
                               port=3306)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # SQL query to retrieve the transactions made by customers in a given zip code for a given month and year
    query = """
    SELECT *
    FROM creditcard
    WHERE LEFT(customer.CUST_ZIP, 5) = %s AND MONTH(Date) = %s AND YEAR(Date) = %s
    ORDER BY DAY(Date) DESC
    """

    # Execute the query with the provided parameters
    cursor.execute(query, (zip_code, month, year))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the transactions
    print("Transactions by Zip Code and Dates:")
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    conn.close()



def display_transactions_by_type(transaction_type):
    # Establish a connection to the MySQL database

    

    conn = mysql.connector.connect(user='root', database='creditcard_capstone',
                               password='password',
                               host="localhost",
                               port=3306)
    breakpoint()
    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    print("I am in transactions_type.")
    # SQL query to retrieve the number and total values of transactions for a given type
    query = """
    SELECT COUNT(*) AS transaction_count, SUM(Transaction_Value) AS total_value
    FROM creditcard
    WHERE TRANSACTION_TYPE = %s
    """

    # Execute the query with the provided parameter
    cursor.execute(query, (transaction_type,))

    # Fetch the result
    result = cursor.fetchone()

    # Display the transaction details
    print("Transaction Type:", transaction_type)
    print("Transaction Count:", result[0])
    print("Total Value:", result[1])

    # Close the cursor and the database connection
    cursor.close()
    conn.close()


def display_transactions_by_state(state):
    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(user='root', database='creditcard_capstone',
                               password='password',
                               host="localhost",
                               port=3306)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # SQL query to retrieve the total number and total values of transactions for branches in a given state
    query = """
    SELECT COUNT(*) AS transaction_count, SUM(Transaction_Value) AS total_value
    FROM creditcard
    JOIN branch ON creditcard.BRANCH_CODE = branch.BRANCH_CODE
    WHERE branch.BRANCH_STATE = %s
    """

    # Execute the query with the provided parameter
    cursor.execute(query, (state,))

    # Fetch the result
    result = cursor.fetchone()

    # Display the transaction details
    print("State:", state)
    print("Transaction Count:", result[0])
    print("Total Value:", result[1])

    # Close the cursor and the database connection
    cursor.close()
    conn.close()





# Main program
def main():
    while True:
        print("Transaction Details Module")
        print("1) Display transactions by zip code for a given month and year")
        print("2) Display number and total values of transactions for a given type")
        print("3) Display total number and total values of transactions for branches in a given state")
        print("4) Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            zip_code = input("Enter the zip code(Ex:12345): ")
            month = input("Enter the month(For January, enter 1): ")
            year = input("Enter the year(Ex:2018): ")
            display_transactions_by_zip(zip_code, month, year)
        elif choice == "2":
            transaction_type = input("Enter the transaction type(Ex:Gas): ")
            display_transactions_by_type(transaction_type)
        elif choice == "3":
            state = input("Enter the state(Ex:NY): ")
            display_transactions_by_state(state)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("did we the main here?")
    
if __name__ == "__main__":
    main() 