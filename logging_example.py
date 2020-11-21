import logging

from achaea.another_logging_example import run_nothing
from achaea.mud_logging import initialize_logging

initialize_logging()

print(f"first_test.py __name__: {__name__}")
log = logging.getLogger("achaea")
log.says("peragus says hi")
log.fighting("vindiconis hits someone")
log.echo("Am I echoing in the main window?")
run_nothing()
