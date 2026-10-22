import pandas as pd


def generate_statistics(df):
    """
    Generates basic statistics for each column
    """

    stats = {}

    for column in df.columns:
        if df[column].dtype in ["int64", "float64"]:
            stats[column] = {
                "type": "numerical",
                "mean": round(float(df[column].mean()), 2),
                "median": round(float(df[column].median()), 2),
                "min": round(float(df[column].min()), 2),
                "max": round(float(df[column].max()), 2)
            }
        else:
            stats[column] = {
                "type": "categorical",
                "top_values": df[column].value_counts().head(3).to_dict()
            }

    return stats


# Testing
if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_data.csv")
    output = generate_statistics(df)
    print(output)