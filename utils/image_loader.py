import base64


def get_base64_image(image_path: str) -> str:
    """
    Convert an image into a Base64 encoded string.

    Parameters
    ----------
    image_path : str
        Path of the image file.

    Returns
    -------
    str
        Base64 encoded image string.
    """

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def load_project_images():
    """
    Load all project images.

    Returns
    -------
    tuple
        (logo_base64, hero_base64)
    """

    logo_base64 = get_base64_image("assets/logo.png")
    hero_base64 = get_base64_image("assets/home_logo.png")

    return logo_base64, hero_base64