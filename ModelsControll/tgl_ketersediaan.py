from . import DbContext
import psycopg2
from datetime import date

# START REGION OF ENTITY CLASS
class Tgl_Ketersediaan:
    def __init__(self,*,id_tanggal: int, tanggal: date):
        self.ID_Tgl_Ketersediaan: int = id_tanggal
        self.Tanggal: date = tanggal
# END REGION OF Entity CLASS

# CREATE
def create_tour_guide(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_tour_guide():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_tour_guide(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_tour_guide(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF TANGGAL KETERSEDIAAN DATA IN FORM OF Tgl_Ketersediaan Class
def get_all_tgl_ketersediaan() -> list[Tgl_Ketersediaan]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            Tgl_Ketersediaans: list[Tgl_Ketersediaan] = []
            for row in rows:
                Tgl_Ketersediaans.append(
                    Tgl_Ketersediaan(
                        id_tanggal=row[index["id_tanggal"]],
                        tanggal=row[index["tanggal"]]
                    )
                )
            return Tgl_Ketersediaans