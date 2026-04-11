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
#Traducción de países
TRADUCCION_PAISES = {
    # América del Norte
    'mexico': 'mexico',
    'méxico': 'mexico',
    'estados unidos': 'united states',
    'canada': 'canada',
    'canadá': 'canada',

    # América Central
    'cuba': 'cuba',
    'panama': 'panama',
    'panamá': 'panama',
    'costa rica': 'costa rica',
    'guatemala': 'guatemala',
    'honduras': 'honduras',
    'nicaragua': 'nicaragua',
    'el salvador': 'el salvador',
    'belize': 'belize',
    'belice': 'belize',
    'haiti': 'haiti',
    'haití': 'haiti',
    'jamaica': 'jamaica',
    'república dominicana': 'dominican republic',
    'republica dominicana': 'dominican republic',
    'puerto rico': 'puerto rico',
    'trinidad': 'trinidad and tobago',

    # América del Sur
    'brasil': 'brazil',
    'argentina': 'argentina',
    'colombia': 'colombia',
    'chile': 'chile',
    'perú': 'peru',
    'peru': 'peru',
    'venezuela': 'venezuela',
    'ecuador': 'ecuador',
    'bolivia': 'bolivia',
    'paraguay': 'paraguay',
    'uruguay': 'uruguay',
    'guyana': 'guyana',
    'surinam': 'suriname',
    'suriname': 'suriname',

    # Europa
    'españa': 'spain',
    'espana': 'spain',
    'francia': 'france',
    'alemania': 'germany',
    'italia': 'italy',
    'portugal': 'portugal',
    'holanda': 'netherlands',
    'países bajos': 'netherlands',
    'paises bajos': 'netherlands',
    'suecia': 'sweden',
    'noruega': 'norway',
    'dinamarca': 'denmark',
    'suiza': 'switzerland',
    'austria': 'austria',
    'belgica': 'belgium',
    'bélgica': 'belgium',
    'grecia': 'greece',
    'polonia': 'poland',
    'rusia': 'russia',
    'ucrania': 'ukraine',
    'rumania': 'romania',
    'rumanía': 'romania',
    'hungria': 'hungary',
    'hungría': 'hungary',
    'chequia': 'czech republic',
    'república checa': 'czech republic',
    'republica checa': 'czech republic',
    'eslovaquia': 'slovakia',
    'croacia': 'croatia',
    'serbia': 'serbia',
    'finlandia': 'finland',
    'irlanda': 'ireland',
    'escocia': 'scotland',
    'reino unido': 'united kingdom',
    'inglaterra': 'united kingdom',
    'turquia': 'turkey',
    'turquía': 'turkey',
    'bulgaria': 'bulgaria',
    'eslovenia': 'slovenia',
    'luxemburgo': 'luxembourg',
    'malta': 'malta',
    'chipre': 'cyprus',
    'islandia': 'iceland',

    # Asia
    'japón': 'japan',
    'japon': 'japan',
    'china': 'china',
    'india': 'india',
    'corea del sur': 'south korea',
    'corea': 'south korea',
    'corea del norte': 'north korea',
    'tailandia': 'thailand',
    'vietnam': 'vietnam',
    'indonesia': 'indonesia',
    'malasia': 'malaysia',
    'filipinas': 'philippines',
    'singapur': 'singapore',
    'bangladesh': 'bangladesh',
    'pakistan': 'pakistan',
    'pakistán': 'pakistan',
    'afganistan': 'afghanistan',
    'afganistán': 'afghanistan',
    'iran': 'iran',
    'irán': 'iran',
    'irak': 'iraq',
    'arabia saudi': 'saudi arabia',
    'arabia saudí': 'saudi arabia',
    'emiratos arabes': 'united arab emirates',
    'emiratos árabes': 'united arab emirates',
    'israel': 'israel',
    'jordan': 'jordan',
    'jordania': 'jordan',
    'siria': 'syria',
    'libano': 'lebanon',
    'líbano': 'lebanon',
    'nepal': 'nepal',
    'myanmar': 'myanmar',
    'camboya': 'cambodia',
    'mongolia': 'mongolia',
    'kazajistan': 'kazakhstan',
    'kazajistán': 'kazakhstan',

    # África
    'marruecos': 'morocco',
    'egipto': 'egypt',
    'nigeria': 'nigeria',
    'sudáfrica': 'south africa',
    'sudafrica': 'south africa',
    'kenia': 'kenya',
    'etiopía': 'ethiopia',
    'etiopia': 'ethiopia',
    'ghana': 'ghana',
    'tanzania': 'tanzania',
    'angola': 'angola',
    'mozambique': 'mozambique',
    'camerun': 'cameroon',
    'camerún': 'cameroon',
    'senegal': 'senegal',
    'costa de marfil': 'ivory coast',
    'madagascar': 'madagascar',
    'zambia': 'zambia',
    'zimbabue': 'zimbabwe',
    'libia': 'libya',
    'argelia': 'algeria',
    'túnez': 'tunisia',
    'tunez': 'tunisia',
    'sudan': 'sudan',
    'sudán': 'sudan',

    # Oceanía
    'australia': 'australia',
    'nueva zelanda': 'new zealand',
    'nueva zelandia': 'new zealand',
    'papua nueva guinea': 'papua new guinea',
    'fiji': 'fiji',
}
# Búsqueda por país
def buscar_por_pais(request):
    aeropuertos = []
    pais = None
    error = None
    pagina_actual = int(request.GET.get('pagina', 1))
    resultados_por_pagina = 10

    if request.method == 'POST':
        pais = request.POST.get('pais', '').strip()
        request.session['pais'] = pais
    elif 'pagina' in request.GET:
        pais = request.session.get('pais', None)
    else:
        request.session.pop('pais', None)
        pais = None

    if pais:
        pais_busqueda = TRADUCCION_PAISES.get(pais.lower(), pais.lower())
        todos_aeropuertos = []
        pagina = 1
        while True:
            response = requests.get(f'{API_BASE}/airports?page={pagina}')
            if response.status_code != 200:
                break
            data = response.json().get('data', [])
            if not data:
                break
            coincidencias = [
                a for a in data
                if pais_busqueda.lower() in a['attributes']['country'].lower()
            ]
            todos_aeropuertos.extend(coincidencias)
            pagina += 1

        total = len(todos_aeropuertos)
        inicio = (pagina_actual - 1) * resultados_por_pagina
        fin = inicio + resultados_por_pagina
        aeropuertos = todos_aeropuertos[inicio:fin]
        total_paginas = (total + resultados_por_pagina - 1) // resultados_por_pagina

        if not todos_aeropuertos:
            error = f'No se encontraron aeropuertos en "{pais}".'
    else:
        total_paginas = 0
        total = 0

    return render(request, 'aeropuertos/pais.html', {
        'aeropuertos': aeropuertos,
        'pais': pais,
        'error': error,
        'pagina_actual': pagina_actual,
        'total_paginas': total_paginas,
        'total': total,
    })