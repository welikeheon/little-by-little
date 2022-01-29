def solution(genres, plays):
    answer = []
    
    genre_play_counts = {}  # the number of total play counts per genre
    for g, p in zip(genres, plays):
        genre_play_counts[g] = genre_play_counts.get(g, 0) + p
    
    # sort by given conditions
    tuples = [(genre_play_counts[genres[i]], plays[i], -i, genres[i]) for i in range(len(plays))]
    tuples.sort(reverse=True, key=lambda x:(x[0], x[1], x[2]))
    
    selected_cnt = {}  # how many genres counted for the answer list?
    for i in range(len(tuples)):
        g = tuples[i][3]
        if selected_cnt.get(g, 0) >= 2: # if there are two genres in answer list
            continue
        
        selected_cnt[g] = selected_cnt.get(g, 0) + 1
        answer.append(-tuples[i][2])
    
    return answer