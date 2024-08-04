def get_cats_info(path: str) -> list[dict]:
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                cat_id, name, age = line.split(',')
                cats_info.append({
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                })
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Invalid data in file')
    except IOError:
        print('Failed to read file')

    return cats_info

cats_info = get_cats_info('cats.csv')
print(cats_info)
