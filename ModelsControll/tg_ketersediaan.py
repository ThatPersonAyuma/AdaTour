from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class TG_Ketersediaan:
    def __init__(self,*,id_tour_guide: str, id_tanggal: int):
        self.ID_Tour_Guide: str = id_tanggal
        self.ID_Tgl_Ketersediaan: int = id_tanggal
# END REGION OF Entity CLASS

# CREATE
def create_tg_ketersediaan(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_tg_ketersediaan():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_tg_ketersediaan(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_tg_ketersediaan(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF KETERSEDIAAN TOUR GUIDE DATA IN FORM OF Tgl_Ketersediaan Class
def get_all_tg_ketersediaan() -> list[TG_Ketersediaan]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            TG_Ketersediaans: list[TG_Ketersediaan] = []
            for row in rows:
                TG_Ketersediaans.append(
                    TG_Ketersediaan(
                        id_tanggal=row[index["id_tanggal"]],
                        tanggal=row[index["tanggal"]]
                    )
                )
            return TG_Ketersediaans