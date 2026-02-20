import os
from PIL import Image, ImageOps
# Image processing
def mini_avatar(img):
    # image_pro_converter
    with Image.open(img) as file:
        return ImageOps.fit(file, (1024, 512), Image.Resampling.LANCZOS)

# One
def menu():

    while True:
        print("Start - 1\nExit - 0")
        start = input("Enter data:")
        if start == "1":
            path = input("Path to images:")
            output = input("Save path:")
            form = input("Сhange all format(No/Yes):")
            os.makedirs(output, exist_ok=True)
            if form.lower() == "yes":
                selected_format = input("Enter_format: ")
                for filename in os.listdir(path):
                    if filename.lower().endswith((".jpg", ".png", ".webp")):
                        file_path = os.path.join(path, filename)
                        try:
                            time = mini_avatar(file_path)
                            if form.lower() == "yes":
                                name = os.path.splitext(filename)[0]
                                filename = f"{name}_converted.{selected_format.lower().replace(".", "")}"
                            save_path = os.path.join(output, filename)
                            time.save(save_path)

                        except Exception as a:
                            print(f"Error {filename} - {a}")
                print(f"Pictures saved along the way:{output}")
            else:
                for filename in os.listdir(path):
                    if filename.lower().endswith((".jpg", ".png", ".webp")):
                        file_path = os.path.join(path, filename)
                        try:
                            time = mini_avatar(file_path)
                            save_path = os.path.join(output, filename)
                            time.save(save_path)
                        except Exception as a:
                            print(f"Error {filename} - {a}")
                print(f"Pictures saved along the way:{output}")


        elif start == "0":
            break


if __name__ == "__main__":
    menu()






