# DrugConditionExtraction

This script extracts drugs and clinical conditions described in the publication:
Toxicity of the Non-Steroidal Anti-Inﬂammatory Drugs (NSAIDs) acetylsalicylic acid, paracetamol, diclofenac, ibuprofen and naproxen towards freshwater invertebrates: A review
by Marco Parolini

## Steps:
1. Clone the project from GitHub
2. Create virtual environment if needed
3. Install packages listed in requirements.txt
   1. pip install -r requirements.txt
4. Download MESH RDF data from https://id.nlm.nih.gov/mesh/
5. Add MESH data to a repository in a triple store. I have used Ontotext Graph DB triple store. The public sparql endpoint has a limit of 1000 results.
   1. https://www.ontotext.com/products/graphdb/
   2. Name the repository 'mesh'
6. Run main.py. This will create the initial_drug_list.csv and initial_condition_list.csv files the data directory.
7. These files can be manually filtered to remove word_list terms in word_list_term column that don't correspond to the drugs or conditions