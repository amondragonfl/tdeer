import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.covariance import EllipticEnvelope

def predict_tdee_with_linear_regression(weights, calorie_intakes):
    """
    Predict the calorie intake required for a 0 weight change (i.e., when no weight is gained or lost) 
    based on daily calorie intake and weight changes using linear regression.

    Parameters:
    -----------
    calorie_intakes : numpy.ndarray
        Array containing daily calorie intake values.
    weights : numpy.ndarray
        Array containing daily weight measurements.

    Returns:
    --------
    float
        The predicted calorie intake required for a 0 weight change.
    
    Notes:
    ------
    The function uses day-to-day differences in weight to model the relationship 
    between calorie intake and weight change using a linear regression model.
    Outliers in weight changes are detected and removed using the EllipticEnvelope 
    method before fitting the regression model.
    """

    weights_diffs = np.diff(weights)
    X = calorie_intakes[:-1].reshape(-1, 1) 
    y = weights_diffs  

    envelope = EllipticEnvelope()
    envelope.fit(y.reshape(-1,1))

    inliers = envelope.predict(y.reshape(-1,1)) == 1
    X_clean = X[inliers]
    y_clean = y[inliers]

    reg = LinearRegression()
    reg.fit(X_clean, y_clean)

    # Predict the calorie intake for 0 weight change (y = 0)
    # Solve for X where y = 0: X = -beta_0 / beta_1
    predicted_calories = -reg.intercept_ / reg.coef_[0]

    return predicted_calories