import subprocess
from datetime import datetime

def get_full_systeminfo():
    result = subprocess.run(
        ["systeminfo"],
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout

def write_markdown(systeminfo_text):
    with open("info.md", "w", encoding="utf-8") as f:
        f.write("# System Information\n\n")
        f.write(f"Time: {datetime.now()}\n\n")
        f.write("```\n")
        f.write(systeminfo_text)
        f.write("\n```")

if __name__ == "__main__":
    systeminfo_text = get_full_systeminfo()
    write_markdown(systeminfo_text)
