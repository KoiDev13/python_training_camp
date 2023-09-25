n, m = map(int, input().split())

pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]

welcome = 'WELCOME'.center(m, '-')

print('\n'.join(pattern + [welcome] + pattern[::-1]))