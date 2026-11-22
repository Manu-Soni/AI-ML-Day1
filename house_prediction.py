"""Predict a house price from its size using a simple linear regression model."""

from sklearn.linear_model import LinearRegression


# Training data: house size in square feet and price in lakh rupees.
HOUSE_SIZES = [[500], [800], [1000], [1200], [1500]]
HOUSE_PRICES = [15, 24, 30, 36, 45]


def train_model():
    """Create and train the model with the example data."""
    model = LinearRegression()
    model.fit(HOUSE_SIZES, HOUSE_PRICES)
    return model


def predict_price(model, size_sq_ft):
    """Return the predicted price, in lakh rupees, for a house size."""
    if size_sq_ft <= 0:
        raise ValueError("House size must be greater than zero square feet.")

    # scikit-learn expects a 2D list: one row (house), one column (size).
    return model.predict([[size_sq_ft]])[0]


def main():
    model = train_model()

    print("Example predictions:")
    for size_sq_ft in (1300, 1600):
        price = predict_price(model, size_sq_ft)
        print(f"House size: {size_sq_ft} sq ft")
        print(f"Predicted price: {price:.2f} lakh rupees\n")

    entered_size = input("Enter a house size in square feet: ")
    try:
        size_sq_ft = float(entered_size)
        price = predict_price(model, size_sq_ft)
    except ValueError as error:
        print(f"Please enter a valid number greater than zero. ({error})")
        return

    print(f"Estimated price for {size_sq_ft:g} sq ft: {price:.2f} lakh rupees")


if __name__ == "__main__":
    main()
