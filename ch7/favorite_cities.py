class City: 
  def __init__(self, name, country, population, landmarks): 
    self.name = name 
    self.country = country 
    self.population = population 
    self.landmarks = landmarks 
brampton = City('Brampton', 'Canada', 700000, 'Gage Park')
print (vars(brampton)) 
