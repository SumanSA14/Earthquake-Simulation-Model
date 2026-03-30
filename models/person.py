class Person:

    def __init__(self,id,lat,lng):

        self.id=id
        self.lat=lat
        self.lng=lng
        self.health=100


    def to_dict(self):

        return {
            "id":self.id,
            "lat":self.lat,
            "lng":self.lng,
            "health":self.health
        }