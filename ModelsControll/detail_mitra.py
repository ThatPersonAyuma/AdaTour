from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class DetailMitra:
    def __init__(self,*,id_jadwal: int, id_mitra: str):
        self.ID_Jadwal: int = id_jadwal
        self.ID_Mitra: str = id_mitra
# END REGION OF Entity CLASS

# CREATE
def create_detail_mitra(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_detail_mitra():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_detail_mitra(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_detail_mitra(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF DETAIL MITRA DATA IN FORM OF DetailMitra Class
def get_all_detail_mitra() -> list[DetailMitra]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            DetailMitras: list[DetailMitra] = []
            for row in rows:
                DetailMitras.append(
                    DetailMitra(
                        id_jadwal=row[index["id_jadwal"]],
                        id_mitra=row[index["id_mitra"]]
                    )
                )
            return DetailMitras