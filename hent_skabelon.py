import os
import urllib.request

qmd_sti = os.environ.get("QUARTO_DOCUMENT_PATH")
if qmd_sti:
    skabelon_mappe = os.path.dirname(os.path.abspath(qmd_sti))
else:
    skabelon_mappe = os.getcwd()

URL = f"{base_url}/ku_skabelon.tex"
DEST = os.path.join(skabelon_mappe, "ku_skabelon.tex")

if os.path.exists(DEST):
    print("Bruger lokal kopi af ku_skabelon.tex")
else:
    try:
        urllib.request.urlretrieve(URL, DEST)
        print("ku_skabelon.tex hentet fra GitHub")
    except Exception as e:
        raise SystemExit(f"Ingen lokal kopi - og kan ikke hente fra GitHub: {e}")
