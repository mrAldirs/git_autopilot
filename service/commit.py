import streamlit as st
from utils.run import run_git_command

def run(project_dir):
    commit_msg = st.text_input("💬 Masukkan pesan commit:")
    if st.button("✅ Git Commit"):
        if commit_msg.strip() == "":
            st.warning("Pesan commit tidak boleh kosong.")
        else:
            output = run_git_command(f'git commit -m "{commit_msg}"', cwd=project_dir)
            st.code(output)