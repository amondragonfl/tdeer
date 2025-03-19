import argparse
from tdeer.utils.csv_processing import validate_csv

def main ():
    parser = argparse.ArgumentParser(description="Accurately estimate your TDEE.")
    parser.add_argument("file_path", type=str, help="Path to CSV file containing weight and calorie data")
    args = parser.parse_args()
    validate_csv(args.file_path)

if __name__ == "__main__":
    main()