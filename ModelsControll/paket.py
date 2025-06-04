from . import DbContext
import psycopg2

class Paket:
    def __init__(self, *, id: int, nama: str, deskripsi: str, harga: int):
        self.ID_Paket: int = id
        self.Nama_Paket: str = nama
        self.Deskripsi_Paket: str = deskripsi
        self.Harga: int = harga
        
    def SaveSelf(self):
        update_tour_guide(
            id=self.ID_Paket,
            nama=self.Nama_Paket,
            deskripsi=self.Deskripsi_Paket,
            harga=self.Harga
        )

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
def update_tour_guide(*, id: int, nama: str, deskripsi: str, harga: int):
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
            
# GET ALL OF PAKET WISATA DATA IN FORM OF Paket Class
def read_all_paket() -> list[Paket]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paket")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            pakets: list[Paket] = []
            for row in rows:
                pakets.append(
                    Paket(
                        id=row[index["id_paket"]],
                        nama=row[index["nama_paket"]],
                        deskripsi=row[index["deskripsi_paket"]],
                        harga=row[index["harga"]]
                    )
                )
            return pakets
