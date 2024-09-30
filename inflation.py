import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
def load_data():
    data = pd.read_csv("Indian Inflation Impact and Policy Assessment Survey .csv")
    return data

df = load_data()

# Set page config
st.set_page_config(page_title="Indian Inflation Survey Results", layout="wide")

# Title and description
st.title("Indian Inflation Impact and Policy Assessment Survey Results")
st.markdown("""
    Is your wallet feeling lighter? Let's talk about it! 💸
    Inflation got you scratching your head? You're not alone! 🤔
""")
st.markdown("""This dashboard presents the results of a survey on recent inflation trends in India.""")

# Sidebar for filtering
st.sidebar.header("Filters")
role = st.sidebar.multiselect("Select Role", df["Which of the following best describes your role or perspective on inflation in India?  "].unique())
industry = st.sidebar.multiselect("Select Industry", df["Industry"].unique())
experience = st.sidebar.slider("Years of Experience", min_value=0, max_value=30, value=(0, 30))

# Apply filters
filtered_df = df
if role:
    filtered_df = filtered_df[filtered_df["Which of the following best describes your role or perspective on inflation in India?  "].isin(role)]
if industry:
    filtered_df = filtered_df[filtered_df["Industry"].isin(industry)]
filtered_df = filtered_df[(filtered_df["Years of Experience"] >= experience[0]) & (filtered_df["Years of Experience"] <= experience[1])]

# Main dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("Overall Inflation Rating")
    fig_inflation = px.pie(filtered_df, names="How would you rate the overall inflation in India over the past 2 years?  ", title="Overall Inflation Rating")
    st.plotly_chart(fig_inflation, use_container_width=True)

    st.subheader("Primary Cause of Inflation")
    fig_cause = px.bar(filtered_df["What do you believe is the primary cause of recent inflation in India?  "].value_counts(), title="Primary Cause of Inflation",  width=800, height=800)
    st.plotly_chart(fig_cause, use_container_width=False)

with col2:
    st.subheader("Most Affected Product Category")
    fig_category = px.pie(filtered_df, names="Which product category do you think has contributed most to inflation recently?  ", title="Most Affected Product Category")
    st.plotly_chart(fig_category, use_container_width=True)

    st.subheader("Impact on Personal Financial Situation")
    fig_impact = px.bar(filtered_df["How has inflation impacted your personal financial situation?   "].value_counts(), title="Impact on Personal Financial Situation", width=800, height=800)
    st.plotly_chart(fig_impact, use_container_width=False)

# Additional insights
st.header("Additional Insights")

col3, col4 = st.columns(2)

with col3:
    st.subheader("RBI's Efforts to Control Inflation")
    fig_rbi = px.pie(filtered_df, names="How would you rate the Reserve Bank of India's efforts to control inflation?  ", title="RBI's Efforts to Control Inflation")
    st.plotly_chart(fig_rbi, use_container_width=True)

with col4:
    st.subheader("Most Affected Section of Society")
    fig_society = px.pie(filtered_df, names="In your opinion, which section of society has been most affected by recent inflation?  ", title="Most Affected Section of Society")
    st.plotly_chart(fig_society, use_container_width=True)

# Government response and future outlook
st.header("Government Response and Future Outlook")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Adequacy of Government Response")
    fig_response = px.pie(filtered_df, names="Do you think the government's response to inflation has been adequate?   ", title="Adequacy of Government Response")
    st.plotly_chart(fig_response, use_container_width=True)

with col6:
    st.subheader("Optimism About Inflation Control")
    fig_optimism = px.pie(filtered_df, names="How optimistic are you about inflation control in India over the next year?   ", title="Optimism About Inflation Control")
    st.plotly_chart(fig_optimism, use_container_width=True)

# Display raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(filtered_df)

# Footer
st.markdown("---")
st.markdown("Dashboard created for visualizing Indian Inflation Impact and Policy Assessment Survey results.")
