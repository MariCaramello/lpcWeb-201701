from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):
    html = """<h1>Animais</h1>
                <ul>
                    <li><a href='/listaanimais'>Registro de Animais</a></li>
                </ul>
                <text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vel justo nec diam venenatis fringilla.<br>
                    Sed vel nibh vitae risus tristique vestibulum. Donec dignissim ultrices pellentesque. Fusce porttitor sem ut <br>
                     eros hendrerit lacinia. Donec et imperdiet ante. Praesent eleifend enim at turpis accumsan viverra. <br>
                     Aliquam id nulla quam. Praesent sit amet blandit velit. In sodales, purus at sollicitudin pellentesque, <br>
                     velit risus venenatis urna, a rhoncus dui sapien ut lectus. Vivamus at varius ligula, sed scelerisque enim. <br>
                     Proin elementum egestas rhoncus. Duis imperdiet, ex nec lobortis sagittis, magna ipsum feugiat eros, sit amet <br>
                      ultricies nulla tortor id magna. Nulla vestibulum nulla eget consequat placerat. Sed lobortis lorem nec venenatis<br>
                       sodales. Pellentesque et mi dignissim, dapibus turpis eget, vehicula turpis.
                </text>
            """
    return HttpResponse(html)

def listaanimais(request):
    html = """<h1>Animais</h1>
                            <ul>
                                <li><a href='/listaanimais'>Registro de Animais</a></li>
                                <li><a href='/listapeixes'>Peixes</a></li>
                                <li><a href='/listaanfibios'>Anfíbios</a></li>
                                <li><a href='/listarepteis'>Repteis</a></li>
                                <li><a href='/listaaves'>Aves</a></li>
                                <li><a href='/listamamiferos'>Mamíferos</a></li>
                            </ul>
                                <h2>Lista de Animais</h2>
                    """
    lista = Animal.objects.all()
    for aaa in lista:
        html += '<li>Nome: {}</li>'.format(aaa.nome)
        html += '<li>Locomoção: {}</li>'.format(aaa.locomocao)
        html += '<li>Respiração: {}</li>'.format(aaa.respiracao)
        html += '<li>Reprodução: {}</li>'.format(aaa.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(aaa.tipohabitat)
        html += '______________________________________________'

    return HttpResponse(html)

def listapeixes(request):
    html = """<h1>Animais</h1>
                        <ul>
                            <li><a href='/listaanimais'>Registro de Animais</a></li>
                            <li><a href='/listapeixes'>Peixes</a></li>
                            <li><a href='/listaanfibios'>Anfíbios</a></li>
                            <li><a href='/listarepteis'>Repteis</a></li>
                            <li><a href='/listaaves'>Aves</a></li>
                            <li><a href='/listamamiferos'>Mamíferos</a></li>
                        </ul>
                            <h2>Lista de Peixes</h2>
                """
    peixes = Peixe.objects.all()
    for p in peixes:
        html += '<li>Nome: {}</li>'.format(p.nome)
        html += '<li>Tipo de peixe: {}</li>'.format(p.nomepeixe)
        html += '<li>Locomoção: {}</li>'.format(p.locomocao)
        html += '<li>Respiração: {}</li>'.format(p.respiracao)
        html += '<li>Reprodução: {}</li>'.format(p.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(p.tipohabitat)
        html += '<li>Nadadeiras: {}</li>'.format(p.tipohabitat)
        html += '<li>Possui escamas?: {}</li>'.format(p.escama)
        html += '______________________________________________'
    return HttpResponse(html)

def listaanfibios(request):
    html = """<h1>Animais</h1>
                        <ul>
                            <li><a href='/listaanimais'>Registro de Animais</a></li>
                            <li><a href='/listapeixes'>Peixes</a></li>
                            <li><a href='/listaanfibios'>Anfíbios</a></li>
                            <li><a href='/listarepteis'>Repteis</a></li>
                            <li><a href='/listaaves'>Aves</a></li>
                            <li><a href='/listamamiferos'>Mamíferos</a></li>
                        </ul>
                            <h2>Lista de Anfíbios</h2>
                """
    anfibios = Anfibio.objects.all()
    for an in anfibios:
        html += '<li>Nome: {}</li>'.format(an.nome)
        html += '<li>Tipo de anfíbio: {}</li>'.format(an.nomeanfibio)
        html += '<li>Locomoção: {}</li>'.format(an.locomocao)
        html += '<li>Respiração: {}</li>'.format(an.respiracao)
        html += '<li>Reprodução: {}</li>'.format(an.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(an.tipohabitat)
        html += '<li>Cauda: {}</li>'.format(an.cauda)
        html += '______________________________________________'
    return HttpResponse(html)

def listarepteis(request):
    html = """<h1>Animais</h1>
                        <ul>
                            <li><a href='/listaanimais'>Registro de Animais</a></li>
                            <li><a href='/listapeixes'>Peixes</a></li>
                            <li><a href='/listaanfibios'>Anfíbios</a></li>
                            <li><a href='/listarepteis'>Repteis</a></li>
                            <li><a href='/listaaves'>Aves</a></li>
                            <li><a href='/listamamiferos'>Mamíferos</a></li>
                        </ul>
                            <h2>Lista de Répteis</h2>
                """
    repteis = Repteis.objects.all()
    for r in repteis:
        html += '<li>Nome: {}</li>'.format(r.nome)
        html += '<li>Tipo de réptil: {}</li>'.format(r.nomerepteis)
        html += '<li>Locomoção: {}</li>'.format(r.locomocao)
        html += '<li>Respiração: {}</li>'.format(r.respiracao)
        html += '<li>Reprodução: {}</li>'.format(r.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(r.tipohabitat)
        html += '<li>Classe: {}</li>'.format(r.classe)
        html += '______________________________________________'
    return HttpResponse(html)

def listaaves(request):
    html = """<h1>Animais</h1>
                        <ul>
                            <li><a href='/listaanimais'>Registro de Animais</a></li>
                            <li><a href='/listapeixes'>Peixes</a></li>
                            <li><a href='/listaanfibios'>Anfíbios</a></li>
                            <li><a href='/listarepteis'>Repteis</a></li>
                            <li><a href='/listaaves'>Aves</a></li>
                            <li><a href='/listamamiferos'>Mamíferos</a></li>
                        </ul>
                            <h2>Lista de Aves</h2>
                """
    aves = Ave.objects.all()
    for av in aves:
        html += '<li>Nome: {}</li>'.format(av.nome)
        html += '<li>Tipo de ave: {}</li>'.format(av.nomeave)
        html += '<li>Locomoção: {}</li>'.format(av.locomocao)
        html += '<li>Respiração: {}</li>'.format(av.respiracao)
        html += '<li>Reprodução: {}</li>'.format(av.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(av.tipohabitat)
        html += '<li>Voa?: {}</li>'.format(av.voa)
        html += '______________________________________________'
    return HttpResponse(html)

def listamamiferos(request):
    html = """<h1>Animais</h1>
                    <ul>
                        <li><a href='/listaanimais'>Registro de Animais</a></li>
                        <li><a href='/listapeixes'>Peixes</a></li>
                        <li><a href='/listaanfibios'>Anfíbios</a></li>
                        <li><a href='/listarepteis'>Repteis</a></li>
                        <li><a href='/listaaves'>Aves</a></li>
                        <li><a href='/listamamiferos'>Mamíferos</a></li>
                    </ul>
                        <h2>Lista de Mamíferos</h2>
            """
    mamiferos = Mamifero.objects.all()
    for m in mamiferos:
        html += '<li>Nome: {}</li>'.format(m.nome)
        html += '<li>Tipo de mamífero: {}</li>'.format(m.nomemamifero)
        html += '<li>Locomoção: {}</li>'.format(m.locomocao)
        html += '<li>Respiração: {}</li>'.format(m.respiracao)
        html += '<li>Reprodução: {}</li>'.format(m.tiporeproducao)
        html += '<li>Habitat: {}</li>'.format(m.tipohabitat)
        html += '<li>Possio pelo?: {}</li>'.format(m.pelo)
        html += '______________________________________________'
    return HttpResponse(html)




