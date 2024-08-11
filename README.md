# Namecheap DNS to Markdown
Namecheap DNS to Markdown Converter

## Description
`namecheap-to-md.py` is a Python script that converts DNS records exported from Namecheap in XML format into a Markdown table. This script is particularly useful for documenting DNS settings or sharing them in a readable format.

## Features
- Parses DNS records from an XML file exported from Namecheap.
- Converts the DNS records into a Markdown table.
- Handles XML namespaces for correct parsing.
- Simple to use with command-line arguments.

## Installation
1. Clone the Repository:

   ```bash
   git clone https://github.com/marksowell/namecheap-to-md.git
   cd namecheap-to-md
   ```
2. Python Requirements:
   - This script requires Python 3.6+ to run.
   - No external dependencies are required.

## How to Export DNS Records from Namecheap
Before using the script, you need to export your DNS records from Namecheap using their API. Follow these steps:

1. Get Your Namecheap API Credentials:

   - Log in to your Namecheap account.
   - Navigate to the API Access page to find your API username, API key, and whitelist your IP address.
2. Use the API to Export DNS Records:

   - Run the following curl command in your terminal, replacing the placeholders with your actual API credentials and domain details:

     ```bash
     curl -X GET "https://api.namecheap.com/xml.response?ApiUser=yourApiUser&ApiKey=yourApiKey&UserName=yourUserName&Command=namecheap.domains.dns.getHosts&ClientIp=yourWhitelistedIP&SLD=yourDomainName&TLD=com" -o dns_records.xml
     ```
   - This will save your DNS records to a file named dns_records.xml.

## Usage
1. Run the Script:

   - Use the script to convert the exported XML file into a Markdown table:

     ```bash
     python namecheap-to-md.py dns_records.xml
     ```
2. View the Output:

   - The script will output the DNS records in Markdown format directly to the terminal. You can copy this output into your documentation or a Markdown file.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a suggestion.
