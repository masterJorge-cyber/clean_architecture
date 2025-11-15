# ----------------------------------------------------
# 1. Responsabilidade: Persistência de Dados
# Razão para mudar: Se mudarmos de salvar em arquivo para salvar em Banco de Dados.
# ----------------------------------------------------
class PirateRepository:
    """Gerencia a persistência (salvar e carregar) dos dados do pirata."""
    
    def __init__(self, filename: str):
        self._filename = filename
        
    def save_status(self, data: dict) -> None:
        """Simula o salvamento de dados em um arquivo."""
        print(f"⚓ REP: Salvando status de {data.get('name')} em {self._filename}")
        # Lógica real de IO, JSON ou DB estaria aqui.
        
    def load_status(self) -> dict:
        """Simula o carregamento de dados."""
        # Lógica real de carregamento estaria aqui.
        return {"name": "Monkey D. Luffy", "base_power": 500}

# ----------------------------------------------------
# 2. Responsabilidade: Lógica de Negócio/Cálculo de Status
# Razão para mudar: Se a fórmula para calcular o nível ou poder mudar.
# ----------------------------------------------------
class CombatStatsCalculator:
    """Calcula e mantém os status de combate do personagem."""
    
    def __init__(self, base_power: int, level: int = 1):
        self._base_power = base_power
        self._level = level
        
    def calculate_total_power(self) -> int:
        """Fórmula de cálculo de poder."""
        # A lógica de negócio está encapsulada aqui
        return self._base_power + (self._level * 10)
    
    def level_up(self, exp: int) -> None:
        """Aumenta o nível e notifica."""
        self._level += (exp // 100)
        print(f"⭐ STATS: Nível aumentado para {self._level}!")

# ----------------------------------------------------
# 3. Responsabilidade: Coordenação (A Classe Principal)
# Razão para mudar: Se mudarmos a forma como o Repositório e o Calculador interagem.
# ----------------------------------------------------
class PirateCaptain:
    """Coordena o uso das outras responsabilidades."""
    
    def __init__(self, name: str, stats_calculator: CombatStatsCalculator, repository: PirateRepository):
        # Encapsulamento de dados
        self.name = name
        
        # Injeção de Dependência (Recebe as responsabilidades)
        self._stats = stats_calculator
        self._repo = repository
        
    def check_power(self) -> None:
        """Mostra o poder total, delegando o cálculo."""
        power = self._stats.calculate_total_power()
        print(f"🏴‍☠️ {self.name}: Poder atual é {power}!")
        
    def save_game(self) -> None:
        """Salva o status atual, delegando ao Repositório."""
        data_to_save = {
            "name": self.name,
            "power": self._stats.calculate_total_power(),
            "level": self._stats._level
        }
        self._repo.save_status(data_to_save)

# --- Exemplo de Uso (main.py faria algo parecido) ---
if __name__ == '__main__':
    # 1. Instancie as classes de responsabilidade única
    repo = PirateRepository("luffy_data.db")
    stats = CombatStatsCalculator(base_power=400, level=10)
    
    # 2. Crie o Capitão, injetando as responsabilidades
    luffy = PirateCaptain("Monkey D. Luffy", stats, repo)
    
    print("\n--- AÇÃO 1: Nível Inicial ---")
    luffy.check_power()
    
    print("\n--- AÇÃO 2: Aumentando Nível ---")
    stats.level_up(250)
    luffy.check_power()
    
    print("\n--- AÇÃO 3: Salvamento ---")
    luffy.save_game()