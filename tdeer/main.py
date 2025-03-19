import argparse
from tdeer.utils.csv_processing import validate_csv, read_csv_as_numpy
from tdeer.utils.statistical_analysis import predict_tdee

def main ():
    parser = argparse.ArgumentParser(description="Accurately estimate your TDEE.")
    parser.add_argument("file_path", type=str, help="Path to CSV file containing weight and calorie data")
    args = parser.parse_args()

if __name__ == "__main__":
    main()