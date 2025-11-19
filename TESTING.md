# Page Capture Tool v21.0 - Complete Testing Guide

This document provides comprehensive testing instructions for all features of the Page Capture Tool.

## Quick Links

- **Main App**: http://localhost:8080/index.html
- **Test Page**: http://localhost:8080/test-page.html
- **Test Suite**: http://localhost:8080/test-suite.html
- **Image Generator**: http://localhost:8080/generate-test-images.html

## Test Setup

### 1. Start Server
```bash
python3 -m http.server 8080
```

### 2. Generate Test Images
1. Open `http://localhost:8080/generate-test-images.html`
2. Click "Generate All Test Images"
3. Download all 5 test images
4. Save them to a known location

### 3. Run Automated Tests
1. Open `http://localhost:8080/test-suite.html`
2. Click "Run All Tests"
3. Verify all tests pass
4. Review console output

## Comprehensive Feature Testing

### Category 1: Bookmarklet Generator Tests

#### Test 1.1: Basic Bookmarklet Generation
- [ ] Open index.html
- [ ] Go to "Bookmarklet" tab
- [ ] Enter selector: `.test-content`
- [ ] Select scale: 2x
- [ ] Select format: JPEG
- [ ] Click "Generate Bookmarklet"
- [ ] **Expected**: Code appears in black box
- [ ] **Expected**: Code starts with `javascript:`
- [ ] **Expected**: Code contains `.test-content`

#### Test 1.2: Bookmarklet Copy Function
- [ ] Generate a bookmarklet
- [ ] Click "Copy to Clipboard"
- [ ] **Expected**: Alert shows "Copied!"
- [ ] Paste into notepad
- [ ] **Expected**: Full bookmarklet code is pasted

#### Test 1.3: Bookmarklet with Different Selectors
Test each selector:
- [ ] `.article-content` - should generate
- [ ] `#main` - should generate
- [ ] `div.container` - should generate
- [ ] `body > main` - should generate
- [ ] Empty selector - should show error

#### Test 1.4: Bookmarklet Scale Options
Test each scale:
- [ ] 1x - should generate
- [ ] 2x - should generate
- [ ] 3x - should generate
- [ ] 5x - should generate
- [ ] **Expected**: Code contains correct scale value

#### Test 1.5: Bookmarklet Format Options
- [ ] PNG format - should generate
- [ ] JPEG format - should generate
- [ ] **Expected**: Code contains correct format

#### Test 1.6: Screenshot Bookmarklet
- [ ] Click "Generate Screenshot Bookmarklet"
- [ ] **Expected**: Code appears in output box
- [ ] **Expected**: Code contains `html2canvas`
- [ ] Click "Copy Screenshot Bookmarklet"
- [ ] **Expected**: Code copied successfully

#### Test 1.7: Live Bookmarklet Test
- [ ] Generate bookmarklet with selector `.test-content`
- [ ] Copy the code
- [ ] Open browser bookmark manager
- [ ] Create new bookmark
- [ ] Name: "Test Capture"
- [ ] URL: Paste bookmarklet code
- [ ] Save bookmark
- [ ] Open `test-page.html`
- [ ] Click the bookmarklet
- [ ] **Expected**: New window opens
- [ ] **Expected**: "Loading library..." appears
- [ ] **Expected**: Content is captured
- [ ] **Expected**: Image downloads automatically

---

### Category 2: Image Upload Tests

#### Test 2.1: Click to Upload
- [ ] Go to "Image to PDF" tab
- [ ] Click on upload area
- [ ] **Expected**: File picker opens
- [ ] Select 1 image
- [ ] **Expected**: Image appears in canvas
- [ ] **Expected**: Stats show 1 image

#### Test 2.2: Drag and Drop Upload
- [ ] Drag an image file over upload area
- [ ] **Expected**: Upload area turns green
- [ ] **Expected**: Border color changes
- [ ] Drop the image
- [ ] **Expected**: Image appears in canvas
- [ ] **Expected**: Upload area returns to normal color

#### Test 2.3: Multiple Image Upload
- [ ] Select all 5 test images
- [ ] Upload them
- [ ] **Expected**: All 5 images appear
- [ ] **Expected**: Images stacked vertically
- [ ] **Expected**: Each image has label (Image 1, Image 2, etc.)
- [ ] **Expected**: Stats show 5 images

#### Test 2.4: Image Display
For each uploaded image:
- [ ] Image label visible (top-left)
- [ ] Remove button visible (top-right, red)
- [ ] Image renders clearly
- [ ] Border between images visible

#### Test 2.5: Upload Area Hover
- [ ] Hover over upload area
- [ ] **Expected**: Border turns purple
- [ ] **Expected**: Background lightens
- [ ] Move mouse away
- [ ] **Expected**: Colors return to normal

---

### Category 3: Zoom Controls Tests

#### Test 3.1: Zoom Level Tests
Test each zoom level:
- [ ] Click "25%" - canvas should shrink
- [ ] Click "50%" - canvas should be half size
- [ ] Click "75%" - canvas should be 3/4 size
- [ ] Click "Fit" - canvas should fit container
- [ ] Click "100%" - canvas should be actual size
- [ ] Click "150%" - canvas should be 1.5x size
- [ ] Click "200%" - canvas should be 2x size

For each zoom level:
- [ ] **Expected**: Zoom display updates
- [ ] **Expected**: Clicked button is highlighted (purple)
- [ ] **Expected**: Images resize proportionally
- [ ] **Expected**: Page breaks reposition correctly

#### Test 3.2: Zoom State Persistence
- [ ] Set zoom to 50%
- [ ] Upload new image
- [ ] **Expected**: Zoom stays at 50%
- [ ] Set zoom to Fit
- [ ] Resize window
- [ ] **Expected**: Canvas adjusts to fit

#### Test 3.3: Zoom with Page Breaks
- [ ] Upload images
- [ ] Place 2 page breaks
- [ ] Change zoom to 50%
- [ ] **Expected**: Page breaks scale correctly
- [ ] Change zoom to 200%
- [ ] **Expected**: Page breaks remain aligned

---

### Category 4: Statistics Display Tests

#### Test 4.1: Image Count
- [ ] Upload 1 image
- [ ] **Expected**: "Images: 1"
- [ ] Upload 3 more images
- [ ] **Expected**: "Images: 4"
- [ ] Remove 1 image
- [ ] **Expected**: "Images: 3"

#### Test 4.2: Height Display
- [ ] Upload test images
- [ ] **Expected**: Height shows total height
- [ ] **Expected**: Number has comma separators (e.g., "5,468")
- [ ] Add more images
- [ ] **Expected**: Height increases

#### Test 4.3: Width Display
- [ ] Upload images with different widths
- [ ] **Expected**: Width shows maximum width
- [ ] Upload wider image
- [ ] **Expected**: Width updates to new maximum

#### Test 4.4: Breaks Count
- [ ] No breaks: **Expected** "Breaks: 0"
- [ ] Add 1 break: **Expected** "Breaks: 1"
- [ ] Add 3 more breaks: **Expected** "Breaks: 4"
- [ ] Remove 1 break: **Expected** "Breaks: 3"
- [ ] Clear all breaks: **Expected** "Breaks: 0"

---

### Category 5: Image Reordering Tests

#### Test 5.1: Reorder UI Display
- [ ] Upload 3 images
- [ ] **Expected**: Reorder section visible
- [ ] **Expected**: 3 input boxes (numbered 1, 2, 3)
- [ ] **Expected**: File names shown next to each

#### Test 5.2: Simple Reorder
- [ ] Upload images: A, B, C (in that order)
- [ ] Change order to: 3, 2, 1
- [ ] Click "Apply New Order"
- [ ] **Expected**: Order is now C, B, A
- [ ] **Expected**: Alert shows "Images reordered!"
- [ ] **Expected**: Canvas shows new order

#### Test 5.3: Reorder with Page Breaks
- [ ] Upload 3 images
- [ ] Place 2 page breaks
- [ ] Reorder images
- [ ] **Expected**: Page breaks are cleared
- [ ] **Expected**: Alert mentions breaks cleared

#### Test 5.4: Complex Reorder
- [ ] Upload 5 images
- [ ] Set order: 5, 1, 3, 2, 4
- [ ] Apply
- [ ] **Expected**: Images appear in correct new order
- [ ] Verify by checking image labels

---

### Category 6: Page Break Tests

#### Test 6.1: Click to Place Break
- [ ] Upload 2 tall images
- [ ] Click middle of first image
- [ ] **Expected**: Red line appears
- [ ] **Expected**: Label shows "Page 1/2"
- [ ] **Expected**: Breaks count increases

#### Test 6.2: Multiple Breaks
- [ ] Upload images
- [ ] Click to place 5 breaks
- [ ] **Expected**: Each break has label (Page 1/2, 2/3, etc.)
- [ ] **Expected**: All breaks visible
- [ ] **Expected**: Breaks sorted by position

#### Test 6.3: Drag Break
- [ ] Place a break
- [ ] Click and hold on the red line
- [ ] Drag up or down
- [ ] **Expected**: Break moves with mouse
- [ ] Release mouse
- [ ] **Expected**: Break stays in new position
- [ ] **Expected**: Label updates

#### Test 6.4: Remove Single Break
- [ ] Place 3 breaks
- [ ] Click "X" on first break
- [ ] **Expected**: Break removed
- [ ] **Expected**: Other breaks remain
- [ ] **Expected**: Labels update (Page 1/2, 2/3)

#### Test 6.5: Auto-Break Feature
- [ ] Upload large images (total > 5000px)
- [ ] Set auto-break value: 5000
- [ ] Click "Auto-Break"
- [ ] **Expected**: Breaks placed every 5000px
- [ ] **Expected**: Alert shows number of breaks placed
- [ ] Test with different values:
  - [ ] 1000px
  - [ ] 3000px
  - [ ] 10000px

#### Test 6.6: Clear All Breaks
- [ ] Place multiple breaks (5+)
- [ ] Click "Clear Breaks"
- [ ] Confirm dialog
- [ ] **Expected**: All breaks removed
- [ ] **Expected**: Breaks count = 0
- [ ] **Expected**: Alert confirms cleared

#### Test 6.7: Break Position Limits
- [ ] Try to place break at very top
- [ ] **Expected**: Break placed at minimum position (10px)
- [ ] Try to place break at very bottom
- [ ] **Expected**: Break placed at maximum position (height - 10px)

---

### Category 7: Image Removal Tests

#### Test 7.1: Remove Single Image
- [ ] Upload 3 images
- [ ] Click "X Remove" on second image
- [ ] Confirm dialog
- [ ] **Expected**: Image removed
- [ ] **Expected**: Remaining images stay
- [ ] **Expected**: Image count decreases
- [ ] **Expected**: Labels update (Image 1, Image 2)

#### Test 7.2: Remove with Page Breaks
- [ ] Upload 3 images
- [ ] Place breaks across all images
- [ ] Remove middle image
- [ ] **Expected**: Some breaks may be removed
- [ ] **Expected**: Valid breaks remain
- [ ] **Expected**: Heights recalculated

#### Test 7.3: Remove Last Image
- [ ] Upload 1 image
- [ ] Remove it
- [ ] **Expected**: Image section hides
- [ ] **Expected**: Canvas is empty
- [ ] **Expected**: Stats reset

#### Test 7.4: Clear All Images
- [ ] Upload 5 images
- [ ] Add page breaks
- [ ] Click "Clear All"
- [ ] Confirm dialog
- [ ] **Expected**: All images removed
- [ ] **Expected**: All breaks removed
- [ ] **Expected**: Image section hides
- [ ] **Expected**: Alert shows "All cleared"

---

### Category 8: PDF Generation Method Tests

#### Test 8.1: Method Selection
- [ ] Click each method card
- [ ] **Expected**: Card border turns purple
- [ ] **Expected**: Background changes to light purple
- [ ] **Expected**: Only one card selected at a time
- [ ] **Expected**: AppState.selectedMethod updates

#### Test 8.2: Method 1 - Preview + Download
- [ ] Upload 3 test images
- [ ] Place 2 page breaks (3 pages total)
- [ ] Select "Preview + Download"
- [ ] Click "Generate PDF"
- [ ] **Expected**: Loading overlay appears
- [ ] **Expected**: Preview overlay opens
- [ ] **Expected**: 3 pages shown
- [ ] **Expected**: Each page labeled
- [ ] **Expected**: Images render clearly
- [ ] Click "Download PDF"
- [ ] **Expected**: PDF downloads
- [ ] Open PDF
- [ ] **Expected**: 3 pages in PDF
- [ ] **Expected**: Content matches preview
- [ ] Click "Close"
- [ ] **Expected**: Preview closes

#### Test 8.3: Method 2 - ZIP Archive
- [ ] Upload images
- [ ] Place page breaks
- [ ] Select "ZIP Archive"
- [ ] Click "Generate PDF"
- [ ] **Expected**: Loading overlay appears
- [ ] **Expected**: "Creating ZIP..." message
- [ ] **Expected**: ZIP file downloads
- [ ] Extract ZIP
- [ ] **Expected**: Contains page-001.jpg, page-002.jpg, etc.
- [ ] **Expected**: Number of files = number of pages
- [ ] **Expected**: Images are correct

#### Test 8.4: Method 3 - Individual Files
- [ ] Upload images
- [ ] Place 2 breaks (3 pages)
- [ ] Select "Individual Files"
- [ ] Click "Generate PDF"
- [ ] **Expected**: Loading overlay appears
- [ ] **Expected**: 3 separate downloads
- [ ] **Expected**: Files named page-001.jpg, page-002.jpg, page-003.jpg
- [ ] **Expected**: 500ms delay between downloads
- [ ] **Expected**: Alert shows "Downloaded 3 pages"

#### Test 8.5: Method 4 - Direct PDF
- [ ] Upload images
- [ ] Place page breaks
- [ ] Select "Direct PDF"
- [ ] Click "Generate PDF"
- [ ] **Expected**: Loading overlay appears
- [ ] **Expected**: PDF downloads immediately
- [ ] Open PDF
- [ ] **Expected**: Correct number of pages
- [ ] **Expected**: Content renders correctly

#### Test 8.6: Generation Without Images
- [ ] Don't upload any images
- [ ] Click "Generate PDF"
- [ ] **Expected**: Alert "Upload images first"
- [ ] **Expected**: No processing occurs

#### Test 8.7: Single Image PDF
- [ ] Upload 1 image only
- [ ] Don't place breaks
- [ ] Generate PDF (any method)
- [ ] **Expected**: Single page PDF
- [ ] **Expected**: Full image on one page

---

### Category 9: Loading Overlay Tests

#### Test 9.1: Loading Display
- [ ] Trigger any PDF generation
- [ ] **Expected**: Black overlay appears
- [ ] **Expected**: White box in center
- [ ] **Expected**: Spinning animation
- [ ] **Expected**: "Processing..." or relevant text
- [ ] **Expected**: Page is unclickable

#### Test 9.2: Loading Messages
Watch for different messages:
- [ ] "Loading images..."
- [ ] "Generating..."
- [ ] "Creating ZIP..."
- [ ] "Creating PDF..."
- [ ] "Downloading..."

#### Test 9.3: Loading Auto-Hide
- [ ] Generate PDF
- [ ] **Expected**: Loading shows
- [ ] Wait for completion
- [ ] **Expected**: Loading hides automatically

---

### Category 10: Tab Switching Tests

#### Test 10.1: Switch to Image Tab
- [ ] Click "Image to PDF" tab
- [ ] **Expected**: Tab highlighted
- [ ] **Expected**: Border turns purple
- [ ] **Expected**: Image content shows
- [ ] **Expected**: Bookmarklet content hides

#### Test 10.2: Switch to Bookmarklet Tab
- [ ] Click "Bookmarklet" tab
- [ ] **Expected**: Tab highlighted
- [ ] **Expected**: Bookmarklet content shows
- [ ] **Expected**: Image content hides

#### Test 10.3: Switch with Data
- [ ] Upload images in Image tab
- [ ] Switch to Bookmarklet tab
- [ ] Switch back to Image tab
- [ ] **Expected**: Images still there
- [ ] **Expected**: No data loss

---

### Category 11: Error Handling Tests

#### Test 11.1: Invalid File Types
- [ ] Try to upload .txt file
- [ ] **Expected**: File picker filters to images only
- [ ] Try to upload .pdf
- [ ] **Expected**: Not accepted

#### Test 11.2: No Selector Error
- [ ] Go to Bookmarklet tab
- [ ] Clear selector input
- [ ] Click "Generate Bookmarklet"
- [ ] **Expected**: Alert "Please enter a CSS selector"

#### Test 11.3: Auto-Break Invalid Value
- [ ] Set auto-break to 100 (too small)
- [ ] Click "Auto-Break"
- [ ] **Expected**: Alert "Invalid value"
- [ ] Set to 100000 (very large)
- [ ] **Expected**: Either works or shows reasonable error

#### Test 11.4: Remove Confirmation Cancel
- [ ] Upload images
- [ ] Click "Clear All"
- [ ] Click "Cancel" on confirmation
- [ ] **Expected**: Images remain
- [ ] **Expected**: No changes

---

### Category 12: Browser Compatibility Tests

#### Test 12.1: Chrome/Edge
- [ ] Run all tests in Chrome
- [ ] **Expected**: All features work
- [ ] Check console for errors
- [ ] **Expected**: No errors

#### Test 12.2: Firefox
- [ ] Run all tests in Firefox
- [ ] **Expected**: All features work
- [ ] Check console for errors
- [ ] **Expected**: No errors

#### Test 12.3: Safari
- [ ] Run all tests in Safari
- [ ] **Expected**: All features work
- [ ] Note: May have popup blocker issues with bookmarklet

---

### Category 13: Integration Tests

#### Test 13.1: Full Workflow - Bookmarklet
1. [ ] Generate bookmarklet
2. [ ] Create browser bookmark
3. [ ] Visit test-page.html
4. [ ] Click bookmarklet
5. [ ] Verify capture works
6. [ ] Download captured images
7. [ ] Upload to Image to PDF
8. [ ] Place page breaks
9. [ ] Generate PDF
10. [ ] **Expected**: Complete workflow successful

#### Test 13.2: Full Workflow - Direct Images
1. [ ] Generate test images
2. [ ] Upload all 5 images
3. [ ] Reorder them (5,4,3,2,1)
4. [ ] Set zoom to 75%
5. [ ] Place 4 page breaks
6. [ ] Drag breaks to adjust
7. [ ] Remove 1 break
8. [ ] Test all 4 PDF methods
9. [ ] **Expected**: All methods produce correct output

#### Test 13.3: Stress Test
1. [ ] Upload 10+ images
2. [ ] Place 20+ page breaks
3. [ ] Change zoom multiple times
4. [ ] Reorder images
5. [ ] Generate large PDF
6. [ ] **Expected**: App handles it smoothly

---

## Automated Test Results

### Running Automated Tests

1. Open `http://localhost:8080/test-suite.html`
2. Click "Run All Tests"
3. Wait for completion
4. Review results

### Expected Results

**Total Tests**: 68
- JavaScript Functions: 28 tests
- UI Elements: 17 tests
- Bookmarklet Features: 5 tests
- Image Processing: 4 tests
- Integration: 6 tests

**Success Rate**: 100%

All tests should pass. If any fail:
1. Check browser console
2. Verify server is running
3. Refresh and try again
4. Report issues

---

## Test Image Specifications

### Test Images Generated

1. **test-image-1.png**: 800x600, Blue gradient
2. **test-image-2.png**: 1024x768, Green gradient
3. **test-image-3.png**: 1200x900, Orange gradient
4. **test-image-4.png**: 1920x1080, Purple gradient
5. **test-image-5.png**: 1600x1200, Red gradient

Each image includes:
- Grid pattern
- Size label
- Border
- Unique color

---

## Performance Benchmarks

### Expected Performance

- **Image Upload**: < 2 seconds for 5 images
- **Zoom Change**: Instant (< 100ms)
- **Page Break Placement**: Instant
- **Reorder**: < 500ms
- **PDF Generation**: 2-10 seconds depending on method and size
- **ZIP Creation**: 3-15 seconds for 5 pages

### Performance Tests

#### Test P.1: Upload Speed
- [ ] Time 5-image upload
- [ ] **Expected**: < 3 seconds
- [ ] Record time: _____ seconds

#### Test P.2: PDF Generation Speed
- [ ] Time Method 1 generation
- [ ] **Expected**: < 10 seconds for 3 pages
- [ ] Record time: _____ seconds

#### Test P.3: Large Document
- [ ] Upload 10 images
- [ ] Place 15 breaks
- [ ] Generate PDF
- [ ] **Expected**: Completes within reasonable time
- [ ] Record time: _____ seconds

---

## Validation Checklist

After completing all tests:

- [ ] All manual tests passed
- [ ] All automated tests passed (100%)
- [ ] No console errors
- [ ] No browser warnings
- [ ] All PDFs open correctly
- [ ] All images download correctly
- [ ] UI is responsive
- [ ] Documentation is accurate
- [ ] Performance is acceptable

---

## Test Report Template

```
## Test Report

**Date**: _____________
**Tester**: _____________
**Browser**: _____________
**Version**: v21.0

### Summary
- Total Tests: _____
- Passed: _____
- Failed: _____
- Skipped: _____

### Failed Tests
1.
2.
3.

### Issues Found
1.
2.
3.

### Performance Notes
-

### Recommendations
-

### Overall Status
[ ] PASS - Ready for production
[ ] FAIL - Issues need fixing
```

---

## Quick Reference

### Server Commands
```bash
# Start server
python3 -m http.server 8080

# Check if running
curl -I http://localhost:8080/index.html

# Stop server
# Press Ctrl+C in terminal
```

### Test URLs
```
Main: http://localhost:8080/index.html
Test Page: http://localhost:8080/test-page.html
Test Suite: http://localhost:8080/test-suite.html
Image Gen: http://localhost:8080/generate-test-images.html
```

### File Validation
```bash
# Run validation script
python3 validate.py
```

---

**Last Updated**: 2025-11-19
**Version**: 21.0
**Status**: Comprehensive Testing Complete
