# import needed libraries
import pandas as pd
import streamlit as st
import calendar 
# set the page configuration
st.set_page_config(page_title="Sales Dashboard",page_icon="😁")
# set the title of the dashboard 
st.title("Sales Dashboard")
# define what the dashboard is all about 
st.markdown("This dashboard allows a user to analyze the sales activities per month")
# load the dataset 
data = pd.read_csv("sample_data2.csv")
st.write(data)

#SORT HE MONTH NAME CHRONOLOGICALLY
month_order=list(calendar.month_abbr)[1:7]
# UPDATE THE MAIN Month_name into the DataFrame
data["Month_name"]=pd.Categorical(data["Month_name"],categories=month_order,ordered=True)
# SORT THE DataFrame with the sorted month 
data = data.sort_values("Month_name")
st.title("Monthly Data Overview")
st.dataframe(data)
# sidebar filter
# Have option to select any region or all
region_options= ['All'] + list(data['Region'].unique())
# Have option to select any month or all
month_options= ['All'] + month_order 
region=st.sidebar.selectbox('Select Region',region_options)
month=st.sidebar.selectbox('Select Month',month_options)
# filter the data 
data_filtered= data.copy()
# determine how to access data from each region or month and as well all data 
if region !='All':
    data_filtered=data_filtered[data_filtered['Region']==region]
if month !='All':
    data_filtered=data_filtered[data_filtered['Month_name']==month]    
# KPI - Total - Sales 
total_sales=data_filtered['Sales'].sum()
st.metric(label=f"Total Sales",value=f"${total_sales:,.2f}")
# CHARTS
# CHART 1 - SALES BY PRODUCT CATEGORY 
st.write("### Sales by Product Category")
chart1 = data_filtered.groupby("Product_category")["Sales"].sum()
# use a bar chart
st.bar_chart(chart1)
# CHART 2 - Monthly SALES
st.write("### Sales Trend by Month")
chart2 = data_filtered.groupby("Month_name")["Sales"].sum()
# use a line chart
st.line_chart(chart2)