<h1 align="center" id="title">ArchiveTool</h1>

<p id="description">Create and extract archive files using shutil and py7zr.</p>


<h2 align="left">Example</h2>
```python
from archive_tool import make_archive, extract_archive

def success_callback(msg: str):
    print(msg)


def failure_callback(msg: str):
    print(msg)

# Create
make_archive("path/to/input/dir", "path/to/output/dir", "zip", success_callback, failure_callback)

# Extract
extract_archive("path/to/archive/file", "path/to/output/dir", success_callback, failure_callback)
```

<h2 align="left">Requirements</h2>

```
pip install py7zr==0.22.0
```

<h2 align="left">Support</h2>

<p align="left">If you'd like to support my ongoing efforts in sharing fantastic open-source projects, you can contribute by making a donation via PayPal.</p>

<div align="center">
  <a href="https://www.paypal.com/paypalme/iamironman0" target="_blank">
    <img src="https://img.shields.io/static/v1?message=PayPal&logo=paypal&label=&color=00457C&logoColor=white&labelColor=&style=flat" height="40" alt="paypal logo"  />
  </a>
</div>
