from pwn import *
import sys

def ask_for_weight(r, coins):
    req = ''
    for c in coins:
        req += c + ' '
    r.sendline(req)

# running locally on their servers
r = remote('0', 9007)

def play(N, C):
    coins = [str(c) for c in range(N)]
    for play in range(C):
        if len(coins) == 1:
            r.sendline(coins[0])
            r.recvline()
            continue


        coins_to_weight = len(coins)/2
        expected_weight = coins_to_weight * 10


        ask_for_weight(r, coins[:coins_to_weight])
        weight = int(r.recvline())

        #print '\nplay {0}/{1}'.format(play+1, C)
        #print 'coins {0} - {1}'.format(coins[0], coins[coins_to_weight])
        #print 'expected', expected_weight
        #print 'actual', weight

        if weight != expected_weight:
            coins = coins[:coins_to_weight]
        else:
            coins = coins[coins_to_weight:]
    
    r.sendline(coins[0])

points = 0
while points < 100:
    recv = r.recvline_regex("^N=\d+ C=\d+")

    N = int(recv.split(' ')[0][2:])
    C = int(recv.split(' ')[1][2:])

    #print 'N', N, 'C', C

    play(N, C)
    answer = r.recvline()
    print answer

    if 'Correct' in answer:
        points += 1
    else:
        sys.exit(1)

print r.recvline()
print r.recvline()
r.close()