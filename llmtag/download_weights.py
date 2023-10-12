import requests

def download_llama_weights(destination_path, url="https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf"):
    """
    Downloads the Llama 2-7b Chat GGUF weights from the given URL and saves it to the specified destination path.
    
    Args:
    - destination_path (str): The path where the file should be saved.
    - url (str, optional): The URL of the file to be downloaded. Default is set to the Llama 2-7b Chat GGUF weights URL.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(destination_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

# Example usage:
# download_llama_weights("path_to_save_file.gguf")
