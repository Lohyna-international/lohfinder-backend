from settings import *
import os


def dummy_image_test():
    image_name = "dummy.png"
    text = "hello world"
    with open(image_name, "w") as file:
        file.write(text)

    result = re.post(
        f"{BACKEND_ADDRESS}/{API_PREFIX}/bin/", files={"file": open(image_name, "rb")}
    )
    assert result.status_code == 200, "Failed to upload file!"

    image = re.get(f"{BACKEND_ADDRESS}/{API_PREFIX}/bin/{image_name}")
    assert image.status_code == 200 and image.text == text, "Failed to download file!"


def clean_up():
    os.remove("dummy.png")


dummy_image_test()
clean_up()
