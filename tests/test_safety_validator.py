import pytest
from src.safety_validator import validate_drug_interaction
from src.drug_data import DrugData

@pytest.fixture
def drug_data():
    return DrugData(
        drug_name='Amoxicillin',
        dosage=125,  # mg
        route='Oral',
        frequency='8h',
        age_min=2,  # months
        age_max=12  # months
    )

def test_validate_drug_interaction(drug_data):
    interacting_drug = DrugData(
        drug_name='Paracetamol',
        dosage=15,  # mg
        route='Oral',
        frequency='4h',
        age_min=2,  # months
        age_max=12  # months
    )
    assert validate_drug_interaction(drug_data, interacting_drug) is True
