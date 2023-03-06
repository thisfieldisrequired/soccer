from django.db import models


class Plane(models.Model):
    manufacturer = models.CharField(max_length=120)  # Производитель
    model = models.CharField(max_length=120)  # Модель
    seats = models.IntegerField()  # Количество мест
    runway_min_lenght = models.IntegerField()  # Минимальная длина полосы


class Airport(models.Model):
    code = models.CharField(max_length=120)  # Код
    country = models.CharField(max_length=120)  # Страна расположения
    city = models.CharField(max_length=120)  # Город расположения
    runway_length = models.IntegerField()  # Длина полосы (м)


class Flight(models.Model):
    number = models.CharField(max_length=120)  # Номер рейса
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, related_name='plane')  # Используемый самолет
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='from_airport')  # Аэропорт вылета
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='to_airport')  # Аэропорт назначения
    passengers_count = models.IntegerField()  # Пассажиров зарегистрировано