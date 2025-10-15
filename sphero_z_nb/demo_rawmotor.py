# sphero_z_nb/demo_rawmotor.py
import time
from sphero_z_nb.api import connect_and_run

# Raw motor 테스트용 경로
path = [
    (100, 100, 2.0),   # 직진
    (255, 0, 1.0),     # 오른쪽 회전
    (0, 255, 1.0),     # 왼쪽 회전
    (150, 150, 2.0)    # 느린 직진
]

if __name__ == "__main__":
    print("🚀 Running Navigation Ball raw motor demo...")
    connect_and_run(path)
