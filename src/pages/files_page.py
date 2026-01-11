from pathlib import Path

from pages.base_page import BasePage


class FilesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_input = self.test_id("file-input")
        self.upload_advance = self.test_id("upload-advance")
        self.download_csv = self.test_id("download-csv")
        self.download_pdf = self.test_id("download-pdf")
        self.download_retry = self.test_id("download-retry")

    def upload_file(self, file_path: Path) -> None:
        self.get(self.file_input).send_keys(str(file_path))

    def advance_upload(self) -> None:
        self.click(self.upload_advance)

    def download_csv_file(self) -> None:
        self.click(self.download_csv)

    def download_pdf_file(self) -> None:
        self.click(self.download_pdf)

    def retry_download(self) -> None:
        self.click(self.download_retry)
