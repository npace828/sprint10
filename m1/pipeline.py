import psycopg2
import queries as q
from sqlite_example import connect_to_db, execute_q
from queries import GET_CHARACTERS


DBNAME = 'vzgjasfg'
USER = 'vzgjasfg'
PASSWORD = 'Np0VIMYWBq_QKrNvWX2taFkPQonRAYeW'
HOST = 'stampy.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER, 
                           password=PASSWORD, 
                           host=HOST)
pg_curs = pg_conn.cursor()

if __name__ == '__main__':
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    print(sl_characters[:5])
   
# Server	stampy.db.elephantsql.com (stampy-01)
# Region	amazon-web-services::us-east-1
# Created at	2023-07-21 18:33 UTC+00:00
# User & Default database	vzgjasfg
# Password	***  
# URL	postgres://vzgjasfg:***@stampy.db.elephantsql.com/vzgjasfg  
# Current database size	
# Max database size