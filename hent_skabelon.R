mappe <- Sys.getenv("QUARTO_DOCUMENT_PATH", unset = getwd())
skabelon <- if (exists("SKABELON")) SKABELON else "ku_skabelon.tex"

for (navn in c(skabelon, "KU_logo.png")) {
  dest <- file.path(mappe, navn)
  if (file.exists(dest)) {
    message("Bruger lokal kopi af ", navn)
  } else {
    tryCatch(
      {
        download.file(paste0(base_url, "/", navn), dest,
                      quiet = TRUE, mode = "wb")
        message(navn, " hentet fra GitHub")
      },
      error = function(e) {
        stop("Ingen lokal kopi af ", navn,
             " - og kan ikke hente fra GitHub: ", e$message)
      }
    )
  }
}
