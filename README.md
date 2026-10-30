# KU_skabelon

LateX-skabeloner til Quarto, der matcher KU's Word-formater. De bruges i REKSTAB Analyse til sagsnotater og rapporter. 

| Skabelon | Fil | Bruges til |
|---|---|---|
| Sagsnotat | 'ku_skabelon.tex' | Sagsnotater, indstillinger, notater |
| Rapport | 'ku_rapportskabelon.tex' | Rapporter med forside og indhold |

'KU_logo.png' (KU-seglet) bruges af begge skabeloner.

## Krav 

- Quarto med LuaLaTeX (f.eks. via TinyTex)
- Skrifttyperne Times New Roman og Arial skal være installerede
- Python (eller R) til hentescriptet

## Kom i gang

Opret en tom '.qmd'-fil i en mappe. Skabelonen og logoet hentes automatisk fra GitHub, første gang dokumentet renderes. 

### Sagsnotat

```yaml
---
titel: "Titel på notatet"
sagsbehandler: "Fornavn Efternavn"
email: "xxx@xxx.ku.dk"
koncern: "Rektoratets Stab"
enhed: "REKSTAB Analyse"
telefon: 12 34 56 78        # valgfri
modtager: "Modtager"        # valgfri
dokumenttype: "SAGSNOTAT"   # valgfri
format:
  pdf:
    template: "ku_skabelon.tex"
    latex_engine: lualatex
---
```
Sæt `SKABELON = "ku_skabelon.tex"` i hentechunket (se nedenfor).


### Rapport
```yaml
---
title: "Rapportens titel"   # OBS: title, ikke titel
undertitel: "Undertitel"    # valgfri
dato: "Oktober 2026"        # valgfri, ellers dagens dato
afsender: "..."             # valgfri, standard: Rektoratets Stab · REKSTAB Analyse
forsidebillede: "fig.png"   # valgfri
format:
  pdf:
    template: "ku_rapportskabelon.tex"
    latex_engine: lualatex
    toc: true               # indholdsfortegnelse (side 2)
---
```

Sæt `SKABELON = "ku_rapportskabelon.tex"` i hentechunket (se nedenfor).

- '#', '##' og '###' giver overskrift 1, 2 og 3. Alle kommer med i indholdet.
- Overskrifterne er ikke nummererede, jf. Word-skabelonen. Nummerering skås til med `\setcounter{secnumdepth}{3}` i skabelonen.
- '####' findes ikke i Word-skabelonen og har derfor ikke et særligt format.

## Hentechunket

Øverst i '.qmd'-filen lige efter YAML: 

```
#| include: false
import urllib.request

SKABELON = "ku_skabelon.tex"   # eller "ku_rapportskabelon.tex"
BRANCH = "main"                # "dev" hvis I tester
base_url = f"https://raw.githubusercontent.com/REKSTAB-analyse/KU_skabelon/{BRANCH}"
exec(urllib.request.urlopen(f"{base_url}/hent_skabelon.py").read())
```

- Findes skabelonen og logoet allerede i mappen, bruges de lokale kopier.
- Slet filerne for at hente den seneste version af skabelonen.
- GitHub cacher filer i op til 5 minutter efter en ændring.

## Vedligeholdelse

1. Ret i branchen 'dev' og test med `BRANCH = "dev"` i hentechunket.
2. Når rettelserne virker, merges 'dev' til 'main'.
3. Brugerne henter fra 'main'.
