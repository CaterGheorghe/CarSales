from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.apps import apps
import pymysql

from .forms import CarForm


def connection():
    s = 'localhost'  # Your server name
    d = 'carsales'
    u = 'root'  # Your login
    p = 'xxxxxx'  # Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn


def carslist(request):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "body_type": row[1], "brand": row[2], "model": row[3],"fuel": row[4],
                     "year":row[5], "kilometres": row[6],"price": row[7]})
    conn.close()
    return render(request, 'carslist.html', {'cars': cars})


def addcar(request):
    if request.method == 'GET':
        return render(request, 'addcar.html', {'car': {}})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            body_type = form.cleaned_data.get("body_type")
            brand = form.cleaned_data.get("brand")
            model = form.cleaned_data.get("model")
            fuel = form.cleaned_data.get("fuel")
            year = form.cleaned_data.get("year")
            kilometres = form.cleaned_data.get("kilometres")
            price = form.cleaned_data.get("price")
        conn = connection()
        cursor = conn.cursor()
        # print(form.cleaned_data.get("id"))
        cursor.execute("INSERT INTO TblCars ( id, body_type, brand, model, fuel, year,kilometres, price) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s)", (id, body_type, brand, model, fuel, year,kilometres, price))
        conn.commit()
        conn.close()
        return redirect('carslist')


def updatecar(request, id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblCars WHERE id = %s", (id))
        print("id: " + str(id))

        for row in cursor.fetchall():
            cr.append({"id": row[0], "body_type": row[1], "brand": row[2], "model": row[3],"fuel": row[4],
                     "year":row[5], "kilometres": row[6],"price": row[7]})
        conn.close()
        return render(request, 'addcar.html', {'car': cr[0]})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            body_type = form.cleaned_data.get("body_type")
            brand = form.cleaned_data.get("brand")
            model = form.cleaned_data.get("model")
            fuel = form.cleaned_data.get("fuel")
            year = form.cleaned_data.get("year")
            kilometres = form.cleaned_data.get("kilometres")
            price = form.cleaned_data.get("price")
            cursor.execute("UPDATE TblCars SET body_type = %s, brand = %s, model =%s, fuel =%s, year = %s, "
                           "kilometres =%s, price = %s WHERE id = %s", (body_type,brand,model, fuel, year, kilometres,
                                                                        price, id))
            conn.commit()
        conn.close()
        return redirect('carslist')


def deletecar(request, id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect('carslist')
