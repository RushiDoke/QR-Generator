# QR-Generator

# Excel-to-Folder QR Code Generator 🚀

An automated Python script that parses Device IDs from an Excel spreadsheet and dynamically organizes the generated QR code images into a clean, nested directory structure.
## 🖼️ Generated Output Samples
<img width="290" height="290" alt="AR1211012006" src="https://github.com/user-attachments/assets/68148339-ca5a-4658-8d14-f864127ae7c3" />

## ⚙️ How it Works
1. **Excel Data Extraction**: The script reads device identification strings (such as `AR1211012006`) directly from columns inside your spreadsheet (`test.xlsx` / `test2.xlsx`).
2. **Dynamic Folder Tree Creation**: For every unique Device ID found, the script automatically establishes a dedicated subfolder within a master directory using the format:
   `QR Codes/` ➔ `[Device ID]/`
3. **Isolated QR Export**: It encodes the identifier into a high-resolution QR matrix image and saves it directly inside that specific device's folder using the matching ID as the file name:
   `QR Codes/[Device ID]/[Device ID].png`

## 📁 Visual Repository Tree
```text
QR Codes/               # Main Output Directory
├── AR1211012006/       # Dynamic Device Sub-folder
│   └── AR1211012006.png# Custom QR Code Image File
├── AR1211012007/       # Next Device Sub-folder
│   └── AR1211012007.png
├── AR1211012008/       # Next Device Sub-folder
│   └── AR1211012008.png
└── ...
```

## 🛠️ Requirements & Setup

This script requires Python 3 along with a couple of basic data parsing and automation packages. Install them via your terminal:

```bash
pip install qrcode pandas openpyxl
```

## 🚀 Usage Instructions

1. Place your target Excel sheet with the Device IDs directly into the root folder.
2. Run the processing script:
   ```bash
   python QR_Code_Generator.py
   ```
3. Open the newly generated **`QR Codes`** folder to view your organized asset directories.
