from pathlib import Path

from pages.files_page import FilesPage


def test_files_upload_download(driver, base_url):
    driver.get(f"{base_url}/files")
    files = FilesPage(driver)
    sample = Path(__file__).resolve().parents[2] / "resources" / "sample.txt"
    files.upload_file(sample)
    files.advance_upload()
    files.download_csv_file()
    files.download_pdf_file()
    files.retry_download()
