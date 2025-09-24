import re
from fastapi import HTTPException

VALID_SECTOR_PATTERN = re.compile("^[a-zA-Z ]+$") 

def validate_sector(sector: str):
    if not VALID_SECTOR_PATTERN.match(sector):
        raise HTTPException(status_code=400, detail="Invalid sector name")
    return sector.lower()