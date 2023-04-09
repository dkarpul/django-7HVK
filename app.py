import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Scenario Predictions Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Scenarios.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="A:D",
        nrows=1000,
    )
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
scenario = st.sidebar.multiselect(
    "Select Scenarios:",
    options=df["Scenario"].unique(),
    default="Kraaicon"
)

location = st.sidebar.multiselect(
    "Select the Locations:",
    options=df["Location"].unique(),
    default="Belcon Redevelopment",
)

df_selection = df.query(
    "Scenario == @scenario & Location ==@location"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Projections")
st.markdown("##")

# # TOP KPI's
# total_sales = int(df_selection["Total"].sum())
# average_rating = round(df_selection["Rating"].mean(), 1)
# star_rating = ":star:" * int(round(average_rating, 0))
# average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Sales:")
#     st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#     st.subheader("Average Rating:")
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader("Average Sales Per Transaction:")
#     st.subheader(f"US $ {average_sale_by_transaction}")

# st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
myvals = (
    df_selection.groupby(['Year','Scenario','Location'],as_index=False)[['Value']].sum()
    #.sum()[["Total"]].sort_values(by="Total")
)
fig_projections = px.bar(
    myvals,
    x="Year",
    y="Value",
    orientation="v",
    title="<b>Projections</b>",
    #color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_projections.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Total",
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_projections, use_container_width=True)
#right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
