#! python3
# -*- coding: utf-8 -*-

import logging

def get_logger(name="mylogger", debug=False, path=None):
    """
    Retourne un logger Python classique pour console.
    """
    level = logging.INFO
    if debug:
        level = logging.DEBUG
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Evite de créer plusieurs handlers si le logger est déjà configuré
    if not logger.hasHandlers():
        # Gestionnaire console
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # Gestionnaire fichier (si un chemin est fourni)
        if path:
            fh = logging.FileHandler(path, mode='a', encoding='utf-8')
            fh.setLevel(level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

    return logger
