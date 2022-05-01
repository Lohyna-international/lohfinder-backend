from settings import *

def dummy_image_test():
    image_name = "dummy.png"
    result = re.post(f"{BACKEND_ADDRESS}/{API_PREFIX}/bin/{image_name}", files={'file' : b'Hello world'})
    print(result)

dummy_image_test()
