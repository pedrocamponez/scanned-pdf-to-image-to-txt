from DataChecker.DataChecker import DataChecker
from PDFConverter.PDFConverter import PDFConverter
from TextExtractor.TextExtractor import TextExtractor

excel_file = "your_data.xlsx"
pdf_input_folder = "folder_containing_pdfs"
pdf_output_folder = "folder_where_images_will_go"
txt_output_folder = "folder_where_txt_files_will_go"

pdf_converter = PDFConverter(pdf_input_folder, pdf_output_folder)
text_extractor = TextExtractor(pdf_output_folder, txt_output_folder)
data_checker = DataChecker(excel_file, txt_output_folder, "path/to/your/output_folder")

pdf_converter.convert_pdfs_to_images()
text_extractor.extract_text_from_images()
data_checker.check_data()
