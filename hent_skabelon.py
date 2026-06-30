import os
import urllib.request

URL = f"{base_url}/ku_skabelon.tex"
DEST = "ku_skabelon.tex"

if os.path.exists(DEST):
    print("Bruger lokal kopi af ku_skabelon.tex")
else:
    try:
        urllib.request.urlretrieve(URL, DEST)
        print("ku_skabelon.tex hentet fra GitHub")
    except Exception as e:
        raise SystemExit(f"Ingen lokal kopi - og kan ikke hente fra GitHub: {e}")
