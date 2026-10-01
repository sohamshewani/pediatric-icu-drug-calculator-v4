from typing import Optional
from src.drug_data import DrugData

from datetime import datetime
from typing import Optional
from src.drug_data import DrugData
from src.user_interface import show_error_message

from typing import List
from src.drug_data import DrugData

Interaction = List[DrugData]


def validate_drug_interaction(drug: DrugData, interacting_drug: DrugData) -> bool:
    # Example: Simple interaction validation logic
    return True
