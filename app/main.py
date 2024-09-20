from fastapi import FastAPI, UploadFile, File, HTTPException
from app.ocr import extract_text_from_file

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF or image (jpg, png).")
    
    # Perform OCR
    extracted_text = await extract_text_from_file(file)
    
    return {"extracted_text": extracted_text}
