import json
from datetime import datetime as dt

#set required schema fields
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
    #try and except to change str to datetime.date
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
            
            # if condition to check for schema
            if not check_schema(row):
                #tells you if there is missing schema in a line
                msg = f"Invalid row schema (missing required fields): {row}"
                print(msg)
            # if statement to check for null values
            elif None in row.values():
                # tells you if a line contains a null
                msg2 = f"Invalid data (contains a null): {row}"
                print(msg2)
            # if schemas and values are correct, append datalines to empty list
            else:
                # changes str to datetime.date
                row["registered_date"] = parse_date(row["registered_date"])
                profiles.append(row)
            line_num += 1
        
        # tells user how many profiles were read
        print(f"Read {len(profiles)} profiles")
        # return appended list
        return profiles

def json_write_into_file(data_file):
    """Writes appended list back into json"""
    for row in profiles:
        # changes datetime.date back into str
        row["registered_date"] = str(row["registered_date"])
    # open json file to write in
    with open(data_file, "w") as json_file:
        json.dump(profiles, json_file, indent=4, skipkeys=True)
