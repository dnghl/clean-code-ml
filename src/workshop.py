def train_model(model_type, X_train, Y_train):
    model = model_type()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    acc = rounding(model.score(X_train, Y_train), 2)
    return model, acc

def rounding(score, deci_pl):
    rounded_score = round(score * 100, deci_pl)
    return rounded_score

def add(numA, numB):
    return numA + numB

def multiply(df):
    return df * 10

def impute_nan(df):
    for col in df.columns:
        df[col] = df[col].fillna(df[col].dropna().median())
    return df
