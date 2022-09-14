import ctypes


def process() -> str:
    lib = ctypes.windll.LoadLibrary("user32.dll")
    handle = lib.GetForegroundWindow()  # 활성화된 윈도우의 핸들얻음
    buffer = ctypes.create_unicode_buffer(255)  # 타이틀을 저장할 버퍼
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))  # 버퍼에 타이틀 저장
    return buffer.value
