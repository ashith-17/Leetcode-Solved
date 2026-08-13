import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0

    condition = (
        (employees["employee_id"] % 2 == 1)
        & (~employees["name"].str.startswith("M"))
    )

    employees.loc[condition, "bonus"] = employees.loc[condition, "salary"]

    result = employees[["employee_id", "bonus"]]
    result=result.sort_values(["employee_id"])
    return result