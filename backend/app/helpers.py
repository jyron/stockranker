import bson


def convert_objectids_to_strings(data):
    """Converts all ObjectIds in a list of dicts to strings."""
    for item in data:
        for key, value in item.items():
            if isinstance(value, bson.ObjectId):
                item[key] = str(value)
    return data
