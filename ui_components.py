from dash import html, dash_table

CARD_STYLE = {
    "padding": "20px",
    "borderRadius": "15px",
    "background": "linear-gradient(135deg,#6dd5ed,#2193b0)",
    "color": "white",
    "width": "220px",
    "textAlign": "center",
    "boxShadow": "0px 6px 20px rgba(0,0,0,0.2)"
}


def card(title, value):

    return html.Div([
        html.H4(title),
        html.H2(value)
    ], style=CARD_STYLE)


def section(title):

    return html.H3(
        title,
        style={
            "marginTop": "40px",
            "marginBottom": "10px"
        }
    )


def table(table_id):

    return dash_table.DataTable(

        id=table_id,

        page_size=10,

        style_table={"overflowX": "auto"},

        style_cell={
            "padding": "10px",
            "textAlign": "left"
        },

        style_header={
            "backgroundColor": "#2c3e50",
            "color": "white"
        }
    )