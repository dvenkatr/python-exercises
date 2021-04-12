PLANET_YEARS = {'earth': 1.0, 
            'mercury': 0.2408467,
            'venus': 0.61519726, 
            'mars': 1.8808158,
            'jupiter': 11.862615, 
            'saturn': 29.447498,
            'uranus': 84.016846, 
            'neptune': 164.79132
            }

class SpaceAge():

    def __init__(self, seconds):
        self.seconds = seconds / 31557600
        for planet in PLANET_YEARS:
            years = lambda arg = PLANET_YEARS[planet] : round(self.seconds / arg, 2)
            setattr(self, 'on_' + planet, years)

# print(SpaceAge(1000000000).on_earth())