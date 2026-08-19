# SpaceX Falcon 9 Launch Records — Interactive Dash Dashboard
# Author: Pritam Acharya
#
# Run with:
#   pip install dash plotly pandas
#   python spacex_dash_app.py
# Then open http://127.0.0.1:8050 in your browser.

import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
spacex_df = pd.read_csv("../data/spacex_launch_geo.csv")
max_payload = spacex_df["PayloadMass"].max()
min_payload = spacex_df["PayloadMass"].min()

launch_sites = spacex_df["LaunchSite"].unique().tolist()
site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": site, "value": site} for site in launch_sites
]

# ---------------------------------------------------------------------------
# App layout
# ---------------------------------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "fontSize": 32},
        ),
        # TASK 1: Launch site dropdown
        dcc.Dropdown(
            id="site-dropdown",
            options=site_options,
            value="ALL",
            placeholder="Select a Launch Site here",
            searchable=True,
            style={"width": "80%", "margin": "0 auto"},
        ),
        html.Br(),
        # TASK 2: Success-rate pie chart
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (kg):"),
        # TASK 3: Payload range slider
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={i: str(i) for i in range(0, 10001, 2500)},
            value=[min_payload, max_payload],
        ),
        # TASK 4: Payload-vs-success scatter chart
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


# ---------------------------------------------------------------------------
# Callbacks
# ---------------------------------------------------------------------------
@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def get_pie_chart(selected_site):
    if selected_site == "ALL":
        fig = px.pie(
            spacex_df,
            values="Class",
            names="LaunchSite",
            title="Total successful launches by site",
        )
    else:
        filtered_df = spacex_df[spacex_df["LaunchSite"] == selected_site]
        counts = filtered_df["Outcome"].value_counts().reset_index()
        counts.columns = ["Outcome", "Count"]
        fig = px.pie(
            counts,
            values="Count",
            names="Outcome",
            title=f"Success vs. failure for {selected_site}",
        )
    return fig


@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def get_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    mask = spacex_df["PayloadMass"].between(low, high)
    filtered_df = spacex_df[mask]
    if selected_site != "ALL":
        filtered_df = filtered_df[filtered_df["LaunchSite"] == selected_site]

    fig = px.scatter(
        filtered_df,
        x="PayloadMass",
        y="Class",
        color="BoosterVersion",
        title="Payload mass vs. landing outcome",
        labels={"Class": "Landing outcome (1 = success)", "PayloadMass": "Payload mass (kg)"},
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
