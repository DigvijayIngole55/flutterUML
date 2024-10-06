import streamlit as st
from workflow_manager import handle_workflow

# Title of the app
st.title("Flutter Code UML Diagram Generator")

# Upload a zip file
uploaded_file = st.file_uploader("Upload a zip file containing Flutter code", type=["zip"])

# Display the name of the uploaded zip file and process it
if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Process the uploaded file and get the parsed output
    results = handle_workflow(uploaded_file)

    # Display the results on the UI
    if results:
        st.write("Parsed Output for Each Dart File:")
        for file_name, parsed_output in results:
            st.write(f"File: {file_name}")
            st.write(f"Parsed Output: {parsed_output}")
