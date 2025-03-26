import logging


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
# logging.getLogger("telegram").setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
