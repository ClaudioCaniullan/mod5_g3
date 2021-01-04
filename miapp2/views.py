
from django.shortcuts import render, redirect
from .forms import PrimerFormulario, Contacto
from django.conf import settings
import json

# Create your views here.

# mostrar index base en el navegador 
def mostrar_base(request):
    return render(request, 'miapp2/index_base.html')



# renderizacion del index extendido

def mostrar_extendido(request):

    # Claudio COMPETENCIAS
    numeros_a = ['1', '2', '3', '4']
    numeros_b = ['5','6','7']

    # Valentina ENLACES 
    linkTitulo='Enlaces de Interés'
    linkrow=[1,2]
    linkcol=[1,2]
    link_range4=[1,2,3,4]
    link_txt0='  Enlaces Tipo '
    link_txt1='Enlace de interés del grupo '
    link_txt2='Ver más'
                
    # Valentina CONTACTO
    conTitulo='Contáctanos'
    con_txtrange={'1':'Nombre','2':'Email','3':'Email'}
    con_txtbtn=['Enviar','Limpiar']

    # Equipo
    equipo = ['Claudio', 'Miguel','Sebastian', 'Valentina', 'Walter']
    
    datos={'numeros_a': numeros_a, 'numeros_b': numeros_b,'linkTitulo':linkTitulo,'linkrows':linkrow,'linkcols':linkcol,'link_range4':link_range4,'link_txt0':link_txt0,'link_txt1':link_txt1,'link_txt2':link_txt2,
    'conTitulo':conTitulo,'con_txtrange':con_txtrange, 'con_txtbtn':con_txtbtn, 'lista_equipo': equipo,'tittle': "Nuestro Equipo"}

    return render(request, 'miapp2/index_extendido.html', context=datos)


# TAREA terminar metodo contacto 
def contacto(request):
    formulario = Contacto(request.POST or None)
    context = {'form': formulario}
    
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        #form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")

        filename= "static/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        #form_data['id'] = guitarras['ultimo_id_generado'] + 1
        #guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['contacto'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        #return redirect('formularios:crear_exitoso')

    return render(request, 'miapp2/contacto.html', context)


# TAREA terminar metodo contador de palabras repetidas 
 def contador_palabras(resquest):
     pass 


# TAREA terminar metodo agregar imagen
 def agregar_imagen(resquest):
     pass


# TAREA terminar metodo agregar contenido de texto
 def agregar_contenido(resquest):
     pass


# CODIGO DEL PROFE 
def crear_guitarra(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}

    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "templates/static/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        form_data['id'] = guitarras['ultimo_id_generado'] + 1
        guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'miapp2/contacto.html', context)


def crear_guitarra_manual(request):
    formulario = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        form_data['fecha_compra']=form_data['fecha_compra'].strftime("%Y-%m-%d")
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            guitarras=json.load(file)
        form_data['id'] = guitarras['ultimo_id_generado'] + 1
        guitarras['ultimo_id_generado'] = form_data['id']
        guitarras['guitarras'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    return render(request, 'formularios/crear_guitarra_manual.html', context)

def crear_exitoso(request):
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
    return render(request, 'formularios/crear_exitoso.html', context=guitarras)

def eliminar_guitarra(request, id):
    if request.method == "POST":
        filename= "/formularios/static/formularios/data/guitarras.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            guitarras=json.load(file)
        for guitarra in guitarras['guitarras']:
            print(int(guitarra['id']), int(id))
            if int(guitarra['id']) == int(id):
                guitarras['guitarras'].remove(guitarra)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(guitarras, file)
        return redirect('formularios:crear_exitoso')
    context = {'id': id} 
    return render(request, "formularios/eliminar_guitarra.html", context)

def grafico2(request):
    lista = []
    filename= "/formularios/static/formularios/data/guitarras.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        guitarras=json.load(file)
        diccionario = guitarras.get('guitarras')
        for elemento in diccionario[-5:]:
            cuerdas = elemento.get('cuerdas')
            lista.append(cuerdas)
    context = {'valor' : lista}
    return render(request, "formularios/grafico2.html", context)

        
        
    
        
