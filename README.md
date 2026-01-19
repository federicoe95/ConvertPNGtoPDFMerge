# ConvertPNGtoPDFMerge
Python script to convert multiple PNG images into a single merged PDF

---------------------------------------------------------------------

This script allows the user to select a folder containing PNG images, converts each image into a PDF, and merges them into a single PDF file.
It prompts the user for the output PDF filename, providing a default suggestion based on a timestamp.
The script validates the filename to prevent invalid characters, empty input, or overwriting existing files, and saves the final PDF in the same folder as the original images.

Key features:

Batch converts PNG files in a folder to PDF.

Merges all generated PDFs into a single document.

User-friendly filename input with default suggestion.

Filename validation for Windows-compatible paths.

Prevents accidental file overwriting.
