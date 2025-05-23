import struct
from datetime import timezone, datetime as dt
from loguru import logger
from typing import Optional

unix_epoch = dt.fromtimestamp(0, timezone.utc)
def unix_time_millis(dt: float) -> float:
    """formats timestamps as milliseconds-since-epoch (double-precision float, only requires 8 bytes)"""
    if dt.tzinfo is None:
        # make dt offset-aware in UTC if it's naive
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        # convert to UTC if it's aware in a different timezone
        dt = dt.astimezone(timezone.utc)
    return (dt - unix_epoch).total_seconds() * 1000.0


def safe_unwrap_exception(ex: Optional[Exception]) -> str:
    if ex is None:
        return "Unknown exception occurred."
    if hasattr(ex, 'message'):
        return ex.message
    return ex

