# Page Capture Tool v21.0

Complete web content to PDF pipeline with bookmarklet generation and image-to-PDF conversion.

## Features

### 1. Bookmarklet Generator
- Generate custom bookmarklets to capture specific elements on web pages
- Configurable CSS selectors
- Multiple scale options (1x, 2x, 3x, 5x)
- Format selection (PNG/JPEG)
- Screenshot bookmarklet for full-page captures

### 2. Image to PDF Converter
- Upload multiple images (PNG/JPEG)
- Visual canvas with zoom controls
- Interactive page break placement
- Image reordering
- Multiple PDF generation methods:
  - **Preview + Download**: In-page preview with download button
  - **ZIP Archive**: Download all pages as ZIP file
  - **Individual Files**: Sequential image downloads
  - **Direct PDF**: Inline PDF generation

## Getting Started

### Running the Application

1. Start a local web server:
   ```bash
   python3 -m http.server 8080
   ```

2. Open in browser:
   ```
   http://localhost:8080/index.html
   ```

## Testing Guide

### Testing the Bookmarklet Generator

1. Open `index.html` in your browser
2. Navigate to the "Bookmarklet" tab
3. Enter a CSS selector (e.g., `.test-content`)
4. Select scale and format options
5. Click "Generate Bookmarklet"
6. Copy the generated code
7. Create a new bookmark in your browser:
   - Right-click bookmark bar → Add Page
   - Name: "Page Capture"
   - URL: Paste the copied bookmarklet code
8. Visit `test-page.html` (or any web page)
9. Click the bookmarklet to test capture

### Testing the Screenshot Bookmarklet

1. Click "Generate Screenshot Bookmarklet"
2. Copy the generated code
3. Create a bookmark with the code
4. Visit any web page and click the bookmark
5. It should capture the entire page

### Testing Image to PDF Converter

#### Method 1: Using Real Images

1. Open `index.html` in your browser
2. Navigate to the "Image to PDF" tab
3. Drag and drop or click to upload images
4. Verify images appear in the canvas
5. Test zoom controls (25%, 50%, 75%, Fit, 100%, 150%, 200%)
6. Click on images to place page breaks
7. Test auto-break feature
8. Test each PDF generation method:
   - Preview + Download (recommended)
   - ZIP Archive
   - Individual Files
   - Direct PDF

#### Method 2: Creating Test Images

You can create simple test images using any image editor or online tools:
- Create 3-5 images with different sizes
- Recommended dimensions: 800x600, 1024x768, 1200x900
- Save as PNG or JPEG
- Use them to test the tool

#### Method 3: Using Browser Screenshots

1. Take screenshots of web pages (use screenshot tools)
2. Upload them to the tool
3. Test the functionality

### Feature Checklist

- [ ] Bookmarklet generator accepts CSS selectors
- [ ] Bookmarklet code can be copied
- [ ] Screenshot bookmarklet generates correctly
- [ ] Images can be uploaded via click
- [ ] Images can be uploaded via drag-and-drop
- [ ] Multiple images display correctly
- [ ] Zoom controls work (all levels)
- [ ] Images can be reordered
- [ ] Page breaks can be placed by clicking
- [ ] Page breaks can be dragged
- [ ] Page breaks can be removed
- [ ] Auto-break feature works
- [ ] Statistics update correctly
- [ ] Method 1 (Preview + Download) generates PDF
- [ ] Method 2 (ZIP) downloads archive
- [ ] Method 3 (Individual) downloads files
- [ ] Method 4 (Direct PDF) creates PDF
- [ ] Individual images can be removed
- [ ] All images can be cleared
- [ ] Loading overlay shows during operations

## Usage Examples

### Example 1: Capturing a Blog Post

1. Visit a blog post
2. Inspect the element to find the content selector (e.g., `.article-content`)
3. Generate a bookmarklet with that selector
4. Click the bookmarklet
5. Images will be downloaded automatically

### Example 2: Converting Screenshots to PDF

1. Take screenshots of multiple web pages
2. Upload them to the Image to PDF converter
3. Reorder them if needed
4. Place page breaks where you want pages to split
5. Select "Preview + Download" method
6. Click "Generate PDF"
7. Review the preview and download

### Example 3: Creating a Multi-Page Document

1. Upload several long images
2. Use auto-break with 5000px intervals
3. Adjust breaks by dragging them
4. Generate PDF with your preferred method

## Browser Compatibility

- **Chrome/Edge**: Fully supported
- **Firefox**: Fully supported
- **Safari**: Fully supported (may have popup blocker issues)

## Dependencies

The tool uses CDN-hosted libraries:
- **JSZip 3.10.1**: For ZIP archive generation
- **jsPDF 2.5.1**: For PDF generation
- **html2canvas 1.4.1**: For bookmarklet captures (loaded dynamically)

## Troubleshooting

### Bookmarklet Issues

**Problem**: Bookmarklet doesn't work
- Ensure you copied the entire code
- Check if popup blocker is preventing new window
- Verify the CSS selector is correct

**Problem**: Element not captured correctly
- Try a different CSS selector
- Increase the scale for better quality
- Check if the element has proper dimensions

### Image to PDF Issues

**Problem**: PDF generation fails
- Try Method 1 (Preview + Download) - most reliable
- Check browser console for errors
- Ensure images are loaded completely

**Problem**: Images don't upload
- Check file format (PNG/JPEG only)
- Check file size (browser memory limits)
- Try fewer images at once

**Problem**: Zoom doesn't work
- Click zoom buttons multiple times
- Try "Fit" mode first
- Refresh the page if canvas appears blank

## Technical Details

### Application State

The tool maintains a client-side state including:
- Image data (as Image objects)
- Image dimensions and heights
- Page break positions
- Zoom settings
- Cached page dimensions for PDF generation

### PDF Generation Methods Explained

1. **Preview + Download**:
   - Generates page images first
   - Displays preview in overlay
   - Creates PDF on demand
   - Most reliable method

2. **ZIP Archive**:
   - Generates page images
   - Packages them in a ZIP file
   - Downloads automatically

3. **Individual Files**:
   - Generates page images
   - Downloads each as separate file
   - Sequential downloads with 500ms delay

4. **Direct PDF**:
   - Generates and downloads PDF immediately
   - No preview step
   - Faster but less flexible

## Performance Considerations

- Large images may slow down rendering
- Many page breaks increase processing time
- Preview method is slower but more reliable
- ZIP compression takes additional time

## File Structure

```
ToolPDFSpl/
├── index.html          # Main application
├── test-page.html      # Test page for bookmarklets
└── README.md          # This file
```

## Server Setup

The application requires a web server to function properly due to browser security restrictions. You can use any of these methods:

### Python (Included)
```bash
python3 -m http.server 8080
```

### Node.js (if installed)
```bash
npx http-server -p 8080
```

### PHP (if installed)
```bash
php -S localhost:8080
```

Then open `http://localhost:8080/index.html` in your browser.

## Future Enhancements

Potential improvements:
- PDF merge functionality
- Image editing tools (crop, rotate)
- Batch bookmarklet execution
- Cloud storage integration
- Custom page sizes for PDF
- Watermark support

## License

This tool is provided as-is for educational and personal use.

## Support

For issues or questions, please refer to the testing guide above or check the browser console for error messages.

---

**Version**: 21.0
**Last Updated**: 2025-11-19
**Status**: All features working
