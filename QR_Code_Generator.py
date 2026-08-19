import pandas as pd
import qrcode
import os
from PIL import ImageDraw, ImageFont

def Qr_Report (excel_file, Column_name) : 
    data_file = pd.read_excel(excel_file)

    if Column_name not in data_file.columns:
        print(f"Error: column '{Column_name}' not in excel file ")

    flag = 0

    if os.path.exists("QR Codes"):
        pass
    else:
        os.mkdir("QR Codes")

    os.chdir("QR Codes")
    for val in data_file[Column_name]:

        device_id = str(val).strip()
        flag += 1
        temp_image = f"{device_id}.png"

        if os.path.exists(f"{device_id}.png"):
            print(f"Device already exists : {device_id}")
            continue
       
        if os.path.exists(f"{device_id}"):
            print(f" ! QR already generated of {device_id} ")
            pass

        else:
            os.mkdir(f"{device_id}")
            os.chdir(f"{device_id}")
            print(f"Generating Qr for Device {flag}: '{device_id}'")
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(device_id)
            qr.make(fit=True)
            pic = qr.make_image(fill_color="black", back_color="white").convert("RGB")

            fianl_img = ImageDraw.Draw(pic)

            fianl_img.text((70, 260), device_id, fill="black", font=ImageFont.truetype("arial.ttf", 20))
            pic.save(temp_image)

            os.chdir("C:\\Users\\sunsh\\Desktop\\Rushikesh\\python\\QR Codes")


Qr_Report(excel_file='C:\\Users\\sunsh\\Desktop\\Rushikesh\\QR code\\test2.xlsx', Column_name='Device ID')
