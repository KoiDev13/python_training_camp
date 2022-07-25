"""
Exercise 3: Slice list into 3 equal chunks and reverse each chunk
"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

lenght=len(sample_list)
chunk_size=int(lenght/3)
start = 0
end = chunk_size

start = 0
for i in range(3):
    indexes = slice(start,end)
    #get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size