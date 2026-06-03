import streamlit as st
import pandas as pd

st.title("KISS Bootleg Database 🎸")
st.write("Double-click any cell in the Status column to update your collection!")

# 1. Read your data
df = pd.read_csv("shows.csv")

# 2. Automatically create a 'Status' column if it doesn't exist yet
if 'Status' not in df.columns:
    df['Status'] = 'Searching'

# 3. Create the interactive table with a dropdown menu
edited_df = st.data_editor(
    df,
    column_config={
        "Status": st.column_config.SelectboxColumn(
            "Status",
            options=["Searching", "Owned (Digital)", "Owned (Physical)", "Upgrading"],
            required=True,
        )
    },
    use_container_width=True,
    hide_index=True
)

# 4. Create a Save Button
if st.button("Save My Collection"):
    edited_df.to_csv("shows.csv", index=False)
    st.success("Database updated successfully! 🤘")