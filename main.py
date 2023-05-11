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

#Note: USED CASCADE ON DELETE AND ON UPDATE ON STOCK TABLE WHILE CREATING

try:
    #Transaction 2: delete depot d2 from Depot and Stock Using Cascade
    cur.execute("BEGIN")
    cur.execute("DELETE FROM Depot WHERE depid = %s", ('d2',))
    cur.execute("COMMIT")
    print("Transaction 2 completed successfully.")

except Exception as e:
    # Roll back the transaction if any error occurs
    cur.execute("ROLLBACK")
    print("Transaction 2 failed Rolling Back. Error message:", e)

try:
    # Transaction 4: change depot d1 name to dd1 in Depot and Stock
    cur.execute("BEGIN")
    cur.execute("UPDATE Depot SET depid = %s WHERE depid = %s ", ('d1', 'dd1'))
    cur.execute("COMMIT")
    print("Transaction 4 completed successfully.")

except Exception as e:
    # Roll back the transaction if any error occurs
    cur.execute("ROLLBACK")
    print("Transaction 4  failed Rolling Back. Error message:", e)

try:
    #Transaction 6: add depot (d100, Chicago, 100) to Depot and (p1, d100, 100) to Stock
    cur.execute("BEGIN")
    cur.execute("INSERT INTO Depot(depid, addr, volume) VALUES (%s, %s, %s)", ('d100', 'Chicago', 100))
    cur.execute("INSERT INTO Stock(prodid, depid, quantity) VALUES (%s, %s, %s)", ('p1', 'd100', 100))
    cur.execute("COMMIT")
    print("Transaction 6 completed successfully.")

except Exception as e:
    # Roll back the transaction if any error occurs
    cur.execute("ROLLBACK")
    print("Transaction 6 failed Rolling Back. Error message:", e)

finally:
    # Close the cursor and database connection
    cur.close()
    conn.close()
