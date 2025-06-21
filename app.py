import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os # Import the os module to check file existence

st.set_page_config(page_title="Ship Clustering App", layout="wide")
st.title("🚢 Ship Clustering Dashboard")

# Define the full path to the CSV file in Google Drive
CSV_PATH = '/content/drive/MyDrive/global_cargo_ship_project/final_clustered_ships.csv'

# Load clustered dataset
# Add a check to ensure the file exists before attempting to read
if not os.path.exists(CSV_PATH):
    st.error(f"Error: The file '{CSV_PATH}' was not found.")
    st.info("Please ensure your Google Drive is mounted and the file path is correct.")
    st.stop() # Stop the Streamlit app if the file is not found
else:
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        st.stop()


# Sidebar
st.sidebar.header("🔍 Filter by Cluster")
selected_clusters = st.sidebar.multiselect("Select Clusters", options=sorted(df['cluster'].unique()), default=sorted(df['cluster'].unique()))

# Filter data
filtered_df = df[df['cluster'].isin(selected_clusters)]

# Cluster Summary
st.subheader("📊 Cluster Summary Statistics")
st.dataframe(filtered_df.groupby('cluster')[['gt', 'dwt', 'length', 'width', 'built_year']].mean().round(1))

# PCA Scatter Plot
st.subheader("📈 PCA Visualization")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='PC1', y='PC2', hue='cluster', palette='Set2', s=70)
plt.title("Clusters of Ships (PCA Projection)")
plt.grid(True)
st.pyplot(fig)

# Raw Data
with st.expander("📄 Show Full Data Table"):
    st.dataframe(filtered_df)
