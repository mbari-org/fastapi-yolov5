import yaml
with open('custom_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

class_names = config['names']

# Write file names to a text file
with open("labels.txt", "w") as file:
    for name in class_names:
        file.write(name + "\n")
        print(name)

print("File names written to names.txt")
