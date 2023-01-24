from entities.location import Location
from repositories.pg_repository import get_connection

conn = get_connection()

def deserialize(row):
    location = Location(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9]
    )
    return location

def get_address_by_zip_code(zip_code):
    cur = conn.cursor()
    cur.execute("SELECT * FROM locations WHERE cep = %s", (zip_code,))
    row = cur.fetchone()
    location = deserialize(row)
    return location

def get_address_by_uf(uf):
    cur = conn.cursor()
    cur.execute("SELECT * FROM locations WHERE uf = %s", (uf,))
    rows = cur.fetchall()
    locations = []
    for row in rows:
        location = deserialize(row)
        locations.append(location)
    return locations

def check_if_address_exists(zip_code):
    cur = conn.cursor()
    cur.execute("SELECT * FROM locations WHERE cep = %s", (zip_code,))
    row = cur.fetchone()
    if row:
        return True
    return False

def save_address(location):
    cur = conn.cursor()
    cur.execute("INSERT INTO locations VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (location.cep, location.logradouro, location.complemento, location.bairro, location.localidade,
                 location.uf, location.ibge, location.gia, location.ddd, location.siafi))
    conn.commit()
    cur.close()

def get_all_locations():
    cur = conn.cursor()
    cur.execute("SELECT * FROM locations")
    rows = cur.fetchall()
    locations = []
    for row in rows:
        location = deserialize(row)
        locations.append(location)
    return locations
