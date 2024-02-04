from d_movies import movies

def av(movies):
    a = 0
    cnt = 0
    for i in movies:
        a += i["imdb"]
        cnt += 1
    print(a/cnt)

av(movies)