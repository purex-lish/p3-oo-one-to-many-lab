class Pet:
    all=[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name,pet_type, owner=None) :
        self.name=name
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet-type.")
        self.pet_type=pet_type
        self._owner=None
        Pet.all.append(self)

        if owner is not None:
          if not isinstance(owner,Owner):
             raise TypeError("Owner must be an instance of the Owner class.")
          self._owner = owner
    @property
    def owner(self):
       return self._owner
    
    @owner.setter
    def owner(self,value):
       if not isinstance(value,Owner):
          raise TypeError("Owner must be an instance of the Owner class. ")
       self._owner=value
        
    

class Owner:
    def __init__(self,name) :
       self.name=name
       self._pet=None

    def pets(self):
         return [pet for pet in Pet.all if pet.owner==self]
   
    def add_pet(self,pet):
      if not isinstance(pet,Pet):
         ValueError("pet must be an instance of Pet class." )
      pet.owner=self

    def get_sorted_pets(self):
      sorted_pets=sorted(self.pets(),key=lambda pet:pet.name)
      return sorted_pets