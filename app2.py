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
        sheet_name="Sheet2"
    )
    df = pd.melt(df, id_vars = ['Scenario'],var_name = 'Year', value_name='Projection')
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
culm_scenario = st.sidebar.multiselect(
    "Select Stacked Scenarios:",
    options=df["Scenario"].unique(),
    default=df["Scenario"].unique()
)

group_scenario = st.sidebar.multiselect(
    "Select Grouped Scenario:",
    options=df["Scenario"].unique(),
    default=df["Scenario"].unique()
)

df_culm_selection = df.query(
    "Scenario == @culm_scenario"
)
df_group_selection = df.query(
    "Scenario == @group_scenario"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Projections")
st.markdown("###")
year_selection = st.sidebar.slider('Year:',
                           min_value=int(df['Year'].min()), 
                           max_value=int(df['Year'].max()),
                           value = (int(df['Year'].min()),int(df['Year'].max())))
st.markdown("###")
mask = df_culm_selection['Year'].between(*year_selection)
fig_projections = px.bar(
    df_culm_selection[mask],
    x="Year",
    y="Projection",
    orientation="v",
    title="<b>Stacked Projections</b>",
    color="Scenario",
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.D3
)

st.plotly_chart(fig_projections, use_container_width=True)

mask = df_group_selection['Year'].between(*year_selection)
fig_projections_grouped = px.bar(
    df_group_selection[mask],
    x="Year",
    y="Projection",
    orientation="v",
    title="<b>Grouped Projections</b>",
    color="Scenario",
    template="plotly_white",
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.D3
)
st.plotly_chart(fig_projections_grouped, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
