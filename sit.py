import pandas as pd
import xml.etree.ElementTree as ET
import os

def generate_sitemap(excel_path):
    # Load the Excel file
    df = pd.read_excel(excel_path)
    
    # Create the root element of the XML file
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Assuming URLs are in the first column
    for url in df[df.columns[0]]:
        if pd.notna(url):
            url_element = ET.SubElement(urlset, 'url')
            loc = ET.SubElement(url_element, 'loc')
            loc.text = str(url)
    
    # Create a tree from the root element
    tree = ET.ElementTree(urlset)
    
    # Generate the path for the sitemap.xml in the same folder as the Excel file
    sitemap_path = os.path.join(os.path.dirname(excel_path), 'sitemap.xml')
    
    # Write the XML to file
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    
    print(f'Sitemap created at {sitemap_path}')

# Example usage
generate_sitemap(r'C:\vimal\games-html\unblocked-game76\sitemaplist.xlsx')
