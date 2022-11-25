# bot.py
import os
import discord
import bs4
import requests
from dotenv import load_dotenv
from datetime import date
from datetime import datetime
from pathlib import Path
import json


# 1
from discord.ext import commands

import main

load_dotenv()

# 2
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    global m
    if message.content == "!fichero":
        base = Path.home()
        rutaFichero = Path(base, 'peliculas.json')
        archivo = open(rutaFichero, 'a')
        url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        movies = soup.select('.top-movie')
        lista2 = []
        for m in movies:
            listaActores = []
            for n in m.select('.mc-right-content .cast .nb a'):
                listaActores.append(n.text)
            pelicula = {
                'Titulo': m.select('.movie-card .mc-right h3 a')[0].attrs['title'],
                'Fecha': m.select('.date')[0].text,
                'Imagen': m.select('.mc-poster img')[0].attrs['src'],
                'Género': m.select('.genre')[0].attrs['title'],
                'Sinopsis': m.select('.synop-text')[0].text,
                'Director': m.select('.director .nb a')[0].text,
                'Reparto': listaActores
            }
            lista2.append(pelicula)
        json.dump(lista2, archivo)
        await message.channel.send(file=discord.file())


    if message.content == "!punto1":
        embed = discord.Embed(title=f"Punto 1", description="Peliculas de hoy:",
                              timestamp=datetime.now(), color=discord.Color.blue())
        await message.channel.send(embed=embed)
        url = 'https://www.filmaffinity.com/es/cat_new_th_es.html'
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        movies = soup.select('.movie-poster')
        fecha = main.obtenerFecha()
        for m in movies:
            if (m.select('.release-text')[0].text == fecha):
                titulo =m.select('.movie-title a')[0].text
                embed2= discord.Embed(title=f"{titulo}", description="Click para ir a la pelicula",
                                      timestamp=datetime.now(), color=discord.Color.blue())
                embed2.add_field(name="Enlace", value=(m.select('a')[0].attrs['href']))
                await message.channel.send(embed=embed2)


    if message.content == "!punto3":
        embed = discord.Embed(title=f"Punto3", description="¿Qué aparatado quieres hacer del punto 3?",
                              timestamp=datetime.now(), color=discord.Color.blue())
        embed.add_field(name="Opción 1", value=("!punto3Fecha"))
        embed.add_field(name="Opción 2", value=("!punto3Genero"))
        await message.channel.send(embed=embed)


    if message.content == "!punto3Fecha":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por fecha",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                sinopsis = m.select('.synop-text')[0].text
                embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                      timestamp=datetime.now(), color=discord.Color.blue())
                embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                embed2.add_field(name="Genero", value=(m.select('.genre')[0].attrs['title']))
                embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                listaActores = []
                for n in m.select('.mc-right-content .cast .nb a'):
                    listaActores.append(n.text)
                embed2.add_field(name="Actores", value=(listaActores))
                await message.channel.send(embed=embed2)

    if message.content == "!punto3Genero":
        embed = discord.Embed(title=f"Punto3Genero", description="¿Qué genero quieres ver?",
                              timestamp=datetime.now(), color=discord.Color.blue())
        embed.add_field(name="Accion", value=("!generoAccion"))
        embed.add_field(name="Animacion", value=("!generoAnimacion"))
        embed.add_field(name="Aventuras", value=("!generoAventuras"))
        embed.add_field(name="Bélico", value=("!generoBelico"))
        embed.add_field(name="Ciencia", value=("!generoCF"))
        embed.add_field(name="Comedia", value=("!generoComedia"))
        embed.add_field(name="Documental", value=("!generoDocumental"))
        embed.add_field(name="Drama", value=("!generoDrama"))
        embed.add_field(name="Fantástico", value=("!generoFantastico"))
        embed.add_field(name="Intriga", value=("!generoIntriga"))
        embed.add_field(name="Romance", value=("!generoRomance"))
        embed.add_field(name="Terror", value=("!generoTerror"))
        embed.add_field(name="Thriller", value=("!generothriller"))
        embed.add_field(name="Western", value=("!generoWestern"))
        await message.channel.send(embed=embed)


    if message.content == "!generoAccion":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Accion",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Acción"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoAnimacion":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Animación",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Animación"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoAventuras":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Aventuras",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Aventuras"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoBelico":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Belico",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Bélico"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoCF":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Ciencia Ficción",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Ciencia ficción"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoDocumental":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Documental",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Documental"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoComedia":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Comedia",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Comedia"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoDrama":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Drama",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Drama"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoFantastico":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Fantastico",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Fantástico"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoIntriga":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Intriga",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Intriga"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoRomance":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Romance",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Romance"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoTerror":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Terror",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Terror"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)

    if message.content == "!generoThriller":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Thriller",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Thriller"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)


    if message.content == "!generoWestern":
            embed = discord.Embed(title=f"Lanzamientos", description="Lanzamientos ordenados por Western",
                              timestamp=datetime.now(), color=discord.Color.blue())
            await message.channel.send(embed=embed)
            url = 'https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
            result = requests.get(url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            movies = soup.select('.top-movie')
            for m in movies:
                genero =m.select('.genre')[0].attrs['title']
                if(genero == "Western"):
                    titulopeli = m.select('.movie-card .mc-right h3 a')[0].attrs['title']
                    sinopsis = m.select('.synop-text')[0].text
                    embed2 = discord.Embed(title=f"{titulopeli}", description=f"{sinopsis}",
                                          timestamp=datetime.now(), color=discord.Color.blue())
                    embed2.add_field(name="Fecha", value=(m.select('.date')[0].text))
                    embed2.add_field(name="Imagen", value=(m.select('.mc-poster img')[0].attrs['src']))
                    embed2.add_field(name="Genero", value=(genero))
                    embed2.add_field(name="Director", value=(m.select('.director .nb a')[0].text))
                    listaActores = []
                    for n in m.select('.mc-right-content .cast .nb a'):
                        listaActores.append(n.text)
                    embed2.add_field(name="Actores", value=(listaActores))
                    await message.channel.send(embed=embed2)
bot.run('MTA0MDE4NDQ2MTk0MzM4MjAyNg.GVmc54.oQVwVlfD1WuQYE50Jss4stcIbE2jvRT1eeZjgM')



