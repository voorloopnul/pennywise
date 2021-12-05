import requests
from pathlib import Path


def tool_list_exists() -> bool:
    home_dir = Path.home()
    pennywise_tool_file = home_dir / ".pennywise" / "pennywise.toml"
    return pennywise_tool_file.exists()


def load_tools(user: str, branch: str) -> None:
    home_dir = Path.home()
    pennywise_tool_file = home_dir / ".pennywise" / "pennywise.toml"
    pennywise_tool_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading tool list from {user}/pennywise")
    url = f"https://raw.githubusercontent.com/{user}/pennywise/{branch}/pennywise.toml"
    response = requests.get(url)
    if response.status_code == 404:
        print("Fork or User not found!")
    elif response.status_code == 200:
        pennywise_tool_file.write_text(response.text)
    else:
        print(f"Failed to load source from {user}")
