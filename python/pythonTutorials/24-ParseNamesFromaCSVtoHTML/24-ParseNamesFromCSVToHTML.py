import csv
html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    for item in csv_data:
        print(item)

    # We don't want headers or first line of bad data
    # next(csv_data)
    # next(csv_data)
    for line in csv_data:
        if line[0] == 'No Reward':
            break

        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)