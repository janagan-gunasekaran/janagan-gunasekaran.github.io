import json
from tableschema import Table


def validate_csv_line_by_line(csv_file_path, schema_file_path):
    def exc_handler(exc, row_number=None, row_data=None, error_data=None):
        errors.append((row_number, exc.errors, error_data))

    errors = []

    with open(schema_file_path) as f:
        schema = json.load(f)
    table_ = Table(csv_file_path, schema=schema)
    row_count = 0
    for _ in table_.iter(exc_handler=exc_handler):
        row_count = row_count + 1
    return errors, row_count
