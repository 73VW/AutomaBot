"""AutomaBot package."""

import sys


if sys.version_info < (3, 6):
    raise ImportError("automabot requires Python 3.6+ because f-str/asyncio. "
                      "<3")
