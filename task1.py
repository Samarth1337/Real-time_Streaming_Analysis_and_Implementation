from blackbox import BlackBox
import random
import binascii
import csv
import sys
import time


def myhashs(s):
    prime_mod = 10**9 + 9
    hash_funcs = []
    a_values = random.sample(range(1, 69997), 25)  
    b_values = random.sample(range(1, 69997), 25)

    hash_results = []
    x = int(binascii.hexlify(s.encode('utf8')), 16)
    for i in range(3):  
        hash_results.append(((a_values[i] * x + b_values[i]) % prime_mod) % 69997)
    return hash_results


if __name__ == '__main__':
    input_path = sys.argv[1]
    stream_size = int(sys.argv[2])
    num_of_asks = int(sys.argv[3])
    output_path = sys.argv[4]

    start_time = time.time()

    result_str = "Time,FPR\n"
    existing_users = set()
    existing_hashes = set()  

    black_box = BlackBox()
    for i in range(num_of_asks):
        stream_users = black_box.ask(input_path, stream_size)
        false_positives = 0
        for s in stream_users:
            hash_results = myhashs(s)
            if any(hash_val in existing_hashes for hash_val in hash_results):
                if s not in existing_users:
                    false_positives += 1
            existing_hashes.update(hash_results)
            existing_users.add(s)
        result_str += f"{i},{false_positives / stream_size}\n"

    with open(output_path, 'w') as f:
        f.writelines(result_str)

    end_time = time.time()
    print('Duration: ', end_time - start_time)