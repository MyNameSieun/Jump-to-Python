from car.Car import Car # car 디렉터리 내의 Car.py 모듈에서 Car 클래스를 임포트

car_1 = Car("Hyundai", "Grandeur", 2024, "black")
car_2 = Car("Kia", "Carnival", 2023, "white")

print(f"make={car_1.make}, model={car_1.model}, year={car_1.year}, color={car_1.color}")
car_1.drive()