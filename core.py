import pandas as pd

def process_data(df):
    df.columns = df.columns.str.lower()

    # Feature engineering
    df["lat_diff"] = df["lat"].diff().abs()
    df["lon_diff"] = df["lon"].diff().abs()
    df["alt_diff"] = df["geoaltitude"].diff().abs()

    # Fill missing values
    df = df.fillna(0)

    # Spoof detection logic
    df["spoof"] = (
        (df["lat_diff"] > 1.0) |
        (df["lon_diff"] > 1.0) |
        (df["velocity"] > 1000) |
        (df["alt_diff"] > 5000)
    ).astype(int)

    df["label"] = df["spoof"].map({0: "Normal", 1: "Spoof"})

    return df