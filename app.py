import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

from utils import load_transactions, save_transaction, monthly_totals, category_totals
from advice import financial_advice
from charts import bar_chart, pie_chart
from ui_components import card, section, table


app = dash.Dash(__name__)
server = app.server
app.title = "Personal Finance Dashboard"


app.layout = html.Div([

    html.H1("💰 Personal Finance Dashboard",
            style={"textAlign": "center"}),

    section("Add Transaction"),

    html.Div([

        dcc.DatePickerSingle(id="date"),

        dcc.Input(id="desc", placeholder="Description"),

        dcc.Input(id="category", placeholder="Category"),

        dcc.Input(id="amount", type="number", placeholder="Amount"),

        html.Button("Add", id="add-btn")

    ], style={"display": "flex", "gap": "10px"}),

    html.Div(id="summary",
             style={"display": "flex", "gap": "30px", "marginTop": "30px"}),

    section("Financial Advice"),

    html.Div(id="advice",
             style={
                 "padding": "20px",
                 "background": "#ecf0f1",
                 "borderRadius": "10px"
             }),

    section("Spending Charts"),

    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="pie-chart"),

    section("All Transactions"),
    table("transactions")

], style={"maxWidth": "1100px", "margin": "auto"})


@app.callback(

    Output("transactions", "data"),
    Output("transactions", "columns"),
    Output("summary", "children"),
    Output("bar-chart", "figure"),
    Output("pie-chart", "figure"),
    Output("advice", "children"),

    Input("add-btn", "n_clicks"),

    State("date", "date"),
    State("desc", "value"),
    State("category", "value"),
    State("amount", "value")

)

def update_dashboard(clicks, date, desc, category, amount):

    if clicks and date and desc and category and amount:
        save_transaction(date, desc, category, amount)

    df = load_transactions()

    if df.empty:
        return [], [], "No data yet", {}, {}, "Add your first transaction."

    monthly = monthly_totals(df)
    category_df = category_totals(df)

    total = df["Amount"].sum()
    avg = round(df["Amount"].mean(), 2)

    top_category = category_df.sort_values("Amount", ascending=False).iloc[0]["Category"]

    cards = [
        card("Total Spending", f"₹{total}"),
        card("Average Expense", f"₹{avg}"),
        card("Top Category", top_category)
    ]

    advice = financial_advice(total)

    return (

        df.to_dict("records"),
        [{"name": i, "id": i} for i in df.columns],

        cards,

        bar_chart(monthly),
        pie_chart(category_df),

        advice
    )


if __name__ == "__main__":
    app.run(debug=True)