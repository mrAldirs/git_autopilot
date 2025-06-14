import streamlit as st
from utils.run import run_git_command

def run(project_dir):
    branch = st.text_input("🌿 Masukkan nama branch tujuan:")
    if st.button("🔀 Git Checkout"):
        if branch.strip() == "":
            st.warning("Branch tidak boleh kosong.")
        else:
            output = run_git_command(f"git checkout {branch}", cwd=project_dir)
            if "error" in output.lower():
                st.error(output)
            else:
                st.success(f"Berhasil checkout ke branch: {branch}")
                st.code(output)