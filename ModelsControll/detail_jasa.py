from . import DbContext
import psycopg2

# START REGION OF ENTITY CLASS
class DetailJasa:
    def __init__(self,*,id_detail_jasa: int, satuan: str,
                kapasitas: int, harga: int, id_mitra: str):
        self.ID_Detail_Jasa: int = id_detail_jasa
        self.Satuan: str = satuan
        self.Kapasitas: int = kapasitas
        self.Harga: int = harga
        self.ID_Mitra: str = id_mitra
# END REGION OF Entity CLASS

# CREATE
def create_detail_jasa(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_detail_jasa():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_detail_jasa(user_id, name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_detail_jasa(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")
            
# GET ALL OF DETAIL JASA DATA IN FORM OF DetailJasa Class
def get_all_detail_jasa() -> list[DetailJasa]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            DetailJasas: list[DetailJasa] = []
            for row in rows:
                DetailJasas.append(
                    DetailJasa(
                        id_detail_jasa=row[index["id_detail_jadwal"]],
                        satuan=row[index["satuan"]],
                        kapasitas=row[index["kapasitas"]],
                        harga=row[index["harga"]],
                        id_mitra=row[index["id_mitra"]]
                    )
                )
            return DetailJasas