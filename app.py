from datetime import datetime

def greet(name: str = "User"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello {name}, Welcome to Jenkins...")
    print(f"Current Date & Time: {current_time}\n")

def main():
    greet("Jonita Fernandes")

if __name__ == "__main__":
    main()
