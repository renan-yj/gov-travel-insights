"""Configuração de logging (arquivo + console)."""
import logging

import config


def configurar_logging() -> logging.Logger:
    """Configura o logger raiz e retorna o logger do projeto."""
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(config.LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger("gov_travel")
