# this tests the client input for valid sectors and malicious inputs
import pytest
from core.validation import validate_sector
from fastapi import HTTPException

def test_validate_sector_valid():
    assert validate_sector("technology") == "technology"
    assert validate_sector("Pharmaceuticals") == "pharmaceuticals"

def test_validate_sector_invalid():
    with pytest.raises(HTTPException):
        validate_sector("tech123")
    with pytest.raises(HTTPException):
        validate_sector("drop; table")