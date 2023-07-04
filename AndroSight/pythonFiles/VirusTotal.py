import os
import requests


def check_apk_with_virustotal(file_path, api_key):
    # Create a dictionary with the API key and the resource (file) to be scanned
    params = {
        'apikey': api_key
    }
    files = {
        'file': open(file_path, 'rb')
    }

    # Send the file to VirusTotal for scanning
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
    response_json = response.json()

    # Retrieve the scan ID from the response
    scan_id = response_json.get('scan_id')

    if scan_id:
        # Check the scan report using the provided scan ID
        params = {
            'apikey': api_key,
            'resource': scan_id
        }
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        report = response.json()

        # Print the status report
        print(f"Scan ID: {scan_id}")
        print(f"SHA-256: {report.get('sha256')}")
        print(f"Scan Date: {report.get('scan_date')}")
        print(f"Total Scans: {report.get('total')}")

        positives = report.get('positives')
        total = report.get('total')

        if positives is not None and total is not None:
            print(f"Detection Ratio: {positives}/{total}")

            if positives > 0:
                print("Status: Malicious")
            else:
                print("Status: Clean")
        else:
            print("Status: Unknown")
    else:
        print("Error: Failed to upload the file to VirusTotal.")

# Provide the folder path and API key
apk_folder_path = 'PATH/TO/FOLDER'
api_key = 'YOUR VIRUSTOTAL API KEY HERE'

# Search for APK files in the folder
apk_files = [file for file in os.listdir(apk_folder_path) if file.endswith('.apk')]

# Process each APK file and retrieve the status report
for apk_file in apk_files:
    apk_file_path = os.path.join(apk_folder_path, apk_file)
    print(f"Processing: {apk_file}")
    check_apk_with_virustotal(apk_file_path, api_key)
    print()
