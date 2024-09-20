import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

async def extract_text_from_file(file):
    # Check if it's a PDF
    if file.content_type == "application/pdf":
        return await extract_text_from_pdf(file)

    # If it's an image (JPG, PNG)
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)

    # Return the result as JSON format
    return {"file_type": "image", "extracted_text": text}

async def extract_text_from_pdf(file):
    # Convert PDF pages to images
    images = convert_from_bytes(file.file.read())

    # Extract text from each image
    extracted_texts = []
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        extracted_texts.append({
            "page_number": i + 1,
            "text": text
        })

    # Return the result as JSON format
    return {"file_type": "pdf", "pages": extracted_texts}

