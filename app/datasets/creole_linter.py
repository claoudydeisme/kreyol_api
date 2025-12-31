import csv
from app.datasets.creole_enforcer import lint_creole_sentence


def lint_parallel_dataset(csv_path: str) -> list:
    issues = []

    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, start=2):
            if row["target_language"] == "ht":
                row_issues = lint_creole_sentence(
                    text=row["target"],
                    row_id=row["id"],
                    row_num=row_num
                )
                issues.extend(row_issues)

    return issues
