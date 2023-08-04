import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(database = "murat",
                        user = "murat",
                        password = "murat",
                        host = "localhost",
                        port = "5432")

# Set autocommit mode
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Get a cursor object
cursorObject = conn.cursor()

# Execute your command
cursorObject.execute("CREATE DATABASE crmdb")

# Close the connection
conn.close()

print("All done!")