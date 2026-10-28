"""Configurações centrais do projeto (Fase 1 — Extração)."""
from pathlib import Path

# --- Caminhos ---
BASE_DIR: Path = Path(__file__).resolve().parent
LOG_DIR: Path = BASE_DIR / "logs"
LOG_FILE: Path = LOG_DIR / "extracao.log"

# PENDENTE: confirmar pasta definitiva em Documentos
DATA_DIR: Path = Path.home() / "Documents" / "gov-travel-insights"
OUTPUT_FILE: Path = DATA_DIR / "diarias_passagens.xlsx"  # sobrescrito a cada execução
STATE_FILE: Path = DATA_DIR / "ultima_execucao.json"     # nº de linhas da execução anterior

# --- Fonte ---
PORTAL_URL: str = "https://www.transparencia.sp.gov.br/home/diarias"
DOWNLOAD_URL: str | None = None  # PENDENTE: link/requisição real de download

# --- Rede / retry ---
MAX_TENTATIVAS: int = 3
INTERVALO_RETRY_SEG: int = 5 * 60
TIMEOUT_SEG: int = 120

# --- Logging ---
LOG_FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
LOG_LEVEL: str = "INFO"
