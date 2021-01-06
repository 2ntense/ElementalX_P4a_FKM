import json
import requests

url_latest_version_no = "https://exkernelmanager.com/kernels/sunfish/11/AOSP/latest"
latest_version_no = requests.get(url_latest_version_no).text.strip()
kernel_file = "-".join(latest_version_no.split("-")[1:])

output_json = {"kernel": {}, "support": {"link": "https://github.com/2ntense"}}
output_json["kernel"]["name"] = "ElementalX for Pixel 4a (sunfish)"
output_json["kernel"]["version"] = latest_version_no
output_json["kernel"]["link"] = f"https://exkernelmanager.com/kernels/sunfish/11/AOSP/{kernel_file}.zip"
output_json["kernel"]["changelog_url"] = "https://exkernelmanager.com/kernels/sunfish/11/AOSP/changelog"
output_json["kernel"]["date"] = ""
output_json["kernel"]["sha1"] = requests.get(
    "https://exkernelmanager.com/kernels/sunfish/11/AOSP/checksum").text.strip()

with open("updater.json", "w") as f:
    json.dump(output_json, f, sort_keys=False, indent=4)
