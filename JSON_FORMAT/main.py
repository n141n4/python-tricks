import json
playlist = {}
playlist["mpanakanto"] = "Nael"
playlist["hira"] = []
playlist["hira"].append("Hiaretako avao")
playlist["hira"].append("Jarina")

#print(playlist)

# Demander au module de transposer notre dictionnaire au format JSON
# json.dump(objet)

print(json.dumps(playlist, indent=4))

# sérialiser dans un fichier
with open('playlist.json', 'w', encoding='utf-8') as fichier:
    json.dump(playlist, fichier, indent=4)

with open('playlist')