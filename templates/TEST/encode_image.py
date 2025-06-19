from stegano import lsb  # Thư viện steganography
from PIL import Image  # Thư viện Pillow để xử lý ảnh

# Đường dẫn tới ảnh gốc
input_image_path = "TEST/hutech_logo.png"  # Đảm bảo đúng đường dẫn tới ảnh gốc

# Thông điệp cần giấu trong ảnh
secret_message = "ilovehutech"

# Mã hóa thông điệp vào ảnh
encoded_image = lsb.hide(input_image_path, secret_message)

# Lưu ảnh đã mã hóa vào thư mục TEST
encoded_image_path = "TEST/hutech_logo_encoded.png"
encoded_image.save(encoded_image_path)

print(f"Image with hidden message saved at {encoded_image_path}")
