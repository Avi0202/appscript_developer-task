#validates input for sector to prevent injection attacks and invalid inputs, list of sectors can be added here to make it more strict
import re
from fastapi import HTTPException

VALID_SECTOR_PATTERN = re.compile("^[a-zA-Z ]+$") 

def validate_sector(sector: str):
    if not VALID_SECTOR_PATTERN.match(sector):
        raise HTTPException(status_code=400, detail="Invalid sector name")
    return sector.lower()