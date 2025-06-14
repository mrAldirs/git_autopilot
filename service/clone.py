# service/clone.py
import streamlit as st
import os
import subprocess
from utils.run import run_command_clone

def get_remote_branches(repo_url):
    try:
        output = subprocess.check_output(["git", "ls-remote", "--heads", repo_url], stderr=subprocess.STDOUT, text=True)
        branches = []
        for line in output.strip().splitlines():
            if "\trefs/heads/" in line:
                branch_name = line.split("\trefs/heads/")[1]
                branches.append(branch_name)
        return branches
    except subprocess.CalledProcessError:
        st.warning("Gagal mengambil daftar branch.")
        return []

def run(root_path):
    st.subheader("🔗 Clone Repository Baru")

    # Inisialisasi session_state kalau belum ada
    if "repo_checked" not in st.session_state:
        st.session_state.repo_checked = False
    if "repo_url" not in st.session_state:
        st.session_state.repo_url = ""
    if "branches" not in st.session_state:
        st.session_state.branches = []

    # Tahap 1: Form untuk cek repo
    with st.form("repo_form"):
        input_repo_url = st.text_input("🌐 Masukkan Git Remote URL", key="input_clone_repo_url")
        check_repo = st.form_submit_button("📥 Cek Repository")

        if check_repo:
            if not input_repo_url:
                st.warning("Mohon masukkan URL repository.")
            else:
                branches = get_remote_branches(input_repo_url)
                if not branches:
                    branches = ["main"]

                # Simpan ke session_state
                st.session_state.repo_checked = True
                st.session_state.repo_url = input_repo_url
                st.session_state.branches = branches

    # Tahap 2: Jika repo sudah dicek, tampilkan form clone
    if st.session_state.repo_checked:
        with st.form("clone_form"):
            clone_dir = st.text_input("📂 Nama Folder untuk Clone", key="clone_dir")
            selected_branch = st.selectbox("🌿 Pilih Branch:", st.session_state.branches, key="branch_select")
            submit_clone = st.form_submit_button("🚀 Jalankan Clone", type="primary")

            if submit_clone:
                if not clone_dir:
                    st.error("Nama folder harus diisi.")
                    return

                target_path = os.path.join(root_path, clone_dir)
                if os.path.exists(target_path):
                    st.error(f"Folder '{target_path}' sudah ada.")
                    return

                command = f"git clone {st.session_state.repo_url} {target_path} -b {selected_branch} --single-branch"
                result = run_command_clone(command, cwd=root_path)

                if isinstance(result, dict) and result.get("success"):
                    st.success(f"✅ Berhasil meng-clone ke {target_path}")
                    st.code(result["output"], language="bash")
                    # Reset state setelah berhasil
                    st.session_state.repo_checked = False
                else:
                    st.error(f"❌ Gagal clone:\n{result.get('error', result)}")
                st.session_state.repo_checked = False
                st.session_state.repo_url = ""
                st.session_state.branches = []
