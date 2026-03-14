import plotly.express as px


def bar_chart(monthly_df):

    if monthly_df.empty:
        return {}

    fig = px.bar(
        monthly_df,
        x="Date",
        y="Amount",
        title="Monthly Spending",
        text="Amount",
        color="Amount"
    )

    fig.update_layout(template="plotly_white")

    return fig


def pie_chart(category_df):

    if category_df.empty:
        return {}

    fig = px.pie(
        category_df,
        names="Category",
        values="Amount",
        title="Spending by Category",
        hole=0.4
    )

    fig.update_layout(template="plotly_white")

    return fig