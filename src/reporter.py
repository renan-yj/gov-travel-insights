"""Métricas e relatório da execução."""
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Relatorio:
    status: str                 # "SUCESSO" | "FALHA"
    arquivo: str | None
    linhas: int | None
    tamanho_mb: float | None
    diff_linhas: int | None     # vs. execução anterior
    erro: str | None = None


def gerar_relatorio(arquivo: Path | None, erro: str | None = None) -> Relatorio:
    """Calcula métricas do arquivo baixado e compara com a execução anterior (STATE_FILE)."""
    # TODO (entrega futura)
    raise NotImplementedError
