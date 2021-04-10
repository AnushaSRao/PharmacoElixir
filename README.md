# PharmacoElixir
## Generating Molecular Alternatives For Life Sciences
The goal is to ease the phase of pre-clinical tasks by building a machine learning model that generates structurally valid molecules using SMILES representation of the molecules.<br>
Focus is on a class of enzymes known as tyrosine kinase, that can transfer a phosphate group from ATP (Adenosine triphosphate) to the tyrosine residues of specific proteins inside a cell; specifically

EGFR - Epidermal Growth Factor Receptor <br>
VEGFR1 - Vascular Endothelial Growth Factor Receptor 1 <br>
VEGFR2 - Vascular Endothelial Growth Factor Receptor 2 <br>
HGFR - Hepatocyte Growth Factor Receptor <br>

## Modules Needed
rdkit <br>
tensorflow-gpu <br>
numpy <br>
pickle <br>
ddc-pub : https://github.com/pcko1/Deep-Drug-Coder.git <br>
molVecGen : git+https://github.com/EBjerrum/molvecgen.git <br>
DeepPurpose : https://github.com/kexinhuang12345/DeepPurpose.git <br> 

## Files Present
Code.ipynb : Complete code to generate valid molecules that bind with the target protein <br>
smiles_dataset.smi : Dataset that consists of 71 SMILES structure which bind with one or more of the target proteins <br>
ProteinBindig.py: Code to find the drug target interaction score <br>

## Run Instructions
1.Run ProteinBinding.py on your local machine <br>
This exposes a public API that needs to be used as the URL to find the Drug Target Interaction score.<br>
2.Run the ipynb notebook using GPU either on colab or on your local machine <br>
Please note the project needs GPU and will not work as expected without the same <br>

