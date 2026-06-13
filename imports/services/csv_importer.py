import pandas as pd


class CSVImporter:
    def __init__(self):
        self.anomalies = []

    def import_file(self, file_path):
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            self.detect_anomalies(index + 1, row)

        return self.anomalies

    def detect_anomalies(self, row_number, row):
        if pd.isna(row.get("paid_by")):
            self.anomalies.append({
                "row": row_number,
                "issue": "Missing payer",
                "action": "Flagged for manual review"
            })

        if pd.isna(row.get("amount")):
            self.anomalies.append({
                "row": row_number,
                "issue": "Missing amount",
                "action": "Flagged for manual review"
            })