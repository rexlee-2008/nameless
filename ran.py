import socket
import time
from hashlib import sha256

HOST = '3.38.57.41'
PORT = 10502

# 서버와 연결
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    for rand_bits in range(2**32):  # 0부터 2^32-1까지의 랜덤 값 시도
        # 랜덤 숫자를 바탕으로 해시값 생성
        correct_input = sha256(str(rand_bits).encode()).digest()
        
        # 서버에 입력값 전송
        s.sendall(correct_input.hex().encode() + b'\n')
        response = s.recv(1024).decode()
        
        print(f'Trying input: {correct_input.hex()}, Response: {response}')

        if "Congrats" in response:
            print("Found the flag!")
            break