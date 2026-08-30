from pathlib import Path


def save_screenshot(driver, name, directory="screenshots"):
    output_dir = Path(directory)
    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / f"{name}.png"
    driver.save_screenshot(str(path))
    return path
