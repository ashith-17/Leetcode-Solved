import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result=views[views["viewer_id"]==views["author_id"]]
    result=result[["author_id"]]
    result=result.drop_duplicates()
    result=result.rename(columns={"author_id":"id"})
    result=result.sort_values("id")
    return result