import os
import logging
from logging.handlers import RotatingFileHandler
import pytest

from app.core.logging import LOG_DIR, LOG_FILE, LOG_LEVEL


@pytest.fixture(autouse=True)
def reset_logger():
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, LOG_FILE), maxBytes=10485760, backupCount=3
    )
    console_handler = logging.StreamHandler()
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[file_handler, console_handler],
    )
    yield
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)


def test_log_directory_creation():
    assert os.path.exists(LOG_DIR), f"The directory {LOG_DIR} must exist"


def test_file_handler_configuration():
    logger = logging.getLogger()
    handlers = logger.handlers
    file_handler = next(
        (h for h in handlers if isinstance(h, RotatingFileHandler)), None
    )
    assert file_handler is not None, "There must be a file handler"
    assert file_handler.baseFilename.endswith(LOG_FILE), f"The log file must be {LOG_FILE}"
    assert file_handler.maxBytes == 10485760, "The maximum size must be 10 MB"
    assert file_handler.backupCount == 3, "It must keep up to 3 log backups"


def test_console_handler_configuration():
    logger = logging.getLogger()
    handlers = logger.handlers
    console_handler = next(
        (h for h in handlers if isinstance(h, logging.StreamHandler)), None
    )
    assert console_handler is not None, "There must be a console handler"


def test_logger_general_configuration():
    logger = logging.getLogger()
    assert logger.level == LOG_LEVEL, f"The logger level must be {LOG_LEVEL}"
    assert any(
        isinstance(h, RotatingFileHandler) for h in logger.handlers
    ), "There must be a configured RotatingFileHandler"
    assert any(
        isinstance(h, logging.StreamHandler) for h in logger.handlers
    ), "There must be a configured StreamHandler"
