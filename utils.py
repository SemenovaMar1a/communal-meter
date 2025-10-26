from datetime import date
import os

def write(line1, line2, line3, line4, line5):
    today = date.today()

    folder_path = os.path.join(
        str(today.year),
        f"{today.month:02d}",
        f"{today.day:02d}",
    )

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'log.txt')

    if not os.path.exists(file_path):
        flag = True
    else:
        flag = False

    with open(file_path, "w", encoding="utf-8") as file:
        if flag:
            file.write("Запись от " + str(today))
            file.write("\n" + line1)
            file.write("\n" + line2)
            file.write("\n" + line3)
            file.write("\n" + line4)
            file.write("\n" + line5)

        else:
            file.write("\nЗапись от " + str(today))
            file.write("\n" + line1)
            file.write("\n" + line2)
            file.write("\n" + line3)
            file.write("\n" + line4)
            file.write("\n" + line5)
        
    with open('показатели_счетчиков.txt', "a", encoding="utf-8") as file:
        if flag:
            file.write("Запись от " + str(today))
            file.write("\n" + line1)
            file.write("\n" + line2)
            file.write("\n" + line3)
            file.write("\n" + line4)
            file.write("\n" + line5)

        else:
            file.write("\nЗапись от " + str(today))
            file.write("\n" + line1)
            file.write("\n" + line2)
            file.write("\n" + line3)
            file.write("\n" + line4)
            file.write("\n" + line5)
            
    return True


def read():
    with open('показатели_счетчиков.txt', "r", encoding="utf-8") as file:
        nums = file.read().splitlines()
        return "\n".join(nums)


