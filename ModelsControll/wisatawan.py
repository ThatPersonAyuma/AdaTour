from . import DbContext
import psycopg2


# #Connect to an existing database
# conn = psycopg2.connect(lib.CONNECTION_STRING)

# # Open a cursor to perform database operations
# cur = conn.cursor()
    # Koneksi ke database
    # conn = psycopg2.connect(
    #     lib.CONNECTION_STRING
    # )
    # cur = conn.cursor()
class Wisatawan:
    def __init__(self, *, id: int, nama: str, kontak: str, nik_visa: str, username: str, password: str, alamat: str|None=None):
        self.Id_Wisatawan: int = id
        self.Nama_Wisatawan: str = nama
        self.Kontak_Wisatawan: str = kontak
        self.Alamat: str = alamat
        self.Nik_Visa: str = nik_visa
        self.Username: str = username
        self.Password: str = password
        
    def SaveSelf(self):
        update_wisatawan(
            user_id=self.Id_Wisatawan,
            name=self.Nama_Wisatawan,
            kontak=self.Kontak_Wisatawan,
            Nik_Visa=self.Nik_Visa,
            username=self.Username,
            password=self.Password,
            alamat=self.Alamat
        )

# CREATE
def create_wisatawan(name, email):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            print("User ditambahkan.")

# READ
def read_all_wisatawan() -> list[tuple[any]]:
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM wisatawan")
            rows = cur.fetchall()
            cur_desc = cur.description
            print(cur_desc[0].name)
            index = {cur_desc[i].name: i for i in range(len(cur_desc))}
            print(index)
            wisatawans: list[Wisatawan] = []
            for row in rows:
                wisatawans.append(
                    Wisatawan(
                        id=row[index["id"]],
                        nama=row[index["nama_wisatawan"]],
                        kontak=row[index["kontak_wisatawan"]],
                        nik_visa=row[index["nik_visa"]],
                        username=row[index["username"]],
                        password=row[index["password"]],
                        alamat=row[index["alamat_wisatawan"]]
                    )
                )
            print(wisatawans[0].Nama_Wisatawan)
            return wisatawans
            
def read_wisatawan_by_name(username: str):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE name==%s", username)
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print(row)
            return cur.fetchall()

# UPDATE
def update_wisatawan(*, user_id: int, name: str, kontak: str, Nik_Visa: str, username: str, password: str, alamat: str|None=None):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            conn.commit()
            print("User diperbarui.")

# DELETE
def delete_wisatawan(user_id):
    with psycopg2.connect(DbContext.CONNECTION_STRING) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            print("User dihapus.")

    # # Contoh penggunaan
    # create_user("Andi", "andi@example.com")
    # read_users()
    # update_user(1, "Andi Updated", "andi.updated@example.com")
    # delete_user(1)

    # # Tutup koneksi
    # cur.close()
    # conn.close()

