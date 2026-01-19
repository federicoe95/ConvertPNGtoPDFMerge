from typing import Optional
from PIL import Image
from PyPDF2 import PdfMerger
import os
from datetime import datetime

def get_filename_with_default(folder: str, default_name: str = None, extension: str = ".pdf") -> Optional[str]:
    """
    Chiede all'utente di inserire un nome file.
    Se l'utente preme INVIO, usa il default_name (se fornito).
    Controlla:
        - Non vuoto (se default non fornito)
        - Non contiene caratteri invalidi per Windows
        - Aggiunge estensione se mancante
        - Evita sovrascrittura
    Restituisce il path completo del file.
    """
    invalid_chars = r'<>:"/\\|?*'

    # Genera default se non passato
    if default_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_name = f"tutte_unite_{timestamp}.pdf"

    while True:
        name = input(f"Inserisci il nome del PDF finale, premio INVIO per accettare il nome seguente: [{default_name}]: ").strip()

        # Se l'utente preme INVIO, usa default
        if not name:
            name = default_name

        # Controllo caratteri invalidi
        if any(c in name for c in invalid_chars):
            print(f"❌ Il nome contiene caratteri non validi: {invalid_chars}")
            continue

        # Aggiunge estensione se manca
        if not name.lower().endswith(extension.lower()):
            name += extension

        full_path = os.path.join(folder, name)

        # Evita sovrascrittura
        if os.path.exists(full_path):
            print("❌ Un file con questo nome esiste già. Scegline un altro.")
            continue

        return full_path

# Chiedi il path della cartella contenente i PNG
png_dir = input("Inserisci il percorso della cartella con i file PNG: ").strip()

if not os.path.isdir(png_dir):
    raise ValueError("Il percorso inserito non è una cartella valida")

# Recupera tutti i PNG nella cartella
png_files = sorted(
    os.path.join(png_dir, f)
    for f in os.listdir(png_dir)
    if f.lower().endswith(".png")
)

if not png_files:
    raise ValueError("Nessun file PNG trovato nella cartella")

pdf_files = []

# 1) Converti PNG → PDF
for png in png_files:
    img = Image.open(png)
    out_pdf = os.path.splitext(png)[0] + ".pdf"
    img.convert("RGB").save(out_pdf)
    pdf_files.append(out_pdf)

# Chiedi il nome del file finale (con ciclo)
output_pdf = get_filename_with_default(png_dir)

# 2) Unisci i PDF
merger = PdfMerger()
for pdf in pdf_files:
    merger.append(pdf)

merger.write(output_pdf)
merger.close()

print(f"✅ Fatto! PDF creato in: {output_pdf}")
