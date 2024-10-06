import zipfile
import io
from code_parser import parse_code
import streamlit as st  # Add Streamlit to handle UI updates

def handle_workflow(uploaded_file):
    # Initialize an empty list to hold results for display
    results = []

    # Unzip the uploaded file
    with zipfile.ZipFile(io.BytesIO(uploaded_file.read())) as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.dart'):
                # Read the Dart file
                with zip_ref.open(file_name) as dart_file:
                    code = dart_file.read().decode('utf-8')
                    # Pass the code to GraphCodeBERT for parsing
                    parsed_output = parse_code(code)
                    # Append the result to the list
                    results.append((file_name, parsed_output))

    # Return the results to the Streamlit UI
    return results
