from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKITIO_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKITIO_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKITIO_URL_ENDPOINT")
)
