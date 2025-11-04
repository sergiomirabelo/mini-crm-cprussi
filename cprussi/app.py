from model import Lead
from repo import LeadRepository
from stages import DEFAULT_STAGE

class MiniCRM:
    def __init__(self):
        self.repo = LeadRepository()

    def add_lead(self):
        name = input("Nome: ")
        company = input("Empresa: ")
        email = input("Email: ")

        lead = Lead(name, company, email, DEFAULT_STAGE)
        self.repo.create(lead.to_dict())

        print("Lead adicionado com sucesso!")

    def list_leads(self):
        leads = self.repo.read_all()
        if not leads:
            print("Nenhum lead cadastrado.")
            return

        print(f"\n## | {'Nome':<20} | {'Empresa':<20} | {'Email':<20}")
        for i, lead in enumerate(leads):
            print(f"{i:02d} | {lead['name']:<20} | {lead['company']:<20} | {lead['email']:<20}")

    def search_leads(self):
        user_filter = input("Busca por: ").strip().lower()
        if not user_filter:
            print("Consulta está vazia.")
            return

        leads = self.repo.read_all()
        results = [
            lead for lead in leads
            if user_filter in f"{lead['name']} {lead['company']} {lead['email']}".lower()
        ]

        if not results:
            print("Nenhum lead encontrado.")
            return

        print(f"\n## | {'Nome':<20} | {'Empresa':<20} | {'Email':<20}")
        for i, lead in enumerate(results):
            print(f"{i:02d} | {lead['name']:<20} | {lead['company']:<20} | {lead['email']:<20}")

    def export_leads(self):
        path_csv = self.repo.export_csv()
        if path_csv:
            print(f"Leads exportados como CSV para {path_csv}")
        else:
            print("Não foi possível exportar os leads. Tente novamente.")

    def run(self):
        while True:
            self.print_menu()
            op = input("Escolha: ")

            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")

    def print_menu(self):
        print("\nMini CRM de Leads - (Adicionar / Listar)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar leads por (nome/empresa/email)")
        print("[4] Exportar leads como CSV")
        print("[0] Sair")


if __name__ == "__main__":
    crm = MiniCRM()
    crm.run()
