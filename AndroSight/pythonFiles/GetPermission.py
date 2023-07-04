import os
import xml.etree.ElementTree as ET
from perm_dictionary import permission_dict
from perm_dictionary import component_dict


# Define the path to the decompressed APK folder
apk_folder_path = 'PATH/TO/FOLDER'

# Search for the manifest file
manifest_file_path = os.path.join(apk_folder_path, 'AndroidManifest.xml')

# Check if the manifest file exists
if os.path.exists(manifest_file_path):
    # Parse the manifest file
    tree = ET.parse(manifest_file_path)
    root = tree.getroot()

    # Extract permissions
    permissions = root.findall('.//uses-permission')

    # Print the extracted permissions and their descriptions
    if permissions:
        print("Permissions:\n")
        for permission in permissions:
            name = permission.get('{http://schemas.android.com/apk/res/android}name')
            if name in permission_dict:
                description = permission_dict[name]
                print(f'{name}: {description}')
                print("")
            else:
                print(name)
    else:
        print("No permissions found in the manifest file.")
else:
    print("Manifest file not found.")


def print_components(manifest_file, component_tag, component_dict):
    tree = ET.parse(manifest_file)
    root = tree.getroot()

    namespace = "{http://schemas.android.com/apk/res/android}"

    components = root.findall(".//application/{}".format(component_tag))
    if components:
        print("{}:".format(component_tag.capitalize()))
        for component in components:
            name = component.get(namespace + "name")
            if name in component_dict:
                description = component_dict[name]
                print("{} - {}".format(name, description))
            else:
                print(name)
        print()

# Usage example
apk_folder_path = 'C:\\Users\\hp\\Desktop\\uploaded\\output'
manifest_file_path = os.path.join(apk_folder_path, 'AndroidManifest.xml')

component_tags = ["activity", "service", "receiver", "provider"]

for tag in component_tags:
    print_components(manifest_file_path, tag, component_dict)
