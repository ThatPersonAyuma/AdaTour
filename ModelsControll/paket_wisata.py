from .DbContext import get_connection
from . import (transportasi, akomodasi, destinasi)

class AkomodasiOfPaket:
    def __init__(self, id_paket, nama_paket, id_akomodasi=None, nama=None, bintang=None, tipe=None, kapasitas=None, alamat=None, kota=None, kontak=None, email=None, password=None):
        self.id_paket = id_paket,
        self.nama_paket = nama_paket,
        self.id_akomodasi = id_akomodasi
        self.nama = nama
        self.tipe = tipe
        self.bintang = bintang
        self.alamat = alamat
        self.kota = kota
        self.kontak = kontak
        self.email = email
        
class TransportasiOfPaket:
    # pw.id_paket,
    # pw.nama AS nama_paket,
    # tr.id_transportasi,
    # tr.nama AS nama_transportasi,
    # tr.jenis,
    # tr.kapasitas,
    # dpt.deskripsi_perjalanan
    def __init__(self, id_paket,nama_paket,id_transportasi,nama_transportasi,jenis,kapasitas,deskripsi_perjalanan):
        self.id_paket = id_paket,
        self.nama_paket = nama_paket,
        self.id_transportasi = id_transportasi,
        self.nama_transportasi = nama_transportasi,
        self.jenis = jenis,
        self.kapasitas = kapasitas,
        self.deskripsi_perjalanan = deskripsi_perjalanan
        
class DestinasiOfPaket:
    def __init__(self, id_paket, nama_paket ,id_destinasi, nama_destinasi, lokasi, deskripsi):
        self.id_paket = id_paket,
        self.nama_paket = nama_paket,
        self.id_destinasi = id_destinasi,
        self.nama_destinasi = nama_destinasi,
        self.lokasi = lokasi,
        self.deskripsi = deskripsi

class PaketWisata:
    def __init__(self, id_paket=None, nama=None, deskripsi=None, durasi_hari=None):
        self.id_paket = id_paket
        self.nama = nama
        self.deskripsi = deskripsi
        self.durasi_hari = durasi_hari

    @staticmethod
    def create(nama, deskripsi, durasi_hari):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO paket_wisata (nama, deskripsi, durasi_hari)
                    VALUES (%s, %s, %s)
                """, (nama, deskripsi, durasi_hari))
                conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM paket_wisata")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    PaketWisata(
                        id_paket = row[index["id_paket"]], 
                        nama = row[index["nama"]], 
                        deskripsi = row[index["deskripsi"]], 
                        durasi_hari = row[index["durasi_hari"]]
                    )
                    for row in rows
                ]

    @staticmethod
    def update(id_paket, nama, deskripsi, durasi_hari):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE paket_wisata
                    SET nama=%s, deskripsi=%s, durasi_hari=%s
                    WHERE id_paket = %s
                """, (nama, deskripsi, durasi_hari, id_paket))
                conn.commit()

    @staticmethod
    def delete(id_paket):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM paket_wisata WHERE id_paket = %s", (id_paket,))
                conn.commit()

def get_akomodasi_paket():
    with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT 
                            pw.id_paket,
                            pw.nama AS nama_paket,
                            ak.id_akomodasi,
                            ak.nama AS nama_akomodasi,
                            ak.kontak,
                            ak.email,
                            ak.bintang,
                            ak.alamat,
                            ak.tipe,
                            ak.kota,
                            dpa.deskripsi_penginapan
                            FROM paket_wisata pw
                            JOIN detail_paket_akomodasi dpa 
                                ON pw.id_paket = dpa.paket_wisata_id_paket
                            JOIN akomodasi ak 
                                ON dpa.id_akomodasi = ak.id_akomodasi;""")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    AkomodasiOfPaket(
                        id_paket = row[index["id_paket"]],
                        nama_paket = row[index["nama_paket"]],
                        id_akomodasi = row[index["id_akomodasi"]],
                        nama = row[index["nama_akomodasi"]],
                        tipe = row[index["tipe"]],
                        bintang = row[index["bintang"]],
                        alamat = row[index["alamat"]],
                        kota = row[index["kota"]],
                        kontak = row[index["kontak"]],
                        email = row[index["email"]],
                        password = row[index["password"]]
                    )
                    for row in rows
                ]
                
def get_transport_paket():
    with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT 
                                    pw.id_paket,
                                    pw.nama AS nama_paket,
                                    tr.id_transportasi,
                                    tr.nama AS nama_transportasi,
                                    tr.jenis,
                                    tr.kapasitas,
                                    dpt.deskripsi_perjalanan
                                FROM paket_wisata pw
                                JOIN detail_paket_transportasi dpt 
                                    ON pw.id_paket = dpt.paket_wisata_id_paket
                                JOIN transportasi tr 
                                    ON dpt.id_transportasi = tr.id_transportasi;""")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    TransportasiOfPaket(
                        id_paket = row[index["id_paket"]],
                        nama_paket = row[index["nama_paket"]],
                        id_transportasi = row[index["id_transportasi"]],
                        nama_transportasi = row[index["nama_transportasi"]],
                        jenis = row[index["jenis"]],
                        kapasitas = row[index["kapasitas"]],
                        deskripsi_perjalanan = row[index["deskripsi_perjalanan"]]
                    )
                    for row in rows
                ]
                
def get_destination_paket():
    with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT 
                                    pw.id_paket,
                                    pw.nama AS nama_paket,
                                    ds.id_destinasi,
                                    ds.nama AS nama_destinasi,
                                    ds.lokasi,
                                    ds.deskripsi
                                FROM paket_wisata pw
                                JOIN detail_paket_destinasi dpd 
                                    ON pw.id_paket = dpd.paket_wisata_id_paket
                                JOIN destinasi ds 
                                    ON dpd.destinasi_id_destinasi = ds.id_destinasi;""")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    DestinasiOfPaket(
                        id_paket = row[index["id_paket"]],
                        nama_paket = row[index["nama_paket"]],
                        id_destinasi = row[index["id_destinasi"]],
                        nama_destinasi = row[index["nama_destinasi"]],
                        lokasi = row[index["lokasi"]],
                        deskripsi = row[index["deskripsi"]]
                    )
                    for row in rows
                ]

def GetAllMitra():
    with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT 
                    pw.id_paket,
                    pw.nama AS nama_paket,
                    pw.deskripsi,
                    pw.durasi_hari,

                    -- AKOMODASI
                    ak.nama AS nama_akomodasi,
                    
                    -- TRANSPORTASI
                    tr.nama AS nama_transportasi,
                    
                    -- DESTINASI
                    ds.lokasi AS lokasi_destinasi

                    FROM paket_wisata pw

                    -- JOIN AKOMODASI
                    LEFT JOIN detail_paket_akomodasi dpa 
                        ON pw.id_paket = dpa.paket_wisata_id_paket
                    LEFT JOIN akomodasi ak 
                        ON dpa.id_akomodasi = ak.id_akomodasi

                    -- JOIN TRANSPORTASI
                    LEFT JOIN detail_paket_transportasi dpt 
                        ON pw.id_paket = dpt.paket_wisata_id_paket
                    LEFT JOIN transportasi tr 
                        ON dpt.id_transportasi = tr.id_transportasi

                    -- JOIN DESTINASI
                    LEFT JOIN detail_paket_destinasi dpd 
                        ON pw.id_paket = dpd.paket_wisata_id_paket
                    LEFT JOIN destinasi ds 
                        ON dpd.destinasi_id_destinasi = ds.id_destinasi;""")
                rows = cur.fetchall()
                columns = [col.name for col in cur.description]
                index = {name: idx for idx, name in enumerate(columns)}

                return [
                    PaketWisata(
                        id_paket = row[index["id_paket"]], 
                        nama = row[index["nama"]], 
                        deskripsi = row[index["deskripsi"]], 
                        durasi_hari = row[index["durasi_hari"]]
                    )
                    for row in rows
                ]