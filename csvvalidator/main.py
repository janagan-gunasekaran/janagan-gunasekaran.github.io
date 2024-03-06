from flask import Flask, render_template, request
import pandas as pd
import os
from validate import validate_csv_line_by_line
app = Flask(__name__)
project_directory = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(project_directory, 'Data')



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            errors = None
            csv_file = request.files['csv-file']
            schema_file = request.files['schema-file']
            if not csv_file and not schema_file:
                return render_template('validator.html', message="No files uploaded")
            schema_filename = schema_file.filename
            schema_file_path = os.path.join(data_folder, schema_filename)
            schema_file.save(schema_file_path)

            csv_filename = csv_file.filename
            csv_file_path = os.path.join(data_folder, csv_filename)
            csv_file.save(csv_file_path)
            errors, row_count = validate_csv_line_by_line(csv_file_path, schema_file_path)
            if errors:
                return render_template('validator.html', errors=errors, error_count=len(errors), line_count=row_count)
        except Exception as err:
            print(err)
            return render_template('validator.html', message="Error: " + str(err))
    return render_template('validator.html', errors=None, error_count=0, line_count=0)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
