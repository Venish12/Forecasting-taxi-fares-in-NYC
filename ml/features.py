import pandas as pd
import numpy as np

JFK_LONLAT = (-73.7781, 40.6413)
LGA_LONLAT = (-73.8740, 40.7769)
EWR_LONLAT = (-74.1745, 40.6895)
MET_LONLAT = (-73.9632, 40.7794)
WTC_LONLAT = (-74.0099, 40.7126)

FEATURE_ORDER = [
    "pickup_longitude","pickup_latitude",
    "dropoff_longitude","dropoff_latitude",
    "passenger_count",
    "pickup_datetime_year","pickup_datetime_month","pickup_datetime_day",
    "pickup_datetime_weekday","pickup_datetime_hour",
    "trip_distance",
    "jfk_drop_distance","lga_drop_distance","ewr_drop_distance",
    "met_drop_distance","wtc_drop_distance",
]

def add_dateparts(df, col):
    df[col + "_year"] = df[col].dt.year
    df[col + "_month"] = df[col].dt.month
    df[col + "_day"] = df[col].dt.day
    df[col + "_weekday"] = df[col].dt.weekday
    df[col + "_hour"] = df[col].dt.hour

def haversine_np(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

def add_landmark_dropoff_distance(df, landmark_name, landmark_lonlat):
    lon, lat = landmark_lonlat
    df[landmark_name + "_drop_distance"] = haversine_np(
        lon, lat, df["dropoff_longitude"], df["dropoff_latitude"]
    )

def make_features(raw_df: pd.DataFrame) -> pd.DataFrame:
    df = raw_df.copy()

    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce")
    if df["pickup_datetime"].isna().any():
        raise ValueError("pickup_datetime must be like: 2015-01-27 13:08:24 UTC")

    add_dateparts(df, "pickup_datetime")

    df["trip_distance"] = haversine_np(
        df["pickup_longitude"], df["pickup_latitude"],
        df["dropoff_longitude"], df["dropoff_latitude"]
    )

    add_landmark_dropoff_distance(df, "jfk", JFK_LONLAT)
    add_landmark_dropoff_distance(df, "lga", LGA_LONLAT)
    add_landmark_dropoff_distance(df, "ewr", EWR_LONLAT)
    add_landmark_dropoff_distance(df, "met", MET_LONLAT)
    add_landmark_dropoff_distance(df, "wtc", WTC_LONLAT)

    return df[FEATURE_ORDER]
