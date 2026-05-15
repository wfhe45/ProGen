import fitz
from PIL import Image, ImageChops
import os

Image.MAX_IMAGE_PIXELS = None

def crop_white_margins(image):
    bg = Image.new(image.mode, image.size, (255, 255, 255))
    diff = ImageChops.difference(image, bg)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)
    return image

def process_file(src_path, dest_path):
    print(f"Processing {src_path} -> {dest_path}")
    if src_path.lower().endswith('.pdf'):
        doc = fitz.open(src_path)
        page = doc[0]
        # Increase resolution for better quality
        zoom = 3  # zoom factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        doc.close()
    else:
        img = Image.open(src_path).convert("RGB")
    
    cropped_img = crop_white_margins(img)
    cropped_img.save(dest_path, "PNG")

source_dir = "/Users/Wenfeng/Desktop/npj/Figure"
dest_dir = "/Users/Wenfeng/Desktop/npj/academic_website_template/static/images"

files_to_process = [
    ("Figure1_3.pdf", "figure1_3.png"),
    ("Final_Overall_Segmentation_ABC.pdf", "figure2.png"),
    ("Figure3.pdf", "figure3.png"),
    ("Figure4.png", "figure4.png"),
    ("Figure5.pdf", "figure5.png"),
]

for src_name, dest_name in files_to_process:
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        process_file(src_path, dest_path)
    else:
        print(f"Source file not found: {src_path}")
