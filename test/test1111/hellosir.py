# Giữ lại các dòng chứa "Test" trong file văn bản

input_file = "@viettel.txt"     # đường dẫn file gốc
output_file = "Viettel.txt"   # file kết quả

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Lọc các dòng có chứa 'Viettel:'
filtered_lines = [line for line in lines if "@Viettel.vn:" in line]

# Ghi ra file mới
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print(f"Đã lọc xong. Kết quả được lưu vào: {output_file}")
