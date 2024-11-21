# Image-Collage-Creater

## **Description**
This program combines four input images into a 2x2 grid and saves the result as a single image file. The user provides the paths to the images and specifies the desired output format (e.g., JPG or PNG). The program handles image resizing, error checking, and saving the final collage.


## **Features**
- Accepts four image file paths as input.
- Resizes all images to ensure uniform dimensions in the collage.
- Arranges the images into a 2x2 grid:
  ```
  | Image 1 | Image 2 |
  | Image 3 | Image 4 |
  ```
- Saves the collage in the specified output format (e.g., JPG, PNG).
- Handles invalid paths, unsupported formats, and other errors gracefully.


## **Prerequisites**
1. **Python version**: Ensure you have Python 3.6 or above installed.
2. **Required Libraries**:
   - `Pillow`: Install it using:
     ```bash
     pip install pillow
     ```

## **How to Use**

1. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the program file (`CreateCollageImage.py.py`) is saved.
   - Run the program by typing:
     ```bash
     python image_collage.py
     ```

2. **Provide Input**:
   - Enter the paths to the four image files when prompted.
   - Example:
     ```
     Please enter the path for Image 1: C:\Images\image1.jpg
     Please enter the path for Image 2: C:\Images\image2.jpg
     Please enter the path for Image 3: C:\Images\image3.jpg
     Please enter the path for Image 4: C:\Images\image4.jpg
     Please specify the output file format (jpg, png): jpg
     ```

3. **Output**:
   - The program creates a new image file (`collage.jpg` or the specified format) in the same directory as the script.


## **Error Handling**
- **Invalid Path**:
  If any of the provided paths are invalid or the file does not exist, the program will display:
  ```
  Error: The file at the specified path does not exist. Please try again.
  ```
- **Unsupported Format**:
  If an unsupported image format is provided, the program will display:
  ```
  Error: The file is not a valid image or is in an unsupported format. Please provide a valid image.
  ```
- **Other Errors**:
  Any other unexpected errors will be reported with a helpful message.
  

## **Testing**
1. Test with:
   - Four valid image files of the same format.
   - Image files of different dimensions (ensures proper resizing).
   - Invalid file paths or non-image files (e.g., text files).
   - A mix of supported and unsupported image formats.

2. Verify that:
   - The collage is created with all images resized correctly.
   - The output file can be opened without errors.


## **Output Image**

![collage](https://github.com/user-attachments/assets/28a65403-6fdb-42d7-a5d9-1982d465ebd0)
