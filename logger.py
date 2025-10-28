import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path('Logs')
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "parser.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3, encoding='UTF-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
