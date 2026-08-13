import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r"(^| )DIAB1"
    result = patients[
        patients["conditions"].str.contains(pattern, regex=True)
    ]
    return result