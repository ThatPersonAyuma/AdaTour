from .DbContext import get_connection

class Role:
    def __init__(self, id_role=None, jenis_role=None):
        self.id_role = id_role
        self.jenis_role = jenis_role

    @staticmethod
    def create(jenis_role):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO roles (jenis_role) VALUES (%s)
                """, (jenis_role,))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM roles")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    Role(
                        id_role = row[index["id_role"]],
                        jenis_role = row[index["jenis_role"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_role, jenis_role):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE roles SET jenis_role=%s WHERE id_role=%s
                """, (jenis_role, id_role))
                conn.commit()

    @staticmethod
    def delete(id_role):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM roles WHERE id_role = %s", (id_role,))
                conn.commit()

def get_role_id(role_name: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""SELECT * FROM roles
                            WHERE jenis_role = \'{role_name}\'""")
            rows = cur.fetchall()
            columns = [col.name for col in cur.description]
            index = {name: idx for idx, name in enumerate(columns)}

            return [
                Role(
                    id_role = row[index["id_role"]],
                    jenis_role = row[index["jenis_role"]]
                )
                for row in rows
            ][0]