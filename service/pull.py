import streamlit as st
from utils.run import run_git_command

def run(project_dir):
    if st.button("🔄 Git Pull"):
        output = run_git_command("git pull", cwd=project_dir)
        st.code(output)
        if "Already up to date." in output:
            st.success("✅ Repository sudah up-to-date.")
        elif "Fast-forward" in output:
            st.success("✅ Berhasil melakukan fast-forward.")
        else:
            st.error("❌ Terjadi kesalahan saat melakukan pull.")