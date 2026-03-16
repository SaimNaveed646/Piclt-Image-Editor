import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image
import io

# Import functions from external file
from assets.functions.edit import *
from assets.functions.adjust import *
from assets.functions.collage import *
from assets.functions.helper import *

# -------------------------------------------------------------------------------------------------------------

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="PicIt - Image Editor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize app state for pages navigation
if "page" not in st.session_state:
    st.session_state.page = "home"
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# Navigation functions to move between pages
def go_to_home():
    st.session_state.page = "home"
def go_to_edit():
    st.session_state.page = "edit"
def go_to_collage():
    st.session_state.page = "collage"

# Background Image
def add_bg_image(image_path: str):
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_image('assets/images/bg1.jpeg')


# -------------------------------------------------------------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------------------------------------------------------------

if st.session_state.page == "home":
    # UI Interface
    # Headers
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif:wght@400;700;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Tektur:wght@400;600&display=swap');

        /* Header */
        header[data-testid="stHeader"] {
            background-color: #D3D3D3;
            color: #000000;
            height: 80px;
            font-weight: 800;
            font-size: 22px;
            padding: 8px 25px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: 0 1px 6px rgba(0,0,0,0.1);
        }
        header[data-testid="stHeader"]::before {
            content: "PicIt - Image Editor";
            margin-left: 35px;
            color: #000000;
        }

        /* App Background */
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        section[data-testid="stSidebar"] {
            background-color: #F5F5F5;
            color: #000000;
        }

        header[data-testid="stHeader"] + div [data-testid="block-container"] {
            padding-top: 180px !important;
        }

        /* Remove Streamlit’s default white block container */
        div[data-testid="stVerticalBlock"] > div:first-child {
            background-color: #FFFFFF !important;
        }
        </style>
    """, unsafe_allow_html=True)

    hero_html = """
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif:wght@400;700;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Tektur:wght@400;600&display=swap');
        body {
          margin: 0;
          padding: 0;
          background: transparent;
          color: #000000;
        }
        .hero-wrap {
          padding: 0 40px;
          box-sizing: border-box;
          width: 100%;
        }
        .main-title {
            font-family: 'Noto Serif', serif;
            font-size: 84px;
            font-weight: 900;
            color: #000000;
            letter-spacing: 2px;
            margin: 0;
            text-align: left;
        }
        .sub-title {
            font-family: 'Noto Serif', serif;
            font-size: 38px;
            font-weight: 700;
            color: #000000;
            margin: 6px 0 18px 0;
            text-align: left;
        }
        .slogan {
            font-family: 'Tektur', sans-serif;
            font-size: 24px;
            font-weight: 400;
            color: #444444;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid #444444;
            display: inline-block;
            min-height: 1.2em;
            margin-top: 10px;
        }
        @keyframes blink {
          50% { border-color: transparent; }
        }
        .cursor-blink {
          animation: blink 0.7s step-end infinite;
        }
        @media (min-width: 1000px) {
          .hero-wrap {
            padding-left: 60px;
          }
        }
      </style>
    </head>
    <body>
      <div class="hero-wrap" id="hero">
        <h1 class="main-title">PicIt</h1>
        <h2 class="sub-title">Image Editor</h2>
        <div>
          <span id="slogan" class="slogan"></span>
        </div>
      </div>
      <script>
        const slogans = [
          "Edit Images On The Go!",
          "Create Collages Quickly!",
          "Enhance Photos Instantly!",
          "Redesign Your Pictures Easily!"
        ];
        const typingSpeed = 100;
        const erasingSpeed = 50;
        const delayAfterTyped = 1200;
        let sloganIndex = 0;
        let charIndex = 0;
        const sloganEl = document.getElementById('slogan');
        function setCursorActive(active) {
          if (active) sloganEl.classList.add('cursor-blink');
          else sloganEl.classList.remove('cursor-blink');
        }
        function typeStep() {
          const text = slogans[sloganIndex];
          if (charIndex < text.length) {
            sloganEl.textContent = text.substring(0, charIndex + 1);
            charIndex++;
            setTimeout(typeStep, typingSpeed);
          } else {
            setCursorActive(false);
            setTimeout(() => {
              setCursorActive(true);
              setTimeout(eraseStep, 50);
            }, delayAfterTyped);
          }
        }
        function eraseStep() {
          if (charIndex > 0) {
            sloganEl.textContent = slogans[sloganIndex].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(eraseStep, erasingSpeed);
          } else {
            sloganIndex = (sloganIndex + 1) % slogans.length;
            setTimeout(typeStep, 120);
          }
        }
        document.addEventListener('DOMContentLoaded', function() {
          setCursorActive(true);
          setTimeout(typeStep, 300);
        });
      </script>
    </body>
    </html>
    """
    components.html(hero_html, height=240, scrolling=False)

    # Sidebar
    st.sidebar.header("Tutorial")
    with st.sidebar.expander("Read Tutorial", expanded=False):
        st.write("""1. Picture Editing:
Upload a single image and then click 'Proceed to Edit'.
Use different editing tools and adjust image properties according to your requirements.
After editing, you can download the image.

2. Collage Creation:
Upload multiple images for collage creation and then select a desired
layout to apply on your images. Click 'Proceed to Collage' to view your collage
and decide whether to download it or not.""")

    # Upload Section
    st.markdown("<div style='height:45px'></div>", unsafe_allow_html=True)
    st.write("### Upload Your Image To Get Started!")

    with st.expander("Upload Image", expanded=False):
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)  # PIL Type Image
            st.image(uploaded_image, caption='Uploaded Image', width=300)
            if st.button("Proceed to Edit >>"):                
                # To maintain image history/states for reset/undo
                st.session_state.original_image = image.copy()  # Original copy
                st.session_state.uploaded_image = image.copy()  # Editing copy
                st.session_state.history = []  # History of edits
                go_to_edit()  # Go to edit page
        else:
            st.warning("Please upload an image to proceed.")

    # Vertical Space
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    # Collage Option
    st.write("### or Create A Collage!")
    with st.expander("Upload Multiple Images", expanded=False):
        uploaded_files = st.file_uploader(
            "Choose images...", 
            type=["jpg", "jpeg", "png"], 
            accept_multiple_files=True
        )
        if uploaded_files and 1 < len(uploaded_files) <= 6:
            i = 0
            cols = st.columns(len(uploaded_files))
            for uploaded_file in uploaded_files:
                cols[i].image(uploaded_file, caption=f'Image {i+1}', width=180)  # One row display
                i += 1 
                                
            st.write(f"Total images uploaded: {len(uploaded_files)}")

            # Layout selection
            layout_options = {
              2: ["Side by Side", "Top-Bottom", "Tilted Pair"],
              3: ["3 in a Row", "2 Top + 1 Bottom", "Cascade Tilt"],
              4: ["2x2 Grid", "Cross Tilt"],
              5: ["2 Top + 3 Bottom", "Tilted Fan"],
              6: ["3x2 Grid", "Diagonal Flow"]
              }

            layout = st.selectbox(" Choose Layout", layout_options[len(uploaded_files)])

            if st.button("Proceed to Collage >>"):
              st.session_state.uploaded_images = uploaded_files # Uploaded images
              st.session_state.selected_layout = layout # Selected layout as argument
              go_to_collage()   # Call function now

        elif uploaded_files and len(uploaded_files) == 1:
            st.warning("Please upload at least two images to create a collage.")
        else:
            st.warning("You can upload up to 2–6 images for a collage.")


# -------------------------------------------------------------------------------------------------------------
# EDITING PAGE
# -------------------------------------------------------------------------------------------------------------


elif st.session_state.page == "edit":
    # Header Bar
    st.markdown("""
        <style>
        header[data-testid="stHeader"] {
            background-color: #D3D3D3;
            color: #000000;
            height: 80px;
            font-weight: 800;
            font-size: 22px;
            padding: 8px 25px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: 0 1px 6px rgba(0,0,0,0.1);
        }
        header[data-testid="stHeader"]::before {
            content: "PicIt - Image Editor";
            margin-left: 35px;
            color: #000000;
        }
        header[data-testid="stHeader"] + div [data-testid="block-container"] {
            padding-top: 180px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize tool and adjustment states
    if "selected" not in st.session_state:
      st.session_state.selected = "None"
    if "last_trigger" not in st.session_state:
      st.session_state.last_trigger = None


    # ------ Sidebar (Editing Page)-------
    # Sidebar Selections
    st.sidebar.header("Tools & Adjustments")
    tools = ["None", "Crop", "Rotate/Resize", "Filter", "Text", "Draw"]
    adjusts = ["None", "Brightness", "Contrast", "Saturation", "Fade", "Sharpness"]

    def sidebar_tool_change():
      st.session_state.selected = st.session_state.sidebar_tool
      st.session_state.last_trigger = "sidebar_tool"

    def sidebar_adjust_change():
      st.session_state.selected = st.session_state.sidebar_adjust
      st.session_state.last_trigger = "sidebar_adjust"

    sidebar_tool = st.sidebar.selectbox("Select a Tool", tools, key="sidebar_tool", on_change=sidebar_tool_change)
    sidebar_adjust = st.sidebar.selectbox("Select an Adjustment", adjusts, key="sidebar_adjust", on_change=sidebar_adjust_change)

    # Sidebar Back Button
    if st.sidebar.button("<< Back to Home"):
      go_to_home()


    # ------ Editing Page -------
    # Title
    with st.columns(5)[2]:
      st.write("### &nbsp;&nbsp;&nbsp;&nbsp;Image Editing")

    # Layout for editing page 
    left_col, mid_col, right_col = st.columns([1.2, 2, 1.2])

    # Track which input triggered the selection
    # --------------------------------------------------------
    # LEFT: Tools
    with left_col:
      st.markdown("<h3 style='text-align:center;'>Tools</h3>", unsafe_allow_html=True)
      tools_btns = ["Crop", "Rotate/Resize", "Filter", "Text", "Draw"]
      _, mid, _ = st.columns([0.5, 2, 0.85])
      for tool in tools_btns:
        with mid:
           if st.button(tool, use_container_width=True, key=f"btn_{tool}"):
              st.session_state.selected = tool
              st.session_state.last_trigger = f"btn_{tool}"

    # MIDDLE: Image
    with mid_col:
      if "uploaded_image" in st.session_state and st.session_state.uploaded_image is not None:
        st.image(st.session_state.uploaded_image, use_container_width=False, width=500)
      else:
        st.warning("No image found. Please upload one first.")
        if st.button("Go to Home"):
            go_to_home()

    # RIGHT: Adjustments
    with right_col:
      st.markdown("<h3 style='text-align:center;'>Adjustments</h3>", unsafe_allow_html=True)
      adjusts_btns = ["Brightness", "Contrast", "Saturation", "Fade", "Sharpness"]
      _, mid, _ = st.columns([0.4, 2, 0.7])
      for adjust in adjusts_btns:
        with mid:
           if st.button(adjust, use_container_width=True, key=f"btn_{adjust}"):
               st.session_state.selected = adjust
               st.session_state.last_trigger = f"btn_{adjust}"

    # --------- Below Image ------------
    # Current Tool Selection, Undo/Reset, Download Section
    undo_reset, mid, download = st.columns([1.2, 2, 1.2])

    # -------------------------------- Editing Place ----------------------------------------
    # !!! Use explicit "Apply" button, which will use edit functions when clicked !!!
    # !!! Use save_state() before applying or using the function !!!

    with mid: 
      # *************************************************************************************
      # -------------------------------- Tools Place ----------------------------------------
      # *************************************************************************************
      if st.session_state.selected == "Crop":
        st.write(f"#### {st.session_state.selected}")
        img = st.session_state.uploaded_image
        if img:
            w, h = img.size
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                left = st.number_input("Left", 0, w, 0)
            with col2:
                top = st.number_input("Top", 0, h, 0)
            with col3:
                bottom = st.number_input("Bottom", 0, h, h)
            with col4:
                right = st.number_input("Right", 0, w, w)
            
            if st.button("Apply Crop"):
                # Before changing image, save old state
                save_state()
                cropped = crop_image(img, left, top, right, bottom)
                st.session_state.uploaded_image = cropped

      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Rotate/Resize":
        st.write(f"#### {st.session_state.selected}")
        img = st.session_state.uploaded_image
        if img:
            w, h = img.size

            # --- Rotate Section ---
            angle = st.slider("Rotate (°)", -180, 180, 0)
            if st.button("Apply Rotation"):
              save_state()  # <-- Save current state for undo
              rotated = rotate_image(img, angle)
              st.session_state.uploaded_image = rotated

            st.divider()

            # --- Resize Section ---
            col1, col2 = st.columns(2)
            with col1:
                new_w = st.number_input("Width", min_value=1, max_value=4000, value=min(w, 4000))
            with col2:    
                new_h = st.number_input("Height",min_value=1, max_value=4000,value=min(h, 4000))

            if st.button("Apply Resize"):
                save_state()  # <-- Save current state for undo
                resized = resize_image(img, new_w, new_h)
                st.session_state.uploaded_image = resized
      
      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Filter":
        st.write(f"#### {st.session_state.selected}")
        selected_filter = st.selectbox(
          "Choose a filter",
          ["None", "BLUR", "GRAYSCALE", "SEPIA", "CONTOUR",
          "EDGE_ENHANCE", "SMOOTH", "EMBOSS"],
          key="filter_select"
          )

        # Apply button - only when user clicks we save image and apply filter
        if st.button("Apply Filter"):
          if selected_filter == "None":
            st.info("Select a filter first.")
          else:
            # Ensure history exists
            if "history" not in st.session_state:
                st.session_state.history = []
            # Save current state (copy) for undo / reset
            save_state()
            apply_filter(st.session_state.uploaded_image, selected_filter)
            st.success(f"Applied {selected_filter} filter successfully.")

      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Text":
        st.write(f"#### {st.session_state.selected}")
        img = st.session_state.uploaded_image
        if img:
            text = st.text_input("Enter text", "Hello PicIt")
            col1, col2 = st.columns(2)
            with col1:
                font_size = st.slider("Font Size", 50, 250, 100)
            with col2:    
                color = st.color_picker("Text Color", "#FFFFFF")

            st.info("Add and move text using X/Y sliders")

            # Sliders to move text (simulate drag)
            col1, col2 = st.columns(2)
            with col1:
                x = st.slider("Move Horizontally (X)", 0, img.size[0], img.size[0] // 4)
            with col2:    
                y = st.slider("Move Vertically (Y)", 0, img.size[1], img.size[1] // 4)

            preview = add_text_to_image(img, text, (x, y), font_size, color)

            if st.button("Apply Text"):
                save_state()  # <-- Save current state for undo

                st.session_state.uploaded_image = preview
                st.success("Text applied to image!")

      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Draw":
        img = st.session_state.uploaded_image
        if img:
            st.write("#### Drawing Settings")
            col1, col2 = st.columns(2)
            with col1:
                color = st.color_picker("Drawing Color", "#FF0000")
            with col2:
                brush_size = st.slider("Line Thickness", 1, 40, 10)

            # --- Make preview only once when tool is selected ---
            if "draw_preview" not in st.session_state or st.session_state.last_trigger != "Draw":
                st.session_state.draw_preview = img.copy()
            st.session_state.last_trigger = "Draw"

            draw_img = st.session_state.draw_preview.copy()

            # Single point drawing
            st.write("#### ✏️ Draw Single Point")
            col1, col2 = st.columns(2)
            with col1:
                x = st.number_input("X Position", 0, img.width, 50)
            with col2:
                y = st.number_input("Y Position", 0, img.height, 50)

            if st.button("Draw Point"):
                st.session_state.draw_preview = draw_on_image(draw_img, [(x, y), (x+1, y+1)], color, brush_size)

            # Line drawing
            st.write("#### 📐 Draw Line")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                x1 = st.number_input("Start X", 0, img.width, 100, key="start_x")
            with col2:
                y1 = st.number_input("Start Y", 0, img.height, 100, key="start_y")
            with col4:
                x2 = st.number_input("End X", 0, img.width, 200, key="end_x")
            with col5:    
                y2 = st.number_input("End Y", 0, img.height, 200, key="end_y")

            if st.button("Draw Line"):
                st.session_state.draw_preview = draw_on_image(draw_img, [(x1, y1), (x2, y2)], color, brush_size)

            # Apply Draw to uploaded_image
            if st.button("Apply Draw"):
                save_state()  # Save original state for undo
                st.session_state.uploaded_image = st.session_state.draw_preview.copy()
                st.success("Drawing applied!")


      # *******************************************************************************************
      # -------------------------------- Adjustments Place ----------------------------------------
      # *******************************************************************************************
      
      elif st.session_state.selected == "Brightness":
        st.write(f"#### Adjust Brightness")
        st.session_state.uploaded_image = apply_brightness(st.session_state.uploaded_image)

      #--------------------------------------------------------------------------------------------------
      
      elif st.session_state.selected == "Contrast":
        st.write(f"#### Adjust Contrast")
        st.session_state.uploaded_image = apply_contrast(st.session_state.uploaded_image)

      #--------------------------------------------------------------------------------------------------
      
      elif st.session_state.selected == "Saturation":
        st.write(f"#### Adjust Saturation")
        st.session_state.uploaded_image = apply_saturation(st.session_state.uploaded_image)

      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Fade":
        st.write(f"#### Adjust Fade")
        st.session_state.uploaded_image = apply_fade(st.session_state.uploaded_image)

      #--------------------------------------------------------------------------------------------------

      elif st.session_state.selected == "Sharpness":
        st.write(f"#### Adjust Sharpness")
        st.session_state.uploaded_image = apply_sharpness(st.session_state.uploaded_image)

      #--------------------------------------------------------------------------------------------------

      else:
        st.write("### Nothing Selected.")


    # Undo / Reset
    with undo_reset:
      _, mid, _ = st.columns([0.5,2,0.8])
      st.markdown("<h3 style='text-align:center;'>Undo/Reset</h3>", unsafe_allow_html=True)
      _, mid, _ = st.columns([0.5,2,0.85])
      with mid:
        if st.button("<- Undo", use_container_width=True):
          undo()
        if st.button("<-- Reset", use_container_width=True):
          reset()

    # Download Section
    with download:
      # Download Text
      st.markdown("<h3 style='text-align:center;'>Download</h3>", unsafe_allow_html=True)
      # Centered Download Button
      _, mid, _ = st.columns([0.4, 2, 0.7])
      with mid:
          if st.button("Download", use_container_width=True):
              buf = io.BytesIO()
              st.session_state.uploaded_image.save(buf, format="PNG")
              st.download_button(
                "Click to Save",
                data=buf.getvalue(),
                file_name="edited_image.png",
                mime="image/png",
                use_container_width=True
              )

  
# -------------------------------------------------------------------------------------------------------------
# COLLAGE PAGE
# -------------------------------------------------------------------------------------------------------------

elif st.session_state.page == "collage":
    # Header Bar
    st.markdown("""
        <style>
        header[data-testid="stHeader"] {
            background-color: #D3D3D3;
            color: #000000;
            height: 80px;
            font-weight: 800;
            font-size: 20px;
            padding: 8px 25px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: 0 1px 6px rgba(0,0,0,0.1);
        }
        header[data-testid="stHeader"]::before {
            content: "PicIt - Image Editor";
            margin-left: 35px;
            color: #000000;
        }
        header[data-testid="stHeader"] + div [data-testid="block-container"] {
            padding-top: 140px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Create a Collage")

    # ------ Sidebar (Collage Page) -------
    st.sidebar.header("Home Page")
    if st.sidebar.button("<< Go to Home"):
      st.session_state.page = "home"

    # ==== CHECK IF IMAGES EXIST ====
    if "uploaded_images" not in st.session_state or not st.session_state.uploaded_images:
        st.warning("Please upload images first.")
        if st.button("<< Back to Home"):
            go_to_home()

    else:
        uploaded_files = st.session_state.uploaded_images
        
        collage_img = create_collage(uploaded_files, st.session_state.selected_layout, len(uploaded_files))  # FUNCTION CALL HERE

        st.image(collage_img, caption="Your Collage", use_container_width=True)

        # ==== DOWNLOAD BUTTON ====
        buf = io.BytesIO()
        collage_img.save(buf, format="PNG")
        st.download_button(
            "Download Collage",
            data=buf.getvalue(),
            file_name="collage.png",
            mime="image/png"
        )

        if st.button("<< Back to Home"):
            go_to_home()


