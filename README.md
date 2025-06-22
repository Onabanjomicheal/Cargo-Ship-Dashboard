# 🚢 Ship Clustering Dashboard

![Vacation Image](https://github.com/Onabanjomicheal/Cargo-Ship-Dashboard/blob/main/Vacation.png)


[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/Onabanjomicheal/Cargo-Ship-Dashboard/main/app.py)

An interactive web application designed to visualize and explore clusters of cargo ships based on their key characteristics. This dashboard transforms complex ship data into actionable insights, aiding in maritime market analysis, fleet optimization, and strategic decision-making.

## Why This Matters
🔥

The global shipping industry relies on efficient fleet management and market understanding. With thousands of vessels varying in size, age, and capacity, identifying distinct ship types can be challenging. This project addresses that by automatically grouping similar ships into "clusters" and providing an interactive dashboard to explore these segments.

Our dashboard enables quick identification of common characteristics within different ship segments, streamlining analysis of market trends, potential acquisitions, or specialized vessel requirements. It turns raw data into clear, actionable intelligence for navigating the complexities of the maritime sector.

## Table of Contents

- [Project Goals](#project-goals)
- [Core Concepts](#core-concepts)
- [Cluster Characteristics & Insights](#cluster-characteristics--insights)
- [Stack and Tools](#stack-and-tools)
- [What to Do Next](#what-to-do-next)
- [Author](#author)

## Project Goals
🎯

The primary goals of this project are:

- To segment a global dataset of cargo ships into distinct clusters based on their attributes (e.g., tonnage, dimensions, built year).
- To provide an interactive Streamlit dashboard for users to visually explore these clusters.
- To offer summarized statistics for each cluster, highlighting their unique characteristics.
- To facilitate data-driven decision-making for maritime businesses in areas like fleet management, market analysis, and investment.

## Core Concepts
🧠

| Concept | Description |
| --------------------- | ------------------------------------------------------------------------------------------------------------- |
| ✅ **Ship Clustering** | Automated grouping of ships with similar characteristics (e.g., GT, DWT, length, width, built year) into distinct segments. |
| ✅ **Principal Component Analysis (PCA)** | A dimensionality reduction technique used to simplify complex ship features into two main components (`PC1`, `PC2`) for 2D visualization. |
| ✅ **Interactive Dashboard** | A web application built with Streamlit that allows users to filter, summarize, and visualize the clustered data dynamically. |

## Cluster Characteristics & Insights
📊

The clustering process typically identifies distinct segments of ships. Based on common patterns in maritime data, these clusters might represent:

| Cluster Type (Hypothetical Example) | Characteristics (Example) | Potential Use/Market (Example) |
|---|---|---|
| ✅ **Ultra-Large Carriers** | Very high GT/DWT, longest/widest, typically newer. | Global main trade routes, economies of scale for bulk/container. |
| ⬜ **Modern Mid-Sized Vessels** | Medium-to-high GT/DWT, modern build year, balanced dimensions. | Flexible routes, diverse cargo types, general cargo. |
| ❌ **Veteran Specialists** | Older build year, diverse GT/DWT, specialized designs (e.g., tankers, cruise). | Niche markets, regional trade, specific cargo needs. |

The "Cluster Summary Statistics" and "PCA Visualization" sections in the dashboard allow users to observe the precise characteristics and visual separation of the clusters identified in *your specific dataset*.

## Stack and Tools
🧰

- **User Interface:** Streamlit (Python web application framework)
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Seaborn, Matplotlib

## What to Do Next
✅

- Explore the deployed app on Streamlit Cloud using the filtering options.
- Analyze the summary statistics to understand each cluster's profile.
- Visually inspect the PCA plot to grasp cluster separation.
- Open an issue with your feedback or suggestions. Let's make this even better!

## Author
👨‍💻

**Onabanjo Micheal**
Engineer | Transportation Researcher | Builder
Passionate about data analysis, machine learning applications, and building intelligent systems.
🔗 [LinkedIn Profile](https://www.linkedin.com/in/micheal-onabanjo/)
