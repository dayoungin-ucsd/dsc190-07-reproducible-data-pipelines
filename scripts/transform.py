import pandas as pd
from pathlib import Path

INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")

df = pd.read_csv(INPUT)

df["date"] = pd.to_datetime(
    df["timestamp"]
).dt.strftime("%Y-%m-%d")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT, index=False)