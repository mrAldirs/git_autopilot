import streamlit as st
from utils.run import run_git_command

def run(project_dir):
    if st.button("📂 Git Status"):
        output = run_git_command("git status", cwd=project_dir)
        st.code(output)
        if "nothing to commit, working tree clean" in output:
            st.success("✅ Tidak ada perubahan yang perlu di-commit.")
        else:
            st.warning("⚠️ Ada perubahan yang belum di-commit.")