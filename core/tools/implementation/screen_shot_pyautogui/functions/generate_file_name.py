from datetime import datetime

def generate_file_name(base_name: str = 'ScreenShot') -> str:
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    base_name = base_name.replace(' ', '_')

    return f"./input_files/{base_name}_{current_time}.png"