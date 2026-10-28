"""Download da planilha do Portal da Transparência com retry."""
import logging
from pathlib import Path

import config

log = logging.getLogger(__name__)


def baixar_planilha(destino: Path = config.OUTPUT_FILE) -> Path:
    """Baixa o Excel e sobrescreve `destino`. Aplica retry (MAX_TENTATIVAS x INTERVALO_RETRY_SEG).

    Raises:
        RuntimeError: se todas as tentativas falharem.
    """
    # TODO (próxima entrega): depende da pendência DOWNLOAD_URL
    raise NotImplementedError("Download ainda não implementado — definir DOWNLOAD_URL.")
