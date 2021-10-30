from ditto.core.base import BaseTool


class Spades(BaseTool):
    image = "staphb/spades:latest"
    prefix_cmd = "spades.py"
