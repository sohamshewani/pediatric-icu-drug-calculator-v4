# Design

## Overview

The Pediatric ICU Drug Calculator is designed with modularity and maintainability in mind. The system is divided into several components, each with a specific responsibility:

1. **Drug Data Management**: Handles drug data storage and retrieval.
2. **Dosage Calculation**: Calculates the appropriate dosage based on patient parameters.
3. **Interaction Validation**: Ensures that drug interactions are safe.
4. **User Interface**: Provides a user-friendly interface for input and output.

## Components

### Drug Data Management

- **DrugData Class**: Manages the storage and retrieval of drug data.
- **DrugData NamedTuple**: Defines the structure of drug data.

### Dosage Calculation

- **calculate_dosage Function**: Calculates the dosage based on the drug data and patient age.
- **validate_dosage Function**: Validates the interaction between the drug and any interacting drug.

### Interaction Validation

- **validate_drug_interaction Function**: Validates the interaction between two drugs.

### User Interface

- **main Function**: Provides a user-friendly interface for input and output.
