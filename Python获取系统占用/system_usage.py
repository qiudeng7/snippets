import psutil
from time import sleep

def getTime()-> str:
    """
    返回当前时间 格式为 年-月-日 时:分:秒
    """
    from datetime import datetime
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_now

def main():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        storage_percent = psutil.disk_usage('/').percent
        
        if cpu_percent>60 or memory_percent >60 or storage_percent>60:
        # if True:
            header = ["create_time","cpu_usage","memory_usage","storage_usage"]
            data = [getTime(),f"{cpu_percent}%",f"{memory_percent}%",f"{storage_percent}%"]
            
            width = 20
            formatted_output = "{:<{width}} {:<{width}} {:<{width}} {:<{width}}\n".format(
                header[0], header[1], header[2], header[3], width=width
            ) + "{:<{width}} {:<{width}} {:<{width}} {:<{width}}\n".format(
                data[0], data[1], data[2], data[3], width=width
            )

            print(formatted_output)
            
            with open("usage.txt",mode="a",encoding="utf-8") as f:
                f.write("\n")
                f.write(formatted_output)
        sleep(60)
    
    
if __name__ =="__main__":
    main()