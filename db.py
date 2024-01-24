import sqlite3

def createDB():

    try:
        conn = sqlite3.connect('math.db')   # :memory: for debugging

        c = conn.cursor()

        # Creates credentials table

        c.execute("""CREATE TABLE credentials (
                cID INTEGER,
                user TEXT,
                passwd TEXT
                )""")

        conn.commit()

        conn.close()

    except sqlite3.OperationalError as err:
        print("An error occurred while creating the database: ", err)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    
if __name__ == "__main__":
    createDB()