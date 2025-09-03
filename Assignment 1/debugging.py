# diagnostic.py -- run this in PyCharm (same interpreter that shows the squiggle)
import sys, os
import numpy as np
import importlib

print("=== interpreter ===")
print(sys.executable)
print("cwd:", os.getcwd())
print("sys.path (first 10):")
for p in sys.path[:10]:
    print(" ", p)

print("\n=== check for shadowing files in cwd ===")
print(os.listdir(os.getcwd()))
for name in ("scipy.py", "signal.py", "scipy", "signal"):
    print(f"{name}: exists ->", os.path.exists(os.path.join(os.getcwd(), name)))

print("\n=== scipy info ===")
try:
    import scipy
    import scipy.signal
    print("scipy version:", scipy.__version__)
    print("scipy __file__:", getattr(scipy, "__file__", None))
    print("scipy.signal __file__:", getattr(scipy.signal, "__file__", None))
    print("'convolve2d' in dir(scipy.signal)?", "convolve2d" in dir(scipy.signal))
    print("names involving 'convolve':",
          [n for n in dir(scipy.signal) if 'convolve' in n.lower()])
except Exception as e:
    print("ERROR importing scipy or scipy.signal:", repr(e))

print("\n=== small functional test ===")
try:
    from scipy.signal import convolve2d
    a = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
    k = np.array([[0,1,0],[1,0,1],[0,1,0]], dtype=float)
    print("a:\n", a)
    print("k:\n", k)
    out = convolve2d(a, k, mode='same')
    print("convolve2d(a,k,'same'):\n", out)
except Exception as e:
    print("ERROR calling convolve2d:", repr(e))

print("\n=== image check (your file) ===")
img_path = "Homework 1 image.png"
print("exists:", os.path.exists(img_path))
if os.path.exists(img_path):
    from PIL import Image
    img = Image.open(img_path)
    arr = (np.asarray(img).astype(float) / 255.0)[:, :, :3]
    gray = arr[:, :, 0]
    print("image shape, dtype, min, max:", gray.shape, gray.dtype, np.min(gray), np.max(gray))
    # quick convolution test on your image:
    filt = np.array([[0,0,0],[0,1,0],[0,0,0]], dtype=float)
    print("filter dtype:", filt.dtype)
    print("conv result summary: min, max, mean:",
          np.min(convolve2d(gray, filt, mode='same')),
          np.max(convolve2d(gray, filt, mode='same')),
          np.mean(convolve2d(gray, filt, mode='same')))
else:
    print("Image not found in cwd.")
