import json
import psycopg2
# Start Region of CONSTANT DATA
CONNECTION_STRING: str
try:
    with open('appsettings.json', 'r') as f:
        config = json.load(f)
        CONNECTION_STRING = config["ConnectionStrings"]["DefaultConnection"]
except:
    raise "Check appsettings.json"
# End Region of CONSTANT DATA

def get_connection():
    return psycopg2.connect(CONNECTION_STRING)

def CreateUserTable():
    with psycopg2.connect(CONNECTION_STRING) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS wisatawan (
                        id SERIAL PRIMARY KEY,
                        nama_wisatawan VARCHAR(100) NOT NULL,
                        kontak_wisatawan VARCHAR(20) NOT NULL,
                        alamat_wisatawan VARCHAR(100) NULL,
                        nik_visa VARCHAR(4000) UNIQUE NOT NULL,
                        username VARCHAR(4000) UNIQUE NULL,
                        password VARCHAR(20) NOT NULL
                        )
                    """
                    )
                conn.commit()