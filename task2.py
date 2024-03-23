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
    for i in range(5):  
        hash_results.append(((a_values[i] * x + b_values[i]) % prime_mod) % 997)
    return hash_results

if __name__ == '__main__':
    input_path = sys.argv[1]
    stream_size = int(sys.argv[2])
    num_of_asks = int(sys.argv[3])
    output_path = sys.argv[4]
    
    start_time = time.time()
    
    result_str = "Time,Ground Truth,Estimation\n"
    total_groundtruth = 0
    total_estimated = 0
    bx = BlackBox()
    for i in range(num_of_asks):
        stream_users = bx.ask(input_path, stream_size)
        gt = set(stream_users)
        exist_hash = []
        max_trailing_zeros_list = []

        for s in stream_users:
            result = myhashs(s)
            exist_hash.append(result)
            max_trailing_zeros_list.append(max(format(max(result), 'b').rfind('0'), 0))

        est_sum = sum(2 ** max_trailing_zeros for max_trailing_zeros in max_trailing_zeros_list)
        est = est_sum // len(max_trailing_zeros_list)

        total_groundtruth += len(gt)
        total_estimated += est
        result_str = result_str + f"{i},{len(gt)},{est}\n"
    
    print(total_estimated/total_groundtruth)
    with open(output_path, 'w') as f:
        f.writelines(result_str)
    
    end_time = time.time()
    print('Duration: ', end_time - start_time)
