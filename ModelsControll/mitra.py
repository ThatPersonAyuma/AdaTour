from . import DbContext
import psycopg2

# Models
class Mitra:
    def __init__(self, *, id, nama, kontak, alamat, id_jenis, password):
        self.ID_Mitra: str = id
        self.Nama_Mitra: str = nama
        self.Kontak_Mitra: str = kontak
        self.Alamat_Mitra: str = alamat
        self.ID_Jenis_Mitra: str = id_jenis
        self.Password: str = password
    def SaveSelf(self):
        update_tour_guide(
            id_mitra=self.ID_Mitra,
            nama=self.Nama_Mitra,
            kontak=self.Kontak_Mitra,
            alamat=self.Alamat_Mitra,
            id_jenis_mitra=self.ID_Jenis_Mitra,
            password=self.Password
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
def update_tour_guide(*, id_mitra: str, nama: str, kontak: str, alamat: str, id_jenis_mitra: str, password: str):
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
def read_all_mitra() -> list[Mitra]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM mitra")
            rows = cur.fetchall()
            cur_desc = cur.description
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            mitras: list[Mitra] = []
            for row in rows:
                mitras.append(
                    Mitra(
                        id=row[index["id_mitra"]],
                        nama=row[index["nama_mitra"]],
                        kontak=row[index["kontak_mitra"]],
                        alamat=row[index["alamat_mitra"]],
                        id_jenis=row[index["id_jenis_mitra"]],
                        password=row[index["password"]]
                    )
                )
            return mitras