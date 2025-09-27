import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

st.title("SMILES Demo")

# 输入 SMILES
smiles = st.text_input("请输入一个 SMILES:")

if st.button("运行"):
    try:
        # ✅ 使用 RDKit
        mol = Chem.MolFromSmiles(smiles)
        img = Draw.MolToImage(mol, size=(200,200))
        st.image(img, caption="分子结构")

        # ✅ 使用 pandas
        df = pd.DataFrame({"SMILES": [smiles], "原子数": [mol.GetNumAtoms()]})
        st.dataframe(df)

        # ✅ 使用 matplotlib
        fig, ax = plt.subplots()
        ax.bar(["原子数"], [mol.GetNumAtoms()])
        st.pyplot(fig)

    except:
        st.error("SMILES 无效，请重新输入！")
