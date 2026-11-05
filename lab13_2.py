from worker import WORKER

workers = []

# Введення даних трьох працівників
for i in range(3):
    name = input("Введіть ім'я працівника: ")
    yearborn = int(input("Введіть рік народження працівника: "))
    work_experience = float(input("Введіть стаж роботи: "))

    worker = WORKER(name, yearborn, work_experience)
    workers.append(worker)

# Підрахунок сумарного стажу
print()
total_work = 0

print("Стаж роботи працівників:")
for worker in workers:
    total_work += worker.work_experience
    print(f"{worker.name}: {worker.work_experience} років")

print(f"Загальний стаж роботи: {total_work} років")

# Підрахунок сумарного віку
print()
total_age = 0

print("Вік працівників:")
for worker in workers:
    total_age += worker.CalcAge()
    print(f"{worker.name}: {worker.CalcAge()} років")

print(f"Загальний вік працівників: {total_age} років")
