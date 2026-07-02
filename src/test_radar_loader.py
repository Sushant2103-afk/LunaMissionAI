"""
Test Radar Loader
"""

import matplotlib.pyplot as plt
import numpy as np

from src.loaders.radar_loader import RadarLoader


loader = RadarLoader(
    r"C:\Users\susha\Desktop\LunarDatasets\DFSAR\data\calibrated\20191019"
)

cube = loader.load()

print("=" * 50)

print("Radar Cube Information")

print("=" * 50)

print("Shape :", cube.shape)
print("Width :", cube.width)
print("Height:", cube.height)

print()

print("HH:", cube.HH.shape)
print("HV:", cube.HV.shape)
print("VH:", cube.VH.shape)
print("VV:", cube.VV.shape)

print()

print("HH Min:", cube.HH.min(), "Max:", cube.HH.max())
print("HV Min:", cube.HV.min(), "Max:", cube.HV.max())
print("VH Min:", cube.VH.min(), "Max:", cube.VH.max())
print("VV Min:", cube.VV.min(), "Max:", cube.VV.max())


def stretch(image):

    vmin = np.percentile(image, 2)
    vmax = np.percentile(image, 98)

    return vmin, vmax


fig, ax = plt.subplots(2, 2, figsize=(12, 12))

channels = [

    ("HH", cube.HH),
    ("HV", cube.HV),
    ("VH", cube.VH),
    ("VV", cube.VV)

]

for axis, (name, img) in zip(ax.ravel(), channels):

    vmin, vmax = stretch(img)

    axis.imshow(
        img,
        cmap="gray",
        vmin=vmin,
        vmax=vmax
    )

    axis.set_title(name)
    axis.axis("off")

plt.tight_layout()

plt.show()

print()

print("=" * 50)

print("Radar Statistics")

print("=" * 50)

stats = cube.statistics()

for channel, values in stats.items():

    print(channel)

    for key, value in values.items():

        print("   ", key, ":", value)