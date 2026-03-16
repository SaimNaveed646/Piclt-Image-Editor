from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# ==== COLLAGE FUNCTION ====
def create_collage(uploaded_files, layout, num_images):
    """
    Creates a collage image based on the number of images and selected layout.
    Handles rotation, borders, and smooth edges.
    Returns a PIL Image object.
    """

    # ==== STEP 1: Preprocess Images ====
    processed = []
    for f in uploaded_files:
        img = Image.open(f).convert("RGBA")
        img = img.resize((250, 250))
        img = ImageOps.expand(img, border=4, fill="#D3D3D3")  # black border
        processed.append(img)

    # ==== STEP 2: Smooth Rotation Helper ====
    def smooth_rotate(image, angle):
        """Rotate image with anti-aliasing and smooth alpha mask."""
        img = image.rotate(angle, resample=Image.BICUBIC, expand=True)
        mask = img.split()[-1].filter(ImageFilter.GaussianBlur(1.2))
        img.putalpha(mask)
        return img

    # ==== STEP 3: Collage Logic ====
    images = processed
    collage = None

    # 2 Images
    if num_images == 2:
        if layout == "Side by Side":
            collage = Image.new("RGB", (520, 260), (255, 255, 255))
            collage.paste(images[0], (10, 5))
            collage.paste(images[1], (260, 5))

        elif layout == "Top-Bottom":
            collage = Image.new("RGB", (260, 520), (255, 255, 255))
            collage.paste(images[0], (5, 10))
            collage.paste(images[1], (5, 260))

        elif layout == "Tilted Pair":
            collage = Image.new("RGBA", (600, 400), (255, 255, 255, 255))
            img1 = smooth_rotate(images[0], -10)
            img2 = smooth_rotate(images[1], 10)
            collage.paste(img1, (70, 80), img1)
            collage.paste(img2, (320, 100), img2)

    # 3 Images
    elif num_images == 3:
        if layout == "3 in a Row":
            collage = Image.new("RGB", (780, 270), (255, 255, 255))
            for i in range(3):
                collage.paste(images[i], (i * 260, 10))
        elif layout == "2 Top + 1 Bottom":
            collage = Image.new("RGB", (520, 520), (255, 255, 255))
            collage.paste(images[0], (10, 10))
            collage.paste(images[1], (260, 10))
            collage.paste(images[2], (130, 260))
        elif layout == "Cascade Tilt":
            collage = Image.new("RGBA", (800, 600), (255, 255, 255, 255))
            offsets = [(50, 50), (220, 150), (390, 250)]
            angles = [-8, 6, -10]
            for i in range(3):
                img = smooth_rotate(images[i], angles[i])
                collage.paste(img, offsets[i], img)

    # 4 Images
    elif num_images == 4:
        if layout == "2x2 Grid":
            collage = Image.new("RGB", (520, 520), (255, 255, 255))
            collage.paste(images[0], (10, 10))
            collage.paste(images[1], (260, 10))
            collage.paste(images[2], (10, 260))
            collage.paste(images[3], (260, 260))
        elif layout == "Cross Tilt":
            collage = Image.new("RGBA", (700, 600), (255, 255, 255, 255))
            positions = [(100, 50), (350, 100), (150, 330), (400, 360)]
            angles = [-15, 15, 10, -10]
            for i in range(4):
                img = smooth_rotate(images[i], angles[i])
                collage.paste(img, positions[i], img)

    # 5 Images
    elif num_images == 5:
        if layout == "2 Top + 3 Bottom":
            collage = Image.new("RGB", (780, 530), (255, 255, 255))
            for i in range(2):
                collage.paste(images[i], (i * 260, 10))
            for i in range(3):
                collage.paste(images[i + 2], (i * 260, 260))
        elif layout == "Tilted Fan":
            collage = Image.new("RGBA", (900, 700), (255, 255, 255, 255))
            base_x, base_y = 150, 100
            angles = [-20, -10, 0, 10, 20]
            for i, angle in enumerate(angles):
                img = smooth_rotate(images[i], angle)
                collage.paste(img, (base_x + i * 70, base_y + i * 30), img)

    # 6 Images
    elif num_images == 6:
        if layout == "3x2 Grid":
            collage = Image.new("RGB", (780, 530), (255, 255, 255))
            for i in range(3):
                collage.paste(images[i], (i * 260, 10))
            for i in range(3, 6):
                collage.paste(images[i], ((i - 3) * 260, 260))
        elif layout == "Diagonal Flow":
            collage = Image.new("RGBA", (900, 700), (255, 255, 255, 255))
            for i in range(6):
                img = smooth_rotate(images[i], i * 3 - 10)
                collage.paste(img, (i * 100, i * 70), img)

    # ==== STEP 4: Return Final Collage ====
    return collage
