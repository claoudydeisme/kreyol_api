# KreyolAPI Demo Setup

This demo provides a user-friendly interface for testing the KreyolAPI translation service.

## Files Included

1. **index.html** - Main landing page with API documentation
2. **demo.html** - Interactive demo page with translation form
3. **styles.css** - Base styles for the landing page
4. **demo-styles.css** - Styles for the demo page
5. **demo.js** - JavaScript functionality for the demo

## Setup Instructions

### 1. Update API URL

In `demo.js`, update the API base URL to match your FastAPI server:

```javascript
const API_BASE_URL = 'http://localhost:8000'; // Change to your API URL
```

If your API is running on a different port or domain, update this accordingly.

### 2. Enable CORS (if needed)

If your API and frontend are on different domains/ports, you need to enable CORS in your FastAPI app.

Add this to your FastAPI main file (e.g., `main.py`):

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
```

### 3. Serve the Frontend

You can serve the HTML files using any web server:

**Option A: Python's built-in server**
```bash
# Navigate to the directory containing the HTML files
python -m http.server 8080
```
Then open `http://localhost:8080` in your browser.

**Option B: Node.js http-server**
```bash
npx http-server -p 8080
```

**Option C: FastAPI Static Files**
Add static file serving to your FastAPI app:

```python
from fastapi.staticfiles import StaticFiles

# Serve static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")
```

Then place all HTML/CSS/JS files in a `static` folder.

### 4. Test the Demo

1. Start your FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open the frontend (depending on your setup method)

3. Navigate to the demo page and try translating:
   - "how are you?" (English → Kreyol)
   - "kijan ou ye?" (Kreyol → English)

## Features

### Translation Form
- **Language Direction Toggle**: Switch between English→Kreyol and Kreyol→English
- **Domain Selection**: Choose from General, Healthcare, or Education domains
- **Character Counter**: Shows remaining characters (500 max)
- **Real-time Translation**: Instant translation via API

### Results Display
- **Confidence Score**: Visual indicator of translation quality
  - High (90%+): Green badge
  - Medium (70-89%): Yellow badge
  - Low (<70%): Red badge
- **Warnings**: Shows any translation issues or simplifications
- **Example Phrases**: Quick-start buttons with common phrases

### Feedback System
- **Thumbs Up/Down**: Quick feedback on translation quality
- **Optional Comments**: Users can provide detailed feedback
- **Thank You Message**: Confirmation after feedback submission

## Customization

### Change Colors
Edit the color values in `demo-styles.css`:
- Primary color: `#38bdf8` (light blue)
- Dark background: `#0f172a`
- Success: `#22c55e` (green)
- Warning: `#f59e0b` (orange)

### Add More Examples
In `demo.html`, add more example buttons:

```html
<button class="example-btn" data-text="Your text here" data-lang="en">
  "Your text here"
</button>
```

### Modify API Response Handling
In `demo.js`, the `displayTranslation()` function handles API responses. Customize it to show additional fields from your API.

## Troubleshooting

### "Translation failed" Error
- Check that your API server is running
- Verify the API_BASE_URL in `demo.js` matches your server
- Check browser console for CORS errors
- Ensure datasets are loaded (check terminal output)

### Datasets Not Loading
- Verify CSV files are in the correct location (`datasets/` folder)
- Check file paths in `registry_data.py`
- Look for error messages in server terminal

### Translation Returns "No translation available yet"
- The text might not exist in your dataset
- Check source/target language codes match CSV
- Verify domain matches CSV data

## API Endpoint Expected

The demo expects this API endpoint structure:

**Request:**
```json
POST /translate
{
  "text": "your text",
  "source_language": "en",
  "target_language": "ht",
  "domain": "general"
}
```

**Response:**
```json
{
  "translation": "translated text",
  "source_language": "en",
  "target_language": "ht",
  "domain": "general",
  "confidence": 0.95,
  "warnings": []
}
```

## Next Steps

1. Add user authentication for personalized features
2. Implement feedback collection endpoint
3. Add translation history for logged-in users
4. Create admin panel for reviewing feedback
5. Add more example phrases for each domain
6. Implement text-to-speech for translations

## Support

For issues or questions, contact: contact@kreyolapi.org
