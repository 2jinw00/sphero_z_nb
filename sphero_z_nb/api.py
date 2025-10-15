# sphero_z_nb/api.py
"""
Custom SpheroEduAPI for Navigation Ball Project
- DriveNB 기반 raw motor 제어
- LED, sequence, stop 제어 포함
"""

import time
from sphero_unsw.toys_scanner import toys_scanner
from sphero_unsw.types import Color
from sphero_z_nb.drive_nb import DriveNB


class SpheroEduAPI:
    """Navigation Ball 전용 커스텀 API"""

    def __init__(self, toy):
        self.toy = toy
        print(f"✅ Connected to {self.toy.name}")

    # -------------------
    # 🔹 기본 제어 함수
    # -------------------
    def raw_motors(self, left: int, right: int, duration: float):
        """좌/우 모터를 개별 제어"""
        DriveNB.drive_raw_motors(self.toy, left, right, duration)

    def stop_roll(self):
        """즉시 정지"""
        DriveNB.stop(self.toy)

    # -------------------
    # 🔹 LED 제어
    # -------------------
    def set_main_led(self, color: Color):
        """LED 색상 설정"""
        try:
            self.toy.set_main_led(color)
        except Exception as e:
            print(f"⚠️ LED 설정 실패: {e}")

    # -------------------
    # 🔹 시퀀스 실행
    # -------------------
    def run_sequence(self, path):
        """
        path: [(left, right, duration), ...]
        """
        for left, right, duration in path:
            print(f"\n🎯 Left={left}, Right={right}, Duration={duration}s")
            self.set_main_led(Color(0, 150, 255))
            self.raw_motors(left, right, duration)
            self.set_main_led(Color(0, 255, 0))
            time.sleep(0.5)
        self.stop_roll()
        self.set_main_led(Color(255, 255, 255))
        print("✅ Sequence complete.")

    def __enter__(self):
        """Allow using SpheroEduAPI in a 'with' block (context manager)."""
        # toy 연결 시작
        self._toy.__enter__()  # sphero_unsw 내부의 BLE 연결 열기
        print(f"✅ Connected to {self._toy.name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Ensure proper disconnect when leaving the 'with' block."""
        try:
            self._toy.__exit__(exc_type, exc_value, traceback)
            print(f"🧹 Disconnected from {self._toy.name}")
        except Exception as e:
            print(f"⚠️ Disconnect error: {e}")


# ---------------------------
# 🔹 유틸리티 실행 도우미
# ---------------------------
def connect_and_run(path):
    print("🔍 Scanning for Sphero toys...")
    scanner = toys_scanner()
    toy = scanner.scan_and_select_toy()
    api = SpheroEduAPI(toy)
    api.run_sequence(path)
    return api
