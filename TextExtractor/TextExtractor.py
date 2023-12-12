import os
import easyocr

class TextExtractor:
    def __init__(self, image_folder, output_folder):
        self.image_folder = image_folder
        self.output_folder = output_folder

    def extract_text_from_images(self):
        os.makedirs(self.output_folder, exist_ok=True)
        reader = easyocr.Reader(['pt'])

        for file_name in os.listdir(self.image_folder):
            if file_name.endswith((".png", ".jpg", ".jpeg")):
                image_path = os.path.join(self.image_folder, file_name)
                self._extract_text_from_image(reader, image_path)

    def _extract_text_from_image(self, reader, image_path):
        result = reader.readtext(image_path)
        sorted_result = sorted(result, key=lambda x: x[0][1])

        text_file_path = os.path.join(self.output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}.txt")
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(f"Text extracted from {os.path.basename(image_path)}:\n")
            for detection in sorted_result:
                text_file.write(str(detection) + "\n")
            text_file.write("=" * 50 + "\n")
