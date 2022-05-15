import os
import psycopg2

conn = psycopg2.connect(
    user=os.environ['DB_USER'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    database=os.environ['DB_NAME'],
    password=os.environ['DB_PASSWORD']
)

def is_available(spot_id, dist):
    if spot_id != 1:
        raise Exception(f'Spot {spot_id} does not exist')

    if dist < 80 and dist > 10:
        return False
    else:
        return True


def frontend(*args):
    spot_id = 1  # hard-coded for now
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT dist FROM parking_view WHERE spot_id = %s',
            (spot_id,)
        )
        dist = cursor.fetchone()[0]
    
    available = is_available(spot_id, dist)
    if available:
        msg = 'Spot is currently available!'
    else:
        msg = 'Spot is currently taken.'
    
    return msg, 200