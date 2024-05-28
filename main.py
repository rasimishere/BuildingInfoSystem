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

def main():
    building = Building("RasimHolding")

    building.add_resident(Resident(101, 1, 1600))
    building.add_resident(Resident(102, 2, 2000))
    building.add_resident(Resident(103, 3, 5200))
    building.add_resident(Resident(104, 4, 8000))

    print("Building Information:")
    print(f"Address: {building.address}")
    print("Residents:")
    for resident in building.residents:
        print(f"  Room Number: {resident.roomNumber}, "
              f"Number of Residents: {resident.numberOfResidents}, "
              f"Rent: {resident.rent}")


if __name__ = "__main__":
main()
