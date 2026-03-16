import streamlit as st

# ------------------------------- Helper Functions --------------------------------------

def save_state():
    """ Save current image state to history for undo functionality """
    st.session_state.history.append(st.session_state.uploaded_image.copy())  # Save copy of current image


def undo():
  ''' Undo last action by reverting to previous image state '''
  if st.session_state.history:
    st.session_state.uploaded_image = st.session_state.history.pop()  # Revert to last state
  else:
    st.warning("No more steps to undo.")


def reset():
    ''' Reset image to original uploaded state '''
    if "original_image" in st.session_state:
        st.session_state.uploaded_image = st.session_state.original_image.copy()  # Reset to original
        st.session_state.history = []
    else:
        st.warning("Original image unavailable!")   

# ---------------------------------------------------------------------------------------