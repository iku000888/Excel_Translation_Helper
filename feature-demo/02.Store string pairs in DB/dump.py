import sqlite3
conn = sqlite3.connect('trans_memory.db')

c = conn.cursor()

# Create table
for row in c.execute('SELECT * FROM trans_mem'):
        #print unicode(row).encode('utf8')
        print repr(row)
