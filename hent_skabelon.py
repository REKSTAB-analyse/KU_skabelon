import os
import urllib.request

# QUARTO_DOCUMENT_PATH er selve mappen med .qmd-filen (ikke filstien)
skabelon_mappe = os.path.abspath(
    os.environ.get("QUARTO_DOCUMENT_PATH") or os.getcwd()
)

FILER = ["ku_skabelon.tex", "KU_logo.png"]

for navn in FILER:
    dest = os.path.join(skabelon_mappe, navn)
    if os.path.exists(dest):
        print(f"Bruger lokal kopi af {navn}")
        continue
    tmp = dest + ".download"
    try:
        urllib.request.urlretrieve(f"{base_url}/{navn}", tmp)
        os.replace(tmp, dest)
        print(f"{navn} hentet fra GitHub")
    except Exception as e:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise SystemExit(
            f"Ingen lokal kopi af {navn} - og kan ikke hente fra GitHub: {e}"
        )
