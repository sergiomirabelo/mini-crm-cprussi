from pathlib import Path
import json, csv

class LeadRepository:
    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        self.db_path.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def create(self, lead_dict):
        leads = self._load()
        leads.append(lead_dict)
        self._save(leads)

    def read_all(self):
        return self._load()

    def export_csv(self):
        path_csv = self.data_dir / "leads.csv"
        leads = self._load()
        try:
            with path_csv.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "company", "email", "stage", "created"])
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead)
            return path_csv
        except PermissionError:
            return None
