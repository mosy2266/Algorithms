def solution(genres, plays):
    answer = []
    genre_dict = {}
    song_cnt = len(genres)
    
    for i in range(song_cnt):
        if genres[i] in genre_dict.keys():
            genre_dict[genres[i]][0] += plays[i]
            genre_dict[genres[i]].append((plays[i], i))
        else:
            genre_dict[genres[i]] = [plays[i],(plays[i],i)]
    
    songs=[]
    for key in genre_dict.keys():
        songs.append(genre_dict[key])
    
    songs.sort(key= lambda x: x[0], reverse=True)

    print(songs)
    
    honor=[]
    for song in songs:
        sorted_songs = sorted(song[1:], key= lambda x: x[0], reverse=True)
        if len(sorted_songs)>1:
            honor += sorted_songs[:2]
        else:
            honor += sorted_songs
    
    for h in honor:
        answer.append(h[1])
        
    return answer