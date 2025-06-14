import streamlit as st
from utils.run import run_git_command
import os

def run(project_dir):
    repo_name = os.path.basename(project_dir.rstrip("/\\"))
    if st.button("🌳 Git Branch", key=f"add_{repo_name}"):
        output = run_git_command("git branch", cwd=project_dir)
        st.code(output, language="bash")