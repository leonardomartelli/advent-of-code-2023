puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

almanac = puzzle_input.split('\n\n')

seeds =  [ int(e) for e in almanac[0].split()[1:] ]



class Range():
    def __init__(self, from_start, to_start, size):
        self.from_start = from_start
        self.to_start = to_start
        self.size = size
        pass

    def is_in(self, entry):
        return entry >= self.from_start and entry < self.from_start + self.size

    def get(self, entry):
        return self.to_start + (entry - self.from_start)

class MapByRange():
    def __init__(self) -> None:
        self.ranges = []
    
    def add_range(self, range):
        self.ranges.append(range)
    
    def has(self, entry):
        return any(r.is_in(entry) for r in self.ranges)
    
    def get(self, entry):
        for range in self.ranges:
            if range.is_in(entry):
                return range.get(entry)
        return entry

seed_soil_lines = almanac[1].split('\n')[1:]
seed_soil_map = MapByRange()

for line in seed_soil_lines:
    entries = [ int(e) for e in line.split()]
    seed_soil_map.add_range(Range(entries[1], entries[0], entries[2]))
    
soil_fertilizer_lines = almanac[2].split('\n')[1:]
soil_fertilizer_map = MapByRange()

for line in soil_fertilizer_lines:
    entries = [ int(e) for e in line.split()]
    soil_fertilizer_map.add_range(Range(entries[1], entries[0], entries[2]))
    
fertilizer_water_lines = almanac[3].split('\n')[1:]
fertilizer_water_map = MapByRange()

for line in fertilizer_water_lines:
    entries = [ int(e) for e in line.split()]
    fertilizer_water_map.add_range(Range(entries[1], entries[0], entries[2]))

water_light_lines = almanac[4].split('\n')[1:]
water_light_map = MapByRange()

for line in water_light_lines:
    entries = [ int(e) for e in line.split()]
    water_light_map.add_range(Range(entries[1], entries[0], entries[2]))

light_temperature_lines = almanac[5].split('\n')[1:]
light_temperature_map = MapByRange()

for line in light_temperature_lines:
    entries = [ int(e) for e in line.split()]
    light_temperature_map.add_range(Range(entries[1], entries[0], entries[2]))

temperature_humidity_lines = almanac[6].split('\n')[1:]
temperature_humidity_map = MapByRange()

for line in temperature_humidity_lines:
    entries = [ int(e) for e in line.split()]
    temperature_humidity_map.add_range(Range(entries[1], entries[0], entries[2]))

humidity_location_lines = almanac[7].split('\n')[1:]
humidity_location_map = MapByRange()

for line in humidity_location_lines:
    entries = [ int(e) for e in line.split()]
    humidity_location_map.add_range(Range(entries[1], entries[0], entries[2]))

locations = []



for seed in seeds:

    soil= seed_soil_map.get(seed)

    fertilizer = soil_fertilizer_map.get(soil)

    water = fertilizer_water_map.get(fertilizer)

    light = water_light_map.get(water)

    temperature = light_temperature_map.get(light)

    humidity = temperature_humidity_map.get(temperature)

    location = humidity_location_map.get(humidity)

    locations.append(location)


print(min(locations))