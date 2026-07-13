import asyncio
import time 
print("*"*40,"\n")
print("case 1")

async def download_file(file_number):
    print(f"starting downloading {file_number}")
    await asyncio.sleep(1)
    print(f"completed download {file_number}")

async def main():
    start=time.time()
    task1=asyncio.create_task(download_file(1))
    task2=asyncio.create_task(download_file(2))
    task3=asyncio.create_task(download_file(3))

    await task1
    await task2
    await task3
    end=time.time()
    print(f"total time taken:{end-start:.2f}seconds")
asyncio.run(main())
print("\n"+"*"*40)

#running multiple tasks with asyncio.gather()

print("*"*40,"\n")
print("case 2")
async def download_file(file_number):
    print(f"downloading file {file_number}....")
    await asyncio.sleep(1)
    print(f"file-{file_number} downloaded")

async def main():
    start=time.time()
    await asyncio.gather(
        download_file(1),
        download_file(2),
        download_file(3)
    )
    end=time.time()
    print(f"all download completed in {end-start:.2f} seconds")

asyncio.run(main())
print("\n"+"*"*40)
#fetch data from coroutines
print("*"*40,"\n")
print("case 3")
async def fetch_data(n):
    print(f"fetching {n}")
    await asyncio.sleep(1)
    return f"data-{n}"
async def main():
    results=await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("fecth data",results)

asyncio.run(main())
print("\n"+"*"*40)