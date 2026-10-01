import click
from src.user_interface import main

@click.command()
@click.option('--drug_name', prompt='Drug Name', help='The name of the drug')
@click.option('--dosage', prompt='Dosage (mg)', type=int, help='Dosage in mg')
@click.option('--route', prompt='Route', help='Route of administration')
@click.option('--frequency', prompt='Frequency', help='Dosage frequency')
@click.option('--age_min', prompt='Age Min (months)', type=int, help='Minimum age for the drug')
@click.option('--age_max', prompt='Age Max (months)', type=int, help='Maximum age for the drug')
@click.option('--patient_age', prompt='Patient Age (months)', type=int, help='Patient age for dosage calculation')
def main(drug_name, dosage, route, frequency, age_min, age_max, patient_age):
    main()
