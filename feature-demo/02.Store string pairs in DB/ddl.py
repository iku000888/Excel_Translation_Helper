import sqlite3
conn = sqlite3.connect('trans_memory.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE trans_mem
             (en text unique,jp text unique)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()



