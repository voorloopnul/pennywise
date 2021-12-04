import requests
from pathlib import Path


def tool_list_exists() -> bool:
    home_dir = Path.home()
    pennywise_tool_file = home_dir / ".pennywise" / "pennywise.toml"
    return pennywise_tool_file.exists()


def load_tools(user: str = "voorloopnul", branch: str = "main") -> None:
    home_dir = Path.home()
    pennywise_tool_file = home_dir / ".pennywise" / "pennywise.toml"
    pennywise_tool_file.parent.mkdir(parents=True, exist_ok=True)

    print("Loading tool list from voorloopnul/pennywise")
    url = f"https://raw.githubusercontent.com/{user}/pennywise/{branch}/pennywise.toml"
    response = requests.get(url)
    pennywise_tool_file.write_text(response.text)

