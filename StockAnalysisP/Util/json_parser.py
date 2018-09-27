import json
def json_parser(file_location):
    with open(file_location) as data_file:
        data = json.load(data_file)
    return data # This will only pull in ticker symbols we are interested in
