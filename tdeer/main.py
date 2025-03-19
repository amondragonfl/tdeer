import argparse
from tdeer.utils.csv_processing import validate_csv, read_csv_as_numpy
from tdeer.utils.statistical_analysis import predict_tdee_with_linear_regression

def main ():
    parser = argparse.ArgumentParser(description="Accurately estimate your TDEE.")
    parser.add_argument("file_path", type=str, help="Path to CSV file containing weight and calorie data")
    args = parser.parse_args()

    if validate_csv(args.file_path):
        weights, calories =  read_csv_as_numpy(args.file_path)
        tdee_est_linear_regression = round(predict_tdee_with_linear_regression(weights, calories))
        print(f"[TDEER] estimates your tdee to be {str(tdee_est_linear_regression)} calories")

if __name__ == "__main__":
    main()