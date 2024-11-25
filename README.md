# Documentation for the `PixelPerfect`

## Overview
The `PixelPerfect` is a graphical user interface (GUI) application written in Python that allows users to perform basic image editing tasks such as opening, saving, rotating, resizing, applying filters, and enhancing images. The application is built using the `tkinter` library for the GUI, and the `Pillow` library for image processing.

---

## Requirements
- **Python**: Version 3.7 or higher.
- **Libraries**: 
  - `tkinter` (comes with Python).
  - `Pillow` (install using `pip install pillow`).

---

## Features
1. **Open Image**: Load an image from the user's file system.
2. **Save Image**: Save the currently edited image.
3. **Rotate Image**: Rotate the image by 90 degrees clockwise.
4. **Resize Image**: Change the dimensions of the image based on user input.
5. **Apply Filter**: Apply a blur filter to the image.
6. **Enhance Image**: Adjust the contrast of the image for better visibility.

---

## Code Breakdown

### 1. **Initialization (`__init__`)**
- Sets up the main application window (`root`), including title, dimensions, and default values for the loaded image.
- Calls methods to create the menu and widgets.

### 2. **Menu Creation (`create_menu`)**
- Adds a **File** menu to the menu bar with options:
  - `Open`: Open an image file.
  - `Save`: Save the edited image.
  - `Exit`: Exit the application.

### 3. **Widget Creation (`create_widgets`)**
- Creates the main canvas for displaying the image (600x400 pixels).
- Adds control buttons for browsing, rotating, resizing, applying filters, and enhancing the image.

### 4. **Open Image (`open_image`)**
- Allows the user to browse and select an image file using a file dialog.
- Supported formats: PNG, JPEG, BMP.

### 5. **Save Image (`save_image`)**
- Lets the user save the currently loaded and edited image via a file dialog.
- Supported formats: PNG, JPEG.

### 6. **Display Image (`display_image`)**
- Resizes the image to fit the canvas dimensions and displays it on the canvas.

### 7. **Rotate Image (`rotate_image`)**
- Rotates the image 90 degrees clockwise and updates the display.

### 8. **Resize Image (`resize_image`)**
- Prompts the user to enter new width and height for the image.
- Resizes the image to the specified dimensions.

### 9. **Apply Filter (`apply_filter`)**
- Applies a blur filter to the image using `ImageFilter.BLUR`.

### 10. **Enhance Image (`enhance_image`)**
- Enhances the image's contrast by a factor of 1.5 using `ImageEnhance.Contrast`.

---

## Code Structure

### Classes
#### 1. **ImageEditorApp**
- **Purpose**: Manages the GUI and image processing functionalities.
- **Attributes**:
  - `root`: Main application window.
  - `image`: Loaded image as a `Pillow.Image` object.
  - `img_display`: Image ready for display as a `PhotoImage`.
  - `canvas`: Canvas widget for displaying images.

### Methods
| Method               | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `__init__`           | Initializes the application, sets up the GUI components.               |
| `create_menu`        | Creates the menu bar and its options.                                  |
| `create_widgets`     | Creates the canvas and control buttons.                                |
| `open_image`         | Opens an image file from the user's system.                           |
| `save_image`         | Saves the currently loaded and edited image.                          |
| `display_image`      | Displays the resized image on the canvas.                             |
| `rotate_image`       | Rotates the image by 90 degrees.                                      |
| `resize_image`       | Resizes the image based on user input dimensions.                     |
| `apply_filter`       | Applies a blur filter to the image.                                   |
| `enhance_image`      | Enhances the image contrast by a factor of 1.5.                       |

---

## Usage Instructions
1. Run the script:
   ```bash
   python image_editor_app.py
   ```
2. Use the **File** menu or **Browse Image** button to open an image.
3. Perform desired operations using the buttons:
   - Rotate, Resize, Apply Filter, Enhance.
4. Save the image using the **File > Save** menu option.

---

## Example Usage

### Opening and Rotating an Image
1. Click **Browse Image** and select an image file.
2. Click **Rotate** to rotate the image.

### Resizing an Image
1. Click **Resize** and input the new width and height when prompted.
2. The image is resized to the specified dimensions.

### Saving an Image
1. Click **Save** under the **File** menu.
2. Choose a location and file name to save the edited image.

---

## Dependencies

| Library   | Purpose                                |
|-----------|----------------------------------------|
| `tkinter` | GUI development for creating the interface. |
| `Pillow`  | Image processing tasks such as opening, saving, resizing, filtering, and enhancing. |

---

## Troubleshooting

### Common Issues
1. **Image not displayed**:
   - Ensure the image file format is supported (PNG, JPEG, BMP).
2. **Error: `AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'`**:
   - Use `Image.Resampling.LANCZOS` instead of `Image.ANTIALIAS`.

### Debugging
- Use `print` statements or a debugger to trace issues in methods like `open_image` or `display_image`.

---

## Future Enhancements
- Add more filters (e.g., sharpening, edge detection).
- Enable cropping and annotating images.
- Add a "Reset" button to revert to the original image.

---

This documentation provides a comprehensive guide to understanding, using, and extending the `ImageEditorApp`.
