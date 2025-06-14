import streamlit as st
import os
from pathlib import Path

# Import modul layanan Git
from service import add, commit, push, pull, status, checkout, log, branch, clone
from utils.run import run_git_command

# Peta nama layanan ke modul
service_modules = {
    "Add": add,
    "Commit": commit,
    "Push": push,
    "Pull": pull,
    "Checkout": checkout,
    "Status": status,
    "Log": log,
    "Branch": branch,
    "Clone": clone,
}

def find_git_repos(root_path):
    """Scan semua subfolder dan return path yang punya .git"""
    repo_paths = []
    for subdir in Path(root_path).iterdir():
        if (subdir / ".git").exists() and subdir.is_dir():
            repo_paths.append(str(subdir))
    return repo_paths

# =========================
# UI AWAL
# =========================

st.set_page_config(page_title="Git Auto Pilot", layout="wide")
st.title("🧠 Git Auto-Pilot with Multi-Repo Detection")

root_path = st.text_input("📁 Masukkan path direktori ROOT:", value="C:/Home/Project/odoo18e/dev/modules")
service = st.selectbox("🛠️ Pilih layanan Git:", list(service_modules.keys()))

if not os.path.exists(root_path):
    st.warning("Folder tidak ditemukan.")
    st.stop()

# =========================
# KHUSUS CLONE
# =========================
if service == "Clone":
    clone.run(root_path)
    st.stop()


# =========================
# UNTUK LAYANAN SELAIN CLONE
# =========================

# Temukan semua repo Git di dalam folder root
found_repos = find_git_repos(root_path)
if not found_repos:
    st.info("Tidak ada Git repository ditemukan dalam folder ini.")
    st.stop()

# Tampilkan checkbox multi-pilih
selected_repos = st.multiselect("✅ Pilih repositori yang ingin diproses:", found_repos)

# Jalankan layanan untuk tiap repo yang dipilih
if selected_repos:
    for repo_path in selected_repos:
        repo_name = os.path.basename(repo_path)
        with st.expander(f"📂 {repo_name}", expanded=False):
            service_modules[service].run(repo_path)
else:
    st.warning("Silakan pilih minimal satu repo.")
