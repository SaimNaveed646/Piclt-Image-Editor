from streamlit_drawable_canvas import st_canvas
import streamlit as st
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont


# !!! No history saving from here, only edited image returns !!!
# !!! Save history using save_state() in main.py before calling these functions !!!
# ---------------------- Tool / Edit Functions ------------------------
def crop_image(img, left, top, right, bottom):
    """Crop and return image using given coordinates."""
    return img.crop((left, top, right, bottom))

# ------------------------------------------------------------------------

def rotate_image(img, angle):
    """Rotate image by given angle."""
    return img.rotate(angle, expand=True)

# ------------------------------------------------------------------------

def resize_image(img, width, height):
    """Resize image to new width & height."""
    return img.resize((width, height))

# ------------------------------------------------------------------------

def apply_filter(img, filter_type):
    """ Apply selected filter to the image and update st.session_state.uploaded_image.
        This function does NOT modify history """
    if img is None:
        return None

    original = img.copy()  # retain original image

    if filter_type == "BLUR":
        out = img.filter(ImageFilter.BLUR)
    elif filter_type == "GRAYSCALE":
        out = img.convert("L").convert("RGB")
    elif filter_type == "SEPIA":
        gray = img.convert("L")
        out = ImageOps.colorize(gray, "#704214", "#C0A080")
    elif filter_type == "CONTOUR":
        out = img.filter(ImageFilter.CONTOUR)
    elif filter_type == "EDGE_ENHANCE":
        out = img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == "SMOOTH":
        out = img.filter(ImageFilter.SMOOTH)
    elif filter_type == "EMBOSS":
        out = img.filter(ImageFilter.EMBOSS)
    else:
        out = img

    st.session_state.uploaded_image = out
    return out

# ------------------------------------------------------------------------

def add_text_to_image(img, text, position, font_size=40, color="white"):
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    draw.text(position, text, fill=color, font=font)
    return img_copy

# ------------------------------------------------------------------------

def draw_on_image(original_img, points, color="red", size=5):
    """
    Draw freehand lines on ORIGINAL image
    points: list of (x, y) coordinates
    """
    from PIL import ImageDraw
    img_copy = original_img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    # Draw lines between points
    if len(points) > 1:
        for i in range(len(points)-1):
            draw.line([points[i], points[i+1]], fill=color, width=size)
    
    return img_copy