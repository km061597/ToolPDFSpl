#!/usr/bin/env python3
"""
Validation script for Page Capture Tool v21.0
Checks if all required functions and elements are present in index.html
"""

import re
import sys

def validate_html_file(filepath):
    """Validate the HTML file for required components"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print("=" * 60)
    print("Page Capture Tool v21.0 - Validation")
    print("=" * 60)

    # Check for required JavaScript functions
    required_functions = [
        'switchTab',
        'showLoading',
        'hideLoading',
        'selectMethod',
        'generateBookmarklet',
        'copyCode',
        'generateScreenshotBookmarklet',
        'copyScreenshotCode',
        'setZoom',
        'handleFiles',
        'renderReorderUI',
        'applyReorder',
        'renderVirtualCanvas',
        'removeImage',
        'clearAllImages',
        'clearAllBreaks',
        'addPageBreak',
        'renderPageBreaks',
        'autoBreak',
        'updateStats',
        'generatePDF',
        'generatePageImages',
        'generateMethod1Preview',
        'generateMethod2ZIP',
        'generateMethod3Individual',
        'generateMethod4DirectPDF',
        'downloadPreviewAsPDF',
        'closePreview'
    ]

    # Check for required HTML elements
    required_elements = [
        'uploadArea',
        'fileInput',
        'imageSection',
        'virtualCanvas',
        'canvasInner',
        'statsBox',
        'reorderSection',
        'reorderList',
        'loadingOverlay',
        'pdfPreview',
        'previewPages',
        'selectorInput',
        'scaleSelect',
        'formatSelect',
        'bookmarkletCode',
        'outputBox',
        'screenshotCode',
        'screenshotOutput'
    ]

    # Check for required libraries
    required_libraries = [
        'jszip',
        'jspdf'
    ]

    print("\n[1] Checking JavaScript Functions...")
    missing_functions = []
    for func in required_functions:
        pattern = f'function {func}\\s*\\('
        if re.search(pattern, content):
            print(f"  ✓ {func}")
        else:
            print(f"  ✗ {func} - MISSING")
            missing_functions.append(func)

    print(f"\n  Functions: {len(required_functions) - len(missing_functions)}/{len(required_functions)} found")

    print("\n[2] Checking HTML Elements...")
    missing_elements = []
    for element in required_elements:
        pattern = f'id=["\']?{element}["\']?'
        if re.search(pattern, content):
            print(f"  ✓ {element}")
        else:
            print(f"  ✗ {element} - MISSING")
            missing_elements.append(element)

    print(f"\n  Elements: {len(required_elements) - len(missing_elements)}/{len(required_elements)} found")

    print("\n[3] Checking External Libraries...")
    missing_libraries = []
    for lib in required_libraries:
        if lib.lower() in content.lower():
            print(f"  ✓ {lib}")
        else:
            print(f"  ✗ {lib} - MISSING")
            missing_libraries.append(lib)

    print(f"\n  Libraries: {len(required_libraries) - len(missing_libraries)}/{len(required_libraries)} found")

    # Check for AppState object
    print("\n[4] Checking Application State...")
    if 'const AppState' in content or 'var AppState' in content:
        print("  ✓ AppState object defined")

        # Check for AppState properties
        state_props = ['images', 'imageHeights', 'totalHeight', 'maxWidth',
                      'pageBreaks', 'selectedMethod', 'zoomMode', 'imageFileNames']
        for prop in state_props:
            if f'{prop}:' in content or f'{prop} :' in content:
                print(f"    ✓ {prop}")
    else:
        print("  ✗ AppState object - MISSING")

    # Check for event listeners
    print("\n[5] Checking Event Listeners...")
    event_listeners = [
        'DOMContentLoaded',
        'dragover',
        'dragleave',
        'drop',
        'click',
        'mousemove',
        'mouseup',
        'mousedown',
        'change'
    ]

    for listener in event_listeners:
        if listener in content:
            print(f"  ✓ {listener}")

    # Check for CSS classes
    print("\n[6] Checking CSS Classes...")
    css_classes = [
        'container',
        'header',
        'tabs',
        'tab',
        'tab-content',
        'upload-area',
        'image-container',
        'virtual-image',
        'page-break',
        'btn',
        'loading-overlay',
        'zoom-controls',
        'method-card',
        'reorder-section'
    ]

    for css_class in css_classes:
        pattern = f'\\.{css_class}\\s*\\{{'
        if re.search(pattern, content):
            print(f"  ✓ .{css_class}")

    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    total_issues = len(missing_functions) + len(missing_elements) + len(missing_libraries)

    if total_issues == 0:
        print("✓ ALL CHECKS PASSED")
        print(f"✓ File size: {len(content):,} bytes")
        print("✓ Ready for deployment")
        return True
    else:
        print(f"✗ {total_issues} ISSUES FOUND:")
        if missing_functions:
            print(f"  - {len(missing_functions)} missing functions")
        if missing_elements:
            print(f"  - {len(missing_elements)} missing elements")
        if missing_libraries:
            print(f"  - {len(missing_libraries)} missing libraries")
        return False

if __name__ == '__main__':
    filepath = 'index.html'

    try:
        success = validate_html_file(filepath)
        sys.exit(0 if success else 1)
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
