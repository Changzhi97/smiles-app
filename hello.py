import streamlit as st
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem

smiles = st.text_input("请输入 SMILES:", "CCO")
mol = Chem.MolFromSmiles(smiles)
AllChem.EmbedMolecule(mol)

mblock = Chem.MolToMolBlock(mol)
view = py3Dmol.view(width=400, height=400)
view.addModel(mblock, "mol")
view.setStyle({"stick": {}})
view.zoomTo()
st.components.v1.html(view._make_html(), height=400)
