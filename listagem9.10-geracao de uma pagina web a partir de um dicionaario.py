filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos"],
    "guerra": ["Rambo","1917","Até o Último Homem"],
    "series_favoritos":["ginny e georgia","sandman","pretendente surpresa","arcane","olympo","bridgerton","Fate: a saga winx","o mundo sombrio de sabrina","eu nunca","celebrity","Emily em paris","com carinho kitty","rainha das lagrimas","steven universo","passarela de sonhos","as tres irmas","perfil falso","the fabulous","o casal perfeito","tore"]
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<p>%s</p>" % e)
página.write("""
</body>
</html>
""")
página.close()