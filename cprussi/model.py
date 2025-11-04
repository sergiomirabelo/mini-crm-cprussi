from datetime import date

class Lead:
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }

# Exemplo opcional de herança/polimorfismo
class VIPLead(Lead):
    def __init__(self, name, company, email, stage, vip_level="Gold"):
        super().__init__(name, company, email, stage)
        self.vip_level = vip_level

    def to_dict(self):
        lead_data = super().to_dict()
        lead_data["vip_level"] = self.vip_level
        return lead_data
