import os
import requests as re


def test_dummy_image(base_url, token):
    image_name = "dummy.png"
    text = "hello world"
    with open(image_name, "w") as file:
        file.write(text)

    result = re.post(
        f"{base_url}/bin/", files={"file": open(image_name, "rb")}, headers=token
    )
    assert result.status_code == 200

    image = re.get(f"{base_url}/bin/{image_name}")

    assert image.status_code == 200
    assert image.text == text
    os.remove("dummy.png")
