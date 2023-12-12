from pdf2image import convert_from_path
import os

class PDFConverter:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def convert_pdfs_to_images(self):
        os.makedirs(self.output_folder, exist_ok=True)

        for file_name in os.listdir(self.input_folder):
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(self.input_folder, file_name)
                self._convert_pdf_to_images(pdf_path)

    def _convert_pdf_to_images(self, pdf_path):
        images = convert_from_path(pdf_path)

        for i, image in enumerate(images):
            image_path = os.path.join(self.output_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{i + 1}.png")
            image.save(image_path, "PNG")
