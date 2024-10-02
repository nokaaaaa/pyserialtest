import serial
import time
from pynput import keyboard

# シリアルポートの設定
ser = serial.Serial('COM8', 115200)  # COMポートは環境に応じて変更

# lキーが押されているかを管理するフラグ
is_l_pressed = False

# キーが押されたときのコールバック関数
def on_press(key):
    global is_l_pressed
    try:
        if key.char == 'l':  # lキーが押されたとき
            is_l_pressed = True
    except AttributeError:
        pass

# キーが離されたときのコールバック関数
def on_release(key):
    global is_l_pressed
    try:
        if key.char == 'l':  # lキーが離されたとき
            is_l_pressed = False
    except AttributeError:
        pass

# キーボードリスナーを開始
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# メインループ
try:
    while True:
        if is_l_pressed:
            ser.write(b'0')  # シリアルポートに'a'を送信
            time.sleep(0.1)  # CPU負荷を抑えるために少し待機
        else:
            ser.write(b'1')
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
