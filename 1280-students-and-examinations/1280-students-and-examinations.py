import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations = examinations.rename(
        columns={"subject_name": "exam_subject"}
    )

    combined = students.merge(
        subjects,
        how="cross"
    )

    combined = combined.merge(
        examinations,
        left_on=["student_id", "subject_name"],
        right_on=["student_id", "exam_subject"],
        how="left"
    )

    result = (
        combined
        .groupby(
            ["student_id", "student_name", "subject_name"],
            as_index=False,
            dropna=False
        )
        .agg(
            attended_exams=("exam_subject", "count")
        )
    )

    result = result.sort_values(
        ["student_id", "subject_name"]
    )

    return result