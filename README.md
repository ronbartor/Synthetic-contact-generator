# Synthetic-contact-generator
Work related for generation of synthetic data for load, scale, and performance testing

Description:
This is a python utility that generates synthetic data files (CSV, txt) for use in scale and performance testing.
The contents of the results files are lists of contacts that include:
- First and last name
- Company name
- Postion in the company
- Address of the company
- Contact telephone number
- Contact email address

In the CSV files the the entries are tabulated as above.
In the TXT file they are complete contacts separated by a '\n'

Usage:
python main.py <number of entries required> <file format "csv" or "txt"> <number of entries per file>
  
Example: python main.py 1000000 "csv" 10000

This will generate 1000000 contacts in 100 CSV files each containing 10000 contacts
  
Note the _number of entries per file_ is used to ensure that the program does not generate massive files
  
  Performance:
  - On a Macbook Air (M1) generating 1,000,000 contacts takes just under 5 seconds
