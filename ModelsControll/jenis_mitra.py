from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class JenisMitra:
    def __init__(self,*,id_jenis_mitra: int, nama_jenis: str):
        self.ID_Jenis_Mitra: int = id_jenis_mitra
        self.Nama_Jenis: str = nama_jenis
# END REGION OF Entity CLASS

# CREATE
def create_jenis_mitra(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_jenis_mitra():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_jenis_mitra(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_jenis_mitra(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF JENIS MITRA DATA IN FORM OF JENIS MITRA Class
def get_all_jenis_mitra() -> list[JenisMitra]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            JenisMitras: list[JenisMitra] = []
            for row in rows:
                JenisMitras.append(
                    JenisMitra(
                        id_jenis_mitra=row[index["id_jenis_mitra"]],
                        nama_jenis=row[index["nama_jenis"]]
                    )
                )
            return JenisMitras