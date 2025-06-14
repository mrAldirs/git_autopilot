import streamlit as st
import os
from utils.run import run_git_command

def run(repo_path):
    repo_name = os.path.basename(repo_path.rstrip("/\\"))

    # === PILIH BRANCH ===
    branches = run_git_command("git branch", cwd=repo_path).splitlines()
    branches = [b.strip().replace("* ", "") for b in branches]
    selected_branch = st.selectbox("🌿 Pilih Branch:", branches, key=f"branch_{repo_name}")
    
    if selected_branch:
        # Checkout ke branch
        run_git_command(f"git checkout {selected_branch}", cwd=repo_path)

        # === STEP 1: ADD ===
        if st.button("➕ Git Add .", key=f"add_{repo_name}"):
            add_output = run_git_command("git add .", cwd=repo_path)
            st.success("✅ Git Add berhasil.")
            st.code(add_output, language="bash")

        # === STEP 2: COMMIT ===
        commit_msg = st.text_input("💬 Pesan Commit:", key=f"msg_{repo_name}")
        if st.button("✅ Git Commit", key=f"commit_{repo_name}"):
            if not commit_msg.strip():
                st.warning("Pesan commit tidak boleh kosong.")
            else:
                commit_output = run_git_command(f'git commit -m "{commit_msg}"', cwd=repo_path)
                st.success("✅ Git Commit berhasil.")
                st.code(commit_output)

        # === STEP 3: PUSH ===
        if st.button("🚀 Git Push", key=f"push_{repo_name}"):
            push_output = run_git_command("git push", cwd=repo_path)
            st.success("✅ Git Push berhasil.")
            st.code(push_output)
