from etl import json_read_and_transform
from etl import json_write_into_file

def main(input_file, output_file):
    json_read_and_transform(input_file)
    json_write_into_file(output_file)

main("./data/vehicles_simple.json", "./data/transformer.json")