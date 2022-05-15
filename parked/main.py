import os
import psycopg2

conn = psycopg2.connect(
    user=os.environ['DB_USER'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    database=os.environ['DB_NAME'],
    password=os.environ['DB_PASSWORD']
)

def parked(request):
    spot_id = int(request.args.get('spot_id'))
    dist = int(request.args.get('dist'))
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO parking (spot_id, dist) VALUES (%s, %s)',
            (spot_id, dist)
        )
        cursor.execute(
            '''
            INSERT INTO parking_view (spot_id, dist) VALUES (%s, %s)
                ON CONFLICT (spot_id) DO UPDATE
                    SET dist = EXCLUDED.dist
            ''',
            (spot_id, dist)
        )
        conn.commit()

    return 'DB write successful', 200
