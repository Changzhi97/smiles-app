import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
import matplotlib.pyplot as plt

st.title("SMILES Demo 🚀")

# 输入 SMILES
smiles = st.text_input("请输入一个 SMILES:")

if st.button("运行"):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            st.error("❌ 无法解析这个 SMILES，请检查输入")
        else:
            # ✅ 使用 rdMolDraw2D 输出 SVG（兼容无 GUI 环境）
            drawer = rdMolDraw2D.MolDraw2DSVG(300, 300)
            rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
            drawer.FinishDrawing()
            svg = drawer.GetDrawingText()
            st.write("### 分子结构")
            st.image(svg)

            # ✅ 使用 pandas 输出性质表
            df = pd.DataFrame({
                "SMILES": [smiles],
                "原子数": [mol.GetNumAtoms()],
                "键数": [mol.GetNumBonds()]
            })
            st.write("### 分子性质")
            st.dataframe(df)

            # ✅ 使用 matplotlib 画图
            fig, ax = plt.subplots()
            ax.bar(["原子数", "键数"], [mol.GetNumAtoms(), mol.GetNumBonds()])
            st.write("### 简单柱状图")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"运行出错: {e}")
