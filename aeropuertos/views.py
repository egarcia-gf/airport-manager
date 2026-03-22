import requests
from django.shortcuts import render, redirect
from django.conf import settings

API_BASE = 'https://airportgap.com/api'
HEADERS = {'Authorization': f'Bearer {settings.AIRPORT_GAP_TOKEN}'}

# Inicio — Buscador
def inicio(request):
    aeropuerto = None
    error = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '').upper().strip()
        response = requests.get(f'{API_BASE}/airports/{codigo}')
        if response.status_code == 200:
            aeropuerto = response.json().get('data', {})
        else:
            error = f'No se encontró el aeropuerto con código {codigo}.'
    return render(request, 'aeropuertos/inicio.html', {
        'aeropuerto': aeropuerto,
        'error': error
    })

# Mis Favoritos
def lista_favoritos(request):
    response = requests.get(f'{API_BASE}/favorites', headers=HEADERS)
    favoritos = response.json().get('data', []) if response.status_code == 200 else []
    return render(request, 'aeropuertos/favoritos.html', {'favoritos': favoritos})

# Agregar Favorito
def agregar_favorito(request):
    if request.method == 'POST':
        airport_id = request.POST.get('airport_id')
        nota = request.POST.get('nota', '')
        print('airport_id:', airport_id)
        print('nota:', nota)
        print('HEADERS:', HEADERS)
        print('TOKEN:', settings.AIRPORT_GAP_TOKEN)
        response = requests.post(
            f'{API_BASE}/favorites',
            headers=HEADERS,
            json={'airport_id': airport_id, 'note': nota}
        )
        print('Status:', response.status_code)
        print('Respuesta:', response.json())
    return redirect('lista_favoritos')

# Eliminar Favorito
def eliminar_favorito(request, favorito_id):
    if request.method == 'POST':
        requests.delete(f'{API_BASE}/favorites/{favorito_id}', headers=HEADERS)
    return redirect('lista_favoritos')

# Calculadora de Distancia
def calcular_distancia(request):
    resultado = None
    error = None
    if request.method == 'POST':
        origen = request.POST.get('origen', '').upper().strip()
        destino = request.POST.get('destino', '').upper().strip()
        response = requests.post(
            f'{API_BASE}/airports/distance',
            json={'from': origen, 'to': destino}
        )
        if response.status_code == 200:
            resultado = response.json().get('data', {})
        else:
            error = 'No se pudo calcular la distancia. Verifica los códigos ingresados.'
    return render(request, 'aeropuertos/distancia.html', {
        'resultado': resultado,
        'error': error
    })

# Comparador de Aeropuertos
def comparar_aeropuertos(request):
    aeropuerto1 = None
    aeropuerto2 = None
    error = None
    if request.method == 'POST':
        codigo1 = request.POST.get('codigo1', '').upper().strip()
        codigo2 = request.POST.get('codigo2', '').upper().strip()
        r1 = requests.get(f'{API_BASE}/airports/{codigo1}')
        r2 = requests.get(f'{API_BASE}/airports/{codigo2}')
        if r1.status_code == 200 and r2.status_code == 200:
            aeropuerto1 = r1.json().get('data', {})
            aeropuerto2 = r2.json().get('data', {})
        else:
            error = 'No se encontró uno o ambos aeropuertos. Verifica los códigos ingresados.'
    return render(request, 'aeropuertos/comparar.html', {
        'aeropuerto1': aeropuerto1,
        'aeropuerto2': aeropuerto2,
        'error': error
    })