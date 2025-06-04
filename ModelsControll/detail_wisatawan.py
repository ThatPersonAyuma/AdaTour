from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class DetailWisatawan:
    def __init__(self,*,id_jadwal: int, id_wisatawan: int):
        self.ID_Jadwal: int = id_jadwal
        self.ID_Wisatawan: int = id_wisatawan
# END REGION OF Entity CLASS

# CREATE
def create_detail_wisatawan(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_detail_wisatawan():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_detail_wisatawan(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_detail_wisatawan(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF DETAIL WISATAWAN DATA IN FORM OF DetailWisatawan Class
def get_all_detail_wisatawan() -> list[DetailWisatawan]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            DetailWisatawans: list[DetailWisatawan] = []
            for row in rows:
                DetailWisatawans.append(
                    DetailWisatawan(
                        id_jadwal=row[index["id_jadwal"]],
                        id_wisatawan=row[index["id_wisatawan"]]
                    )
                )
            return DetailWisatawans