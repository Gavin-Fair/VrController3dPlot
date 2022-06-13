import csv
import time
import triad_openvr


v = triad_openvr.triad_openvr()
namefile = 'FILENAME.csv'
header1 = "x1_value"
header2 = "y1_value"
header3 = "z1_value"
header4 = "x2_value"
header5 = "y2_value"
header6 = "z2_value"

x1_value = 0
y1_value = 0
z1_value = 0
x2_value = 0
y2_value = 0
z2_value = 0

fieldnames = [header1, header2, header3, header4, header5, header6]


with open(namefile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    c1 = ""
    c2 = ""
    for each in v.devices["controller_1"].get_pose_euler():
        c1 += "%.4f" % each
        c1 += " "

    for each in v.devices["controller_2"].get_pose_euler():
        c2 += "%.4f" % each
        c2 += " "
        
    with open(namefile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            header1: x1_value,
            header2: y1_value,
            header3: z1_value,
            header4: x2_value,
            header5: y2_value,
            header6: z2_value
        }

        csv_writer.writerow(info)
        print(f" Controller 1: X:{x1_value}| Y:{y1_value}| Z:{z1_value}\n"
              f"Controller 2: X:{x2_value}| Y:{y2_value}| Z:{z2_value}")

        x1_value = float("".join(str(integer) for integer in [c1[0:6]]))
        x1_value = x1_value * 100
        y1_value = float("".join(str(integer) for integer in [c1[7:13]]))
        y1_value = y1_value * 100
        z1_value = float("".join(str(integer) for integer in [c1[14:20]]))
        z1_value = z1_value * 100
        x2_value = float("".join(str(integer) for integer in [c2[0:6]]))
        x2_value = x2_value * 100
        y2_value = float("".join(str(integer) for integer in [c2[7:13]]))
        y2_value = y2_value * 100
        z2_value = float("".join(str(integer) for integer in [c2[14:20]]))
        z2_value = z2_value * 100
    time.sleep(1)
