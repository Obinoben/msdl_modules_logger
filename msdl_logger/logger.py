#! python3
# -*- coding: utf-8 -*-

import logging

def get_logger(name="mylogger", debug=False):
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
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # Format classique : date, niveau, message
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
