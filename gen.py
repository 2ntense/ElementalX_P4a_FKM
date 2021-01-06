import hashlib
import json
import requests

url_latest_version_no = "https://exkernelmanager.com/kernels/sunfish/11/AOSP/latest"
latest_version_no = requests.get(url_latest_version_no).text.strip()
kernel_file = "-".join(latest_version_no.split("-")[1:]) + ".zip"
url_kernel_file = f"https://exkernelmanager.com/kernels/sunfish/11/AOSP/{kernel_file}"

with open(kernel_file, "w+b") as f:
    r = requests.get(url_kernel_file, stream=True)
    for chunk in r.iter_content(chunk_size=128):
        f.write(chunk)

    f.seek(0)
    sha1 = hashlib.sha1()
    while True:
        data = f.read(65536)
        if not data:
            break
        sha1.update(data)

    sha1_checksum = sha1.hexdigest()


output_json = {"kernel": {}, "support": {"link": "https://github.com/2ntense/ElementalX_P4a_FKM"}}
output_json["kernel"]["name"] = "ElementalX for Pixel 4a (sunfish)"
output_json["kernel"]["version"] = latest_version_no
output_json["kernel"]["link"] = url_kernel_file
output_json["kernel"]["changelog_url"] = "https://exkernelmanager.com/kernels/sunfish/11/AOSP/changelog"
output_json["kernel"]["date"] = ""
output_json["kernel"]["sha1"] = sha1_checksum

with open("updater.json", "w") as f:
    json.dump(output_json, f, sort_keys=False, indent=4)
