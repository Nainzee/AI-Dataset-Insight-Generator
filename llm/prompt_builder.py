def build_prompt(column, stats, chart_type):
    if chart_type == "heatmap":
        return """You are a data analyst.
Analyze the correlation matrix heatmap across numerical variables in the dataset.
Explain key correlation patterns and relationships between variables in simple language in 2 sentences."""

    if chart_type == "scatter":
        return f"""You are a data analyst.
Analyze the relationship between variables: {column}
Chart Type: scatter plot.
Explain any visible correlation, clustering, or trend in simple language in 2 sentences."""

    if stats and stats.get("type") == "categorical":
        top_cats = stats.get("top_values", {})
        top_cats_str = ", ".join([f"{k}: {v}" for k, v in top_cats.items()]) if top_cats else "N/A"
        return f"""You are a data analyst.
Analyze the categorical column: {column}
Chart Type: {chart_type}
Top categories (count): {top_cats_str}
Explain the distribution or most prominent category in simple language in 2 sentences."""

    mean_val = stats.get("mean", "N/A") if stats else "N/A"
    median_val = stats.get("median", "N/A") if stats else "N/A"
    min_val = stats.get("min", "N/A") if stats else "N/A"
    max_val = stats.get("max", "N/A") if stats else "N/A"

    return f"""You are a data analyst.
Analyze the numerical column: {column}
Chart Type: {chart_type}
Statistics:
- Mean: {mean_val}
- Median: {median_val}
- Min: {min_val}
- Max: {max_val}
Explain the distribution, pattern, or skewness in simple language in 2 sentences."""