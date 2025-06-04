from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class MitraKetersediaan:
    def __init__(self,*,id_tanggal: int, id_mitra: str):
        self.ID_Tgl_Ketersediaan: int = id_tanggal
        self.Id_Mitra: str = id_mitra
# END REGION OF Entity CLASS

# CREATE
def create_mitra_ketersediaan(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_mitra_ketersediaan():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_mitra_ketersediaan(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_mitra_ketersediaan(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# READ ALL KETERSEDIAAN MITRA AS A CLASS
def get_all_mitra_ketersediaan() -> list[MitraKetersediaan]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            MitraKetersediaans: list[MitraKetersediaan] = []
            for row in rows:
                MitraKetersediaans.append(
                    MitraKetersediaan(
                        id_tanggal=row[index["id_tanggal"]],
                        id_mitra=row[index["id_mitra"]]
                    )
                )
            return MitraKetersediaans