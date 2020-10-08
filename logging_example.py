
import achaea.mud_logging
import achaea.inner_test
import logging

print(f"first_test.py __name__: {__name__}")
log = logging.getLogger("achaea")
log.says("peragus says hi")
log.fighting("vindiconis hits someone")
log.echo("Am I echoing in the main window?")
