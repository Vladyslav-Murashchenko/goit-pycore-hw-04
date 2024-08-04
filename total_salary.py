def total_salary(path: str) -> tuple[int, float]:
    total_salary = 0
    average_salary = 0.0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                _, salary = line.split(',')
                total_salary += int(salary)

            average_salary = total_salary / len(lines)
    except FileNotFoundError:
        print('File not found')
    except ZeroDivisionError:
        print('File is empty')
    except ValueError:
        print('Invalid data in file')
    except IOError:
        print('Failed to read file')

    return total_salary, average_salary

total, average = total_salary('salary.csv')

print(f'Total salary: {total}')
print(f'Average salary: {average}')
