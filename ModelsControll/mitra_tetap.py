from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class MitraTetap:
    def __init__(self,*,id_mitra: str, id_paket: int):
        self.ID_Mitra: str = id_mitra
        self.ID_Paket: int = id_paket
# END REGION OF Entity CLASS 

# CREATE
def create_mitra_tetap(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_mitra_tetap():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_mitra_tetap(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_mitra_tetap(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# READ ALL MITRATETAP AS A CLASS
def get_all_mitraTetap() -> list[MitraTetap]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            mitraTetaps: list[MitraTetap] = []
            for row in rows:
                mitraTetaps.append(
                    MitraTetap(
                        id_mitra=row[index["id_mitra"]],
                        id_paket=row[index["id_paket"]]
                    )
                )
            return mitraTetaps