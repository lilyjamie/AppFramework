from utils.ADBConnect import AdbDeviceManage
from utils.Log import Log
from utils.Filepath import *

log = Log(LOG_PATH)

adb = AdbDeviceManage()
adb.adb_connect()
