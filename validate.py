import os
import json
import jsonschema
from jsonschema import validate


def get_schema() -> dict:
    """Загрузка JSON схемы."""
    file_path = (os.path.dirname(__file__)) + "/goods.schema.json"
    with open(file_path, 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data: dict) -> bool:
    """Валидация JSON."""
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError:
        print("Given JSON data is InValid")
        return False

    print("Given JSON data is Valid")
    return True
