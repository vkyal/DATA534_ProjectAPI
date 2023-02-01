class getLongLat:
    
    def __init__(self,city,forcastType):
        self.city = city
        # 1 : Civil; 2 : Meteo; 3 : Astro
        self.forcastType = forcastType
      
    def __str__(self):
        if (self.forcastType == 0) :
            forcastStr = "Civil Forcast"
        elif (self.forcastType == 1) :
            forcastStr = "Meteo Forcast"
        else :
            forcastStr = "Astro Forcast"
        return f'City Name : {self.city}\nForcast Type: {forcastStr}'
    


        
        
