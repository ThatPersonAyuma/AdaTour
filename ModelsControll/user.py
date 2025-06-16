from .DbContext import get_connection

class User:
    def __init__(self, id_user=None, id_role=None, username=None, jenis_role=None, password=None, nama_lengkap=None, kontak=None, alamat=None, nik=None):
        self.id_user = id_user
        self.id_role = id_role
        self.jenis_role = jenis_role
        self.username = username
        self.password = password
        self.nama_lengkap = nama_lengkap
        self.kontak = kontak
        self.alamat = alamat
        self.nik = nik

    @staticmethod
    def create(id_role, username, password, nama_lengkap, kontak, alamat):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (id_role, username, password, nama_lengkap, kontak, alamat)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (id_role, username, password, nama_lengkap, kontak, alamat))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    User(
                        id_user = row[index["id_user"]],
                        id_role = row[index["id_role"]],
                        username = row[index["username"]],
                        password = row[index["password"]],
                        nama_lengkap = row[index["nama_lengkap"]],
                        kontak = row[index["kontak"]],
                        alamat = row[index["alamat"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_user, id_role, username, password, nama_lengkap, kontak, alamat):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE users
                    SET id_role=%s, username=%s, password=%s, nama_lengkap=%s, kontak=%s, alamat=%s
                    WHERE id_user = %s
                """, (id_role, username, password, nama_lengkap, kontak, alamat, id_user))
                conn.commit()

    @staticmethod
    def delete(id_user):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id_user = %s", (id_user,))
                conn.commit()
                
    @staticmethod
    def user_auth(username: str, password: str) -> list:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM users u
                                JOIN roles r ON r.id_role = u.id_role
                                WHERE username = %s
                                    AND \"password\" = %s""", (username, password))
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                if len(rows) > 1:
                    raise "Two or more User must not have same name and same password"
                
                return [
                    User(
                        id_role = row[index["id_role"]],
                        username = row[index["username"]],
                        jenis_role = row[index["jenis_role"]],
                        password = row[index["password"]],
                        nama_lengkap = row[index["nama_lengkap"]],
                        kontak = row[index["kontak"]],
                        alamat = row[index["alamat"]]
                    )
                    for row in rows
                ]
                
    @staticmethod
    def IsUserExist(username: str) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM users
                                WHERE username = \'{username}\'""")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}
                return False if len(rows) == 0 else True