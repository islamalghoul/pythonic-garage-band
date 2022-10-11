


class Musician:
    def __init__(self,name):
        self.name=name
    def play_solos(self):
        return 
    def get_instrument(self):
        return
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
    def play_solo(self):
        return self.play_solos()



class Band():
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
    @classmethod
    def to_list(cls):
        return cls.instances
    def play_solos(self):
        array=[]
        for i in self.members:  
            array.append(i.play_solos())

        return array
        

class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)
    def play_solos(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return "guitar"
  

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)
        
       
    def play_solos(self):
        return  "bom bom buh bom"
    def get_instrument(self):
        return "bass"



class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)
    def play_solos(self):
        return "rattle boom crash"
    def get_instrument(self):
        return "drums"
