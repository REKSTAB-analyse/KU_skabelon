URL  <- "https://raw.githubusercontent.com/REKSTAB-analyse/KU_skabelon/main/ku_skabelon.tex"
DEST <- "ku_skabelon.tex"

tryCatch(
  download.file(URL, DEST, quiet = TRUE),
  error = function(e) {
    if (!file.exists(DEST))
      stop("✗ Kan ikke hente skabelon og ingen lokal kopi: ", e$message)
  }
)
