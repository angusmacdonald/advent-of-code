import time
from typing import List, Dict
import logging
import sys
from tqdm import tqdm


def load_lines_from_file() -> List[str]:
    with open('day5/input.txt') as f:
        return f.readlines()


def find_line_number_with_text(lines: List[str], text: str) -> int:
    for i in range(0, len(lines)):
        if lines[i].startswith(text):
            return i+1
    return -1


def get_mappings_for_type(lines: List[str], type: str) -> Dict:
    logging.info(f'get_mappings_for_type({type})')
    line_number = find_line_number_with_text(lines, type)
    if line_number == -1:
        return {}

    dest = {}
    for i in range(find_line_number_with_text(lines, type), len(lines)):
        line = lines[i].strip().lstrip()

        if not line:
            break

        dest_start, source_start, num_range = line.split(' ')
        data = {'source': int(source_start), 'dest': int(
            dest_start), 'range': int(num_range)}
        dest.update(
            {range(int(source_start), int(source_start)+int(num_range)): data})
    return dest


def find_in_map(range_list: Dict[range, Dict], value: int) -> int:
    for key in range_list:
        if value in key:
            diff = value - range_list[key]['source']
            return range_list[key]['dest'] + diff
    return value


def find_diff(range_list: List, value: int) -> [int, int]:
    # returns dist to end, and dest start val
    for entry in range_list:
        if entry['source'] <= value and value <= (entry['source'] + entry['range']):
            diff = value - entry['source']
            return (entry['source'] + entry['range'] - value), (entry['dest'] + diff)
    return 0, 0


logging.basicConfig(level=logging.INFO)
lines = load_lines_from_file()

seeds = lines[0][len('seeds: '):].strip().lstrip().split(' ')
seeds = [int(i) for i in seeds]

# break out seeds into pairs of seeds
seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

logging.info(seeds)

seed_to_soil_map = get_mappings_for_type(lines, 'seed-to-soil')
soil_to_fertilizer_map = get_mappings_for_type(lines, 'soil-to-fertilizer')
fertilizer_to_water_map = get_mappings_for_type(lines, 'fertilizer-to-water')
water_to_light_map = get_mappings_for_type(lines, 'water-to-light')
light_to_temperature_map = get_mappings_for_type(lines, 'light-to-temperature')
temperature_to_humidity_map = get_mappings_for_type(
    lines, 'temperature-to-humidity')
humity_to_location_map = get_mappings_for_type(lines, 'humidity-to-location')

# set min_value to max int
min_value = sys.maxsize
min_seed = -1

total_iterations = 0

for pair in seed_pairs:
    seed_start = pair[0]
    seed_end = pair[0] + pair[1]
    total_iterations += seed_end-seed_start

with tqdm(total=total_iterations) as pbar:
    for pair in seed_pairs:
        seed_start = pair[0]
        seed_end = pair[0] + pair[1]

        for i in range(0, seed_end-seed_start):
            seed = seed_start+i
            logging.debug(f'seed: {seed}')

            soil = find_in_map(seed_to_soil_map, seed)
            logging.debug(f'soil: {soil}')
            fertilizer = find_in_map(soil_to_fertilizer_map, soil)
            logging.debug(f'fertilizer: {fertilizer}')
            water = find_in_map(fertilizer_to_water_map, fertilizer)
            logging.debug(f'water: {water}')
            light = find_in_map(water_to_light_map, water)
            logging.debug(f'light: {light}')
            temperature = find_in_map(light_to_temperature_map, light)
            logging.debug(f'temperature: {temperature}')
            humidity = find_in_map(temperature_to_humidity_map, temperature)
            logging.debug(f'humidity: {humidity}')
            location = find_in_map(humity_to_location_map, humidity)
            logging.debug(f'location: {location}')

            logging.debug(f'seed: {seed} location: {location}')
            if location < min_value:
                min_value = location
                min_seed = seed
            pbar.update(1)

    print(min_value)


pbar.close()
