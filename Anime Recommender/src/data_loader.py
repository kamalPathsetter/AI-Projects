import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8").dropna()
        required_columns = {
            "Name",
            "Genres",
            "sypnopsis"
        }
        
        missing_columns = required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(f"Missing columns: {missing_columns}")

        df["Combined Info"] = (
            "Title: " + df["Name"] + 
            "Genres: " + df["Genres"] + 
            "Overview: " + df["sypnopsis"]
        )

        df[["Combined Info"]].to_csv(self.processed_csv, index=False, encoding="utf-8")    

        return self.processed_csv
    