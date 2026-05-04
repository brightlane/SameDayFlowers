from xml.etree.ElementTree import Element, SubElement, tostring

def add_to_sitemap(url):
    sitemap_file = "sitemap.xml"

    if not os.path.exists(sitemap_file):
        root = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    else:
        import xml.etree.ElementTree as ET
        tree = ET.parse(sitemap_file)
        root = tree.getroot()

    url_el = SubElement(root, "url")
    loc = SubElement(url_el, "loc")
    loc.text = url

    lastmod = SubElement(url_el, "lastmod")
    lastmod.text = date_str

    with open(sitemap_file, "wb") as f:
        f.write(tostring(root))
