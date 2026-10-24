def solution(m, musicinfos):
    answer = '(None)'
    
    def time_to_minute(time):
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute
    
    def convert_melody(melody):
        note = {'C#':'H', 'D#':'I', 'E#':'J', 'F#':'K', 'G#':'L', 'A#':'M', 'B#':'N'}
        
        i = 0
        converted = ''
        while i < len(melody):
            if i < len(melody)-1 and melody[i] + melody[i+1] in note:
                converted += note[melody[i]+melody[i+1]]
                i += 2
            else:
                converted += melody[i]
                i += 1
                
        return converted
    
    max_time = 0
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(",")
        song = convert_melody(melody)
        m = convert_melody(m)
        
        runtime = time_to_minute(end) - time_to_minute(start)
        songtime = len(song)
        
        if runtime < songtime:
            song = song[:runtime]
        else:
            song = (runtime//songtime) * song + song[:runtime%songtime]
        
        if m in song and runtime > max_time:
            answer = name
            max_time = runtime
        
    return answer