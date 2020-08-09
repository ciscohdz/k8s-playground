import requests
import time

def main():
    for _ in range(15):
        with requests.get("http://google.com", stream=True) as response:
            size = sum(len(chunk) for chunk in response.iter_content(4096*5))
            print(f"{size} bytes")

            time.sleep(2)


if __name__ == "__main__":
    main()