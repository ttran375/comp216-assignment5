import os
import time
from threading import Thread
import requests

# Define the folder where files will be saved
download_folder = "downloaded_images"

# Create the folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


def download_file(url):
    # Extract the filename from the URL
    filename = url.split("/")[-1] + ".jpg"
    filepath = os.path.join(download_folder, filename)
    response = requests.get(url, stream=True)

    # Save the file to the local disk
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded {filename} to {download_folder}")
    else:
        print(f"Failed to download from {url}")


img_urls = [
    "https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0",
    "https://images.unsplash.com/photo-1485833077593-4278bba3f11f",
    "https://images.unsplash.com/photo-1593179357196-ea11a2e7c119",
    "https://images.unsplash.com/photo-1526515579900-98518e7862cc",
    "https://images.unsplash.com/photo-1582376432754-b63cc6a9b8c3",
    "https://images.unsplash.com/photo-1567608198472-6796ad9466a2",
    "https://images.unsplash.com/photo-1487213802982-74d73802997c",
    "https://images.unsplash.com/photo-1552762578-220c07490ea1",
    "https://images.unsplash.com/photo-1569691105751-88df003de7a4",
    "https://images.unsplash.com/photo-1590691566903-692bf5ca7493",
    "https://images.unsplash.com/photo-1497206365907-f5e630693df0",
    "https://images.unsplash.com/photo-1469765904976-5f3afbf59dfb",
]


def download_images_sequentially(urls):
    start_time = time.perf_counter()
    for url in urls:
        download_file(url)
    end_time = time.perf_counter()
    print(f"Sequential download time: {end_time - start_time:.2f} seconds")


download_images_sequentially(img_urls)


def download_images_with_threads(urls):
    start_time = time.perf_counter()
    threads = []

    # Start all threads
    for url in urls:
        thread = Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print(f"Threaded download time: {end_time - start_time:.2f} seconds")


download_images_with_threads(img_urls)
