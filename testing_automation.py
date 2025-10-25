from pathlib import Path
import requests
import time


def send_listings(folder_path, endpoint):
    """Read .txt files from `folder_path` and POST each as {"text": ...} JSON.

    Args:
        folder_path: Path to the directory containing .txt files.
        endpoint: URL to POST each JSON payload to.
    """
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Folder not found or not a directory: {folder}")

    txt_files = sorted(folder.glob("*.txt"))
    if not txt_files:
        print(f"No .txt files found in {folder}")
        return

    for f in txt_files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Skipping {f.name}: could not read file ({e})")
            continue

        payload = {"text": text}

        try:
            resp = requests.post(endpoint, json=payload)
            print(f"[{f.name}] -> {resp.status_code}\n{resp.text}\n")
        except requests.RequestException as e:
            print(f"[{f.name}] request failed: {e}")
        
        time.sleep(10)  # brief pause between requests



if __name__ == "__main__":
    ENDPOINT = "http://localhost:8000/validate-listing"
    folder_input = input("please enter the listing folder link: ").strip()
    send_listings(folder_input, ENDPOINT)
