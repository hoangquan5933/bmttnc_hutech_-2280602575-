# caesar_cipher.py
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caeser import Ui_MainWindow          # ⚠️ Đảm bảo module tên “caeser” đúng; nếu bạn đặt “caesar” thì sửa lại.

API_BASE_URL = "http://127.0.0.1:5000/api/caesar"


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Khởi tạo giao diện
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện nút
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    # ----------------------------------------------------------------
    #                       HÀM GỌI API
    # ----------------------------------------------------------------
    def call_api_encrypt(self):
        """Gọi API mã hoá (encrypt)."""
        url = f"{API_BASE_URL}/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        self._call_api(
            url=url,
            payload=payload,
            result_field="encrypted_message",
            output_widget=self.ui.txt_cipher_text,
            success_msg="Encrypted Successfully"
        )

    def call_api_decrypt(self):
        """Gọi API giải mã (decrypt)."""
        url = f"{API_BASE_URL}/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        self._call_api(
            url=url,
            payload=payload,
            result_field="decrypted_message",
            output_widget=self.ui.txt_plain_text,
            success_msg="Decrypted Successfully"
        )

    # ----------------------------------------------------------------
    #                    HÀM HỖ TRỢ CHUNG CHO 2 API
    # ----------------------------------------------------------------
    def _call_api(self, *, url, payload, result_field, output_widget, success_msg):
        """Hàm gọi POST, xử lý trả về & hiển thị thông báo."""
        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                output_widget.setText(data.get(result_field, ""))

                QMessageBox.information(self, "Thông báo", success_msg)
            else:
                QMessageBox.warning(
                    self,
                    "Lỗi",
                    f"API trả về mã trạng thái {response.status_code}: {response.text}",
                )
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Không kết nối được API:\n{e}")

# --------------------------------------------------------------------
#                          CHẠY CHƯƠNG TRÌNH
# --------------------------------------------------------------------
if __name__ == "__main__":           # <-- 2 dấu gạch dưới ở hai bên
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
