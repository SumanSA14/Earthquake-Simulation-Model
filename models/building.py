class Building:

    def __init__(self,id,lat,lng):

        self.id=id
        self.lat=lat
        self.lng=lng
        self.damage=0


    def to_dict(self):

        return {
            "id":self.id,
            "lat":self.lat,
            "lng":self.lng,
            "damage":self.damage
        }