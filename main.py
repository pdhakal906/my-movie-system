import streamlit as st
import pandas as pd
import json

# Path to your JSON file
json_file_path = "Watched.json"

# Function to load JSON file
def load_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

# Main function to run the Streamlit app
def main():
    st.title("JSON to DataFrame Viewer")
    
    # Load JSON file
    data = load_json(json_file_path)
    
    # Convert JSON to DataFrame
    df = pd.json_normalize(data)
    df = df.drop_duplicates()
    # Display DataFrame
    st.write("### DataFrame:")
    st.dataframe(df)
    


if __name__ == "__main__":
    main()
