class Resident:
    def __init__(self, roomNumber, numberOfResidents, rent):
        self.roomNumber = roomNumber
        self.numberOfResidents = numberOfResidents
        self.rent = rent

    def __repr__(self):
        return (f"Resident(roomNumber={self.roomNumber}, "
                f"numberOfResidents={self.numberOfResidents}, "
                f"rent={self.rent})")

class Building:
    def __init__(self, address):
        self.address = address
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def __repr__(self):
        return (f"Building(address='{self.address}', "
                f"residents={self.residents})")
