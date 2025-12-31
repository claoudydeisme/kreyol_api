import csv
from pathlib import Path
from typing import List, Dict
from app.datasets.creole_enforcer import lint_creole_sentence

class DatasetLoadError(Exception):
    pass

class ParallelDataset:
    def __init__(self, path: str):
        base_dir = Path(__file__).resolve().parents[2]
        self.path = base_dir / path
        self.pairs = []

    def load(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f"Dataset not found: {self.path}")

        self.pairs.clear()
        lint_issues = []

        with self.path.open("r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            #print("CSV HEADERS:", reader.fieldnames)
            #print("DATASET INSTANCE ID (load):", id(self))


            required_fields = {
                "id",
                "source_language",
                "target_language",
                "source",
                "target",
                "domain"
            }

            if not required_fields.issubset(reader.fieldnames or []):
                raise ValueError(
                    f"CSV must contain columns: {required_fields}"
                )

            for row_num, row in enumerate(reader, start=2):
                #print("ROW RAW:", row)
                self._validate_row(row, row_num)
                # append the row so they can be read
                self.pairs.append(row)
                # 🔒 Creole linting enforced at load-time
                if row["target_language"] == "ht":
                    issues = lint_creole_sentence(
                        text=row["target"],
                        row_id=row.get("id", "unknown"),
                        row_num=row_num
                    )
                    lint_issues.extend(issues)
            # 🚨 Block dataset if CRITICAL issues exist
        #critical = [i for i in lint_issues if i["severity"] == "CRITICAL"]
        #if critical:
            #raise DatasetLoadError(
                #f"Dataset blocked: {len(critical)} CRITICAL Creole violations"
            #)

        # ⚠️ Log non-blocking issues
        for issue in lint_issues:
            if issue["severity"] in ("WARNING", "ERROR"):
                print(
                    f"[{issue['severity']}] "
                    f"Row {issue['row']} ({issue['code']}): {issue['message']}"
                )

                self.pairs.append(row)

    def _validate_row(self, row: Dict, row_num: int) -> None:
        if row["source_language"] == row["target_language"]:
            raise ValueError(
                f"Row {row_num}: source_language == target_language"
            )

        if not row["source"].strip() or not row["target"].strip():
            raise ValueError(
                f"Row {row_num}: empty source or target"
            )

    def get_all(self) -> List[Dict]:
        return self.pairs

    def filter(
        self,
        source_language: str | None = None,
        target_language: str | None = None,
        domain: str | None = None,
    ) -> List[Dict]:
        results = self.pairs

        if source_language:
            results = [p for p in results if p["source_language"] == source_language]
        if target_language:
            results = [p for p in results if p["target_language"] == target_language]
        if domain:
            results = [p for p in results if p["domain"] == domain]

        return results
