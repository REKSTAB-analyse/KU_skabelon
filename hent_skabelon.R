URL  <- paste0(base_url, "/ku_skabelon.tex")
DEST <- "ku_skabelon.tex"

if (file.exists(DEST)) {
  message("Bruger lokal kopi af ku_skabelon.tex")
} else {
  tryCatch(
    {
      download.file(URL, DEST, quiet = TRUE)
      message("ku_skabelon.tex hentet fra GitHub")
    },
    error = function(e) {
      stop("Ingen lokal kopi - og kan ikke hente fra GitHub: ", e$message)
    }
  )
}
