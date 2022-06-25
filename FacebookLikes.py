def FacebookLikes(Likes):
    if len(Likes) == 0:
        return "no one likes this"
    elif len(Likes) == 1:
        return f"{Likes} likes this"
    elif len(Likes) == 2:
        return f"{Likes[0]} and {Likes[1]} like this"
    elif len(Likes) == 3:
        return f"{Likes[0]}, {Likes[1]} and {Likes[2]} like this"
    else:
        return f"{Likes[0]}, {Likes[1]} and {len(Likes)-2} others like this"

FacebookLikes(["Alex", "Jacob",'Babucarr','Ali'])