import pandas as pd
from pathlib import Path

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

VALID_EVENTS = {"click", "view", "purchase", "signup"}

df = pd.read_csv(INPUT)

df = df.dropna()
df = df[df["event_type"].isin(VALID_EVENTS)]

df["duration_seconds"] = pd.to_numeric(
    df["duration_seconds"],
    errors="coerce"
)

df = df.dropna(subset=["duration_seconds"])
df = df[df["duration_seconds"] > 0]

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="mixed",
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime(
    "%Y-%m-%dT%H:%M:%S"
)

df["duration_seconds"] = df["duration_seconds"].astype(int)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT, index=False)
