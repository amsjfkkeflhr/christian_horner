import yaml

dictionary_list = [{
    "company": "WWT",
    "email": "christian.horner@wwt.com",
    "first_name": "Christian",
    "github_username": "AMSJFKKEFLHR",
    "last_name": "Horner"
}]

with open("christian_horner.yaml", 'w') as file:
    yaml.dump(dictionary_list, file)
