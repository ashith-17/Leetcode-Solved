import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    red_companies = company[company["name"] == "RED"]

    red_orders = orders.merge(
        red_companies,
        on="com_id",
        how="inner"
    )

    red_sales_ids = red_orders["sales_id"].unique()

    result = sales_person[
        ~sales_person["sales_id"].isin(red_sales_ids)
    ]

    return result[["name"]]