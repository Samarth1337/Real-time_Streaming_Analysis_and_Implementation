from blackbox import BlackBox
import csv
import random
import sys
import time

def reservoir_sampling(stream_users, reservoir_size, seq_num):
    reservoir = stream_users[:reservoir_size]

    for i in range(reservoir_size, len(stream_users)):
        probability = reservoir_size / (i + 1)
        if random.random() < probability:
            replace_index = random.randint(0, reservoir_size - 1)
            reservoir[replace_index] = stream_users[i]

    return [seq_num] + [reservoir[i] for i in range(0, reservoir_size, 20)]

if __name__ == '__main__':
    random.seed(553)

    input_path = sys.argv[1]
    stream_size = int(sys.argv[2])
    num_of_asks = int(sys.argv[3])
    output_path = sys.argv[4]

    s_t = time.time()

    bx = BlackBox()
    reservoir_size = 100
    seq_num = 0
    users_list = []

    result_str = "seqnum,0_id,20_id,40_id,60_id,80_id\n"

    for i in range(num_of_asks):
        stream_users = bx.ask(input_path, stream_size)
        
        for user in stream_users:
            seq_num += 1
            if len(users_list) < reservoir_size:
                users_list.append(user)
            elif random.random() < reservoir_size / seq_num:
                users_list[random.randint(0, reservoir_size - 1)] = user

            if seq_num % 100 == 0:
                result_str += ','.join(map(str, reservoir_sampling(users_list, reservoir_size, seq_num))) + '\n'

    with open(output_path, 'w') as f:
        f.writelines(result_str)

    e_t = time.time()
    print('Duration: ', e_t - s_t)
