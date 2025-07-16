import requests
import json
import csv

# Download the latest MITRE ATT&CK Enterprise matrix JSON
url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
response = requests.get(url)
data = response.json()

# Map tactic shortname to full tactic name
tactic_map = {
    obj["x_mitre_shortname"]: obj["name"]
    for obj in data["objects"]
    if obj["type"] == "x-mitre-tactic"
}

rows = []

# Loop through all attack patterns (techniques)
for obj in data["objects"]:
    if obj["type"] == "attack-pattern" and not obj.get("revoked", False):
        tid, url = "", ""
        for ref in obj.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                tid = ref.get("external_id", "")
                url = ref.get("url", "")
        name = obj.get("name", "")
        description = obj.get("description", "").replace("\n", " ").strip()

        # Get full tactic names for this technique
        tactic_names = []
        for t in obj.get("kill_chain_phases", []):
            if t.get("kill_chain_name") == "mitre-attack":
                shortname = t.get("phase_name")
                if shortname in tactic_map:
                    tactic_names.append(tactic_map[shortname])

        rows.append({
            "Technique ID": tid,
            "Name": name,
            "Tactics": ", ".join(tactic_names),
            "Description": description,
            "URL": url
        })

# Save to CSV
csv_filename = "mitre_attack_documentation.csv"
with open(csv_filename, mode="w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f" MITRE ATT&CK techniques saved to: {csv_filename}")
