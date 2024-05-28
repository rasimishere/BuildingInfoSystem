class Resident:
    def __init__(self, roomNumber, numberOfResidents, rent):
        self.roomNumber = roomNumber
        self.numberOfResidents = numberOfResidents
        self.rent = rent

    def __repr__(self):
        return (f"Resident(roomNumber={self.roomNumber}, "
                f"numberOfResidents={self.numberOfResidents}, "
                f"rent={self.rent})")
