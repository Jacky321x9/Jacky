import base64

# อ่านไฟล์ Python
with open("B.py", "rb") as f:
    file_content = f.read()

# เข้ารหัสเป็น Base64
encoded_content = base64.b64encode(file_content).decode('utf-8')

# แสดงผลหรือบันทึกเป็นไฟล์
print(encoded_content)

# ถ้าต้องการบันทึกผลเป็นไฟล์ Base64
with open("encoded_script.txt", "w") as f:
    f.write(encoded_content)