import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="prass", 
    user="postgres", 
    password="Addha17" 
)

# Open a cursor to perform database operations
cur = conn.cursor()



try:
    #Transaction 2: delete depot d1 from Depot and Stock
    cur.execute("BEGIN")
    cur.execute("DELETE FROM Stock WHERE depid = 'd1';")
    print("d1 Deleted From Stock")
    cur.execute("DELETE FROM Depot WHERE depid = 'd1';")
    print("d1 Deleted From Depot")
    conn.commit()
    print("Transaction 2 completed successfully.")

except psycopg2.Error as e:
    # Rollback in case of errors
    print("Error occurred during transaction2. Rolling back changes.")
    print(e)
    conn.rollback()

try:
    # Transaction 4: change depot d1 name to dd1 in Depot and Stock
    cur.execute("BEGIN")
    cur.execute("UPDATE Depot SET depid = 'dd1' WHERE depid = 'd1';")
    print("print d1 changed to dd1 in depot")
    cur.execute("UPDATE Stock SET depid = 'dd1' WHERE depid = 'd1';")
    print("print d1 changed to dd1 in stock")
    conn.commit()
    print("Transaction 4 completed successfully.")
except psycopg2.Error as e:
    # Rollback in case of errors
    print("Error occurred during transaction4. Rolling back changes.")
    print(e)
    conn.rollback()

try:
    #Transaction 6: add depot (d100, Chicago, 100) to Depot and (p1, d100, 100) to Stock
    cur.execute("BEGIN")
    cur.execute("INSERT INTO Depot (depid, addr, volume) VALUES ('d100', 'Chicago', 100);")
    print("Row Added to Depot")
    cur.execute("INSERT INTO Stock (prodid, depid, quantity) VALUES ('p1', 'd100', 100);")
    print("Row Inserted to stock")
    print("Transaction 6 completed successfully.")

    # Commit the changes to the database
    conn.commit()

except psycopg2.Error as e:
    # Rollback in case of errors
    print("Error occurred during transaction6. Rolling back changes.")
    print(e)
    conn.rollback()

finally:
    # Close the cursor and database connection
    cur.close()
    conn.close()
