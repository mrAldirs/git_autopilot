import streamlit as st
from utils.run import run_git_command

def run(project_dir):
    if st.button("📜 Git Log (last 5)"):
        output = run_git_command("git log -5 --oneline", cwd=project_dir)
        st.code(output)