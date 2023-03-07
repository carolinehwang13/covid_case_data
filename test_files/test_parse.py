import pytest
from main import Parser

def test_parse_md_simple():
    p = Parser("/Users/carolineh/Desktop/cs_general/gao_pres/maryland_simple.csv")
    p.write_csv()
    assert 1 == 1