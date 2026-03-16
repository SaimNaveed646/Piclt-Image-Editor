import streamlit as st
from PIL import Image, ImageEnhance

# ------------------------ Adjustment Functions ------------------------

def apply_brightness(image):
    # Create a slider to let user choose brightness level (0 = dark, 1 = Normal, 2 = bright)
    # Default value is 1.0 (original image)
    value = st.slider("Brightness", 0.0, 2.0, 1.0, 0.01)

    # Create a Brightness enhancer object using PIL
    enhancer = ImageEnhance.Brightness(image)

    # Apply the enhancement with the chosen value
    image = enhancer.enhance(value)

    # Return the adjusted image
    return image


def apply_contrast(image):
    # Slider to control contrast level (0 = gray image, 2 = very high contrast)
    value = st.slider("Contrast", 0.0, 2.0, 1.0, 0.01)

    # Create Contrast enhancer object
    enhancer = ImageEnhance.Contrast(image)

    # Apply the enhancement with the chosen value
    image = enhancer.enhance(value)

    # Return final adjusted image
    return image


def apply_saturation(image):
    # Slider for saturation (0 = black & white, 2 = highly colorful)
    value = st.slider("Saturation", 0.0, 2.0, 1.0, 0.01)

    # Create Color enhancer (PIL calls it "Color" instead of "Saturation")
    enhancer = ImageEnhance.Color(image)

    # Apply enhancement
    image = enhancer.enhance(value)

    # Return the adjusted image
    return image


def apply_fade(image):
    # Slider for fade (0 = original image, 1 = completely white)
    value = st.slider("Fade", 0.0, 1.0, 0.0, 0.01)

    # Create a plain white image of same size to blend with
    faded = Image.new("RGB", image.size, (255, 255, 255))

    # Blend the image with white color depending on slider value
    image = Image.blend(image, faded, value)

    # Return the faded image
    return image


def apply_sharpness(image):
    # Slider for sharpness (0 = blurry, 2 = very sharp)
    value = st.slider("Sharpness", 0.0, 2.0, 1.0, 0.01)

    # Create a Sharpness enhancer
    enhancer = ImageEnhance.Sharpness(image)

    # Apply enhancement
    image = enhancer.enhance(value)

    # Return adjusted image
    return image
