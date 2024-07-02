# Archive-Tool
Create and extract archive files using shutil and py7zr.

## Examlpe
```python
from archive_tool import make_archive, extract_archive

# Usages

# Create
result = make_archive(dir_path="path/to/input/dir", output_path="path/to/output/dir", archive_format="zip")

# Extract
result = extract_archive(dir_path="path/to/archive/file", output_path="path/to/output/dir")

# Both function will return True if archive/extraction successfull otherwise False.
```

Make sure to install py7zr version: 0.21.1 
```
pip install py7zr==0.21.1
```

###

<h2 align="left">Support</h2>

###

<p align="left">If you'd like to support my ongoing efforts in sharing fantastic open-source projects, you can contribute by making a donation via PayPal.</p>

###

<div align="center">
  <a href="https://www.paypal.com/paypalme/iamironman0" target="_blank">
    <img src="https://img.shields.io/static/v1?message=PayPal&logo=paypal&label=&color=00457C&logoColor=white&labelColor=&style=flat" height="40" alt="paypal logo"  />
  </a>
</div>

###
