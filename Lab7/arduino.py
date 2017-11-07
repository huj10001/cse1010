import socket, traceback

global _the_address
_the_address = '10.0.2.2'

global the_port
_the_port    = 22134

global _the_arduino
_the_arduino = None

def connect(address=_the_address, port=_the_port):
  global _the_arduino
  if _the_arduino:
    disconnect()
  try:
    _the_arduino = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _the_arduino.connect((address, port))
  except Exception as exception:
    print('Error, ard.connect:')
    traceback.print_exc()

def disconnect():
  global _the_arduino
  if _the_arduino:
    # kill the thread
    _the_arduino.close()
    _the_arduino = None

def _socket_read_line(socket):
  line = ''
  while True:
    bytes = socket.recv(1)
    if len(bytes) == 0:
      return None
    if bytes[0] == 0xff: # sending ^C from the client causes this
      return None
    char = bytes.decode('utf-8')
    if char == '\n' or char == '':
      break
    else:
      line += char
  return line

def receive():
  global _the_arduino
  line = _socket_read_line(_the_arduino)
  return line

# Sends a string to the Arduino.
# Ensures that the string is newline-terminated.
def send(string):
  global _the_arduino
  string = string.strip() + '\n'
  string = string.encode(encoding='utf-8')
  _the_arduino.sendall(string)
