import xml.etree.ElementTree as ET
import sys

def xml_to_markdown(xml_file):
    # Parse the XML file
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError:
        print(f"Error: The file '{xml_file}' is not a valid XML file.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: The file '{xml_file}' does not exist.")
        sys.exit(1)

    # Extract the namespace from the root tag
    namespace = {'ns': root.tag.split('}')[0].strip('{')}

    # Find the DNS records in the XML
    records = []
    for host in root.findall(".//ns:host", namespace):
        record = {
            "Name": host.attrib.get("Name"),
            "Type": host.attrib.get("Type"),
            "Address": host.attrib.get("Address"),
            "MXPref": host.attrib.get("MXPref", "N/A"),
            "TTL": host.attrib.get("TTL", "N/A")
        }
        records.append(record)

    if not records:
        print("No DNS records found in the XML file.")
        return

    # Generate Markdown table
    markdown_table = "| Name | Type | Address | MX Pref | TTL |\n"
    markdown_table += "|------|------|---------|---------|-----|\n"
    for record in records:
        markdown_table += f"| {record['Name']} | {record['Type']} | {record['Address']} | {record['MXPref']} | {record['TTL']} |\n"

    # Output the Markdown table
    print("DNS Records in Markdown table format:")
    print(markdown_table)

if __name__ == "__main__":
    # Ensure a file name is provided
    if len(sys.argv) != 2:
        print("Usage: python xml_to_md.py <filename.xml>")
        sys.exit(1)

    # Get the file name from the command line arguments
    xml_file = sys.argv[1]

    # Convert the XML file to a Markdown table
    xml_to_markdown(xml_file)
