    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.set_page_config(page_title="Ship Clustering App", layout="wide")
    st.title("🚢 Ship Clustering Dashboard")

    # Load clustered dataset - Now, it should be in the same directory as app.py in the GitHub repo
    # Streamlit Cloud will find it here because you uploaded it to the repo
    try:
        df = pd.read_csv("final_clustered_ships.csv")
    except FileNotFoundError:
        st.error("Error: 'final_clustered_ships.csv' not found. Please ensure it is in the same GitHub repository as app.py.")
        st.stop()
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
    
