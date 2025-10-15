# sphero_z_nb/drive_nb.py
import time
from spherov2.commands.drive import Drive as BaseDrive

class DriveNB(BaseDrive):
    """
    Navigation Ball용 Drive 확장 클래스
    - spherov2 원본 Drive를 건드리지 않고 raw motor 제어 기능 추가
    """

    @staticmethod
    def drive_raw_motors(toy, left_speed: int, right_speed: int, duration: float = 0.0):
        """
        BOLT 또는 BOLT+에서 직접 모터 제어 수행
        - left_speed, right_speed: 0~255
        - duration: 유지 시간 (초)
        """
        try:
            left = max(0, min(255, int(left_speed)))
            right = max(0, min(255, int(right_speed)))

            # 1번 command ID: set_raw_motors()
            toy._execute(BaseDrive._encode(toy, 1, None, [1, left, 1, right]))
            print(f"⚙️ Raw motor command sent (L={left}, R={right})")

            if duration > 0:
                time.sleep(duration)
                DriveNB.stop(toy)

        except Exception as e:
            print(f"❌ drive_raw_motors() failed: {e}")

    @staticmethod
    def stop(toy):
        """즉시 모터 정지"""
        try:
            toy._execute(BaseDrive._encode(toy, 1, None, [0, 0, 0, 0]))
            print("🛑 Motors stopped.")
        except Exception as e:
            print(f"⚠️ stop() failed: {e}")
