import pandas as pd

def select_charts(df):

    charts = []

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Histogram + Boxplot for top numeric columns (limit to avoid API rate limits and UI clutter)
    for col in numeric_cols[:4]:
        charts.append({
            "column": col,
            "chart_type": "histogram"
        })

        charts.append({
            "column": col,
            "chart_type": "box"
        })

    # Bar + Pie for categorical
    for col in categorical_cols[:2]:   # limit to avoid too many charts
        charts.append({
            "column": col,
            "chart_type": "bar"
        })

        charts.append({
            "column": col,
            "chart_type": "pie"
        })

    # Scatter for first numeric pair
    if len(numeric_cols) >= 2:
        charts.append({
            "x": numeric_cols[0],
            "y": numeric_cols[1],
            "chart_type": "scatter"
        })

    # Correlation heatmap
    charts.append({
        "chart_type": "heatmap"
    })

    return charts