import json

with open('data/cities.json', 'r') as json_file1:
    city_data = json_file1.read()
    city_data = json.loads(city_data)
     
with open('data/libraries.json', 'r') as json_file2:
    library_data = json_file2.read()
    library_data = json.loads(library_data)
    
combined = {}
for i,city in enumerate(city_data,1):
    city_name = city['name']
    popu = city['population']
    
    book_total = 0
    for j,library in enumerate(library_data,1):
        if library['city'] == city_name:
            book_total += library['books']
            
    a1 = dict(population=popu, books=book_total)
    combined[city_name] = a1
    
json_str = json.dumps(combined, indent=4)
with open('combined.json', 'w') as json_file:
    json_file.write(json_str)