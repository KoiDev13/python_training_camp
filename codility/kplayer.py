def solution(S,A):
    message = S[0]
    while A[0] != 0:
        next_player = A[0]
        message += S[next_player]
        A = A[1:] + [next_player]
    return message

S = "cdeo"
A = [3,2,0,1]
message = solution(S,A)
print(message)
