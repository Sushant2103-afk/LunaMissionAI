from loaders.xml_loader import XMLLoader
import xml.etree.ElementTree as ET

tree = ET.parse(
    r"C:\Users\susha\Desktop\LunarDatasets\DFSAR\data\calibrated\20191019\ch2_sar_ncxl_20191019t215745389_d_sri_xx_fp_xx_d18.xml"
)

root = tree.getroot()


def print_tree(element, level=0):

    tag = element.tag.split("}")[-1]

    print("   " * level + tag)

    for child in element:

        print_tree(child, level + 1)


print_tree(root)