import random
import time

def cal_wealth(population, met_min, gold_min, water_resource, fields):
    return (gold_min * 1000) + met_min * 100 + (water_resource * 10000 / population) + (fields * population)

def rain(water_reso):
    return water_reso + random.randint(0, 5)

def discover_gold_min(golds):
    return golds + random.uniform(0.1, 0.5)

def cosume_water(water_reso, population):
    return water_reso - (population * 0.01 * water_reso)

nations = [{"name":"Fairy_land" ,"population": 200, "metal_mines": 3, "gold_mines": 10, "water_resource": 50, "agriculture_fields": 120},
           {"name":"Unicorn_land" ,"population": 110, "metal_mines": 3, "gold_mines": 8, "water_resource": 30, "agriculture_fields": 110},
           {"name":"Tatooine" ,"population": 110, "metal_mines": 200, "gold_mines": 12, "water_resource": 25, "agriculture_fields": 40},
           {"name":"Naboo" ,"population": 25, "metal_mines": 3, "gold_mines": 13, "water_resource": 50, "agriculture_fields": 80},
           {"name":"Dathamir" ,"population": 80, "metal_mines": 200, "gold_mines": 5, "water_resource": 20, "agriculture_fields": 45},
           {"name":"Ghostland" ,"population": 30, "metal_mines": 10, "gold_mines": 18, "water_resource": 10, "agriculture_fields": 50},
           {"name":"Torran" ,"population": 200, "metal_mines": 100, "gold_mines": 5, "water_resource": 30, "agriculture_fields": 90},
           {"name":"Sind" ,"population": 300, "metal_mines": 3, "gold_mines": 1, "water_resource": 55, "agriculture_fields": 100}]

# for each nation, calculate the initial wealth using cal_wealth
# not remove this line

time.sleep(1)

# call rain function and update water resources and re-calculate wealth function

