# PharmacoElixir
## Generating Molecular Alternatives For Life Sciences
The goal is to ease the phase of pre-clinical tasks by building a machine learning model that generates structurally valid molecules using SMILES representation of the molecules.
Focus is on a class of enzymes known as tyrosine kinase, that can transfer a phosphate group from ATP (Adenosine triphosphate) to the tyrosine residues of specific proteins inside a cell; specifically

EGFR - Epidermal Growth Factor Receptor
VEGFR1 - Vascular Endothelial Growth Factor Receptor 1
VEGFR2 - Vascular Endothelial Growth Factor Receptor 2
HGFR - Hepatocyte Growth Factor Receptor

## Modules Needed
rdkit
tensorflow-gpu
numpy 
pickle
ddc-pub : https://github.com/pcko1/Deep-Drug-Coder.git
molVecGen : git+https://github.com/EBjerrum/molvecgen.git
DeepPurpose : https://github.com/kexinhuang12345/DeepPurpose.git

## Files Present
Capstone.ipynb : Complete code to generate valid molecules that bind with the target protein
smiles_dataset : Dataset that consists of 71 SMILES structure which bind with one or more of the target proteins 

