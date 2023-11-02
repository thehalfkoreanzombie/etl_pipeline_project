import json
from datetime import datetime as dt

REQUIRED_SCHEMA_FIELDS = {"license_plate", "make_model", "year", "color", "registered_date", "registered_name", "registered_address"}

def check_schema(row, required_fields=REQUIRED_SCHEMA_FIELDS):
    """
    checks if a json row (or dict) contains all required fields (or keys)
    """
    # loop through all the required fields
    for field_name in required_fields:
        # return false if any key is not in the dict
        if field_name not in row:
            return False
    # otherwise return true
    return True

def parse_date(value, dtfmt="%Y-%m-%d"):
    """
    function to parse a date string into datetime.date object.
    return None if there are any issues
    """
    try:
        return dt.strptime(value, dtfmt).date()
    except:
        return None
profiles = []
# open the JSON file for reading
def json_read_and_transform(data_file):
    with open(data_file, "r") as json_file:
        line_num = 1
        # establish 'for' loop to go through each entry
        for line in json_file:
            # read json string (the line) into a dict
            row = json.loads(line.strip())
            #print(type(row))
            if not check_schema(row):
                msg = f"Invalid row schema (missing required fields): {row}"
                print(msg)
            elif None in row.values():
                msg2 = f"Invalid data (contains a null): {row}"
                print(msg2)
            else:
                row["registered_date"] = parse_date(row["registered_date"])
                #print(f"{line_num:02d}: {row}")
                profiles.append(row)
            line_num += 1
        print(f"Read {len(profiles)} profiles")
        return profiles
    
#json_read_and_transform("./data/vehicles_simple.json")

def json_write_into_file(data_file):
    for row in profiles:
        row["registered_date"] = str(row["registered_date"])
    with open(data_file, "w") as json_file:
        json.dump(profiles, json_file, indent=4, skipkeys=True)
    

#json_write_into_file("./data/transformer.json")
