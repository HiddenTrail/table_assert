from robot.api.deco import keyword, not_keyword
from robot.libraries.BuiltIn import BuiltIn
import json
import os

class TableAssertionBrowserLibrary:

    @keyword("Verify Table")
    def verify_table(self, expected_filepath, table_locator, header_appendix="//th", row_appendix="//tr", cell_appendix="//td", init=False):

        headers = self._get_table_headers(table_locator, header_appendix)
        data = self._get_table_data(table_locator, row_appendix, cell_appendix)
        actual_json = _convert_to_json(headers, data)

        if init:
            _write_json_to_file(expected_filepath + "_template", actual_json)
        else:
            expected_json = _read_json_from_file(expected_filepath)
            if expected_json != actual_json:
                _write_json_to_file(expected_filepath + "_actual", actual_json)
                raise AssertionError(f"Table in {table_locator} does not match expected content at {expected_filepath}")

    @keyword("Verify Table Init")
    def verify_table_init(self, expected_filepath, table_locator, header_appendix="//th", row_appendix="//tr", cell_appendix="//td"):

        self.verify_table(expected_filepath, table_locator, header_appendix, row_appendix, cell_appendix, init=True)

    @not_keyword
    def _get_table_headers(self, table_locator, header_appendix):

        library_handle = BuiltIn().get_library_instance("Browser")
        header_elements = library_handle.get_elements(f"{table_locator}{header_appendix}")

        return [library_handle.get_text(header) for header in header_elements]

    @not_keyword
    def _get_table_data(self, table_locator, row_appendix, cell_appendix):

        library_handle = BuiltIn().get_library_instance("Browser")
        rows = library_handle.get_elements(f"{table_locator}{row_appendix}")
        data = []
        row_number = 0
        for row in rows:
            row_number += 1
            cell_elements = library_handle.get_elements(f"{table_locator}{row_appendix}[{row_number}]{cell_appendix}")
            row_data = [library_handle.get_text(cell) for cell in cell_elements]
            if row_data:
                data.append(row_data)

        return data

@not_keyword
def _convert_to_json(headers, data):

    json_data = []
    for row in data:
        row_dict = {headers[i]: row[i] for i in range(len(row))}
        for header in headers[len(row):]:
            row_dict[header] = None
        json_data.append(row_dict)

    return json.loads(json.dumps(json_data))

@not_keyword
def _write_json_to_file(filepath, json_content):

    _ensure_path_exists(filepath)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(json_content, file, indent=4)
    print("JSON written to " + filepath)

@not_keyword
def _ensure_path_exists(filepath):

    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

@not_keyword
def _read_json_from_file(filepath):

    file = open(filepath, "r")
    content = json.load(file)
    file.close()

    return content
