from . import DbContext
import psycopg2

class Tour_Guide:
    Id_TG:str
    Nama_TG: str
    Kontak_TG: str
    Alamat_TG: str
    Nik: str
    Password: str
    def SaveSelf(self):
        update_tour_guide(
            id=self.Id_TG,
            name=self.Nama_TG,
            kontak=self.Kontak_TG,
            alamat=self.Alamat_TG,
            nik=self.Nik,
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
def update_tour_guide(*, id: str, name: str, kontak: str, alamat: str, nik: str, password: str):
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