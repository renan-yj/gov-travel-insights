"""Ponto de entrada — executado pela tarefa agendada (dias úteis, 8:30)."""
import sys

from src.downloader import baixar_planilha
from src.logger import configurar_logging
from src.reporter import gerar_relatorio


def main() -> int:
    log = configurar_logging()
    log.info("Início da extração")
    try:
        arquivo = baixar_planilha()
        relatorio = gerar_relatorio(arquivo)
    except Exception as e:  # falha final após retries
        log.exception("Falha na extração")
        relatorio = gerar_relatorio(None, erro=str(e))
    log.info("Relatório: %s", relatorio)
    return 0 if relatorio.status == "SUCESSO" else 1


if __name__ == "__main__":
    sys.exit(main())
