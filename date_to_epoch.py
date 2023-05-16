from datetime import datetime

def date_to_epoch(date: datetime, ) -> int:
    """Convert python datetime to epoch"""
    return date.strftime("%s")

def str_to_epoch(date: str, ) -> int:
    """Convert python str (dd-mmm-yyyy) to epoch"""
    date = datetime.strptime(date, "%d-%b-%Y")
    return date.strftime("%s")
