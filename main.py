import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader
import traceback
def safe_ocr(pdf_path, output_path="cao_output_text.txt", dpi=300):
    total_pages = len(PdfReader(pdf_path).pages)
    
    for page_num in range(1, total_pages + 1):
        try:
            print(f"[INFO] Processing page {page_num}/{total_pages}")
            images = convert_from_path(pdf_path, dpi=dpi, first_page=page_num, last_page=page_num)
            if not images:
                print(f"[WARN] No image returned for page {page_num}")
                continue
            
            image = images[0].convert("L")
            text = pytesseract.image_to_string(image, lang='eng')

            with open(output_path, "a", encoding="utf-8") as f:
                f.write(f"\n--- Page {page_num} ---\n{text}\n")

        except Exception as e:
            print(f"[ERROR] Failed on page {page_num}: {str(e)}")
            traceback.print_exc()
            continue 

    print(f"[✓] Extraction complete! Output in '{output_path}'")

if __name__ == "__main__":
    safe_ocr("CAO.pdf") 
