users = []  # list that contains all the users no matter what type they are.
runways = []    # lists that contains all the airport's runways.
gates = []

# ---------------------------------------------------------
class User:
    def __init__(self):
        self.iden = 0
        self.name = ""
        self.age = 0
        self.email = ""
        self.password = ""
        self.type = 0

    def set_id(self, ide):
        self.iden = ide

    def set_name(self, n):
        self.name = n

    def set_age(self, a):
        self.age = a

    def set_email(self, e):
        self.email = e

    def set_password(self, p):
        self.password = p

    def set_type(self, t):
        self.type = t

    def get_id(self):
        return self.iden

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_type(self):
        return self.type


# ---------------------------------------------------------
class Runway:
    def __init__(self):
        self.nRunway = 0
        self.status = ""

    def set_nRunway(self, n):
        self.nRunway = n

    def set_status(self, s):
        self.status = s

    def get_nRunway(self):
        return self.nRunway

    def get_status(self):
        return self.status


# ---------------------------------------------------------
class Airline:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.yFoundation = 0
        self.countries = 0

    def set_name(self, n):
        self.name = n

    def set_type(self, t):
        self.type = t

    def set_yFoundation(self, y):
        self.yFoundation = y

    def set_countries(self, c):
        self.countries = c

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_countries(self):
        return self.countries


# ---------------------------------------------------------
class Gate:
    def __init__(self):
        self.nGate = 0
        self.status = ""

    def set_nGate(self, n):
        self.nGate = n

    def set_status(self, s):
        self.status = s

    def get_nGate(self):
        return self.nGate

    def get_status(self):
        return self.status


# ---------------------------------------------------------
class Crowd:
    def __init__(self):
        self.name = ""
        self.dBirth = ""
        self.iden = 0
        self.company = ""
        self.rol = ""

    def set_name(self, n):
        self.name = n

    def set_dBirth(self, b):
        self.dBirth = b

    def set_iden(self, i):
        self.iden = i

    def set_company(self, c):
        self.company = c

    def set_rol(self, r):
        self.rol = r

    def get_name(self):
        return self.name

    def get_dBirth(self):
        return self.dBirth

    def get_iden(self):
        return self.iden

    def get_company(self):
        return self.company

    def get_rol(self):
        return self.rol


# ---------------------------------------------------------
class Plane:
    def __init__(self):
        self.model = ""
        self.iden = 0
        self.aConstruccion = ""
        self.airline = Airline()

    def set_model(self, m):
        self.model = m

    def set_iden(self, i):
        self.iden = i

    def set_aConstruction(self, aC):
        self.aConstruccion = aC

    def set_Airline(self, a):
        self.airline = a

    def get_model(self):
        return self.model

    def get_iden(self):
        return self.iden

    def get_aConstruction(self):
        return self.aConstruccion

    def get_Airline(self):
        return self.airline


# ---------------------------------------------------------
class Airport:
    def __init__(self):
        self.name = ""
        self.city = ""
        self.country = ""

    def set_name(self, n):
        self.name = n

    def set_city(self, c):
        self.city = c

    def set_country(self, c):
        self.city = c

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country


class Flight:
    pass
