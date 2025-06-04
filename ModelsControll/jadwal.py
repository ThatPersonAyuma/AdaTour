from . import DbContext
import psycopg2
from datetime import datetime

# START REGION OF ENTITY CLASS
class Jadwal:
    def __init__(self,*,id_jadwal: int, tgl_pelaksanaan: datetime, pemesanan: bool,
                keberangkatan: bool, id_paket: , id_tg: , 
                total_harga: int, reschedule: int = None):
        self.ID_Jadwal: int= id_jadwal
        self.Tgl_Pelaksanaan: datetime = tgl_pelaksanaan
        self.Pemesanan: bool= pemesanan
        self.Keberangkatan: bool=keberangkatan
        self.ID_Paket: = id_paket
        self.ID_TourGuide: = id_tg
        self.Reschedule: int|None = reschedule
        self.Total_Harga: int= total_harga
    def SaveSelf(self):
        update_Jadwal(
            
        )
# END REGION OF Entity CLASS 

# CREATE
def create_jadwal(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_jadwal():
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# UPDATE
def update_jadwal(id_jadwal, tgl_pelaksanaan, pemesanan,
                keberangkatan, id_paket, id_tg,
                reschedule, total_harga):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                        UPDATE users SET name = {id_jadwal}, email = %s WHERE id = %s
                        """)
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_jadwal(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")

# GET ALL OF JADWAL DATA IN FORM OF JENIS Jadwal Class
def get_all_jadwal() -> list[Jadwal]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            Jadwals: list[Jadwal] = []
            for row in rows:
                Jadwals.append(
                    Jadwal(
                        
                    )
                )
            return Jadwals